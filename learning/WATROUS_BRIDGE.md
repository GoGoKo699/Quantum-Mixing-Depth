# From Watrous to optimal quantum mixing depth

A noisy qubit loses its initial polarization. In a large register, many small residual signals can still reveal the input through a joint measurement. Reversible gates can change how quickly those signals encounter the noise by spreading them across more sites. This project asks for the least circuit depth that suppresses every input signal to a prescribed global accuracy, including correlations with an external reference, while retaining every physical output.

The selected educational anchor is **John Watrous, _The Theory of Quantum Information_, Cambridge University Press, 2018**. Section and theorem numbers below refer to the author's prepublication text, whose front matter is dated January 2018. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the published book as appearing in April 2018 and provides the [contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf), individual chapters, and [errata](https://cs.uwaterloo.ca/~watrous/TQI/TQI.errata.pdf). The text is linked here, not reproduced.

Watrous provides the language of states, channels, measurements, and channel distance. The connections below explain how that language supports the mixing proofs. The [30-milestone map](MILESTONES.md) organizes the complete understanding route. Exact claims and assumptions have their authoritative home in [the model](../science/model.md) and its linked proof pages.

## Targeted reading from the single anchor

Each entry is a focused lookup for a part of the project. The research dependencies used to obtain the depth laws are identified separately at the end of this bridge.

