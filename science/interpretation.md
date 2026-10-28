# Information spreading and irreversible loss

A unitary circuit preserves information. Local noise removes it. The result of combining them depends on where the information is stored while the noise acts.

The [main theorems](model.md) quantify the fastest complete mixing of an unknown register under a fixed local depolarizing channel. On a regular lattice, the optimal depth is the $`(d+1)`$th root of $`\log n`$; with unrestricted pair connectivity it is $`\log\log n`$. The comparison uses the entire quantum channel, including reference correlations, and does not supply initialized qubits or discard any output.

## Why control can accelerate a fixed bath

For a Pauli observable $`P`$,

```math
\mathcal D_\eta^{\otimes n}(P)=\eta^{w(P)}P.
```

A correlation supported on many qubits is exposed to independent noise on each of those sites. Its coefficient therefore decays faster per round than a single-site coefficient. Clifford control changes the support while keeping a single Pauli path, so its accumulated attenuation is exactly

```math
\eta^{\sum_{\ell}w(P_\ell)}.
```

This connects operator spreading with information loss. The mechanism itself is established in earlier noisy-circuit work, including [Quek et al.](../references/RELATED_WORK.md#quek2024). The question resolved here is how fast **complete-channel** mixing can occur under bounded local gate layers, and whether that speed can be attained with all physical qubits initially unknown.

A subtlety appears when every qubit is an input. A Clifford permutes the entire Pauli basis. At any single time, some input Pauli must be mapped to a single-site output Pauli. Thus a unitary cannot make every nonidentity Pauli have large final weight. The construction instead forces every Pauli to have a large **sum of weights at selected times**. Initial waiting suppresses operators that begin with large weight, and later waiting suppresses operators that acquire it during control. The recursive coordinate sequence makes this alternative hold across a spatial block.

## The causal origin of the dimensional exponent

After $`\ell`$ nearest-neighbor layers in $`d`$ dimensions, a local input can influence at most order $`\ell^d`$ sites. The upper bound on accumulated volume through depth $`D`$ scales as

```math
\sum_{\ell=1}^{D}\ell^d=\Theta_d(D^{d+1}).
```

This alone is an intuition, rather than a trace-distance proof. The [inverse-observable argument](causal_bound.md) makes it operational. It constructs bounded final observables whose expectation values still encode initial local bits. Disjoint full causal histories allow these observables to be measured jointly with exactly independent biases on the product input used in the converse.

There are at least order $`n/D^d`$ separated histories. Their individual biases can be as small as an exponential in the negative spacetime volume, yet sufficiently many such biases remain distinguishable together. The necessary balance has the form

```math
\frac{n}{\mathrm{poly}(D)}
\exp[-O_{d,\eta}(D^{d+1})]=O_\epsilon(1),
```

which forces $`D^{d+1}=\Omega(\log n)`$.

The [upper construction](geometric_construction.md) reaches the same scale. A block of side $`m`$ contains order $`m^d`$ qubits. A fixed number of coordinate-line stages ensures volume-proportional total checkpoint weight for every Pauli. Waiting order $`m`$ rounds at those checkpoints supplies attenuation exponential in $`m^{d+1}`$. The control itself also takes order $`m`$ depth. Blocks of side order $`(\log n)^{1/(d+1)}`$ then mix the complete register.

## Unrestricted connectivity changes cone growth

With unrestricted pairs, a two-qubit gate layer can at most double an input cone. Its accumulated size is bounded by an exponential in depth, rather than a power. The same inverse-observable argument therefore gives a logarithm of a logarithm.

The matching [unrestricted-connectivity construction](unrestricted_connectivity.md) uses logarithmic-size blocks. Its imported spreading theorem supplies a logarithmic-depth Clifford within each block. A constant number of noise rounds before and after that circuit suppresses every Pauli enough to mix all blocks jointly. The exact primary dependency is [Anand et al., Theorem 3.4](../references/RELATED_WORK.md#anand2026).

The architecture changes how rapidly information can be exposed to independent noise. The local noise strength and complete-channel target remain the same.

## Global accuracy and a local relaxation time

Under passive depolarization, each local Pauli multiplier is $`\eta^D`$. A single qubit therefore approaches equilibrium in a number of rounds independent of register size, for fixed local accuracy.

The global requirement is stronger. Small biases on many sites can be distinguished jointly, so passive complete mixing requires

```math
D_{\mathrm{pass}}=
\frac{\log n}{2\log(1/\eta)}+O_{\eta,\epsilon}(1).
```

The [exact passive error](passive.md) is a distance between two binomial distributions. The controlled laws improve this global scale. They should not be read as saying that a local observable takes $`\log n`$ rounds to relax.

## What has been counted

| Resource or requirement | Treatment |
|---|---|
| Physical qubits | Exactly the $`n`$ arbitrary input qubits |
| Quantum reference | Arbitrary input entanglement is included in the error |
| Output registers | Every physical qubit is retained |
| Elementary controls | Disjoint one- or two-qubit gates per charged round |
| Idle time | Counted, with noise on every site |
| Noise during compiled gates | Included after every elementary gate layer |
| Randomness for construction | A circuit may be selected offline; execution uses that fixed circuit |
| Final inverse Clifford | Used only in the analysis, never executed |
| Classical circuit design | Separate from the optimized execution-depth resource |
| Gate count | An upper bound is supplied; its optimality is not claimed |

The unknown input can contain arbitrary entropy and correlations. Since there are no extra qubits, the result does not rely on a supplied mixed workspace whose purification is omitted from the error criterion.

## Limits of the statement

**Noise and time.** The theorem assumes independent identical depolarization after each gate layer. A continuous Hamiltonian acting simultaneously with noise generally produces a different map. A physical elapsed-time interpretation requires a device model realizing the prescribed rounds.

**Geometry.** The upper bound applies to regular filled boxes admitting the stated block tiling. The converse applies more broadly to fixed-density lattice subsets. A long thin region can have fewer available propagation directions than its ambient lattice.

**Asymptotic parameters.** Dimension, noise strength, and target global error are fixed while the number of qubits grows. The finite bounds retain their parameter dependence, but the constants have not been optimized. The results do not establish a finite-device crossover advantage.

**Meaning of erasure.** The target is the infinite-temperature state $`\tau_n`$. This is complete loss of information from the retained register, not initialization to a pure state. The analysis does not assign heat or work costs and does not compare quantum and classical computational power.

The two noise endpoints are outside the fixed-parameter theorem: $`\eta=0`$ mixes the register exactly in one noise round, while $`\eta=1`$ supplies no dissipative mechanism.

## Evidence and reading route

The asymptotic laws follow from the written proofs and the stated imported theorems. The [finite examples](finite_examples.md) make the Pauli spreading, checkpoint accumulation, and reference-sensitive error reduction explicit on small registers. The [verification suite](../verification/README.md) checks those finite identities and selected dense-channel calculations; it does not replace the arbitrary-size converse or the source theorem used for unrestricted connectivity.

Read [related work](../references/RELATED_WORK.md) to separate the inherited mechanisms and compilation results from the optimal-depth conclusions.

