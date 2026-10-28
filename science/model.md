# Complete mixing under local control

A noisy quantum register loses information even when no gates are applied. The rate of this loss changes when reversible control spreads information across the register. The question here is the minimum circuit depth needed to erase **every possible input**, including its correlations with an external system, while keeping every physical output.

This page fixes the operational model and the exact scope of the results. The proofs are organized into [channel distance](channel_distance.md), [causal lower bounds](causal_bound.md), [geometric constructions](geometric_construction.md), [unrestricted connectivity](unrestricted_connectivity.md), and the [passive benchmark](passive.md).

## Register, noise, and one charged round

The register contains $`n`$ qubits with Hilbert space $`\mathcal H_n=(\mathbb C^2)^{\otimes n}`$. Its input is arbitrary and may be entangled with an inaccessible reference $`R`$. All $`n`$ physical qubits are inputs to the channel. There is no separately initialized workspace.

For a fixed retention parameter $`0<\eta<1`$, one-qubit depolarization is

```math
\mathcal D_\eta(X)
=
\eta X+(1-\eta)\mathrm{Tr}(X)\frac{I_2}{2},
\qquad
\mathcal N_\eta=\mathcal D_\eta^{\otimes n}.
```

A larger $`\eta`$ means weaker noise. Throughout, $`\lambda=-\log\eta>0`$, and logarithms are natural unless a base is written explicitly.

A charged round consists of a layer $`U_\ell`$ of disjoint one- or two-qubit unitary gates, followed by $`\mathcal N_\eta`$ on **every site**, including idle sites. With $`\mathrm{Ad}_U(X)=UXU^\dagger`$, a depth-$`D`$ protocol implements

```math
\Psi_D
=
(\mathcal N_\eta\circ\mathrm{Ad}_{U_D})
\circ\cdots\circ
(\mathcal N_\eta\circ\mathrm{Ad}_{U_1}).
```

Identity layers are allowed and count as rounds. The control sequence is fixed before execution. It may depend on the register, architecture, noise parameter, and desired accuracy, but does not depend on the unknown input. Gates can be arbitrary unitaries in the lower bound. The upper constructions use Clifford gates.

There are no auxiliary qubits, measurements, feedback, resets, discarded registers, or fresh random control choices during execution. The depolarizing channel is the specified coupling to an unobserved environment. Its environment is not an output of the task. These assumptions make the resource being optimized precise: elementary parallel gate-and-noise rounds under a fixed bath.

## Whole-register error

Write $`\tau_n=I_{2^n}/2^n`$ and define the maximally mixed replacer by

```math
\mathcal R_n(X)=\mathrm{Tr}(X)\tau_n.
```

The complete mixing error is

```math
\delta(\Psi_D)
=
\frac12\|\Psi_D-\mathcal R_n\|_\diamond.
```

For a difference of quantum channels, this equals the largest output half-trace distance over input states with a reference. In particular, the target condition is

```math
\frac12
\left\|
(\Psi_D\otimes\mathrm{id}_R)(\rho_{AR})
-\tau_n\otimes\rho_R
\right\|_1
\le \epsilon
```

