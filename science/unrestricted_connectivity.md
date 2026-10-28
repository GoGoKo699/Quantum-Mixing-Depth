# Optimal mixing depth with unrestricted connectivity

In the [discrete circuit model](model.md), every round consists of a parallel layer of disjoint one- or two-qubit unitaries followed by local depolarization on every qubit. Write $`0<\eta<1`$ for the retention parameter, $`\lambda=-\ln\eta`$, and

```math
\mathcal R_n(X)=\mathrm{Tr}(X)\frac{I}{2^n},
\qquad
\varepsilon(\Phi)=\frac12\|\Phi-\mathcal R_n\|_\diamond.
```

All $`n`$ qubits contain arbitrary input information, all outputs are retained, and the diamond norm includes arbitrary input entanglement with an external reference. The construction below uses a fixed Clifford circuit and the specified bath. No auxiliary qubits or random control are used during execution.

<a id="theorem-unrestricted-connectivity"></a>

## Theorem: unrestricted-connectivity depth

For fixed $`\eta\in(0,1)`$ and $`\epsilon\in(0,1)`$, the minimum depth satisfying $`\varepsilon(\Phi)\le\epsilon`$ obeys

```math
D_\star(n;\eta,\epsilon)
=\Theta_{\eta,\epsilon}(\log\log n)
\qquad (n\longrightarrow\infty).
```

The upper bound uses exactly $`n`$ qubits and $`O_{\eta,\epsilon}(n\log\log n)`$ two-qubit gates. The lower bound permits arbitrary two-qubit unitaries.

