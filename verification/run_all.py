#!/usr/bin/env python3
"""Finite checks for the complete-mixing proofs.

Integer Pauli checks exhaust the stated finite spaces. Dense NumPy checks are
numerical cross-checks, not interval-certified proofs. Nothing here searches for
new asymptotic claims or supplies runtime random control to the mixing protocol.
"""

from __future__ import annotations

import argparse
from collections import Counter
import itertools
import json
import math
from pathlib import Path
import random
import sys


HERE = Path(__file__).resolve().parent
EXPECTED = HERE / "expected_results.json"
NUMERICAL_TOLERANCE = 2e-11

# Gates are chronological. Qubit 0 is the least significant computational bit.
# Every CX acts on adjacent vertices of a three-site line.
LINE3 = (
    ("CX", 0, 1),
    ("CX", 1, 2),
    ("H", 1),
    ("CX", 1, 0),
    ("CX", 2, 1),
    ("H", 1),
    ("CX", 0, 1),
)

# A separate two-site fixture permits exhaustive checking of a 2x2x2 cube.
LINE2 = (
    ("CX", 0, 1),
    ("H", 0),
    ("S", 1),
    ("CX", 1, 0),
    ("H", 1),
    ("S", 0),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def transform(x: int, z: int, gate: tuple) -> tuple[int, int]:
    """Conjugate a phase-free Pauli by H, S, or CX using exact bit arithmetic."""
    name = gate[0]
    if name == "H":
        q = gate[1]
        flip = ((x ^ z) >> q) & 1
        x ^= flip << q
        z ^= flip << q
    elif name == "S":
        q = gate[1]
        z ^= ((x >> q) & 1) << q
    elif name == "CX":
        control, target = gate[1:]
        x ^= ((x >> control) & 1) << target
        z ^= ((z >> target) & 1) << control
    else:
        raise ValueError(f"Unsupported gate: {gate}")
    return x, z


def circuit_image(x: int, z: int, gates: tuple) -> tuple[int, int]:
    for gate in gates:
        x, z = transform(x, z, gate)
    return x, z


def word(x: int, z: int, n: int) -> str:
    # Display order is qubit 0, qubit 1, ..., not matrix tensor-factor order.
    return "".join("IXZY"[((x >> q) & 1) + 2 * ((z >> q) & 1)] for q in range(n))


def commutes(x: int, z: int, other_x: int, other_z: int) -> bool:
    return ((x & other_z).bit_count() + (z & other_x).bit_count()) % 2 == 0


def line_certificate(n: int, gates: tuple) -> tuple[dict, list[int]]:
    mask = (1 << n) - 1
    table = []
    histogram = Counter()
    minimum = 2 * n + 1
    witness = None
    for packed in range(1 << (2 * n)):
        x, z = packed & mask, packed >> n
        out_x, out_z = circuit_image(x, z, gates)
        table.append(out_x | (out_z << n))
        if packed:
            branch = (x | z).bit_count() + (out_x | out_z).bit_count()
            histogram[branch] += 1
            if branch < minimum:
                minimum = branch
                witness = {"input": word(x, z, n), "output": word(out_x, out_z, n)}
    require(len(set(table)) == len(table), "Line map is not a permutation")
    for p, image_p in enumerate(table):
        for q, image_q in enumerate(table):
            require(
                commutes(p & mask, p >> n, q & mask, q >> n)
                == commutes(image_p & mask, image_p >> n, image_q & mask, image_q >> n),
                "Line map failed the exact symplectic check",
            )
    return {
        "qubits": n,
        "primitive_rounds": len(gates),
        "gates": [list(gate) for gate in gates],
        "nonidentity_paulis_checked": (1 << (2 * n)) - 1,
        "branch_weight_minimum": minimum,
        "branch_weight_histogram": dict(sorted(histogram.items())),
        "minimum_witness": witness,
        "symplectic_pairs_checked": len(table) ** 2,
    }, table


def axes_sequence(dimension: int) -> list[int]:
    if dimension == 1:
        return [0]
    previous = axes_sequence(dimension - 1)
    return previous + [dimension - 1] + previous


def coordinate_lines(sides: tuple[int, ...], axis: int) -> list[tuple[int, ...]]:
    strides = [math.prod(sides[:j]) for j in range(len(sides))]
    other_axes = [j for j in range(len(sides)) if j != axis]
    lines = []
    for values in itertools.product(*(range(sides[j]) for j in other_axes)):
        base = sum(value * strides[j] for j, value in zip(other_axes, values))
        lines.append(tuple(base + t * strides[axis] for t in range(sides[axis])))
    return lines


def stage_data(sides: tuple[int, ...], axis: int, table: list[int]) -> tuple:
    m = sides[axis]
    scatter_tables = []
    for line in coordinate_lines(sides, axis):
        scatter = [sum(((v >> j) & 1) << q for j, q in enumerate(line)) for v in range(1 << m)]
        scatter_tables.append((line, scatter))
    return m, table, scatter_tables


def apply_stage(x: int, z: int, stage: tuple) -> tuple[int, int]:
    m, table, lines = stage
    mask = (1 << m) - 1
    out_x = out_z = 0
    for line, scatter in lines:
        local_x = local_z = 0
        for j, q in enumerate(line):
            local_x |= ((x >> q) & 1) << j
            local_z |= ((z >> q) & 1) << j
        image = table[local_x | (local_z << m)]
        out_x |= scatter[image & mask]
        out_z |= scatter[image >> m]
    return out_x, out_z


def structured_samples(sides: tuple[int, ...]) -> list[int]:
    """All weight-one/two Paulis, line/sheet patterns, and fixed-seed samples."""
    n = math.prod(sides)
    samples = set()
    for weight in (1, 2):
        for sites in itertools.combinations(range(n), weight):
            for labels in itertools.product((1, 2, 3), repeat=weight):
                x = z = 0
                for site, label in zip(sites, labels):
                    if label in (1, 3):
                        x |= 1 << site
                    if label in (2, 3):
                        z |= 1 << site
                samples.add(x | (z << n))
    supports = [{*range(n)}]
    for axis, length in enumerate(sides):
        supports.extend(set(line) for line in coordinate_lines(sides, axis))
        stride = math.prod(sides[:axis])
        for value in range(length):
            supports.append({q for q in range(n) if (q // stride) % length == value})
    for support in supports:
        bitmask = sum(1 << q for q in support)
        samples.update((bitmask, bitmask << n, bitmask | (bitmask << n)))
    rng = random.Random(20261028)
    for _ in range(2048):
        samples.add(rng.randrange(1, 1 << (2 * n)))
    return sorted(samples)


def checkpoint_check(sides: tuple[int, ...], line_data: dict, exhaustive: bool) -> dict:
    n = math.prod(sides)
    axes = axes_sequence(len(sides))
    stages = [stage_data(sides, axis, line_data[sides[axis]][1]) for axis in axes]
    certified_bound = math.prod(line_data[m][0]["branch_weight_minimum"] for m in sides)
    packed_inputs = range(1, 1 << (2 * n)) if exhaustive else structured_samples(sides)
    mask = (1 << n) - 1
    minimum = n * (len(axes) + 1) + 1
    histogram = Counter()
    witness = None
    count = 0
    for packed in packed_inputs:
        initial_x, initial_z = packed & mask, packed >> n
        x, z = initial_x, initial_z
        checkpoints = [(x | z).bit_count()]
        for stage in stages:
            x, z = apply_stage(x, z, stage)
            checkpoints.append((x | z).bit_count())
        weight_sum = sum(checkpoints)
        require(weight_sum >= certified_bound, f"Checkpoint bound failed on {sides}")
        histogram[weight_sum] += 1
        count += 1
        if weight_sum < minimum:
            minimum = weight_sum
            witness = {"input": word(initial_x, initial_z, n), "checkpoint_weights": checkpoints}
    return {
        "sides": list(sides),
        "qubits": n,
        "stage_axes_zero_based": axes,
        "checkpoint_count": len(axes) + 1,
        "exhaustive": exhaustive,
        "nonidentity_paulis_checked": count,
        "certified_induction_bound": certified_bound,
        "minimum_observed_checkpoint_sum": minimum,
        "minimum_witness": witness,
        "checkpoint_sum_histogram": dict(sorted(histogram.items())),
    }


def pauli_matrix(np, x: int, z: int, n: int):
    dimension = 1 << n
    matrix = np.zeros((dimension, dimension), dtype=complex)
    phase = (1j) ** (x & z).bit_count()
    for column in range(dimension):
        matrix[column ^ x, column] = phase * (-1 if (z & column).bit_count() % 2 else 1)
    return matrix


def elementary_matrix(np, gate: tuple, n: int):
    dimension = 1 << n
    matrix = np.zeros((dimension, dimension), dtype=complex)
    name = gate[0]
    for column in range(dimension):
        if name == "CX":
            control, target = gate[1:]
            row = column ^ ((((column >> control) & 1) << target))
            matrix[row, column] = 1
        elif name == "H":
            q = gate[1]
            matrix[column, column] = (-1 if (column >> q) & 1 else 1) / math.sqrt(2)
            matrix[column ^ (1 << q), column] = 1 / math.sqrt(2)
        elif name == "S":
            matrix[column, column] = 1j if (column >> gate[1]) & 1 else 1
        else:
            raise ValueError(gate)
    return matrix


def site_paulis(np, total_qubits: int, active_qubits: int) -> list[tuple]:
    return [
        tuple(pauli_matrix(np, x << q, z << q, total_qubits) for x, z in ((1, 0), (1, 1), (0, 1)))
        for q in range(active_qubits)
    ]


def depolarize(np, matrix, eta: float, operators: list[tuple]):
    for triple in operators:
        matrix = ((1 + 3 * eta) / 4) * matrix + ((1 - eta) / 4) * sum(
            operator @ matrix @ operator for operator in triple
        )
    return matrix


def inverse_depolarize(np, matrix, eta: float, operators: list[tuple]):
    for triple in operators:
        conditional = (matrix + sum(operator @ matrix @ operator for operator in triple)) / 4
        matrix = matrix / eta - (1 / eta - 1) * conditional
    return matrix


def hermitian_norm(np, matrix) -> float:
    return float(np.max(np.abs(np.linalg.eigvalsh((matrix + matrix.conj().T) / 2))))


def trace_distance(np, first, second) -> float:
    difference = first - second
    return float(np.sum(np.abs(np.linalg.eigvalsh((difference + difference.conj().T) / 2))) / 2)


def passive_binomial_error(n: int, survival: float) -> float:
    p0 = (1 + 3 * survival) / 4
    return sum(
        abs(math.comb(n, j) * p0 ** j * (1 - p0) ** (n - j)
            - math.comb(n, j) * 0.25 ** j * 0.75 ** (n - j))
        for j in range(n + 1)
    ) / 2


def dense_clifford_checks(np, line_table: list[int]) -> dict:
    n = 3
    dimension = 1 << n
    ideal = np.eye(dimension, dtype=complex)
    gates = [elementary_matrix(np, gate, n) for gate in LINE3]
    for gate in gates:
        ideal = gate @ ideal
    maximum_residual = 0.0
    for packed, image in enumerate(line_table):
        pauli = pauli_matrix(np, packed & 7, packed >> 3, n)
        predicted = pauli_matrix(np, image & 7, image >> 3, n)
        actual = ideal @ pauli @ ideal.conj().T
        sign = float(np.trace(predicted.conj().T @ actual).real / dimension)
        require(abs(abs(sign) - 1) < NUMERICAL_TOLERANCE, "Dense line phase is not +/-1")
        maximum_residual = max(maximum_residual, float(np.linalg.norm(actual - round(sign) * predicted)))
    require(maximum_residual < NUMERICAL_TOLERANCE, "Dense line matrix disagrees with bit action")

    wait_rounds = 3
    exponents = [0]
    for packed in range(1, 64):
        x, z = packed & 7, packed >> 3
        exponent = wait_rounds * (x | z).bit_count()
        for gate in LINE3:
            x, z = transform(x, z, gate)
            exponent += (x | z).bit_count()
        exponent += wait_rounds * (x | z).bit_count()
        exponents.append(exponent)
    require(min(exponents[1:]) >= wait_rounds * 4, "Inserted waits violated branch bound")
    character = np.array([
        [1 if commutes(p & 7, p >> 3, q & 7, q >> 3) else -1 for p in range(64)]
        for q in range(64)
    ], dtype=float)
    phi = np.zeros(dimension * dimension, dtype=complex)
    for index in range(dimension):
        phi[index + dimension * index] = 1 / math.sqrt(dimension)
    phi_density = np.outer(phi, phi.conj())
    target = np.eye(dimension * dimension) / (dimension * dimension)
    choi_operators = site_paulis(np, 2 * n, n)
    embedded_gates = [np.kron(np.eye(dimension), gate) for gate in gates]
    inverse_ideal = np.kron(np.eye(dimension), ideal.conj().T)
    cases = []
    for eta in (0.85, 0.97):
        eigenvalues = np.array([eta ** exponent for exponent in exponents])
        probabilities = (character @ eigenvalues) / 64
        require(float(probabilities.min()) >= -NUMERICAL_TOLERANCE, "Negative Pauli probability")
        require(abs(float(probabilities.sum()) - 1) < NUMERICAL_TOLERANCE, "Pauli probabilities not normalized")
        chi_square = float(np.sum(eigenvalues[1:] ** 2))
        parseval_value = float(64 * np.sum((probabilities - 1 / 64) ** 2))
        pauli_error = float(np.sum(np.abs(probabilities - 1 / 64)) / 2)

        choi = phi_density.copy()
        for _ in range(wait_rounds):
            choi = depolarize(np, choi, eta, choi_operators)
        for gate in embedded_gates:
            choi = gate @ choi @ gate.conj().T
            choi = depolarize(np, choi, eta, choi_operators)
        for _ in range(wait_rounds):
            choi = depolarize(np, choi, eta, choi_operators)
        decoded = inverse_ideal @ choi @ inverse_ideal.conj().T
        pauli_choi = np.zeros_like(decoded)
        for q, probability in enumerate(probabilities):
            bell = np.kron(np.eye(dimension), pauli_matrix(np, q & 7, q >> 3, n)) @ phi
            pauli_choi += probability * np.outer(bell, bell.conj())
        choi_residual = float(np.linalg.norm(decoded - pauli_choi))
        choi_error = trace_distance(np, choi, target)
        require(choi_residual < NUMERICAL_TOLERANCE, "Noisy Choi matrix disagrees with Pauli path")
        require(abs(choi_error - pauli_error) < NUMERICAL_TOLERANCE, "Choi error differs from exact Pauli TV")
        require(abs(chi_square - parseval_value) < NUMERICAL_TOLERANCE, "Pauli Parseval identity failed")
        require(pauli_error <= math.sqrt(chi_square) / 2 + NUMERICAL_TOLERANCE, "Chi-square error bound failed")

        product_probabilities = np.outer(probabilities, probabilities).reshape(-1)
        product_chi = float(4096 * np.sum((product_probabilities - 1 / 4096) ** 2))
        product_error = float(np.sum(np.abs(product_probabilities - 1 / 4096)) / 2)
        require(abs(product_chi - ((1 + chi_square) ** 2 - 1)) < NUMERICAL_TOLERANCE, "Product chi-square identity failed")
        require(product_error <= math.sqrt(product_chi) / 2 + NUMERICAL_TOLERANCE, "Product error bound failed")
        cases.append({
            "eta": eta,
            "chi_square": chi_square,
            "checkpoint_only_chi_square_bound": 63 * eta ** (2 * wait_rounds * 4),
            "exact_half_diamond_from_pauli_distribution": pauli_error,
            "passive_half_diamond_at_same_round_count": passive_binomial_error(n, eta ** (len(LINE3) + 2 * wait_rounds)),
            "direct_choi_half_trace_distance": choi_error,
            "decoded_choi_frobenius_residual": choi_residual,
            "parseval_residual": abs(chi_square - parseval_value),
            "two_block_chi_square": product_chi,
            "two_block_exact_half_diamond": product_error,
            "two_block_chi_square_error_bound": min(1.0, math.sqrt(product_chi) / 2),
        })
    return {
        "qubits": n,
        "input_reference_dimension": dimension,
        "gate_rounds": len(LINE3),
        "wait_rounds_per_endpoint": wait_rounds,
        "total_noisy_rounds": len(LINE3) + 2 * wait_rounds,
        "minimum_actual_accumulated_pauli_weight": min(exponents[1:]),
        "accumulated_weight_histogram": dict(sorted(Counter(exponents[1:]).items())),
        "dense_ideal_action_maximum_frobenius_residual": maximum_residual,
        "cases": cases,
    }


def embed_two_qubit(np, local, first: int, second: int, n: int):
    dimension = 1 << n
    matrix = np.zeros((dimension, dimension), dtype=complex)
    clear = ~((1 << first) | (1 << second))
    for column in range(dimension):
        local_column = ((column >> first) & 1) | (((column >> second) & 1) << 1)
        for local_row in range(4):
            row = (column & clear) | ((local_row & 1) << first) | (((local_row >> 1) & 1) << second)
            matrix[row, column] = local[local_row, local_column]
    return matrix


def hamiltonian_unitary(np, terms: list[tuple[float, int, int]]):
    hamiltonian = sum(coefficient * pauli_matrix(np, x, z, 2) for coefficient, x, z in terms)
    energies, vectors = np.linalg.eigh(hamiltonian)
    return (vectors * np.exp(-1j * energies)) @ vectors.conj().T


def inverse_witness_check(np) -> dict:
    n = 4
    dimension = 1 << n
    eta = 0.82
    # First correlate the middle sites. Only in the second layer do the selected
    # endpoint input cones grow, to disjoint regions {0,1} and {2,3}.
    middle = hamiltonian_unitary(np, [(0.31, 3, 0), (0.23, 0, 1), (0.17, 1, 3)])
    left = hamiltonian_unitary(np, [(0.27, 2, 1), (0.19, 3, 3), (0.13, 0, 2)])
    right = hamiltonian_unitary(np, [(0.22, 1, 2), (0.11, 1, 1), (0.37, 2, 3)])
    layers = [
        embed_two_qubit(np, middle, 1, 2, n),
        embed_two_qubit(np, left, 0, 1, n) @ embed_two_qubit(np, right, 2, 3, n),
    ]
    operators = site_paulis(np, n, n)
    identity = np.eye(dimension)
    rho = np.ones((dimension, dimension), dtype=complex) / dimension
    for layer in layers:
        rho = depolarize(np, layer @ rho @ layer.conj().T, eta, operators)

    original = [pauli_matrix(np, 1 << q, 0, n) for q in (0, 3)]
    witnesses = []
    for observable in original:
        for layer in layers:
            observable = inverse_depolarize(np, layer @ observable @ layer.conj().T, eta, operators)
        witnesses.append(observable)

    def heisenberg(observable):
        for layer in reversed(layers):
            observable = depolarize(np, observable, eta, operators)
            observable = layer.conj().T @ observable @ layer
        return observable

    single_residual = max(float(np.linalg.norm(heisenberg(observable) - initial)) for observable, initial in zip(witnesses, original))
    product_residual = float(np.linalg.norm(heisenberg(witnesses[0] @ witnesses[1]) - original[0] @ original[1]))
    commutator_residual = float(np.linalg.norm(witnesses[0] @ witnesses[1] - witnesses[1] @ witnesses[0]))
    support_residual = 0.0
    for observable, outside in zip(witnesses, ((2, 3), (0, 1))):
        for site in outside:
            conditional = (observable + sum(operator @ observable @ operator for operator in operators[site])) / 4
            support_residual = max(support_residual, float(np.linalg.norm(observable - conditional)))

    kappa = 2 / eta - 1
    # Each selected cone has size one in round 1 and size two in round 2.
    norm_bound = kappa ** 3
    witness_norms = [hermitian_norm(np, observable) for observable in witnesses]
    require(max(witness_norms) <= norm_bound + NUMERICAL_TOLERANCE, "Inverse-witness norm bound failed")
    require(max(single_residual, product_residual, commutator_residual, support_residual) < NUMERICAL_TOLERANCE, "Inverse-witness identity failed")
    bias = 1 / norm_bound
    actual_probabilities = []
    expected_probabilities = []
    target_probabilities = []
    for signs in itertools.product((-1, 1), repeat=2):
        effects = [(identity + sign * observable / norm_bound) / 2 for sign, observable in zip(signs, witnesses)]
        effect = effects[0] @ effects[1]
        actual_probabilities.append(float(np.trace(rho @ effect).real))
        expected_probabilities.append(math.prod((1 + sign * bias) / 2 for sign in signs))
        target_probabilities.append(float(np.trace(effect).real / dimension))
    moment_residual = max(abs(a - b) for a, b in zip(actual_probabilities, expected_probabilities))
    target_residual = max(abs(p - 0.25) for p in target_probabilities)
    require(max(moment_residual, target_residual) < NUMERICAL_TOLERANCE, "Joint POVM distribution failed")
    povm_tv = sum(abs(p - 0.25) for p in actual_probabilities) / 2
    output_trace_distance = trace_distance(np, rho, identity / dimension)
    require(povm_tv <= output_trace_distance + NUMERICAL_TOLERANCE, "POVM data processing failed")

    tensor = rho.reshape(4, 4, 4, 4)  # B,A,B',A' because qubits 0,1 are low bits.
    rho_left = np.trace(tensor, axis1=0, axis2=2)
    rho_right = np.trace(tensor, axis1=1, axis2=3)
    region_correlation = float(np.linalg.norm(rho - np.kron(rho_right, rho_left)))
    require(region_correlation > 1e-4, "Fixture did not create correlated final regions")
    return {
        "qubits": n,
        "noisy_rounds": len(layers),
        "eta": eta,
        "selected_input_sites": [0, 3],
        "selected_final_cones": [[0, 1], [2, 3]],
        "norm_bound": norm_bound,
        "actual_witness_norms": witness_norms,
        "single_inverse_identity_frobenius_residual": single_residual,
        "product_inverse_identity_frobenius_residual": product_residual,
        "commutator_frobenius_residual": commutator_residual,
        "outside_cone_support_frobenius_residual": support_residual,
        "independent_bit_bias": bias,
        "joint_probabilities_sign_order_minus_plus": actual_probabilities,
        "joint_product_distribution_residual": moment_residual,
        "maximally_mixed_target_distribution_residual": target_residual,
        "povm_total_variation": povm_tv,
        "bhattacharyya_lower_bound": 1 - math.exp(-2 / (8 * norm_bound ** 2)),
        "output_half_trace_distance": output_trace_distance,
        "final_regions_product_state_frobenius_distance": region_correlation,
    }


def passive_binomial_checks(np) -> list[dict]:
    cases = []
    for n, eta, depth in ((1, 0.91, 3), (2, 0.91, 3), (4, 0.91, 3), (3, 0.75, 2)):
        survival = eta ** depth
        p0 = (1 + 3 * survival) / 4
        one = np.array([p0] + [(1 - survival) / 4] * 3)
        distribution = np.array([1.0])
        for _ in range(n):
            distribution = np.outer(distribution, one).reshape(-1)
        direct = float(np.sum(np.abs(distribution - 4 ** (-n))) / 2)
        binomial = passive_binomial_error(n, survival)
        lower = 1 - math.exp(-n * survival ** 2 / 8)
        upper = min(1.0, math.sqrt((1 + 3 * survival ** 2) ** n - 1) / 2)
        require(abs(direct - binomial) < NUMERICAL_TOLERANCE, "Passive binomial reduction failed")
        require(lower <= direct + NUMERICAL_TOLERANCE and direct <= upper + NUMERICAL_TOLERANCE, "Passive finite error bounds failed")
        cases.append({
            "qubits": n,
            "eta": eta,
            "depth": depth,
            "direct_pauli_half_diamond": direct,
            "binomial_total_variation": binomial,
            "finite_lower_bound": lower,
            "finite_upper_bound": upper,
        })
    return cases


def compare_expected(actual, expected, path="root") -> None:
    if isinstance(expected, dict):
        require(isinstance(actual, dict) and actual.keys() == expected.keys(), f"Baseline keys differ at {path}")
        for key in expected:
            compare_expected(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        require(isinstance(actual, list) and len(actual) == len(expected), f"Baseline list differs at {path}")
        for index, (value, reference) in enumerate(zip(actual, expected)):
            compare_expected(value, reference, f"{path}[{index}]")
    elif isinstance(expected, float):
        require(isinstance(actual, (float, int)) and math.isclose(actual, expected, rel_tol=1e-9, abs_tol=NUMERICAL_TOLERANCE), f"Baseline float differs at {path}: {actual} vs {expected}")
    else:
        require(actual == expected, f"Baseline value differs at {path}: {actual} vs {expected}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save the computed JSON report to this path")
    parser.add_argument("--write-expected", action="store_true", help="Replace the expected report after all mathematical checks pass")
    parser.add_argument("--json", action="store_true", help="Print the full computed JSON report")
    args = parser.parse_args()
    try:
        import numpy as np
    except ImportError as exc:
        raise SystemExit("NumPy is required for the independent dense checks; install verification/requirements.txt") from exc

    line2 = line_certificate(2, LINE2)
    line3 = line_certificate(3, LINE3)
    require(line3[0]["branch_weight_minimum"] == 4, "Three-site branch certificate changed")
    require(line3[0]["branch_weight_histogram"] == {4: 45, 6: 18}, "Three-site exact histogram changed")
    line_data = {2: line2, 3: line3}
    report = {
        "schema_version": 1,
        "line_certificates": [line2[0], line3[0]],
        "checkpoint_checks": [
            checkpoint_check((2, 3), line_data, True),
            checkpoint_check((3, 3), line_data, True),
            checkpoint_check((2, 2, 2), line_data, True),
            checkpoint_check((3, 3, 3), line_data, False),
        ],
        "noisy_clifford": dense_clifford_checks(np, line3[1]),
        "nonclifford_inverse_witness": inverse_witness_check(np),
        "passive_binomial_checks": passive_binomial_checks(np),
        "status": "PASS",
    }
    # JSON normalizes integer dictionary keys so comparison matches the file.
    rendered = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    normalized = json.loads(rendered)
    if args.write_expected:
        EXPECTED.write_text(rendered, encoding="utf-8")
    else:
        require(EXPECTED.exists(), "Expected report missing; do not silently create a baseline")
        compare_expected(normalized, json.loads(EXPECTED.read_text(encoding="utf-8")))
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    if args.json:
        print(rendered, end="")
    else:
        exhaustive = sum(case["nonidentity_paulis_checked"] for case in report["checkpoint_checks"] if case["exhaustive"])
        sampled = sum(case["nonidentity_paulis_checked"] for case in report["checkpoint_checks"] if not case["exhaustive"])
        print("PASS: exact line certificates and recursive checkpoint checks")
        print(f"  {exhaustive:,} exhaustive checkpoint inputs; {sampled:,} labeled sample inputs")
        print("PASS: actual noisy Clifford paths, dense Choi matrices, and Pauli chi-square identities")
        print("PASS: non-Clifford inverse witnesses and joint POVM product moments")
        print("PASS: passive Pauli-distribution versus binomial error formula")
        print(f"{'Wrote' if args.write_expected else 'Matched'} {EXPECTED.name}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
