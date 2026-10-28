# From Pauli attenuation to complete-channel mixing

The upper constructions track individual Pauli operators through Clifford circuits. This page explains why those coefficients control the distance of the **whole channel** from complete depolarization, including inputs entangled across blocks or with an external reference.

The lower bound uses a different route: physical measurements of bounded inverse observables. That argument is developed in [causal bounds](causal_bound.md).

## Pauli conventions

Let $`\mathcal P_n=\{I,X,Y,Z\}^{\otimes n}`$ denote Hermitian Pauli representatives, with overall phases omitted when counting labels. There are $`4^n`$ labels. Pauli weight $`w(P)`$ counts nonidentity tensor factors.

The operators form an orthogonal basis:

```math
\mathrm{Tr}(PQ)=2^n\mathbf 1_{\{P=Q\}},
\qquad
X=2^{-n}\sum_{P\in\mathcal P_n}\mathrm{Tr}(PX)P.
```

Local depolarization acts diagonally in this basis:

```math
\mathcal N_\eta(P)=\eta^{w(P)}P.
```

For labels $`P,Q`$, define the commutation character $`\chi(P,Q)\in\{+1,-1\}`$ by $`PQP=\chi(P,Q)Q`$. These characters obey

```math
\sum_{P\in\mathcal P_n}\chi(P,Q)\chi(P,Q')
=
4^n\mathbf 1_{\{Q=Q'\}}.
```

This is Fourier orthogonality on the binary Pauli-label group. Global signs of a Hermitian representative have no effect on conjugation or weight.

## Lemma: noisy Clifford reduction

Take a fixed Clifford circuit $`U=U_D\cdots U_1`$, with the required noise after each layer. For an input Pauli $`P`$, let

```math
P_\ell
=
U_\ell\cdots U_1P U_1^\dagger\cdots U_\ell^\dagger
```

be its signed ideal image after layer $`\ell`$. Every $`P_\ell`$ is a signed Pauli. Therefore the noisy circuit satisfies

```math
\Psi_D(P)
=
a_P UPU^\dagger,
\qquad
a_P=\eta^{\sum_{\ell=1}^{D}w(P_\ell)},
\qquad
a_I=1.
```

An idle round contributes the current Pauli weight to the exponent. Noise does not branch a Pauli into a superposition, because depolarization is diagonal in the same basis.

For analysis, set

```math
\Lambda=\mathrm{Ad}_{U^\dagger}\circ\Psi_D.
```

Then $`\Lambda(P)=a_PP`$. This is a completely positive trace-preserving Pauli-diagonal map. Its Pauli-error representation is

```math
\Lambda(X)=\sum_{Q\in\mathcal P_n}p_Q QXQ,
\qquad
p_Q=4^{-n}\sum_{P\in\mathcal P_n}\chi(Q,P)a_P.
```

The coefficients satisfy $`p_Q\ge0`$ and $`\sum_Qp_Q=1`$. One way to see positivity is to apply $`\Lambda`$ to half of a maximally entangled state: its Choi state is diagonal in the Pauli-generated Bell basis, with eigenvalues $`p_Q`$. Complete positivity of the actual circuit then gives the claim.

This positivity is not inferred merely from $`a_P\ge0`$; an arbitrary positive list of Pauli multipliers need not define a channel. Here it follows from composition of physical maps.

Because output unitary conjugation leaves both the diamond norm and the maximally mixed replacer invariant,

```math
\frac12\|\Psi_D-\mathcal R_n\|_\diamond
=
\frac12\|\Lambda-\mathcal R_n\|_\diamond.
```

The inverse ideal circuit is not executed. It is a change of representation in the proof, with no additional rounds or physical outputs.

## Lemma: Pauli-channel distance

For Pauli channels $`\Lambda_p`$ and $`\Lambda_q`$ on the same register,

```math
\|\Lambda_p-\Lambda_q\|_\diamond
=
\sum_{P\in\mathcal P_n}|p_P-q_P|.
```

**Upper bound.** Each Pauli conjugation is a unitary channel and has diamond norm one. The triangle inequality gives

```math
\left\|\sum_P(p_P-q_P)\mathrm{Ad}_P\right\|_\diamond
\le\sum_P|p_P-q_P|.
```

