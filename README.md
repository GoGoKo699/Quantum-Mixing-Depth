# Quantum Mixing Depth

**How quickly can local noise erase an entire unknown quantum register when coherent control is allowed?**

This project determines the optimal number of noisy gate rounds for complete mixing. The target is the maximally mixed state on the whole register, with all input correlations with an external reference removed to a fixed global accuracy. Every physical qubit is initially an arbitrary input, and every output is retained.

| Architecture or protocol | Optimal depth |
|---|---:|
| [Regular lattice, noise only at fixed contacts](science/stationary_contacts.md) | $`\Theta(\max\{A,(A\ln n)^{1/(d+1)}\})`$ |
| Passive independent depolarization | $`\Theta(\log n)`$ |
| Nearest-neighbor chain | $`\Theta((\log n)^{1/2})`$ |
| Nearest-neighbor square lattice | $`\Theta((\log n)^{1/3})`$ |
| Nearest-neighbor cubic lattice | $`\Theta((\log n)^{1/4})`$ |
| Unrestricted pair connectivity | $`\Theta(\log\log n)`$ |

These are fixed-noise, fixed-error asymptotic statements. The first row has one noisy contact per $`A`$ sites arranged on a regular grid. The remaining rows use uniform noise. With noise on every site of a filled regular $`d`$-dimensional lattice,

```math
D_{\min}(n)
=
\Theta_{d,\eta,\epsilon}
\!\left((\log n)^{1/(d+1)}\right).
```

One uniform-noise round applies disjoint one- or two-qubit unitaries, followed by independent depolarization of retention $`0<\eta<1`$ on every qubit. The error criterion is

```math
\frac12\lVert \Psi_D-\mathcal R_n\rVert_\diamond\le\epsilon,
\qquad
\mathcal R_n(X)=\mathrm{Tr}(X)\frac{I_{2^n}}{2^n}.
```

The lower bounds allow arbitrary unitary gates. Matching upper constructions use fixed Clifford circuits, with **no auxiliary qubits, measurements, resets, discarded outputs, or fresh random control choices during execution**.

## Why geometry sets the rate

A local Pauli operator can spread over order $`D^d`$ sites in depth $`D`$. Its accumulated exposure to independent noise is therefore limited by a spacetime volume of order $`D^{d+1}`$. The converse turns this causal restriction into a physical distinguishability bound using inverse-channel observables on disjoint histories.

The construction reaches that scale by arranging Clifford circuits along coordinate lines. Every nonidentity Pauli acquires enough total weight across selected stage boundaries, where local noise suppresses it. A complete-channel calculation then combines many blocks while allowing arbitrary entanglement between them and an external reference.

