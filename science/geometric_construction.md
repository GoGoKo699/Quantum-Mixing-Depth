# Optimal complete mixing on a lattice

This construction matches the geometric lower bound using only the qubits whose information is being erased. It organizes Clifford gates along coordinate lines so that every nonidentity Pauli operator acquires a large total support across selected stage boundaries. Local depolarization at those boundaries then suppresses the entire quantum channel, including its action on inputs entangled with a reference.

## Theorem: geometric mixing depth

Fix $`d\geq1`$, $`0<\eta<1`$, and $`0<\epsilon<1`$. Consider $`n=L^d`$ arbitrary input qubits on the filled lattice cube $`[L]^d`$, with rounds as defined in [the model](model.md): a layer of disjoint nearest-neighbor two-qubit unitaries and one-qubit unitaries, followed by depolarization with retention $`\eta`$ on every site. Identity layers are allowed and are charged as rounds.

Let $`D_{\min}([L]^d,\eta,\epsilon)`$ be the minimum number of rounds for which

```math
\frac12\left\|\Psi_D-\mathcal R_n\right\|_\diamond
\leq\epsilon,
\qquad
\tau_n=I/2^n.
```

Then, as $`L\to\infty`$,

```math
D_{\min}([L]^d,\eta,\epsilon)
=\Theta_{d,\eta,\epsilon}\!\left((\ln n)^{1/(d+1)}\right).
\tag{G1}
```

The lower bound allows arbitrary unitary gates. The upper uses a fixed Clifford circuit, with no ancillary qubits, measurements, resets, discarded outputs, or fresh randomness during execution. Every input qubit may be entangled with an inaccessible reference, and every physical output is included in the criterion.

The same upper bound applies to filled rectangular regions whose shortest side is at least the block scale specified below. A thin or sparse region is not covered by the matching upper solely because it is embedded in $`\mathbb Z^d`$.