for every $`\rho_{AR}`$. A reference of dimension $`2^n`$ suffices for the maximization. The channel conventions and operational meaning of this norm follow the standard framework in [Watrous](../references/RELATED_WORK.md#watrous2018).

The output must approach the maximally mixed state **and** lose its input-reference correlations. Uniform outcomes in one measurement basis or small expectations of a selected set of local observables do not by themselves imply this condition.

Every allowed round is unital, so it preserves $`\tau_n`$. Appending an identity/noise round cannot increase $`\delta`$, by trace-norm contractivity with a reference. This observation permits circuits on different blocks to be padded to the same depth.

## Architectures and optimization

For an interaction graph $`G`$, let

```math
D_{\min}(G,\eta,\epsilon)
=
\min\{D:\text{ an allowed circuit on }G
\text{ has }\delta(\Psi_D)\le\epsilon\}.
```

Two architectures are considered.

- **Geometric locality.** One qubit occupies each vertex of the filled box $`[L]^d`$, with nearest-neighbor gates and fixed integer dimension $`d\ge1`$. Here $`n=L^d`$. The same upper construction works on rectangular boxes that can be tiled into blocks with comparable side lengths at the required scale. The lower bound applies to arbitrary occupied subsets of the lattice at this fixed site density.
- **Unrestricted pair connectivity.** Any two qubits may interact in a layer, subject to disjointness of the pairs. This still permits only two-qubit gates, not a free global unitary.

The geometric matching statement concerns growing regular regions. An arbitrarily thin or irregular subset of a higher-dimensional lattice need not have the same attainable exponent.

## Theorem G: the geometric optimum

Fix $`d\ge1`$, $`0<\eta<1`$, and $`0<\epsilon<1`$, independently of $`n`$. On the filled box $`[L]^d`$,

```math
D_{\min}([L]^d,\eta,\epsilon)
=
\Theta_{d,\eta,\epsilon}
\!\left((\log n)^{1/(d+1)}\right),
\qquad n=L^d\longrightarrow\infty.
```

The lower bound holds for arbitrary allowed unitary circuits. The matching upper uses a fixed Clifford circuit on precisely the $`n`$ input qubits and retains all of them. It uses at most $`O_{d,\eta,\epsilon}(n(\log n)^{1/(d+1)})`$ elementary gates. The gate-count upper is a resource bound for the construction; gate-count optimality is not asserted.

The [causal converse](causal_bound.md) limits the accumulated spacetime support of inverse observables. The [geometric construction](geometric_construction.md) makes every nonidentity Pauli accumulate sufficient support at a finite sequence of boundaries between stages, and then lets the local noise act there. Its imported implementation ingredient is linear-depth nearest-neighbor Clifford synthesis from [Maslov and Yang](../references/RELATED_WORK.md#maslov2023).

## Theorem A: the unrestricted-connectivity optimum

Fix $`0<\eta<1`$ and $`0<\epsilon<1`$. On the complete interaction graph,

```math
D_{\min}(K_n,\eta,\epsilon)
=
\Theta_{\eta,\epsilon}(\log\log n).
```

Again all $`n`$ physical qubits are arbitrary inputs, no auxiliaries are supplied, and every output is retained. A matching construction uses $`O_{\eta,\epsilon}(n\log\log n)`$ gates.

The lower bound is a consequence of bounded fan-in. The no-auxiliary upper uses the precise Pauli-spreading bound of [Anand et al.](../references/RELATED_WORK.md#anand2026), followed by the complete-channel conversion proved in [unrestricted connectivity](unrestricted_connectivity.md). That spreading theorem is an imported ingredient. The geometric result above does not depend on it.

## Proposition P: the passive benchmark

With every $`U_\ell=I`$, the exact channel is $`\mathcal D_{\eta^D}^{\otimes n}`$. Its minimum depth obeys

```math
D_{\mathrm{pass}}(n,\eta,\epsilon)
=
\frac{\log n}{2\log(1/\eta)}
+
O_{\eta,\epsilon}(1).
```

The [passive account](passive.md) proves finite upper and lower bounds and gives an exact binomial expression for its diamond error. This compares the controlled protocols with the same physical register, local noise strength, and complete-channel accuracy.

## Mechanism and boundaries

The physical quantity behind the bounds is the total support exposed to noise over time. A Pauli of weight $`w`$ loses a factor $`\eta^w`$ per noise round. Local circuits can make this support grow, but finite propagation speed limits its accumulated size. The upper and lower bounds meet at this spacetime scale.

The exponents hold with dimension, noise, and global error fixed. The proof supplies finite parameter inequalities, but does not claim optimal constants or a uniform joint limit as noise vanishes, accuracy tends to zero, or dimension grows. Offline selection and synthesis of the fixed control circuit are distinct from its execution depth.

The model is discrete. A local depolarizing channel applied after each gate layer is not automatically the channel generated by simultaneous bounded Hamiltonian control and noise. The result concerns loss of information to an infinite-temperature state. It is not a theorem about cooling to a pure state or the heat and work cost of erasure.

For the relation to established noisy-circuit mixing mechanisms, see [related work](../references/RELATED_WORK.md). For the physical synthesis and interpretation, continue to [information spreading and loss](interpretation.md).