The upper bound uses Theorem 3.4 of [Anand, Gorokhovsky, Hritz, and Sun, arXiv:2608.18536v1](../references/RELATED_WORK.md#anand2026) as an external Pauli-spreading theorem. Sections below prove the simultaneous branch-number consequence, the complete-channel estimate, and the treatment of arbitrary register sizes. The [causal-cone converse](causal_bound.md#corollary-unrestricted-connectivity) supplies the matching lower bound.

<a id="external-spreading-theorem"></a>

## 1. The external spreading statement and its applicability

Use $`b`$ for an even block size, $`w(P)`$ for the weight of a Pauli string, and $`r`$ for a weight cutoff. Pauli strings are counted modulo phase, so there are $`3^w\binom bw`$ strings of weight $`w`$.

Theorem 3.4 of the [versioned primary source](https://arxiv.org/html/2608.18536v1) gives the following cumulative weight bound. For prescribed constants $`a,\beta,\delta>0`$, there is a constant $`C`$ such that, for every sufficiently large even $`b`$ and every $`T\ge C\log b`$,

```math
\Pr\!\left[w(UPU^\dagger)\le r\right]
\le
\frac{4^{\delta b}}{4^b-1}\,3^r2^{bH_2(r/b)}
+\frac{b^{-a}}{3^{w(P)}\binom b{w(P)}}
+e^{-\beta b},
\qquad\mathrm{(1)}
```

for each fixed nonidentity Pauli $`P`$ and $`1\le r\le b/2`$. Here $`H_2`$ is binary entropy, and $`U`$ is sampled from the source's random matching ensemble. The source uses different letters for block size, cutoff, and polynomial-tail exponent; equation (1) preserves its cumulative bound and parameter dependence.

We choose the uniform distribution on the two-qubit Clifford group. Each round is a uniformly sampled perfect matching with an independent Clifford on each pair. A nonidentity two-qubit Pauli is mapped uniformly to the other fifteen nonidentity Paulis. The induced transition matrix on nonzero support patterns $`01,10,11`$ is therefore

```math
K'=
\begin{pmatrix}
1/5&1/5&3/5\\
1/5&1/5&3/5\\
1/5&1/5&3/5
\end{pmatrix}.
```

It is reversible with stationary distribution $`(1/5,1/5,3/5)`$, and $`K'_{11,11}=3/5\in(0,1)`$. These are the hypotheses of Theorem 3.4. Uniform Clifford sampling also satisfies the circuit ensemble's local invariance, positive-entanglement, and inverse-invariance conditions. A matching round is one allowed parallel two-qubit layer on the same $`b`$ sites; the theorem introduces no ancillary systems. In particular, (1) concerns each fixed input Pauli, rather than an average over input states.

<a id="lemma-logarithmic-depth-branch-number"></a>

## 2. A logarithmic-depth Clifford with linear Pauli branch number

Choose a constant $`\alpha\in(0,1/2)`$ such that

```math
f(\alpha):=H_2(\alpha)+\alpha\log_2 3<1.
```

For example, $`\alpha=1/10`$ is admissible. Fix $`\delta>0`$ with $`\delta+f(\alpha)<1`$, $`a>2`$, and $`\beta>f(\alpha)\ln2`$. All these constants are independent of $`b,n,\eta,\epsilon`$. Set

```math
r=\lfloor\alpha b\rfloor,
\qquad
A_r=\sum_{w=1}^r3^w\binom bw,
\qquad
B_r=3^r2^{bH_2(r/b)}.
```

The binomial-tail estimate and monotonicity of $`H_2(x)+x\log_2 3`$ on $`[0,1/2]`$ imply

```math
A_r\le B_r\le 2^{bf(\alpha)}.
```

Apply the union bound to (1) over every nonidentity input Pauli of weight at most $`r`$. No independence between these events is required. The probability of any low-weight input having a low-weight output is at most

```math
\begin{aligned}
&\Pr\!\left[\exists P\ne I:
 w(P)\le r,\ w(UPU^\dagger)\le r\right]\\
&\quad\le
\frac{4^{\delta b}A_rB_r}{4^b-1}
+r b^{-a}+A_r e^{-\beta b}\\
&\quad\le
(1+o(1))2^{-2[1-\delta-f(\alpha)]b}
+b^{1-a}
+e^{-[\beta-f(\alpha)\ln2]b}.
\qquad\mathrm{(2)}
\end{aligned}
```

The middle term follows exactly from

```math
\sum_{w=1}^r
\left(3^w\binom bw\right)
\frac{b^{-a}}{3^w\binom bw}
=r b^{-a}.
```

Keeping the normalized polynomial tail in (1) is essential. Replacing it by a uniform polynomial error before taking the union bound would lose the needed estimate.

The right side of (2) tends to zero. Thus there are absolute constants $`b_0,C_{\mathrm{spr}}`$ such that, for every even $`b\ge b_0`$, a fixed Clifford $`U_b`$ of depth at most $`\lceil C_{\mathrm{spr}}\log b\rceil`$ satisfies

```math
\mathcal B(U_b)
:=\min_{P\ne I}\bigl[w(P)+w(U_bPU_b^\dagger)\bigr]
>\alpha b.
\qquad\mathrm{(3)}
```

Indeed, either the input weight exceeds $`r`$, or its output weight does. In either case their sum is at least $`r+1>\alpha b`$. This simultaneous statement concerns all physical Paulis, with no distinguished logical subspace or initialized check register.

<a id="lemma-block-mixing"></a>

## 3. Noise before and after the circuit gives a complete block estimate

Fix a block of even size $`b\ge b_0`$ and a circuit $`U_b=U_T\cdots U_1`$ satisfying (3). Choose the constant number of idle rounds

```math
s=\left\lceil\frac{\ln4+1}{2\lambda\alpha}\right\rceil.
\qquad\mathrm{(4)}
```

Execute $`s`$ identity/noise rounds, the $`T`$ layers of $`U_b`$ with noise after every layer, and another $`s`$ identity/noise rounds. Let $`\Phi_b`$ be the resulting physical channel.

For analysis define $`\Lambda_b=\mathrm{Ad}_{U_b^\dagger}\circ\Phi_b`$. This conjugation is not an implemented decoding operation. Since the maximally mixed state is unitary invariant,

```math
\frac12\|\Phi_b-\mathcal R_b\|_\diamond
=\frac12\|\Lambda_b-\mathcal R_b\|_\diamond.
```

Let $`P_\ell=U_\ell\cdots U_1 P U_1^\dagger\cdots U_\ell^\dagger`$, with irrelevant Pauli phases suppressed. Each noisy Clifford layer attenuates the coefficient of the same ideal Pauli trajectory. Thus $`\Lambda_b`$ is a CPTP Pauli-diagonal map and its eigenvalue on $`P\ne I`$ is

```math
a_P
=\exp\!\left[
-\lambda\left(
s w(P)+\sum_{\ell=1}^{T}w(P_\ell)
+s w(U_bPU_b^\dagger)
\right)\right]
\le e^{-\lambda s\alpha b}.
\qquad\mathrm{(5)}
```

The internal noise is included exactly. The inequality uses only the two endpoint weights, so no assumption about ideal gates being physically noiseless is needed beyond the model's unitary-then-noise ordering.

A CPTP Pauli-diagonal map is a Pauli channel. Write $`p_b`$ for its Pauli-error distribution and $`u_b`$ for the uniform distribution on the $`4^b`$ Paulis. The [Pauli-channel distance lemma](channel_distance.md#lemma-pauli-channel-distance) and Fourier Parseval yield

```math
\begin{aligned}
\chi^2(p_b\|u_b)
&=\sum_{P\ne I}a_P^2\\
&\le(4^b-1)e^{-2\lambda s\alpha b}\\
&\le e^{-[2\lambda s\alpha-\ln4]b}
\le e^{-b}.
\qquad\mathrm{(6)}
\end{aligned}
```

The factor $`4^b-1`$ is retained before choosing $`s`$. Consequently this is a complete-channel estimate, rather than only a bound on an individual observable or on the output purity of selected inputs.

<a id="arbitrary-register-sizes"></a>

## 4. Blocks, odd register sizes, and depth padding

Set $`q_\epsilon=\ln(1+4\epsilon^2)`$. Let $`b`$ be the smallest even integer at least

```math
\max\!\left\{b_0,\ 2,\ \ln\frac{2n}{q_\epsilon}\right\}.
\qquad\mathrm{(7)}
```

Write $`n_{\mathrm e}=2\lfloor n/2\rfloor`$. For sufficiently large $`n`$, $`n_{\mathrm e}\ge b`$. Decompose

```math
n_{\mathrm e}=Bb+r,
\qquad B=\left\lfloor\frac{n_{\mathrm e}}b\right\rfloor,
\qquad 0\le r<b.
```

The remainder $`r`$ is even. Use one block of size $`b+r`$ and $`B-1`$ blocks of size $`b`$. Every block size $`b_j`$ is even and belongs to $`[b,2b)`$. If $`n`$ is odd, retain the one remaining input qubit as an idle noisy wire. This partition adds no qubits and initializes no part of the input.

Run the block protocols in parallel. Choose the common total depth

```math
D=\max\!\left\{
2s+\max_j T_j,
\left\lceil\frac{\ln(6/q_\epsilon)}{2\lambda}\right\rceil
\right\}.
\qquad\mathrm{(8)}
```

Each encoder begins after the initial $`s`$ idle rounds. After its last gate layer, that block idles until round $`D`$. It therefore receives at least $`s`$ final noise rounds. All idle rounds are charged and noise continues on every wire. Equations (5) and (6) remain valid for each block.

The optional last qubit receives $`D`$ depolarizing layers, so its Pauli-error chi-square divergence is exactly $`3\eta^{2D}\le q_\epsilon/2`$. By (7),

```math
\sum_{j=1}^{B}\chi^2(p_{b_j}\|u_{b_j})
\le B e^{-b}\le n e^{-b}\le q_\epsilon/2.
```

The block operations factor as channels, regardless of entanglement in the input. Applying the [chi-square tensorization lemma](channel_distance.md#lemma-chi-square-tensorization) to their Pauli-error distributions gives

```math
\begin{aligned}
1+\chi^2(p_{\mathrm{total}}\|u_n)
&=\prod_{j=1}^{B}
\left(1+\chi^2(p_{b_j}\|u_{b_j})\right)
\left(1+3\eta^{2D}\right)^{n-n_{\mathrm e}}\\
&\le\exp\!\left[
\sum_{j=1}^{B}\chi^2(p_{b_j}\|u_{b_j})
+3\eta^{2D}\right]\\
&\le e^{q_\epsilon}=1+4\epsilon^2.
\qquad\mathrm{(9)}
\end{aligned}
```

Conjugating by the product of the ideal block inverses preserves the distance to $`\mathcal R_n`$. The Pauli-channel diamond identity followed by Cauchy-Schwarz now gives

```math
\varepsilon(\Phi)
=\frac12\|p_{\mathrm{total}}-u_n\|_1
\le\frac12\sqrt{\chi^2(p_{\mathrm{total}}\|u_n)}
\le\epsilon.
\qquad\mathrm{(10)}
```

Since $`b=O_\epsilon(\log n)`$ and $`T_j\le\lceil C_{\mathrm{spr}}\log(2b)\rceil`$, (8) is $`O_{\eta,\epsilon}(\log\log n)`$. Each matching round contains $`b_j/2`$ two-qubit gates, yielding a total of $`O(n\log\log n)`$ gates.

For the finitely many sizes with $`n_{\mathrm e}<b`$, including $`n=1`$, use passive depolarization for

```math
D_{\mathrm{small}}
=\left\lceil\frac{\ln(3n/q_\epsilon)}{2\lambda}\right\rceil
```

rounds. Then $`(1+3\eta^{2D_{\mathrm{small}}})^n-1\le4\epsilon^2`$. This supplies a valid protocol for every positive integer $`n`$ and does not change the asymptotic bound at fixed $`\eta,\epsilon`$.

<a id="fixed-circuit-selection"></a>

## 5. Selecting a fixed circuit

Equation (2) establishes existence of a simultaneous branch-number circuit with probability tending to one. Choose one such circuit for each block size and keep it fixed for every execution. Reusing a circuit on several blocks does not average the implemented channel over circuits; the physical noise channels alone generate the Pauli-error distribution used in (6) through (10).

The selection can also be made by a finite classical search. Sample a candidate matching circuit and check the images of all Paulis of weight at most $`\lfloor\alpha b\rfloor`$ in its binary symplectic representation. For sufficiently large $`b`$, the expected number of trials is bounded. At $`b=O(\log n)`$, even enumeration of all $`4^b`$ Paulis takes polynomial time in $`n`$, with constants inherited from the theorem. This is a construction argument, not a claim of optimized preprocessing or practical gate counts.

<a id="matching-lower-bound"></a>

## 6. Matching the arbitrary-unitary lower bound

For $`\kappa=2/\eta-1`$, the [unrestricted causal-cone corollary](causal_bound.md#corollary-unrestricted-connectivity) proves that every allowed depth-$`D`$ circuit satisfies

```math
\varepsilon(\Phi)
\ge
1-\exp\!\left[
-\frac{n}{8\,4^D\,\kappa^{2^{D+2}-4}}
\right].
\qquad\mathrm{(11)}
```

Thus $`\varepsilon(\Phi)\le\epsilon<1`$ requires

```math
\ln n
\le D\ln4+(2^{D+2}-4)\ln\kappa
+\ln[-8\ln(1-\epsilon)],
```

which implies $`D\ge\log_2\ln n-O_{\eta,\epsilon}(1)`$. Together with (8), this proves the theorem. The lower bound does not use Clifford dynamics or the external spreading result.

The conclusion concerns the exact discrete noise model. Constants depend on the fixed noise retention and target error; the argument does not identify optimal constants or a simultaneous continuous-time control law. The [related-work comparison](../references/RELATED_WORK.md) identifies the inherited rapid-mixing mechanism and the specific compilation and spreading inputs.