Scrambling-enhanced noise and rapidly mixing noisy circuits are [established prior mechanisms](references/RELATED_WORK.md#quek2024). The result developed here is the matching controlled mixing optimum, its dimensional dependence, and its whole-register guarantee. The geometric upper imports [linear-depth Clifford synthesis](references/RELATED_WORK.md#maslov2023). The unrestricted-connectivity upper additionally imports the precise [Pauli-spreading theorem of Anand et al.](references/RELATED_WORK.md#anand2026).

## When only the contacts are noisy

A contact grid has two limits. The total number of contact uses bounds how much information can be erased, while the number inside a causal cone bounds how fast a local input can lose its bias. Returning SWAP sweeps and Clifford spreading jointly attain both bounds. With one contact the optimal depth is $`\Theta(n)`$, compared with $`\Theta(n\ln n)`$ for SWAP-only transport. At the same contact count, packing equally spaced planes into a slab can change the depth from polylogarithmic to linear in the lattice side length. [Proof and comparisons](science/stationary_contacts.md)

## Run the lattice mixing circuit

1. **Plan the blocks and gates.** Start with the supplied unknown state on all lattice qubits. For stationary contacts, use the [contact-aligned tiling and sweep count](science/stationary_contacts.md#returning-sweeps-and-clifford-upper-bound), including its whole-cube case. Choose each length's [line Clifford](science/geometric_construction.md#lemma-line-branch-weight) in advance and [compile it into nearest-neighbor layers](science/geometric_construction.md#linear-depth-on-a-line).
2. **Run coordinate stages and noise checkpoints.** Run the blocks in parallel using the [coordinate-line order](science/geometric_construction.md#coordinate-line-recursion), which is axes 1, 2, 1 in two dimensions. Apply independent depolarization at the fixed contacts after every gate or idle layer. At each checkpoint, including before the first and after the last stage, run the planned number of sweeps in parallel across all contact cells. Each sweep follows a serpentine path starting at its contact. Alternate SWAPs on pairs 1–2, 3–4, and so on, then 2–3, 4–5, and so on, for twice the cell size in rounds. Each wire label returns to its starting site after two visits to the contact.
3. **Return all physical outputs.** The gate and noise rounds alone mix the register. For any input and idle reference, the joint output is within the chosen half-trace-distance error of the maximally mixed register tensored with the unchanged reference state. No measurements or classical output processing are required.

With noise on every site, use the [uniform-noise tiling](science/geometric_construction.md#tiling-the-physical-register) and its prescribed idle rounds at each checkpoint. Every site depolarizes after each gate or idle layer. The [three-qubit line example](science/finite_examples.md#1-an-exact-three-qubit-line-example) and [two-site contact example](science/finite_examples.md#5-stationary-contact-examples) show finite gate sequences and their errors.

## Read the science

Begin with the [model and exact claims](science/model.md). The [physical interpretation](science/interpretation.md) connects the proof mechanisms and resource assumptions.

| To inspect | Scientific account |
|---|---|
| Input, noise, architecture, accuracy, and quantifiers | [Model](science/model.md) |
| Exact Pauli-channel diamond distance and block composition | [Channel distance](science/channel_distance.md) |
| Arbitrary-unitary lower bounds from causal histories | [Causal bound](science/causal_bound.md) |
| Matching no-auxiliary construction on regular lattices | [Geometric construction](science/geometric_construction.md) |
| Sparse noise, transport-only benchmark, and the effect of contact placement | [Stationary contacts](science/stationary_contacts.md) |
| Matching logarithm-of-logarithm depth with unrestricted pairs | [Unrestricted connectivity](science/unrestricted_connectivity.md) |
| Exact passive error and its logarithmic mixing scale | [Passive depolarization](science/passive.md) |
| Concrete Pauli circuits and dense-channel calculations | [Finite examples](science/finite_examples.md) |
| Primary dependencies and the closest operational comparisons | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

## Learn the project

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Begin with the [Watrous bridge](learning/WATROUS_BRIDGE.md), which maps selected sections to the project, translates channel and norm conventions, and explains the steps supplied by the mixing proofs.

The [30-milestone understanding map](learning/MILESTONES.md) gives the connected route. Its background/preliminaries phase builds from individual states and operations to the complete operational question. Its narrative/innovation phase connects Pauli attenuation, causal witnesses, geometric constructions, and the unrestricted-connectivity comparison into the optimal-depth result. Each milestone has an understanding target, earlier dependencies, conceptual connections, and direct source pointers.

The [three-qubit line example](science/finite_examples.md#1-an-exact-three-qubit-line-example) provides a concrete circuit to inspect alongside this route. The scientific pages above remain the authoritative homes of the exact statements and proofs.

[The LLM reading guide](llms.txt) maps scientific questions and study routes to those files.

## Reproduce the finite checks

From the repository root, install the documented dependency and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite checks exact Pauli propagation, recursive checkpoint weights, noisy-channel identities, the passive binomial reduction, non-Clifford inverse witnesses, returning contact sweeps, and finite depth comparisons. [Verification documentation](verification/README.md) specifies the examples, numerical tolerances, expected outputs, and what the checks establish. Finite enumeration and numerical residuals complement the written proofs; they do not prove the asymptotic laws.

## Scope

The time resource is discrete gate-and-noise rounds. A continuously driven Hamiltonian with simultaneous noise is a separate dynamical model. The uniform-noise geometric upper uses regular filled regions admitting the stated tiling. The stationary-contact law uses filled cubes and aligned contact grids.

Dimension, noise strength, and complete-channel error are fixed in the asymptotic statements. Constants are conservative. Circuit execution uses a selected fixed control sequence; classical design cost is a separate resource. The target is an infinite-temperature state, so no pure-state initialization or heat/work-cost claim is made.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