**Lower bound.** Let $`|\Phi_n\rangle=2^{-n/2}\sum_x|x\rangle|x\rangle`$. The states $`(P\otimes I)|\Phi_n\rangle`$ form an orthonormal basis. Applying the channel difference to one half of $`|\Phi_n\rangle\langle\Phi_n|`$ therefore gives a diagonal operator with eigenvalues $`p_P-q_P`$. Its trace norm is their absolute sum, attaining the upper bound.

Complete depolarization corresponds to the uniform Pauli-error distribution $`u_P=4^{-n}`$. Consequently,

```math
\delta(\Psi_D)=\frac12\|p-u\|_1.
```

This exact reduction controls the worst entangled input, rather than a chosen state, observable, or measurement basis. General channel and Choi conventions are reviewed in [Watrous](../references/RELATED_WORK.md#watrous2018).

## Lemma: Fourier chi-square identity

For the Pauli-diagonal channel above,

```math
\chi^2(p\|u)
:=
\sum_Q\frac{(p_Q-u_Q)^2}{u_Q}
=
\sum_{P\ne I}a_P^2.
```

Indeed, the identity multiplier contributes exactly the uniform distribution. Subtracting it gives

```math
p_Q-u_Q
=
4^{-n}\sum_{P\ne I}\chi(Q,P)a_P.
```

Squaring, summing over $`Q`$, and using character orthogonality proves the identity. Cauchy–Schwarz then gives

```math
\delta(\Psi_D)
\le
\min\left\{1,\frac12
\sqrt{\sum_{P\ne I}a_P^2}\right\}.
```

A uniform attenuation estimate $`|a_P|\le e^{-A}`$ for all nonidentity Paulis yields

```math
\chi^2(p\|u)\le (4^n-1)e^{-2A}.
```

The factor $`4^n-1`$ is essential. Controlling only single-site Paulis or a typical Pauli does not establish the complete-channel bound.

## Lemma: chi-square tensorization

Let block $`j`$ have Pauli-error distribution $`p_j`$ and uniform distribution $`u_j`$. Set $`\xi_j=\chi^2(p_j\|u_j)`$. For the tensor-product channel,

```math
1+\chi^2\!\left(\bigotimes_{j=1}^{B}p_j
\,\middle\|\,
\bigotimes_{j=1}^{B}u_j\right)
=
\prod_{j=1}^{B}(1+\xi_j).
```

To verify this, write $`1+\chi^2(p\|u)=\sum_xp(x)^2/u(x)`$. The sum factors for product distributions. Hence

```math
\delta\!\left(\bigotimes_{j=1}^{B}\Psi_j\right)
\le
\frac12\sqrt{\prod_{j=1}^{B}(1+\xi_j)-1}
\le
\frac12\sqrt{\exp\!\left(\sum_{j=1}^{B}\xi_j\right)-1}.
```

A sufficient condition for error at most $`\epsilon`$ is therefore

```math
\sum_{j=1}^{B}\xi_j\le\log(1+4\epsilon^2).
```

The physical input need not be a product across blocks. The distributions being tensorized are the channel's Pauli-error distributions. The diamond norm already maximizes over arbitrary correlations between blocks and with a reference.

## How the upper bounds use this identity

The geometric construction acts on blocks of side scale $`m`$, with volume of order $`m^d`$. It forces every nonidentity Pauli to acquire integrated weight of order $`m^{d+1}`$, giving

```math
\xi_j\le\exp[-c_{d,\eta}m^{d+1}]
```

once $`m`$ exceeds a parameter-dependent threshold. Taking $`m`$ of order $`(\log n)^{1/(d+1)}`$ makes the sum over blocks bounded by the required constant.

With unrestricted connectivity, logarithmic-depth spreading on a block of $`b`$ qubits gives a different estimate, $`\xi_j\le e^{-c_\eta b}`$. Blocks of size $`b=\Theta(\log n)`$ then mix the whole register in depth $`O(\log b)=O(\log\log n)`$.

These reductions explain why blockwise constructions still give a global reference-sensitive statement. The [finite examples](finite_examples.md) compare direct channel calculations with the Pauli representation on small registers.

