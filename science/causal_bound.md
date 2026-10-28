# A causal-cone lower bound on complete mixing

Local noise cannot remove all information before sufficiently many noisy sites have entered the causal history of the input. This file proves that statement for arbitrary unitary gates. The proof constructs a final measurement whose outcomes retain a calculable bias, even when the circuit generates correlations outside the measured regions.

The result applies to the discrete rounds defined in [the model](model.md). On $`n`$ physical qubits, round $`\ell`$ applies a layer $`U_\ell`$ of disjoint one- and two-qubit unitaries, followed by the product depolarizing channel $`\mathcal N_\eta=\mathcal D_\eta^{\otimes n}`$, where $`0<\eta<1`$. Write

```math
\Psi_D=(\mathcal N_\eta\circ\mathrm{Ad}_{U_D})\circ\cdots\circ
(\mathcal N_\eta\circ\mathrm{Ad}_{U_1}),
\qquad
\mathrm{Ad}_U(X)=UXU^\dagger.
```

The complete-mixing error is

```math
\frac12\left\|\Psi_D-\mathcal R_n\right\|_\diamond,
\qquad
\tau_n=\frac{I}{2^n},
\qquad
\mathcal R_n(X)=\mathrm{Tr}(X)\tau_n.
```

All physical qubits are arbitrary inputs and remain in the output. The lower bound uses a single product input, so it also applies to the stronger requirement that mixing hold for every input entangled with an inaccessible reference. Throughout this file, $`\ln`$ denotes the natural logarithm and

```math
\kappa=\frac{2}{\eta}-1>1.
```

## Full syntactic causal cones

For input site $`i`$, set $`C_i(0)=\{i\}`$. Given $`C_i(\ell-1)`$, form $`C_i(\ell)`$ by including both output sites of every two-qubit gate in layer $`\ell`$ that touches $`C_i(\ell-1)`$. Sites acted on by one-qubit gates or identities remain included.

These are full syntactic cones. A gate contributes both output wires even if its particular matrix, or the particular observable being evolved, produces a smaller actual support. This convention retains the entire possible causal history and gives

```math
C_i(\ell-1)\subseteq C_i(\ell).
```

Consequently, cones that are disjoint at the final layer are disjoint at every earlier layer. Define their accumulated sizes by

```math
V_i(D)=\sum_{\ell=1}^{D}|C_i(\ell)|.
```

The sum starts after the first gate layer, because this is where the first noise channel acts. For $`D=0`$, the sum is zero.

## Theorem: causal-cone bound

Let $`S`$ be any set of input sites whose final full syntactic cones $`\{C_i(D):i\in S\}`$ are pairwise disjoint. Then every circuit of the stated form satisfies

```math
\frac12\left\|\Psi_D-\mathcal R_n\right\|_\diamond
\geq
1-\exp\!\left[
-\frac18\sum_{i\in S}\kappa^{-2V_i(D)}
\right].
\qquad\mathrm{(C1)}
```

In particular, if $`|S|=M`$ and $`V_i(D)\leq V`$ for all selected sites, then

```math
\frac12\left\|\Psi_D-\mathcal R_n\right\|_\diamond
\geq
1-\exp\!\left[-\frac{M}{8\kappa^{2V}}\right].
\qquad\mathrm{(C2)}
```

No Clifford assumption enters this theorem.

### Proof: bounded inverse observables

Let $`E_j`$ be the conditional expectation that replaces site $`j`$ by its maximally mixed state:

```math
E_j(A)=\frac{I_j}{2}\otimes\mathrm{Tr}_j A,
```

with tensor factors placed in their original order. The single-site depolarizing map and its linear inverse are

```math
\mathcal D_{\eta,j}=\eta\,\mathrm{id}+(1-\eta)E_j,
\qquad
\mathcal D_{\eta,j}^{-1}
=\eta^{-1}\mathrm{id}-(\eta^{-1}-1)E_j.
\qquad\mathrm{(C3)}
```

The inverse is not a physical channel. It is used only to construct a mathematical observable. Both maps preserve the identity and trace and are self-adjoint for the Hilbert–Schmidt inner product. Because $`E_j`$ is unital and completely positive, it contracts the operator norm. Therefore

```math
\left\|\mathcal D_{\eta,j}^{-1}(A)\right\|_\infty
\leq
\left[\eta^{-1}+(\eta^{-1}-1)\right]\|A\|_\infty
=\kappa\|A\|_\infty.
\qquad\mathrm{(C4)}
```

