# Complete mixing through stationary noise contacts

Only designated lattice sites depolarize in this model. Coherent gates can move information to those sites and spread it across many carriers. The optimal depth is set by both the total rate of contact uses and the number of uses accessible within a causal cone.

## The stationary-contact law

Put $`n=L^d`$ qubits on the filled nearest-neighbor cube $`[L]^d`$. For each coordinate, let $`s_j\mid L`$. Partition the cube into cells of side lengths $`s_1,\ldots,s_d`$, with one contact at the minimum-coordinate corner of each cell. Write

```math
A=\prod_{j=1}^d s_j,\qquad |S|=n/A.
```

Each charged round first applies disjoint one- and two-qubit gates, then applies independent depolarization of retention $`\eta`$ at the fixed sites in $`S`$. Noncontacts are noiseless. The identity gate layer is allowed. The policy is a fixed gate sequence with no auxiliary qubits, measurements, resets, discarded outputs, or fresh control randomness. Every output is included in the distance to the maximally mixed replacer $`\mathcal R_n`$. The half-diamond error permits arbitrary reference entanglement.

For fixed $`d`$, $`0<\eta<1`$, and $`0<\epsilon<1/2`$, the optimal depth satisfies, uniformly in the allowed spacings as $`L\to\infty`$,

```math
D_{\min}(L,S,\eta,\epsilon)
=\Theta_{d,\eta,\epsilon}\!\left(
\max\left\{A,(A\ln n)^{1/(d+1)}\right\}\right).
```

