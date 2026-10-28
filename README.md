# Quantum Mixing Depth

**How quickly can local noise erase an entire unknown quantum register when coherent control is allowed?**

This project determines the optimal number of noisy gate rounds for complete mixing. The target is the maximally mixed state on the whole register, with all input correlations with an external reference removed to a fixed global accuracy. Every physical qubit is initially an arbitrary input, and every output is retained.

| Architecture or protocol | Optimal depth |
|---|---:|
| Passive independent depolarization | $`\Theta(\log n)`$ |
| Nearest-neighbor chain | $`\Theta((\log n)^{1/2})`$ |
| Nearest-neighbor square lattice | $`\Theta((\log n)^{1/3})`$ |
| Nearest-neighbor cubic lattice | $`\Theta((\log n)^{1/4})`$ |
| Unrestricted pair connectivity | $`\Theta(\log\log n)`$ |

These are fixed-noise, fixed-error asymptotic statements. More generally, on a filled regular $`d`$-dimensional lattice,

```math
D_{\min}(n)
=
\Theta_{d,\eta,\epsilon}
\!\left((\log n)^{1/(d+1)}\right).
```

One round applies disjoint one- or two-qubit unitaries, followed by independent depolarization of retention $`0<\eta<1`$ on every qubit. The error criterion is

```math
\frac12\|\Psi_D-\mathcal R_n\|_\diamond\le\epsilon,
\qquad
\mathcal R_n(X)=\operatorname{Tr}(X)\frac{I_{2^n}}{2^n}.
```

The lower bounds allow arbitrary unitary gates. Matching upper constructions use fixed Clifford circuits, with **no auxiliary qubits, measurements, resets, discarded outputs, or fresh random control choices during execution**.

## Why geometry sets the rate

A local Pauli operator can spread over order $`D^d`$ sites in depth $`D`$. Its accumulated exposure to independent noise is therefore limited by a spacetime volume of order $`D^{d+1}`$. The converse turns this causal restriction into a physical distinguishability bound using inverse-channel observables on disjoint histories.

The construction reaches that scale by arranging Clifford circuits along coordinate lines. Every nonidentity Pauli acquires enough total weight across selected stage boundaries, where local noise suppresses it. A complete-channel calculation then combines many blocks while allowing arbitrary entanglement between them and an external reference.

Scrambling-enhanced noise and rapidly mixing noisy circuits are [established prior mechanisms](references/RELATED_WORK.md#quek2024). The result developed here is the matching controlled mixing optimum, its dimensional dependence, and its whole-register guarantee. The geometric upper imports [linear-depth Clifford synthesis](references/RELATED_WORK.md#maslov2023). The unrestricted-connectivity upper additionally imports the precise [Pauli-spreading theorem of Anand et al.](references/RELATED_WORK.md#anand2026).

## Read the science

Begin with the [model and exact claims](science/model.md). The [physical interpretation](science/interpretation.md) connects the proof mechanisms and resource assumptions.

| To inspect | Scientific account |
|---|---|
| Input, noise, architecture, accuracy, and quantifiers | [Model](science/model.md) |
| Exact Pauli-channel diamond distance and block composition | [Channel distance](science/channel_distance.md) |
| Arbitrary-unitary lower bounds from causal histories | [Causal bound](science/causal_bound.md) |
| Matching no-auxiliary construction on regular lattices | [Geometric construction](science/geometric_construction.md) |
| Matching logarithm-of-logarithm depth with unrestricted pairs | [Unrestricted connectivity](science/unrestricted_connectivity.md) |
| Exact passive error and its logarithmic mixing scale | [Passive depolarization](science/passive.md) |
| Concrete Pauli circuits and dense-channel calculations | [Finite examples](science/finite_examples.md) |
| Primary dependencies and the closest operational comparisons | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

[The LLM reading guide](llms.txt) maps questions to the authoritative statements and proofs.

## Reproduce the finite checks

From the repository root, install the documented dependency and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite checks exact Pauli propagation, recursive checkpoint weights, noisy-channel identities, the passive binomial reduction, and a non-Clifford inverse-witness example. [Verification documentation](verification/README.md) specifies the examples, numerical tolerances, expected outputs, and what the checks establish. Finite enumeration and numerical residuals complement the written proofs; they do not prove the asymptotic laws.

## Scope

The time resource is discrete gate-and-noise rounds. A continuously driven Hamiltonian with simultaneous noise is a separate dynamical model. Geometric achievability is proved on regular filled regions admitting the stated tiling, while the lower bound also covers arbitrary fixed-density lattice subsets.

Dimension, noise strength, and complete-channel error are fixed in the asymptotic statements. Constants are conservative. Circuit execution uses a selected fixed control sequence; classical design cost is a separate resource. The target is an infinite-temperature state, so no pure-state initialization or heat/work-cost claim is made.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