The lower half of (G1) is [the lattice causal-cone bound](causal_bound.md#corollary-lattice-depth). The remainder of this file proves the upper half, including finite error and depth bounds. Set

```math
\lambda=-\ln\eta>0,
\qquad
\alpha=\frac1{10}.
```

## Lemma: line branch weight

For every positive integer $`m`$, there is an $`m`$-qubit Clifford $`V_m`$ such that

```math
w(P)+w(V_mPV_m^\dagger)\geq\alpha m
\qquad\text{for every nonidentity Pauli }P.
\tag{G2}
```

Here $`w(P)`$ counts nonidentity tensor factors; Pauli phases are ignored.

**Proof.** The Clifford group acts transitively on the nonidentity Pauli operators modulo phase. One way to see this is to use local Clifford gates to turn each nonidentity factor into $`Z`$, CNOT gates to reduce a product of $`Z`$ operators to one factor, and a swap to move it to the first site. Thus a uniformly sampled Clifford sends any fixed nonidentity Pauli uniformly to one of the $`4^m-1`$ nonidentity Paulis.

Put $`r=\lfloor\alpha m\rfloor`$ and let

```math
A_r=\sum_{j=1}^{r}3^j\binom mj
```

be the number of nonidentity Paulis with weight at most $`r`$. A union bound gives

```math
\Pr\!\left[
\exists P\neq I: w(P)\leq r,
\ w(V_mPV_m^\dagger)\leq r
\right]
\leq\frac{A_r^2}{4^m-1}.
\tag{G3}
```

Write $`H_2(x)=-x\log_2x-(1-x)\log_2(1-x)`$ and $`\beta=H_2(\alpha)+\alpha\log_23<2/3`$. The binomial-tail bound for $`\alpha\leq1/2`$ implies

```math
A_r
\leq3^r\sum_{j=0}^{r}\binom mj
\leq2^{\beta m}.
```

For completeness, the binomial-tail bound follows by setting $`q=r/m`$. For $`0<q\leq1/2`$ and $`j\leq r`$,
$`q^j(1-q)^{m-j}\geq q^r(1-q)^{m-r}=2^{-mH_2(q)}`$.
Summing these terms in the binomial distribution gives
$`\sum_{j=0}^{r}\binom mj\leq2^{mH_2(q)}`$; the case $`r=0`$ is immediate.

Since $`4^m-1\geq(3/4)4^m`$, the right side of (G3) is at most

```math
\frac43\,2^{-2(1-\beta)m}
<\frac43\,2^{-2m/3}<1
\qquad(m\geq1).
```

There is therefore a Clifford with no such pair. For this Clifford at least one of the two weights is greater than $`r`$, which implies (G2). $`\square`$

The argument is an existence proof. A suitable $`V_m`$ is selected in advance and then used as a fixed unitary, independently of the unknown input state. No random choice is averaged into the implemented quantum channel.

## Linear depth on a line

The compilation input is [Maslov and Yang, Lemma 4](../references/RELATED_WORK.md#maslov2023): an arbitrary $`m`$-qubit Clifford can be implemented on a linear nearest-neighbor architecture, without ancillary qubits, with two-qubit gate depth at most $`7m-4`$.

That source counts entangling depth. The present model charges all rounds, including one-qubit gates. To translate the source bound, take an entangling-layer schedule of depth $`h`$. On each wire, combine the one-qubit gates between consecutive two-qubit gates and move their product immediately before the next two-qubit gate on that wire. Such movement crosses only gates on other wires and therefore preserves the ideal unitary. One parallel one-qubit layer before each entangling layer, plus a final one-qubit layer, implements the same Clifford in at most $`2h+1`$ charged layers. Thus the conservative bound

```math
D_{\mathrm{line}}(m)\leq14m
\tag{G4}
```

is sufficient. Equivalently, these local factors can be absorbed into the arbitrary two-qubit Clifford gates allowed by the model. Every compiled layer is followed by the required product noise.

Only the ideal product of the compiled gates must equal $`V_m`$. During its noisy implementation, every input Pauli follows the corresponding Clifford Pauli path and acquires scalar factors $`\eta^{w}`$. Additional noisy rounds cannot create new Pauli components or increase the magnitude of that coefficient. This is the [noisy Clifford reduction](channel_distance.md#lemma-noisy-clifford-reduction).

## Coordinate-line recursion

Let

```math
R=[m_1]\times\cdots\times[m_d],
\qquad
b=\prod_{j=1}^{d}m_j
```

be a filled rectangular block. A line stage in coordinate $`j`$ applies a fixed Clifford $`V_{m_j}`$ obeying (G2) to every coordinate-$`j`$ line, in parallel. The lines are disjoint, and every gate in their compiled circuits is a nearest-neighbor lattice gate.

Define the sequence of line stages recursively. For $`d=1`$, apply $`V_{m_1}`$. For $`d>1`$:

1. Apply the $`(d-1)`$-dimensional sequence in parallel in every hyperplane with fixed last coordinate.
2. Apply $`V_{m_d}`$ along all lines in the last coordinate, in parallel.
3. Apply the same $`(d-1)`$-dimensional sequence in each hyperplane again.

The last sequence need not invert the first. Let $`S_R`$ be the ideal Clifford obtained from the complete sequence. The number of line stages satisfies

```math
q_1=1,
\qquad q_d=2q_{d-1}+1=2^d-1.
\tag{G5}
```

For example, the coordinate sequences in dimensions two and three are $`(1,2,1)`$ and $`(1,2,1,3,1,2,1)`$.

For an input Pauli $`P`$, let $`P_j`$ be its ideal image after the first $`j`$ line stages, with $`P_0=P`$. There are $`q_d+1=2^d`$ stage boundaries, including the initial and final boundaries. Define

```math
W_R(P)=\sum_{j=0}^{q_d}w(P_j).
\tag{G6}
```

## Lemma: checkpoint weight

For every nonidentity Pauli on $`R`$,

```math
W_R(P)\geq\alpha^d b.
\tag{G7}
```

**Proof.** Proceed by induction on $`d`$. The case $`d=1`$ is (G2).

For $`d>1`$, a hyperplane with fixed last coordinate has volume
$`b'=\prod_{j=1}^{d-1}m_j`$.
Let $`r`$ be the number of such hyperplanes on which the input Pauli is nonidentity. This number is unchanged by the first recursive sequence: a Clifford acting within one hyperplane sends its identity Pauli to itself and sends every nonidentity Pauli to another nonidentity Pauli.

Let $`r'`$ be the number of nonidentity hyperplanes immediately after the middle line stage. By the induction hypothesis and additivity of Pauli weight on disjoint hyperplanes, the total weight at the checkpoints of the first recursive sequence is at least $`r\alpha^{d-1}b'`$. The total for the last recursive sequence is at least $`r'\alpha^{d-1}b'`$.

These checkpoint sets are disjoint: the first ends immediately before the middle line stage, and the second begins immediately after it. Together they contain every checkpoint of the full sequence. Therefore

```math
W_R(P)\geq(r+r')\alpha^{d-1}b'.
\tag{G8}
```

At least one line acted on in the middle stage has a nonidentity incoming Pauli restriction, because the full incoming Pauli is nonidentity. On this line the incoming weight is at most $`r`$, and the outgoing weight is at most $`r'`$: each line meets each hyperplane at one site. The line branch-weight property gives

```math
r+r'\geq\alpha m_d.
\tag{G9}
```

Combining (G8) and (G9) proves $`W_R(P)\geq\alpha^d m_db'=\alpha^d b`$. $`\square`$

The lemma controls all nonidentity Paulis, including those chosen to have small support at an intermediate checkpoint. It does not require every Pauli to have large support at the final boundary.

## Proposition: block mixing

Insert $`t`$ identity rounds at each of the $`2^d`$ checkpoints of the block sequence, where $`t`$ is a positive integer. Each identity round is followed by the same product depolarization as every gate round. Let $`\Psi_R`$ be the resulting noisy channel.

After conjugating the output by the inverse ideal Clifford $`S_R^\dagger`$ for analysis, the resulting Pauli channel $`\Lambda_R`$ has coefficients

```math
\Lambda_R(P)=a_PP,
\qquad
a_I=1,
\qquad
0\leq a_P\leq e^{-\lambda t\alpha^d b}\qquad(P\neq I).
\tag{G10}
```

If $`p_R`$ is its Pauli-error distribution and $`u_R`$ is uniform over the $`4^b`$ Paulis, then

```math
\chi^2(p_R\Vert u_R)
\leq(4^b-1)e^{-2\lambda t\alpha^d b}.
\tag{G11}
```

**Proof.** Every elementary Clifford gate permutes Pauli operators up to sign, and depolarization multiplies a Pauli by $`\eta`$ for each occupied site. At the checkpoints, the inserted identity rounds contribute the factor

```math
\eta^{tW_R(P)}
\leq\eta^{t\alpha^db}.
```

Noise during the compiled line stages only contributes further factors in $`(0,1]`$. Consequently,
$`\Psi_R(P)=a_PS_RPS_R^\dagger`$ with the bound (G10). The final inverse conjugation is used only to compute channel distance; it is not part of the implemented protocol. It leaves the maximally mixed target invariant.

The channel $`\Lambda_R`$ is completely positive, trace preserving, and diagonal in the Pauli basis, so it is a Pauli channel. Parseval's identity for its Pauli-error probabilities gives

```math
\chi^2(p_R\Vert u_R)=\sum_{P\neq I}a_P^2,
```

which proves (G11). The normalization and complete-channel distance identities are given in [the channel-distance analysis](channel_distance.md#lemma-pauli-channel-distance). $`\square`$

For the construction below, set $`t=m`$ and write $`c=\lambda\alpha^d`$. If $`m\geq\ln4/c`$, then every block of volume $`b\geq m^d`$ satisfies

```math
\begin{aligned}
\chi^2(p_R\Vert u_R)
&\leq \exp\!\left[b\ln4-2cmb\right]\\
&\leq e^{-cmb}
\leq e^{-cm^{d+1}}.
\end{aligned}
\tag{G12}
```

## Tiling the physical register

Consider a filled rectangular register $`[L_1]\times\cdots\times[L_d]`$ with $`n=\prod_jL_j`$. Fix an integer $`m\leq\min_jL_j`$.

Each coordinate interval can be partitioned into intervals of integer lengths between $`m`$ and $`2m-1`$. Explicitly, write $`L_j=q_jm+r_j`$ with $`q_j\geq1`$ and $`0\leq r_j<m`$; use one interval of length $`m+r_j`$ and $`q_j-1`$ intervals of length $`m`$. Their Cartesian products tile the register into $`B`$ disjoint rectangular blocks, each with volume at least $`m^d`$. No site is omitted or added, and

```math
B\leq\frac{n}{m^d}.
\tag{G13}
```

Run the block protocols in parallel, with $`t=m`$ noise rounds at every checkpoint. Use the same recursive coordinate sequence in each block. During a line stage, shorter compiled circuits can be padded with identities so that every block reaches the next checkpoint at the same round. This padding only adds depolarization along existing Pauli paths.

Each line has length at most $`2m`$, so (G4) bounds each line stage by $`28m`$ charged rounds. The full protocol therefore has depth

```math
D\leq C_dm,
\qquad
C_d=28(2^d-1)+2^d.
\tag{G14}
```

The first term counts all compiled gate rounds, including one-qubit gates. The second counts the inserted idle rounds at all checkpoints. Constants are chosen for transparent accounting and are not optimized.

## Complete error of the parallel blocks

The ideal block Cliffords tensor together. Conjugating the whole output by their inverse tensor product reduces the analysis to a tensor product of Pauli channels. This is a channel identity, so it applies to arbitrary inputs entangled across blocks and with an inaccessible reference.

By [chi-square tensorization](channel_distance.md#lemma-chi-square-tensorization), (G12) implies

```math
\begin{aligned}
\frac12\left\|\Psi_D-\mathcal R_n\right\|_\diamond
&\leq\frac12
\sqrt{\left(1+e^{-cm^{d+1}}\right)^B-1}\\
&\leq\frac12
\sqrt{\exp\!\left(B e^{-cm^{d+1}}\right)-1}.
\end{aligned}
\tag{G15}
```

This is a finite error bound for every permitted tiling, provided $`m\geq\ln4/c`$. In particular, it suffices that

```math
B e^{-cm^{d+1}}\leq\ln(1+4\epsilon^2).
\tag{G16}
```

A simple explicit block choice avoids solving an implicit equation involving $`B`$. Put

```math
L_\epsilon=\ln(1+4\epsilon^2),
\qquad
\ln_+(x)=\max\{0,\ln x\},
```

and choose

```math
m_n=
\left\lceil
\max\left\{
1,\frac{\ln4}{c},
\left(\frac{\ln_+(n/L_\epsilon)}{c}\right)^{1/(d+1)}
\right\}
\right\rceil.
\tag{G17}
```

Whenever $`\min_jL_j\geq m_n`$, the tiling and protocol exist. Because $`B\leq n`$, this choice implies (G16), and hence error at most $`\epsilon`$ with depth at most $`C_dm_n`$.

For fixed $`d`$, $`\eta`$, and $`\epsilon`$,

```math
m_n=O_{d,\eta,\epsilon}\!\left((\ln n)^{1/(d+1)}\right).
```

On growing cubes, $`m_n=o(L)`$, so the tiling condition holds for all sufficiently large $`L`$. This proves the upper half of (G1). Combining it with the arbitrary-unitary lattice converse completes the theorem.

## Scope and inherited ingredients

High Pauli weight increases attenuation by local depolarization. That mechanism and rapidly mixing noisy-circuit constructions are established, including in [Quek et al.](../references/RELATED_WORK.md#quek2024). The present proof uses the inherited [linear-neighbor Clifford compiler](../references/RELATED_WORK.md#maslov2023), an elementary branch-weight existence argument, and the coordinate recursion to control every nonidentity Pauli simultaneously. The complete-channel estimate is what makes the conclusion uniform over unknown quantum inputs and references.

The theorem concerns the prescribed sequence of unitary layers and local-noise rounds. It does not identify the noisy evolution during a finite-duration entangling Hamiltonian with an ideal Clifford followed by depolarization. The proof also does not require or establish a finite-temperature thermal reset, a continuous-time control optimum, or a separation from classical reversible mixing.
