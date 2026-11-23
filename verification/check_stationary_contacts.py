"""Finite checks for mixing with stationary depolarizing contacts."""

from fractions import Fraction
from itertools import product
from math import comb

import numpy as np

from run_all import circuit_image, commutes


PAULIS = (
    np.eye(2, dtype=complex),
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
)
SWAP_GATES = (("CX", 0, 1), ("CX", 1, 0), ("CX", 0, 1))
CZ_GATES = (("H", 1), ("CX", 0, 1), ("H", 1))


def swap_exposures(length, contacts, schedule):
    """Return the final token ordering and post-layer contact counts."""
    tokens = list(range(length))
    visits = [0] * length
    for matching in schedule:
        for left in matching:
            tokens[left], tokens[left + 1] = tokens[left + 1], tokens[left]
        for contact in contacts:
            visits[tokens[contact]] += 1
    return tokens, visits


def binomial_tv(size, probability, baseline):
    """Exact total variation of the two binomial laws at rational rates."""
    return sum(
        comb(size, count)
        * abs(
            probability**count * (1 - probability) ** (size - count)
            - baseline**count * (1 - baseline) ** (size - count)
        )
        for count in range(size + 1)
    ) / 2


def conjugate(unitary, operator):
    return unitary @ operator @ unitary.conj().T


def permutation_matrix(outputs):
    return np.eye(len(outputs))[:, outputs]


def twirl_contact(operator, contact_paulis):
    return sum(conjugate(pauli, operator) for pauli in contact_paulis) / 4


def depolarize_contact(operator, contact_paulis, retention):
    return retention * operator + (1 - retention) * twirl_contact(
        operator, contact_paulis
    )


def choi_error(prefixes, retention):
    """Apply the physical layers to one half of a two-qubit Bell state."""
    dimension = prefixes[0].shape[0]
    reference = np.eye(dimension)
    maximally_entangled = reference.reshape(-1) / np.sqrt(dimension)
    choi = np.outer(maximally_entangled, maximally_entangled)
    contact_paulis = [np.kron(np.kron(np.eye(2), pauli), reference) for pauli in PAULIS]

    previous = np.eye(dimension)
    for prefix in prefixes:
        layer = prefix @ previous.conj().T
        choi = conjugate(np.kron(layer, reference), choi)
        choi = depolarize_contact(choi, contact_paulis, retention)
        previous = prefix

    error_operator = choi - np.eye(dimension**2) / dimension**2
    return np.abs(np.linalg.eigvalsh(error_operator)).sum() / 2


def pauli_error(prefixes, retention):
    """Compute total variation from exact exposure counts and Pauli characters."""
    labels = tuple(product(range(4), repeat=2))
    # Bit zero corresponds to the second tensor factor in the matrix calculation.
    coefficients = {}
    for x, z in labels:
        images = [circuit_image(x, z, gates) for gates in prefixes]
        exposures = sum((image_p | image_q) & 1 for image_p, image_q in images)
        coefficients[x, z] = retention**exposures

    probabilities = [
        sum(
            (1 if commutes(qx, qz, x, z) else -1) * coefficients[x, z]
            for x, z in labels
        )
        / len(labels)
        for qx, qz in labels
    ]
    assert all(probability >= 0 for probability in probabilities)
    assert sum(probabilities) == 1
    uniform = Fraction(1, len(labels))
    return sum(abs(probability - uniform) for probability in probabilities) / 2


