# Passive depolarization and its global mixing scale

The controlled protocols are compared with the same register subjected to the same noise, with every unitary layer replaced by the identity. No auxiliary space or weaker error criterion is introduced into this baseline.

Let $`\lambda=-\log\eta>0`$. After $`D`$ idle rounds,

```math
\Psi_D^{\mathrm{pass}}
=
\mathcal D_a^{\otimes n},
\qquad
a=\eta^D=e^{-\lambda D}.
```

Each individual qubit relaxes on a constant round scale at fixed $`\eta`$. Requiring one fixed global error for the entire register gives a different dependence on $`n`$.

## Exact complete-channel error

The single-qubit Pauli-error probabilities are

```math
p_I=\frac{1+3a}{4},
\qquad
p_X=p_Y=p_Z=\frac{1-a}{4}.
```

The completely depolarizing channel has all four probabilities equal to $`1/4`$. By the [Pauli-channel distance identity](channel_distance.md#lemma-pauli-channel-distance), the half-diamond error is the total variation distance between the corresponding product distributions.

Both distributions, conditional on the number $`J`$ of identity labels, are uniform over patterns with that number of identities. Thus the full error has the exact one-dimensional expression

```math
\delta_{\mathrm{pass}}(n,D)
=
\mathrm{TV}\!\left(
\mathrm{Bin}\!\left(n,\frac{1+3\eta^D}{4}\right),
\mathrm{Bin}\!\left(n,\frac14\right)
\right).
```

Equivalently, with $`p=(1+3\eta^D)/4`$,

```math
\delta_{\mathrm{pass}}(n,D)
=
\frac12\sum_{j=0}^{n}\binom nj
\left|
p^j(1-p)^{n-j}
-\left(\frac14\right)^j\left(\frac34\right)^{n-j}
\right|.
```

This formula includes the optimal reference-assisted input. It is not a restriction to product quantum inputs.

## Finite upper bound

One qubit has three nonidentity Pauli multipliers equal to $`a`$. Write $`p_{\mathrm P}`$ for its four-outcome Pauli-error distribution and $`u`$ for the uniform distribution on those four outcomes. Fourier chi-square tensorization gives

```math
\chi^2(p_{\mathrm P}^{\otimes n}\|u^{\otimes n})
=
(1+3a^2)^n-1.
```

Therefore

```math
\delta_{\mathrm{pass}}(n,D)
\le
\min\left\{1,\frac12\sqrt{(1+3\eta^{2D})^n-1}\right\}.
```

In particular, it is sufficient to choose

```math
D\ge
\frac{\log(3n)-\log\!\bigl(\log(1+4\epsilon^2)\bigr)}
{2\lambda}.
```

The ceiling and a maximum with zero give an integer sufficient depth. This follows from $`(1+x)^n\le e^{nx}`$.

## Finite lower bound

Use the valid input $`|+\rangle^{\otimes n}`$ and measure every output qubit in the $`X`$ basis. The outcomes are independent bits of bias $`a`$; on $`\tau_n`$ they are independent fair bits.

The Bhattacharyya affinity of one biased bit with a fair bit is

```math
B(a)=\frac{\sqrt{1+a}+\sqrt{1-a}}{2}
\le e^{-a^2/8}.
```

Affinity tensorizes, and total variation is at least one minus affinity. The channel error consequently satisfies

```math
\delta_{\mathrm{pass}}(n,D)
\ge
1-\exp\!\left(-\frac{n\eta^{2D}}8\right).
```

If the error is at most $`\epsilon<1`$, this implies the necessary bound

```math
D\ge
\frac{\log n-\log[-8\log(1-\epsilon)]}{2\lambda}.
```

A negative right-hand side is simply a vacuous finite-size lower bound.

## The passive cutoff scale

The two finite bounds differ by only a constant number of rounds when $`\eta`$ and $`\epsilon`$ are fixed. Hence

```math
D_{\mathrm{pass}}(n,\eta,\epsilon)
=
\frac{\log n}{2\lambda}+O_{\eta,\epsilon}(1).
```

The logarithm arises because many individually small residual biases remain jointly distinguishable. The causal lower bound for controlled circuits uses the same statistical accumulation, but obtains the residual biases through inverse-channel observables on separated causal cones.

Control changes how quickly those local records can be attenuated. The [geometric](geometric_construction.md) and [unrestricted-connectivity](unrestricted_connectivity.md) constructions accelerate their destruction while preserving the same whole-register error criterion.