| Project connection | Watrous sections and results | Relevant milestones |
|---|---|---|
| Tensor operators, Pauli expansions, and witness norms | [Sections 1.1.2–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); norm duality and Hölder's inequality in Eqs. (1.173)–(1.174) | [M02](MILESTONES.md#m02), [M08](MILESTONES.md#m08) |
| Density operators, reductions, and reference systems | [Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | [M01](MILESTONES.md#m01), [M03](MILESTONES.md#m03) |
| Channels, adjoints, and Choi positivity | [Sections 2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); Definition 2.13 and Theorems 2.22 and 2.26 | [M04](MILESTONES.md#m04), [M10](MILESTONES.md#m10) |
| The maximally mixed replacement target | [Section 2.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), Eqs. (2.152)–(2.155) | [M05](MILESTONES.md#m05), [M13](MILESTONES.md#m13) |
| Physical measurements and residual distinguishability | [Sections 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Section 3.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), Theorem 3.4 and Proposition 3.5 | [M07](MILESTONES.md#m07), [M16](MILESTONES.md#m16) |
| Complete channel error and the sufficient reference dimension | [Sections 3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); Definition 3.43 and Theorems 3.46 and 3.51 | [M09](MILESTONES.md#m09), [M10](MILESTONES.md#m10) |
| Combining many weak distinguishability signals | [Section 3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); Definition 3.11, Proposition 3.16, and Theorem 3.33 | [M14](MILESTONES.md#m14), [M17](MILESTONES.md#m17) |
| Pauli mixtures and preservation of the maximally mixed state | [Sections 4.1.1–4.1.2 and 4.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) | [M05](MILESTONES.md#m05), [M10](MILESTONES.md#m10), [M27](MILESTONES.md#m27) |

The project supplies its own circuit-support arguments, Fourier chi-square calculation, geometric recursion, and conversion from a spreading theorem to complete mixing. These steps are developed below and in the corresponding science pages.

## Notation and the complete target

Watrous uses column vectors and adjoints. The project also uses Dirac notation. These represent the same finite-dimensional objects.

| Watrous notation or convention | Project notation or convention |
|---|---|
| Input space $`\mathcal X`$ | $`\mathcal H_n=(\mathbb C^2)^{\otimes n}`$, of dimension $`2^n`$ |
| Vector $`u`$ and rank-one state $`uu^*`$ | $`\lvert\psi\rangle`$ and $`\lvert\psi\rangle\langle\psi\rvert`$ |
| Operator or map adjoint $`A^*`$, $`\Phi^*`$ | $`A^\dagger`$, $`\Phi^\dagger`$ |
| Spectral norm $`\lVert A\rVert`$ | Operator norm $`\lVert A\rVert_\infty`$ |
| Frobenius norm $`\lVert A\rVert_2`$ | Hilbert–Schmidt norm $`\lVert A\rVert_2`$ |
| Completely mixed state $`\omega`$ and channel $`\Omega`$ | $`\tau_n=I/2^n`$ and $`\mathcal R_n(X)=\mathrm{Tr}(X)\tau_n`$ |
| Identity map $`\mathbf 1_{\mathrm{L}(\mathcal Z)}`$ | $`\mathrm{id}_R`$ when the space belongs to a reference |

Watrous's completely bounded trace norm, written with three vertical bars and subscript 1, is exactly the norm denoted $`\lVert\Phi\rVert_\diamond`$ here. The project's error includes a separate factor of one half:

```math
\delta(\Psi_D)=\frac12\lVert\Psi_D-\mathcal R_n\rVert_\diamond.
```

Theorems 3.46 and 3.51 make this a maximization over quantum input states on the register and a reference of dimension $`2^n`$. Applied to the channel difference, they give

```math
\delta(\Psi_D)
=\max_{\rho_{AR}}
\frac12\left\|
(\Psi_D\otimes\mathrm{id}_R)(\rho_{AR})
-\tau_n\otimes\rho_R
\right\|_1,
\qquad \dim R=2^n.
```

Pure joint states suffice for this maximum; including mixed states does not change it. The target leaves the reference marginal $`\rho_R`$ intact while removing all correlations between it and the register. In equal-prior discrimination between $`\Psi_D`$ and $`\mathcal R_n`$, the optimal success probability is $`(1+\delta(\Psi_D))/2`$. Thus the error parameter directly bounds residual distinguishability of the complete channel.

Three systems have different roles. The physical register $`A`$ contains all $`n`$ arbitrary input qubits and is retained at the output. The reference $`R`$ represents correlations that the mixing guarantee must handle; the control circuit never acts on it. An initialized auxiliary workspace would be an additional resource for implementing the protocol, and the model supplies none. The specified bath is the unobserved environment responsible for depolarization. Keeping all physical outputs refers to the register, not to that bath.

## Noise retention and charged rounds

The one-qubit map is

```math
\mathcal D_\eta(X)
=\eta X+(1-\eta)\mathrm{Tr}(X)\frac{I_2}{2},
\qquad 0<\eta<1.
```

Here $`\eta`$ measures retention: a larger value means weaker noise. For a traceless Pauli matrix, $`\mathcal D_\eta(P)=\eta P`$. A noise-strength convention written as $`(1-p)X+p\mathrm{Tr}(X)I_2/2`$ therefore has $`p=1-\eta`$. This $`p`$ is different from the total probability of a nonidentity Pauli error, which is $`3(1-\eta)/4`$.

Each charged round consists of disjoint one- or two-qubit gates followed by $`\mathcal D_\eta`$ on every site. An idle site receives the same noise, and an identity layer still costs one round. The depth counts this discrete sequence. It does not identify a noisy finite-duration entangling Hamiltonian with an ideal unitary followed by depolarization.

With $`\lambda=-\ln\eta>0`$, a coefficient multiplied by $`\eta^s`$ has attenuation $`e^{-\lambda s}`$. Natural logarithms are used in the depth estimates. The binary entropy $`H_2`$ appearing in Pauli-counting bounds uses base-two logarithms explicitly.

## Choi normalization and what a Choi test establishes

Watrous's Choi representation in Section 2.2.2 uses the unnormalized vector

```math
\lvert\Omega_n\rangle=\sum_{x\in\{0,1\}^n}
\lvert x\rangle_A\lvert x\rangle_R,
\qquad
J_{\mathrm W}(\Phi)
=(\Phi\otimes\mathrm{id}_R)
(\lvert\Omega_n\rangle\langle\Omega_n\rvert).
```

For a trace-preserving map, $`\mathrm{Tr}_A J_{\mathrm W}(\Phi)=I_R`$ and $`\mathrm{Tr}J_{\mathrm W}(\Phi)=2^n`$. The normalized Choi state used in the project's Bell-basis argument and dense verification is

```math
\lvert\Phi_n\rangle=2^{-n/2}\lvert\Omega_n\rangle,
\qquad
\omega_\Phi
=(\Phi\otimes\mathrm{id}_R)
(\lvert\Phi_n\rangle\langle\Phi_n\rvert)
=2^{-n}J_{\mathrm W}(\Phi).
```

In particular, $`\omega_{\mathcal R_n}=I_{AR}/4^n`$. Theorems 2.22 and 2.26 connect positivity and partial-trace constraints to a physical channel, with the normalization above kept explicit.

A maximally entangled input is one permitted test, so any channel obeys

```math
\frac12\lVert\omega_\Phi-\omega_{\mathcal R_n}\rVert_1
\le\frac12\lVert\Phi-\mathcal R_n\rVert_\diamond.
```

Equality requires an additional argument. For the Pauli channels used below, orthogonal Bell outputs attain a matching upper bound. This special structure is why the finite Choi calculation certifies their full channel distance. A normalized Choi trace distance alone does not establish the same equality for an arbitrary channel.

## Worked example: one noisy qubit and a reference

Take one physical qubit, apply $`D`$ identity/noise rounds, and retain it. Composition gives $`\mathcal D_a`$ with $`a=\eta^D`$. For an arbitrary Bloch-vector state,

```math
\rho=\frac12(I+\boldsymbol r\cdot\boldsymbol\sigma),
\qquad
\mathcal D_a(\rho)-\frac I2
=\frac a2\boldsymbol r\cdot\boldsymbol\sigma.
```

The two eigenvalues of the difference are $`\pm a\lvert\boldsymbol r\rvert/2`$. Consequently the largest output half-trace distance accessible without an entangled reference is $`a/2`$, attained by every pure input.

Now test the same physical channel using the joint input

```math
\lvert\Phi_1\rangle=\frac{\lvert00\rangle+\lvert11\rangle}{\sqrt2}.
```

Only the first qubit passes through the noise. The actual and target joint outputs are

```math
\omega_a
=a\lvert\Phi_1\rangle\langle\Phi_1\rvert
 +(1-a)\frac{I_4}{4},
\qquad
\omega_0=\frac{I_4}{4}.
```

Their difference has one eigenvalue $`3a/4`$ and three eigenvalues $`-a/4`$. Its half-trace norm is therefore $`3a/4`$. The binary measurement with effects $`\lvert\Phi_1\rangle\langle\Phi_1\rvert`$ and $`I_4-\lvert\Phi_1\rangle\langle\Phi_1\rvert`$ attains this statistical distance: the first outcome has probability $`(1+3a)/4`$ under the noisy channel and $`1/4`$ under the target.

To see that no other input does better, write the channel as

```math
\mathcal D_a
=\frac{1+3a}{4}\mathrm{Ad}_I
 +\frac{1-a}{4}
  (\mathrm{Ad}_X+\mathrm{Ad}_Y+\mathrm{Ad}_Z),
\qquad \mathrm{Ad}_P(X)=PXP^\dagger.
```

The replacer has coefficient $`1/4`$ for each of these four unitary channels. Each unitary channel has diamond norm one, so the triangle inequality gives

```math
\lVert\mathcal D_a-\mathcal R_1\rVert_\diamond
\le\frac{3a}{4}+3\frac a4=\frac{3a}{2}.
```

The Bell input attains this bound. Hence

```math
\delta(\mathcal D_{\eta^D})=\frac34\eta^D.
```

For example, $`\eta=1/2`$ and $`D=2`$ give $`a=1/4`$. A test on the physical qubit alone reaches half-trace distance $`1/8`$; the complete error is $`3/16`$. The physical protocol still has one qubit and two charged rounds. The second qubit belongs to the reference in the distinguishing test, not to an auxiliary workspace controlled by the protocol.

Any one-qubit unitary commutes with depolarization as a channel. Inserting such gates changes the output by an overall unitary and leaves this error unchanged. The acceleration in the many-qubit constructions therefore depends on changing the support of information across different noisy sites.

## From a Pauli path to an entire channel

For a tensor Pauli $`P`$, its weight $`w(P)`$ counts nonidentity factors. Product depolarization gives

```math
\mathcal D_\eta^{\otimes n}(P)=\eta^{w(P)}P.
```

A Clifford gate sends a Pauli to another Pauli up to sign. If $`P_\ell`$ is the ideal image after layer $`\ell`$, the actual noisy circuit therefore satisfies

```math
\Psi_D(P)=a_PUPU^\dagger,
\qquad
a_P=e^{-\lambda\sum_{\ell=1}^{D}w(P_\ell)},
\qquad U=U_D\cdots U_1.
```

The sum counts noisy support throughout the circuit, including idle intervals. Conjugating the output by $`U^\dagger`$ in the analysis produces a Pauli-diagonal channel $`\Lambda(P)=a_PP`$. This change of representation preserves distance to the maximally mixed replacer. The inverse circuit is not executed.

Complete positivity makes $`\Lambda`$ a mixture of Pauli conjugations with probabilities $`p_Q`$. The Bell-basis argument from the one-qubit example extends to all $`4^n`$ Pauli labels and proves

```math
\delta(\Psi_D)=\frac12\sum_Q\lvert p_Q-4^{-n}\rvert.
```

The [channel-distance proof](../science/channel_distance.md#lemma-pauli-channel-distance) supplies both inequalities. Its Fourier calculation then turns the whole probability distribution into a sum over attenuation coefficients:

```math
\chi^2(p\Vert u)=\sum_{P\ne I}a_P^2,
\qquad u_Q=4^{-n},
\qquad
\delta(\Psi_D)\le\frac12\sqrt{\sum_{P\ne I}a_P^2}.
```

There are $`4^n-1`$ nonidentity terms. A bound for one observable, or for a typical Pauli, leaves the other terms uncontrolled. This counting step explains why the upper constructions establish simultaneous support bounds for every nonidentity Pauli.

For independent block channels, the Pauli-error probabilities factor even when the physical input is entangled across blocks. If block $`j`$ has chi-square divergence $`\xi_j`$, [tensorization](../science/channel_distance.md#lemma-chi-square-tensorization) gives

```math
1+\chi^2_{\mathrm{total}}=\prod_j(1+\xi_j),
\qquad
\delta(\Psi_D)
\le\frac12\sqrt{\exp\!\left(\sum_j\xi_j\right)-1}.
```

The product here concerns a representation of the channel. It imposes no product-state promise on its input. A sufficient global error budget is $`\sum_j\xi_j\le\ln(1+4\epsilon^2)`$.

## Why a reversible circuit needs several noisy checkpoints

A Clifford permutes the nonidentity Pauli labels. At any fixed time, some input Pauli is mapped to a weight-one output Pauli. Thus a uniform large final weight for every input is unavailable. The useful condition combines support at more than one time.

For a block of $`b`$ qubits, suppose a fixed Clifford $`V`$ satisfies

```math
w(P)+w(VPV^\dagger)\ge\alpha b
\qquad(P\ne I)
```

for a positive constant $`\alpha`$. An operator with small initial support must acquire large final support. An operator that ends with small support is exposed to noise while its initial support is large. Waiting for $`s`$ charged rounds before and after the circuit therefore gives

```math
a_P\le e^{-\lambda s\alpha b},
\qquad
\xi\le(4^b-1)e^{-2\lambda s\alpha b}.
```

The gate-round noise contributes additional attenuation along the same Clifford path and is included in the exact formula. The endpoint inequality simply supplies a convenient bound on it.

With unrestricted connectivity, the [spreading argument](../science/unrestricted_connectivity.md#lemma-logarithmic-depth-branch-number) produces this branch-weight property in depth $`O(\ln b)`$. Choosing a sufficiently large constant $`s`$ makes $`\xi\le e^{-b}`$. Blocks with $`b=\Theta(\ln n)`$ then meet the global error budget in depth $`O(\ln\ln n)`$. The normalized tail in the imported spreading theorem is essential to selecting one circuit that works for every input Pauli.

On a lattice, the [coordinate-line recursion](../science/geometric_construction.md#coordinate-line-recursion) uses several checkpoints. In dimension $`d`$, a block with side scale $`m`$ has volume of order $`m^d`$. The recursion guarantees a checkpoint weight sum at least $`\alpha^d b`$ for every nonidentity Pauli. Waiting $`m`$ rounds at each checkpoint gives attenuation with an exponent of order $`m^{d+1}`$, and the compiled line circuits also cost order $`m`$ depth. Choosing $`m=\Theta((\ln n)^{1/(d+1)})`$ meets the global budget. The proof handles boundary blocks and counts their padding rounds explicitly.

## From norm bounds to a measurement that survives the noise

An upper construction demonstrates that one circuit mixes quickly. A minimum-depth theorem must also rule out every shallower circuit, including non-Clifford circuits whose observables become sums of many Paulis. The [causal converse](../science/causal_bound.md#theorem-causal-cone-bound) uses operator norms and measurements instead of tracking one Pauli path.

For input site $`i`$, let $`C_i(\ell)`$ be its full syntactic causal cone after layer $`\ell`$, and write

```math
V_i(D)=\sum_{\ell=1}^{D}\lvert C_i(\ell)\rvert,
\qquad \kappa=2/\eta-1.
```

A cone includes both outputs of every gate it touches, regardless of accidental cancellations in a particular operator. Starting from $`X_i`$, invert the adjoint channel algebraically to define a Hermitian final observable $`A_i`$ satisfying

```math
\Psi_D^\dagger(A_i)=X_i,
\qquad
\lVert A_i\rVert_\infty\le\kappa^{V_i(D)}=:K_i.
```

The inverse noise map is not physical. Its purpose is to construct a witness whose forward expectation can be evaluated exactly. On one site, it has the form

```math
\mathcal D_\eta^{-1}
=\eta^{-1}\mathrm{id}-(\eta^{-1}-1)E,
\qquad E(X)=\mathrm{Tr}(X)I_2/2.
```

For Hermitian $`H`$, positivity and unitality of $`E`$ preserve the order interval $`-\lVert H\rVert_\infty I\le H\le\lVert H\rVert_\infty I`$. Hence $`E`$ contracts its operator norm. The triangle inequality bounds the inverse by $`\kappa`$ on each affected site. Multiplying these factors over the full causal history gives $`K_i`$.

The norm bound converts the mathematical inverse into a physical binary POVM:

```math
F_i(\pm)=\frac12\left(I\pm\frac{A_i}{K_i}\right).
```

On input $`\lvert+\rangle^{\otimes n}`$, its output bit has bias $`K_i^{-1}`$. On the maximally mixed target, the same bit is fair. When the selected full cones are disjoint, the inverse recursion also preserves the relevant products. This proves exact independence of these particular readouts. It does not assume that the final quantum state factors across the measured regions.

For classical distributions $`P,Q`$, Watrous's unsquared fidelity becomes the Bhattacharyya coefficient $`\sum_x\sqrt{P(x)Q(x)}`$. Its product rule and trace-distance bound explain the statistical step. A direct calculation for a bit of bias $`a`$ gives an affinity at most $`e^{-a^2/8}`$, so the joint measurements yield

```math
\delta(\Psi_D)
\ge1-\exp\!\left[-\frac18
\sum_i\kappa^{-2V_i(D)}\right].
```

Watrous's measurement framework explains why this classical distinguishability lower-bounds channel error. The project supplies the inverse-witness construction, the disjoint-history product identity, and the packing argument that finds many such witnesses.

## How the three depth scales fit together

With no control, every local Pauli retains $`\eta^D`$. The [passive proof](../science/passive.md) shows that the complete error changes on the scale $`n\eta^{2D}=O(1)`$, giving

```math
D_{\mathrm{pass}}
=\frac{\ln n}{2\ln(1/\eta)}+O_{\eta,\epsilon}(1).
```

Control changes the causal volume available to each initial signal. On a fixed-dimensional lattice, $`V_i(D)=O_d(D^{d+1})`$, and order $`n/D^d`$ disjoint cones can be selected. With unrestricted two-qubit pairings, $`V_i(D)=O(2^D)`$, and at least $`n/4^D`$ disjoint cones can be selected. Substituting these bounds into the measurement inequality gives the two lower-depth scales. The constructions above attain them:

| Architecture | Optimal complete-mixing depth at fixed noise and error | Authoritative proof |
|---|---|---|
| Passive noise | $`\Theta(\ln n)`$ | [Passive benchmark](../science/passive.md) |
| Filled regular regions in fixed dimension $`d`$ | $`\Theta((\ln n)^{1/(d+1)})`$ | [Geometric construction](../science/geometric_construction.md) and [lattice converse](../science/causal_bound.md#corollary-lattice-depth) |
| Unrestricted pair connectivity | $`\Theta(\ln\ln n)`$ | [Unrestricted construction](../science/unrestricted_connectivity.md) and [pair-connectivity converse](../science/causal_bound.md#corollary-unrestricted-connectivity) |

The upper and lower bounds quantify the same physical task. All input qubits remain in the output; the error is global and reference-sensitive; every elementary noise round is charged. The geometric matching upper requires the regular regions stated in the model. The constants depend on fixed $`d`$, $`\eta`$, and $`\epsilon`$ where applicable. These are discrete mixing laws for an infinite-temperature target, with no heat or work assignment and no claim of pure-state initialization.

## Source inheritance and the remaining reading route

Watrous is the single educational anchor. The primary research sources below have distinct scientific roles.

| Ingredient | Source and its role | Connection established in this repository |
|---|---|---|
| Channel representations and distance | [Watrous (2018)](../references/RELATED_WORK.md#watrous2018) supplies the foundations used throughout this bridge. | The Pauli Fourier identity and block error budget connect those foundations to the constructions. |
| Increased decay through high Pauli weight | [Quek et al. (2024)](../references/RELATED_WORK.md#quek2024) establish the earlier noisy-circuit mechanism and closely related mixing constructions. | The model specifies the complete-channel optimization and the arbitrary-input, retained-output resource accounting. |
| Linear-depth nearest-neighbor Clifford implementation | [Maslov and Yang (2023), Lemma 4](../references/RELATED_WORK.md#maslov2023) is the compiler input. | The geometric proof counts all charged rounds and combines line branch weights through its checkpoint recursion. |
| Logarithmic-depth Pauli spreading on random matchings | [Anand et al., arXiv:2608.18536v1, Theorem 3.4](../references/RELATED_WORK.md#anand2026) is the external input for unrestricted connectivity. | A normalized-tail union bound selects a fixed circuit with simultaneous branch weight, followed by complete-channel conversion. |

The arbitrary-unitary converse is proved in [causal bounds](../science/causal_bound.md). The geometric theorem does not depend on the unrestricted-connectivity spreading theorem. Circuit selection occurs before execution; the implemented controls are fixed and do not average over fresh random choices.

For a concrete many-qubit circuit, continue to [finite examples](../science/finite_examples.md). The [verification account](../verification/README.md) distinguishes exhaustive Pauli checks, sampled checks, and dense numerical channel calculations from the arbitrary-size proofs and imported results. The [interpretation](../science/interpretation.md) connects those proofs to information spreading, global accuracy, and physical resource accounting. The [milestone map](MILESTONES.md) gives the local-to-global route through the same scientific account.