def check_three_round_circuits():
    """Compare a Clifford schedule to every possible swap-only schedule."""
    identity = np.eye(4)
    swap = permutation_matrix([0, 2, 1, 3])
    flipped_cnot = permutation_matrix([0, 3, 2, 1])
    hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    controlled_z = np.diag([1, 1, 1, -1])
    clifford_prefixes = (
        identity,
        swap @ flipped_cnot @ np.kron(np.eye(2), hadamard),
        swap @ controlled_z,
    )
    clifford_gates = (
        (),
        (("H", 0), ("CX", 0, 1)) + SWAP_GATES,
        CZ_GATES + SWAP_GATES,
    )
    retention = Fraction(1, 2)
    clifford_error = pauli_error(clifford_gates, retention)
    assert clifford_error == Fraction(3, 16)
    np.testing.assert_allclose(
        choi_error(clifford_prefixes, float(retention)), float(clifford_error), atol=1e-12, rtol=0
    )

    swap_errors = []
    for choices in product((0, 1), repeat=3):
        prefixes = [(identity, swap)[choice] for choice in choices]
        gate_prefixes = [((), SWAP_GATES)[choice] for choice in choices]
        error = pauli_error(gate_prefixes, retention)
        np.testing.assert_allclose(
            choi_error(prefixes, float(retention)), float(error), atol=1e-12, rtol=0
        )
        swap_errors.append(error)
    assert min(swap_errors) == Fraction(3, 8)
    return clifford_error, min(swap_errors)


def check_non_clifford_inverse_witness():
    """Test the inverse-observable construction with genuine Pauli mixing."""
    identity, x, y, z = PAULIS
    register_identity = np.eye(4)
    contact_paulis = [np.kron(pauli, identity) for pauli in PAULIS]
    layers = (
        np.cos(0.27) * register_identity - 1j * np.sin(0.27) * np.kron(x, x),
        np.cos(0.43) * register_identity - 1j * np.sin(0.43) * np.kron(z, y),
    )
    retention = 0.7
    initial = np.kron(identity, z)
    witness = initial
    for layer in layers:
        rotated = conjugate(layer, witness)
        witness = (
            rotated / retention
            - (1 / retention - 1) * twirl_contact(rotated, contact_paulis)
        )

    recovered = witness
    for layer in reversed(layers):
        recovered = conjugate(
            layer.conj().T, depolarize_contact(recovered, contact_paulis, retention)
        )
    np.testing.assert_allclose(recovered, initial, atol=1e-12)
    np.testing.assert_allclose(np.trace(witness), 0, atol=1e-12)
    bound = (2 / retention - 1) ** len(layers)
    assert np.linalg.norm(witness, ord=2) <= bound

    output = np.kron(identity / 2, (identity + z) / 2)
    for layer in layers:
        output = depolarize_contact(conjugate(layer, output), contact_paulis, retention)
    effect = (register_identity + witness / bound) / 2
    np.testing.assert_allclose(np.trace(effect @ output), (1 + 1 / bound) / 2, atol=1e-12)


def run_checks():
    for length in range(1, 129):
        odd_even_schedule = [range(layer % 2, length - 1, 2) for layer in range(2 * length)]
        tokens, visits = swap_exposures(length, (0,), odd_even_schedule)
        assert tokens == list(range(length))
        assert visits == [2] * length

    contacts = (0, 2, 4)
    tokens, visits = swap_exposures(6, contacts, (contacts, contacts))
    assert tokens == list(range(6))
    assert visits == [1] * 6
    # A Pauli error from retention 1/10 is the identity with probability 13/40.
    spaced_error = binomial_tv(6, Fraction(13, 40), Fraction(1, 4))
    assert spaced_error == Fraction(1360729530, 8192000000)
    clustered_contact_distance = min(6 - contact for contact in (1, 2, 3))
    assert clustered_contact_distance > 2
    clifford_error, swap_error = check_three_round_circuits()
    check_non_clifford_inverse_witness()

    return {
        "returning_sweep_lengths_checked": 128,
        "spaced_six_qubit_half_diamond": str(spaced_error),
        "clustered_six_qubit_half_diamond_lower": "1/2",
        "clifford_three_round_half_diamond": str(clifford_error),
        "transport_three_round_half_diamond": str(swap_error),
        "non_clifford_inverse_witness": True,
    }


def main():
    for name, value in run_checks().items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