The lower bound allows arbitrary gates on the specified one- and two-qubit supports. The upper uses fixed Clifford gates. The case $`A=1`$ gives the [uniform-noise lattice law](geometric_construction.md#theorem-geometric-mixing-depth). The terms cross at $`A\asymp (\ln n)^{1/d}`$ when the allowed grids approach that scale. With one contact for the entire cube, $`A=n`$ and the depth is linear in $`n`$.

## Throughput and causal converses

**Throughput.** A depth-$`D`$ circuit uses $`K=D|S|`$ one-qubit depolarizers. Each is a mixture of four Pauli conjugations, so the normalized Choi state of the full circuit is a mixture of at most $`4^K`$ pure states, even with arbitrary interleaved unitaries. The normalized Choi state of $`\mathcal R_n`$ is $`I/4^n`$. Testing the support of the actual Choi state gives

```math
\tfrac12\lVert \Psi_D-\mathcal R_n\rVert_\diamond
\ge 1-4^{K-n},\qquad
D\ge A\left(1+\frac{\ln(1-\epsilon)}{n\ln 4}\right)
\quad\text{if the error is at most }\epsilon.
```

An entropy refinement counts likely contact strings. Let $`p_\eta=((1+3\eta)/4,(1-\eta)/4,(1-\eta)/4,(1-\eta)/4)`$ and use base-two entropy $`H(p_\eta)`$ and self-information standard deviation $`\sigma_\eta`$ in bits. For any $`0<\delta<1-\epsilon`$, Chebyshev's inequality gives probability at least $`1-\delta`$ to strings with self-information at most $`KH(p_\eta)+\sigma_\eta\sqrt{K/\delta}`$. There are at most $`2^{KH(p_\eta)+\sigma_\eta\sqrt{K/\delta}}`$ such strings. Projecting onto the span of their Choi vectors and comparing with the tracial Choi state yields the necessary condition

```math
KH(p_\eta)+\sigma_\eta\sqrt{K/\delta}
\ge 2n+\log_2(1-\delta-\epsilon).
```

At fixed $`\eta,\epsilon`$ this gives $`D/A\ge2/H(p_\eta)-O_{\eta,\epsilon}(n^{-1/2})`$, by taking a fixed $`\delta`$ and either using $`K=O(n)`$ in the square-root term or using the stronger direct bound when $`K`$ exceeds a sufficiently large multiple of $`n`$.

**Causal exposure.** In the [inverse-observable proof](causal_bound.md#theorem-causal-cone-bound), let $`C_i(\ell)`$ be the full forward cone of input site $`i`$ just after gates in round $`\ell`$. Set

```math
V_i(D)=\sum_{\ell=1}^D |C_i(\ell)\cap S|,\qquad
\kappa=2/\eta-1.
```

Only inverse noise maps on contacts inside the cone can increase the norm of the inverse observable. The recursive observable for $`X_i`$ therefore has norm at most $`\kappa^{V_i(D)}`$ and pulls back to $`X_i`$ exactly. On disjoint full cones the recursion also pulls back products. Measuring the normalized observables on the evolved product $`|+\rangle^{\otimes n}`$ gives independent bits of biases $`\kappa^{-V_i(D)}`$, whereas the tracial output gives independent fair bits.

Greedy packing of radius-$`D`$ lattice balls supplies at least $`n/(4D+1)^d`$ disjoint cones. With $`V_{\max}=\max_i V_i(D)`$, the binary affinity bound gives

```math
\tfrac12\lVert \Psi_D-\mathcal R_n\rVert_\diamond
\ge 1-\exp\!\left[-\frac{n}{8(4D+1)^d\kappa^{2V_{\max}}}\right].
```

At round $`\ell`$ the number of contacts in any cone is at most $`\prod_j(1+2\ell/s_j)`$ by enclosing the cone in a coordinate box. The rank bound gives $`D\ge A/2`$ at the stated error. Then $`s_j\le A\le 2D`$ for every $`j`$, giving $`V_{\max}\le 4^d D^{d+1}/A`$ by using $`1+2D/s_j\le 4D/s_j`$ in every round. If $`(A\ln n)^{1/(d+1)}\le A`$, throughput suffices. Otherwise $`A<(\ln n)^{1/d}`$ and the targeted depth is at most $`(\ln n)^{1/d}`$. For $`D`$ below this target, the packing factor costs $`O_d(\ln\ln n)`$ in the logarithm. The error inequality then forces $`D^{d+1}/A=\Omega_{d,\eta,\epsilon}(\ln n)`$.

## Returning sweeps and Clifford upper bound

**Returning sweep.** In every cell choose a serpentine nearest-neighbor path starting at its contact. Alternate SWAP matchings on edges $`(1,2),(3,4),\ldots`$ and $`(2,3),(4,5),\ldots`$ of the path for $`2A`$ rounds. Each wire label moves one position per round in the interior. At an endpoint it waits one round and reverses. Thus every label returns to its initial position and visits the contact exactly twice, counting positions after the gate layer. For a singleton the two layers are idle. The executed channel on the cell is exactly $`\mathcal D_{\eta^2}^{\otimes A}`$ because the independent noise acts on the visiting wire labels and the final permutation is the identity. All cells sweep in parallel. This applies to arbitrary cell inputs and correlations.

**Checkpoint schedule.** Set $`m=\lceil\max\{A,(A\ln n)^{1/(d+1)}\}\rceil`$ and $`q=\lceil C m/A\rceil`$, with $`C`$ a constant chosen below. When $`m\le L`$, tile the lattice with rectangular blocks of side lengths at least $`m`$ and at most $`4m`$, aligned to whole contact cells. In coordinate $`j`$, group $`\lceil m/s_j\rceil`$ consecutive cells and attach any remaining cells to the final full group. Such a group fits because $`s_j\mid L`$ and $`m\le L`$. Run the existing [recursive coordinate-line Clifford schedule](geometric_construction.md#coordinate-line-recursion) in each block. Insert $`q`$ returning sweeps at each of its $`2^d`$ checkpoints. The compiled gate stages have depth $`O_d(m)`$, and each set of sweeps costs $`2qA=O(m)`$.

For each nonidentity Pauli in a block of volume $`b`$, the sum of its ideal checkpoint weights is at least $`\alpha^d b`$ with $`\alpha=1/10`$ by the [checkpoint lemma](geometric_construction.md#lemma-checkpoint-weight). Its coefficient is at most $`\exp[-2q(-\ln\eta)\alpha^d b]`$ after the sweeps. Contact noise during the compiled gate stages only adds factors in $`(0,1]`$ along each Clifford Pauli path. Consequently, after undoing the ideal final Clifford for analysis,

```math
\chi^2(p_b\Vert u_b)
\le \exp\!\left[b\ln 4-4q(-\ln\eta)\alpha^d b\right].
```

Let $`L_\epsilon=\ln(1+4\epsilon^2)`$ and choose $`C=C(d,\eta,\epsilon)`$ large enough that the last expression is at most $`e^{-c b m/A}`$, where $`c=2+\ln_+(1/L_\epsilon)/\ln 2`$ and $`\ln_+(x)=\max(0,\ln x)`$. This is possible since $`m/A\ge1`$. When $`m\le L`$ and $`n\ge2`$, each block has $`b\ge m^d`$, so the sum over at most $`n`$ blocks is at most $`n e^{-c\ln n}\le L_\epsilon`$. When $`m>L`$, use one whole-cube block, with gate depth $`O_d(L)`$ and sweep depth $`O_d(m)`$. Its chi-square bound is at most $`e^{-cn}\le L_\epsilon`$. The singleton case uses the same single-block bound. In all cases, [Pauli distance and chi-square tensorization](channel_distance.md#lemma-chi-square-tensorization) give half-diamond error at most $`\epsilon`$ for the full register. This proves the matching depth.

## Transport-only benchmark

Allow only SWAPs and onsite unitary rotations. Follow the wire labels through the sequence and undo the ideal output unitary for analysis. Depolarization commutes with onsite rotations, so the resulting channel is the product of depolarizers of retentions $`\eta^{k_i}`$, where wire $`i`$ has encountered $`k_i`$ contact ticks and $`\sum_i k_i=D n/A`$. Measuring $`X`$ on product $`|+\rangle`$ inputs gives independent bits. Jensen's inequality and the same affinity bound give

```math
\tfrac12\lVert \Psi_D-\mathcal R_n\rVert_\diamond
\ge 1-\exp\!\left[-\frac18\sum_i\eta^{2k_i}\right]
\ge 1-\exp\!\left[-\frac{n}{8}\eta^{2D/A}\right].
```

Thus transport needs $`\Omega_{\eta,\epsilon}(A\ln n)`$ rounds. Repeating the returned sweeps $`O_{\eta,\epsilon}(\ln n)`$ times gives a product channel with small enough tracial chi-square distance and attains the order. The comparison charges the same contacts, rounds and error criterion to both control classes.

For a finite comparison, place the only contact on the second tensor factor of two sites and set $`\eta=1/2`$. Take the ideal gate prefixes $`I`$, $`\mathrm{SWAP}\,\mathrm{CNOT}_{2\to 1}(I\otimes H)`$, and $`\mathrm{SWAP}\,\mathrm{CZ}`$. The actual gates are consecutive prefix quotients. The three pulled-back Pauli error subspaces have generators $`(IX,IZ)`$, $`(XI,ZX)`$, and $`(XZ,ZI)`$. Their Fourier multipliers yield exact error $`3/16`$. Three rounds of transport give optimal visit counts $`(1,2)`$ up to exchange and error $`3/8`$. The [finite verification](../verification/README.md#stationary-contacts) compares these calculations with direct Choi evolution.

## Equal contact count, different layouts

Take $`2\le s\mid L`$. For a periodic layout, take all planes $`x_1=1+js`$ with $`0\le j\lt L/s`$, giving $`A=s`$. For a clustered layout, take the same number of planes as the slab $`1\le x_1\le L/s`$. A site at $`x_1=L`$ has a contact-free forward cone for $`D\lt L-L/s`$. Its exact inverse observable has norm one and distinguishes the evolved state from the maximally mixed state by half-diamond error at least $`1/2`$. For an upper bound, use whole-cube Clifford stages and, at each checkpoint, a fixed number of sweeps along the longitudinal paths, each beginning at its first-plane contact. The resulting attenuation is at least that of the single-plane schedule because extra contact noise only damps the Clifford paths. Depth is $`O_{d,\eta,\epsilon}(L)`$ by the weight and chi-square bounds. Hence the clustered optimum is $`\Theta_{d,\eta,\epsilon}(L)`$, while fixed-$`s`$ periodic depth is $`\Theta_{d,\eta,\epsilon}((\ln n)^{1/(d+1)})`$.

## Scope and dependencies

The theorem concerns discrete unitary and noise layers with calibrated fixed retention and a fixed global target error. General disordered layouts, exact leading depth constants, weak-noise limits and continuous-time Hamiltonian control remain open here. The protocol uses the existing branch-weight Clifford construction and known nearest-neighbor synthesis. The [related-work comparison](../references/RELATED_WORK.md#stationary-noise-and-contact-geometry) covers boundary-dissipative random circuits, inherited noise-enhanced scrambling, and the distinct pure-reset contact model.
