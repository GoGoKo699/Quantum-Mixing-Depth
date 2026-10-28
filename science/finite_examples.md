# Finite examples and verification

The examples below test the mechanisms used in the [geometric construction](geometric_construction.md#theorem-geometric-mixing-depth) and [causal-cone converse](causal_bound.md#theorem-causal-cone-bound). They use the same discrete unitary-then-depolarization model. Every qubit is an input, every output is retained, and no auxiliary initialization is used.

The runnable checks are in [verification/run_all.py](../verification/run_all.py), with [instructions](../verification/README.md) and [complete reference output](../verification/expected_results.json). Integer enumeration certifies the stated finite Pauli results. Dense matrix checks provide numerical corroboration at the reported precision.

<a id="exact-line-example"></a>

## 1. An exact three-qubit line example

On sites $`0,1,2`$ of a line, apply the following seven gates chronologically:

```math
\mathrm{CX}_{0\to1},\quad
\mathrm{CX}_{1\to2},\quad
H_1,\quad
\mathrm{CX}_{1\to0},\quad
\mathrm{CX}_{2\to1},\quad
H_1,\quad
\mathrm{CX}_{0\to1}.
```

Every two-qubit gate is nearest-neighbor. Call the resulting Clifford $`V_3`$. Exact enumeration of its 63 nonidentity Pauli inputs gives

```math
\min_{P\ne I}\bigl[w(P)+w(V_3PV_3^\dagger)\bigr]=4.
```

There are 45 inputs with weight sum 4 and 18 with weight sum 6. For example, $`XII`$ maps to $`YZY`$. The words list sites 0 through 2 from left to right. The verifier checks that the full Pauli map is a permutation and preserves every commutation relation. An independent $`8\times8`$ matrix calculation checks all 64 Pauli matrices, including their signs; its largest Frobenius residual was $`1.26\times10^{-15}`$.

The finite constant 4 is a property of this particular three-qubit circuit. It is not substituted for the fixed asymptotic constant $`\alpha=1/10`$ in the [line-branch existence lemma](geometric_construction.md#lemma-line-branch-weight). No claim is made that seven gates is optimal.

<a id="recursive-checkpoints"></a>

## 2. Recursive checkpoint sums

The proof of the [checkpoint-weight lemma](geometric_construction.md#lemma-checkpoint-weight) can retain exact finite line branch weights. If the line circuit on axis $`j`$ has branch weight $`B_j`$, the same induction gives

```math
W_d(P)\ge\prod_{j=1}^d B_j
\qquad(P\ne I).
```

This is the finite form tested below. In addition to $`V_3`$, the verifier includes a fixed two-qubit Clifford with exact branch weight $`B_2=2`$. That smaller fixture supplies an exhaustively accessible eight-qubit three-dimensional test; it is not used to infer a large-block spreading rate.

| Block | Nonidentity inputs checked | Checkpoints | Bound from line certificates | Minimum found | Coverage |
|---|---:|---:|---:|---:|---|
| $`2\times3`$ | 4,095 | 4 | 8 | 8 | Exhaustive |
| $`3\times3`$ | 262,143 | 4 | 16 | 16 | Exhaustive |
| $`2\times2\times2`$ | 65,535 | 8 | 8 | 8 | Exhaustive |
| $`3\times3\times3`$ | 5,399 | 8 | 64 | 68 | Specified sample only |

The $`3\times3`$ circuit uses axis stages $`(0,1,0)`$. An input $`XXIIIIIII`$ has checkpoint weights

```math
(2,2,6,6),
```

so the sum 16 saturates the certified bound. The first stage need not increase a particular operator's weight. The theorem constrains the accumulated checkpoint weight, which is precisely the quantity charged by the inserted noise intervals.

The larger 3D case uses axis stages $`(0,1,0,2,0,1,0)`$. Its test set includes every weight-one and weight-two Pauli, structured line and hyperplane patterns, and fixed-seed pseudorandom samples. Its observed minimum 68 is **not** a certificate of the minimum over all $`4^{27}-1`$ nonidentity Paulis. The universal lower bound 64 for this fixture follows from the exact three-qubit line certificate and the mathematical induction.

<a id="noisy-choi-check"></a>

## 3. Actual noisy paths and complete block error

Use $`V_3`$ with three idle/noise rounds before its first gate and three after its last gate. Each of the seven gate rounds is also followed by local depolarization. The total cost is therefore 13 noisy rounds on the same three input qubits.

For every Pauli input, the verifier follows the support after each elementary gate. Its attenuation exponent is

```math
S(P)=3w(P)+\sum_{\ell=1}^{7}w(P_\ell)
       +3w(V_3PV_3^\dagger).
```

The endpoint branch certificate guarantees $`S(P)\ge12`$. Exact enumeration gives the stronger minimum $`S(P)=20`$ after the gate-round noise is included. Thus the calculation does not pretend that the encoding gates are noiseless, nor replace their intermediate supports by their endpoint supports.

After analytical conjugation by $`V_3^\dagger`$, the Pauli eigenvalues are exactly $`a_P=\eta^{S(P)}`$. The verifier constructs the Pauli-error probabilities by the finite Fourier transform and checks

```math
\chi^2(p\|u)=\sum_{P\ne I}a_P^2.
```

Independently, it starts from a maximally entangled state of the three data qubits and an eight-dimensional reference, executes every dense gate and noise channel on the data, and forms the normalized $`64\times64`$ Choi matrix. The direct trace distance from $`I/64`$ agrees with the exact Pauli-channel half-diamond error.

| Retention $`\eta`$ | Actual $`\chi^2`$ | Controlled half-diamond error | Passive half-diamond error after the same 13 rounds |
|---|---:|---:|---:|
| 0.85 | 0.0110793480 | 0.0322754419 | 0.1352655614 |
| 0.97 | 10.7376393808 | 0.4693022840 | 0.6928322563 |

These are exact Pauli-distribution expressions evaluated numerically for this finite circuit. They are not asymptotic estimates. The passive comparison uses the same three qubits, noise retention, round count, and complete error criterion. Its value is calculated using the [binomial formula](passive.md).

The decoded dense Choi matrix differs from the independently constructed Pauli-mixture Choi matrix by less than $`5.9\times10^{-16}`$ in Frobenius norm in these two cases. This verifies the full finite linear map, including its reference behavior, rather than only selected output states.

For two disjoint copies of the block protocol, direct enumeration of the $`4^6`$ Pauli-error probabilities gives half-diamond errors 0.0469861664 and 0.6759112960, respectively. The verifier checks the tensorization identity

```math
1+\chi^2(p\otimes p\|u\otimes u)
=\bigl(1+\chi^2(p\|u)\bigr)^2
```

and the resulting Cauchy-Schwarz upper bound. At $`\eta=0.97`$ that bound exceeds one before capping and is therefore uninformative, while the direct finite error remains well defined. Small block examples need not lie in the asymptotic regime where the theorem's coarse error bound is useful.

<a id="inverse-witness-check"></a>

## 4. Non-Clifford inverse witnesses with correlated final regions

The causal-cone proof requires independence of the constructed measurement outcomes. It does not require the corresponding final spatial regions to be in a product state. A four-qubit dense example checks this distinction.

In round one, apply a non-Clifford unitary to the middle pair $`(1,2)`$. In round two, apply non-Clifford unitaries in parallel to $`(0,1)`$ and $`(2,3)`$. Apply retention $`\eta=0.82`$ depolarization to every site after each round. The selected input sites are 0 and 3; their full forward cones are initially singleton sites and then the disjoint pairs $`\{0,1\}`$ and $`\{2,3\}`$.

For reproducibility, the three two-qubit gates are $`e^{-iH}`$ with the following Hamiltonians on the ordered pair $`(a,b)`$:

```math
\begin{aligned}
H_{\mathrm{middle}}
 &=0.31X_aX_b+0.23Z_a+0.17Y_aZ_b,\\
H_{\mathrm{left}}
 &=0.27Z_aX_b+0.19Y_aY_b+0.13Z_b,\\
H_{\mathrm{right}}
 &=0.22X_aZ_b+0.11Y_a+0.37Z_aY_b.
\end{aligned}
```

Starting from $`|+\rangle^{\otimes4}`$, the two final pairs are correlated: the Frobenius distance between the output and the product of its two pair marginals is 0.0734722832. An argument based only on independence of the spatial output regions would therefore fail on this example.

Construct the two witnesses by the exact inverse-adjoint recursion used in the [converse](causal_bound.md#theorem-causal-cone-bound). The cone sizes are one and two in the successive rounds, so the common norm bound is

```math
K=(2/\eta-1)^3=2.9799190377.
```

The actual witness norms are 1.7002823659 and 1.7694445094. Dense evolution verifies

```math
\Phi^\dagger(A_0)=X_0,\qquad
\Phi^\dagger(A_3)=X_3,\qquad
\Phi^\dagger(A_0A_3)=X_0X_3,
```

with Frobenius residuals below $`1.8\times10^{-14}`$. The witnesses commute and remain supported on their disjoint forward cones to the same numerical precision.

The two POVMs $`(I\pm A_i/K)/2`$ then give independent bits of bias $`1/K=0.3355795870`$. In sign order $`(--),(-+),(+-),(++)`$, the probabilities are

```math
(0.1103636213,
  0.2218465852,
  0.2218465852,
  0.4459432083).
```

They agree with the product formula to within $`1.2\times10^{-16}`$. Their total variation from fair independent bits is 0.1959432083, below the physical output's trace distance 0.5110428241 as required by data processing. The analytical Bhattacharyya lower bound is 0.0277608005. This finite gap is consistent with a converse designed to obtain the depth scaling rather than tight constants.

<a id="passive-check"></a>

## 5. Passive baseline and verification limits

For four small choices of register size, noise retention, and depth, the verifier independently constructs the complete $`4^n`$ passive Pauli-error distribution and the two binomial distributions in the [passive error formula](passive.md). Their total variation distances agree within $`2.3\times10^{-16}`$. The stated finite upper and lower bounds also hold in all four cases.

The exact finite enumerations and the noisy three-qubit example check different parts of the proof. They do not replace the probabilistic existence argument for a family of good line Cliffords, the imported linear-depth synthesis theorem, or the arbitrary-size causal-cone argument. The 27-qubit calculation is sampled. Dense calculations use floating-point linear algebra, not interval arithmetic. The non-Clifford check verifies the converse's witnesses for one valid input, rather than computing that channel's full diamond norm.

No discrepancy was found in these checks. The full [JSON output](../verification/expected_results.json) records the finite counts, witnesses, histograms, numerical errors, and tolerances needed to reproduce this assessment.