For each selected input site, start from its Pauli $`X_i`$ and define

```math
A_i^{(0)}=X_i,
\qquad
A_i^{(\ell)}
=\mathcal N_\eta^{-1}\!\left(
U_\ell A_i^{(\ell-1)}U_\ell^\dagger
\right).
\qquad\mathrm{(C5)}
```

Every $`A_i^{(\ell)}`$ is Hermitian and traceless. Its support lies in $`C_i(\ell)`$: unitary conjugation enlarges support only within the next syntactic cone, and each inverse single-site noise map preserves support. On sites outside this cone the observable has an identity factor, which the inverse map leaves unchanged. Applying (C4) only on cone sites gives

```math
\|A_i^{(D)}\|_\infty
\leq
\prod_{\ell=1}^{D}\kappa^{|C_i(\ell)|}
=\kappa^{V_i(D)}=:K_i.
\qquad\mathrm{(C6)}
```

Let $`\Psi_\ell`$ denote the first $`\ell`$ rounds. The adjoint of the last round cancels its inverse in (C5), so induction gives the exact identity

```math
\Psi_\ell^\dagger\!\left(A_i^{(\ell)}\right)=X_i.
\qquad\mathrm{(C7)}
```

### Proof: products on disjoint histories

For every subset $`T\subseteq S`$, one also has

```math
\Psi_D^\dagger\!\left(\prod_{i\in T}A_i^{(D)}\right)
=\prod_{i\in T}X_i.
\qquad\mathrm{(C8)}
```

To prove this, apply the chronological inverse recursion (C5) to $`\prod_{i\in T}X_i`$. Unitary conjugation always preserves products. After each unitary layer, the evolved factors have disjoint supports because their full syntactic cones are disjoint at that layer. The inverse product noise therefore acts independently on these factors, preserving their product form. The recursion gives exactly $`\prod_{i\in T}A_i^{(\ell)}`$ at step $`\ell`$, and the same adjoint cancellation proves (C8).

This argument does not assume that the final state factors across the selected cones, or that qubits outside those cones are uncorrelated. Independence of the measurement outcomes below follows from (C8).

### Proof: a physical measurement that retains bias

Use the valid input

```math
\rho_+=|+\rangle\!\langle+|^{\otimes n}.
```

On each selected final cone, measure the binary POVM

```math
F_i(s_i)=\frac12\left(I+s_i\frac{A_i^{(D)}}{K_i}\right),
\qquad s_i\in\{-1,+1\}.
\qquad\mathrm{(C9)}
```

The operator-norm bound (C6) ensures positivity. The two effects sum to the identity. Because their supports are disjoint, these POVMs form a valid joint measurement.

Expanding its joint probabilities and using (C8) gives

```math
\begin{aligned}
P(s)
&=\mathrm{Tr}\!\left[
\Psi_D(\rho_+)\prod_{i\in S}F_i(s_i)
\right]\\
&=2^{-M}\sum_{T\subseteq S}
\prod_{i\in T}\frac{s_i}{K_i}
=\prod_{i\in S}\frac{1+a_i s_i}{2},
\qquad a_i=K_i^{-1}.
\end{aligned}
\qquad\mathrm{(C10)}
```

Here $`\mathrm{Tr}(\rho_+\prod_{i\in T}X_i)=1`$ for every subset. Thus the measured bits are exactly independent, with biases $`a_i`$.

On $`\tau_n`$, the same measurement gives the uniform product distribution $`Q(s)=2^{-M}`$. Indeed, each witness has zero trace on its support, and the supports are disjoint, so every nonempty product of witnesses has zero expectation in $`\tau_n`$.

For a bit with bias $`a\in[0,1]`$, its Bhattacharyya coefficient with the uniform bit is

```math
B(a)=\frac{\sqrt{1+a}+\sqrt{1-a}}{2}.
```

Since

```math
B(a)^2=\frac{1+\sqrt{1-a^2}}{2}
\leq 1-\frac{a^2}{4},
```

one has $`B(a)\leq e^{-a^2/8}`$. Total variation obeys

```math
\mathrm{TV}(P,Q)
=1-\sum_s\min\{P(s),Q(s)\}
\geq 1-\sum_s\sqrt{P(s)Q(s)}.
```

The coefficient factorizes for the distributions in (C10). Hence

```math
\mathrm{TV}(P,Q)
\geq 1-\prod_{i\in S}B(a_i)
\geq 1-\exp\!\left[-\frac18\sum_{i\in S}a_i^2\right].
\qquad\mathrm{(C11)}
```

Measurement cannot increase trace distance, and the diamond norm includes the particular input $`\rho_+`$. Combining (C6), (C10), and (C11) proves (C1). Equation (C2) follows immediately. $`\square`$

## Corollary: unrestricted connectivity

For arbitrary pair connectivity, every depth-$`D`$ circuit satisfies

```math
\frac12\left\|\Psi_D-\mathcal R_n\right\|_\diamond
\geq
1-\exp\!\left[
-\frac{n}{8\,4^D\,\kappa^{\,2^{D+2}-4}}
\right].
\qquad\mathrm{(C12)}
```

**Proof.** A layer of disjoint two-qubit gates at most doubles a cone, so $`|C_i(\ell)|\leq 2^\ell`$ and

```math
V_i(D)\leq\sum_{\ell=1}^{D}2^\ell=2^{D+1}-2.
```

Each output site belongs to the forward cones of at most $`2^D`$ input sites, as its full backward cone has that size bound. Since a forward cone contains at most $`2^D`$ output sites, it intersects at most $`4^D`$ input cones, counting itself. Greedily selecting a cone and removing all intersecting cones produces at least $`n/4^D`$ pairwise disjoint cones. Apply (C2). $`\square`$

If the error is at most $`\epsilon\in(0,1)`$, a necessary finite condition is

```math
\ln n
\leq
D\ln4+(2^{D+2}-4)\ln\kappa
+\ln\!\left[-8\ln(1-\epsilon)\right].
\qquad\mathrm{(C13)}
```

For fixed $`\eta`$ and $`\epsilon`$, this implies

```math
D\geq\log_2\ln n-O_{\eta,\epsilon}(1).
\qquad\mathrm{(C14)}
```

For example, $`D\leq2^D`$ bounds the first two terms in (C13) by $`(\ln4+4\ln\kappa)2^D`$, which directly yields (C14). The matching upper bound is given in [the all-to-all construction](unrestricted_connectivity.md).

## Corollary: lattice depth

Put the $`n`$ qubits on distinct vertices of $`\mathbb Z^d`$ and permit two-qubit gates only on nearest-neighbor edges. The occupied region need not be a filled box for this lower bound. Define

```math
S_d(D)=\sum_{\ell=1}^{D}(2\ell+1)^d.
```

Then

```math
\frac12\left\|\Psi_D-\mathcal R_n\right\|_\diamond
\geq
1-\exp\!\left[
-\frac{n}{8(4D+1)^d\kappa^{2S_d(D)}}
\right].
\qquad\mathrm{(C15)}
```

**Proof.** The forward cone from site $`i`$ lies in the lattice ball of radius $`\ell`$ around $`i`$, and therefore contains at most $`(2\ell+1)^d`$ sites at round $`\ell`$. Select input sites greedily at pairwise lattice distance greater than $`2D`$. Each selection excludes at most $`(4D+1)^d`$ occupied sites, leaving at least $`n/(4D+1)^d`$ selected sites. Their radius-$`D`$ balls, and hence their full final cones, are disjoint. Equation (C2) with $`V=S_d(D)`$ proves the claim. $`\square`$

Success with error at most $`\epsilon\in(0,1)`$ requires

```math
\ln n
\leq
d\ln(4D+1)+2\ln\kappa\,S_d(D)
+\ln\!\left[-8\ln(1-\epsilon)\right].
\qquad\mathrm{(C16)}
```

For fixed $`d`$, $`\eta`$, and $`\epsilon`$, the bound $`S_d(D)\leq D(2D+1)^d`$ gives

```math
D=\Omega_{d,\eta,\epsilon}\!\left((\ln n)^{1/(d+1)}\right).
\qquad\mathrm{(C17)}
```

[The geometric construction](geometric_construction.md#theorem-geometric-mixing-depth) attains this order on filled regular regions. The lower bound remains valid for sparse or thin regions; a matching upper with the ambient dimension is not asserted for such layouts.

## Relation to earlier mixing constructions

Scrambling-enhanced decay under local noise and its connection to light-cone size are established mechanisms, including in [Quek et al.](../references/RELATED_WORK.md#quek2024). The bound here addresses the opposite direction of the optimization: every admissible circuit, with arbitrary unitary gates, must leave distinguishable information until its causal histories have accumulated sufficient noisy support. The inverse observables are a proof device; the final binary POVMs are physical measurements.
