# A 30-milestone map of quantum mixing depth

This map follows one question: how many local gate-and-noise rounds are needed to replace every possible input of a quantum register by the maximally mixed state, including the removal of correlations with an inaccessible reference? The [scientific model](../science/model.md) fixes that task. The [proof pages](../science/model.md#theorem-g-the-geometric-optimum) give the authoritative statements and derivations.

The selected educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](WATROUS_BRIDGE.md) identifies the relevant sections and translates their conventions. Section and theorem numbers below refer to the author's January 2018 manuscript. Links labeled with a Watrous section open the corresponding official chapter PDF. The book supplies the channel, norm, and composite-system framework; the project pages supply the causal-cone, checkpoint, and depth arguments. Primary research papers cited for imported results are proof dependencies, not additional educational anchors.

The allocation is **13 background/preliminary milestones and 17 narrative/innovation milestones**. The background moves from individual states and observables to complete channel error on a composite register. The narrative moves from individual surviving observables and local spreading operations to matching depth laws, their interpretation, and their scope. Each phase ends in a synthesis. Dependencies name earlier milestones that supply a direct conceptual prerequisite; their own dependencies are inherited.

| Phase | Milestones | Scientific progression | Closing synthesis |
| --- | --- | --- | --- |
| Background and preliminaries | M01–M13 | States and local noise; circuits and distinguishability; complete channel distance and tensor products | The exact optimization problem and its resources |
| Narrative and innovation | M14–M30 | Passive benchmark; universal converse; geometric and unrestricted constructions; meaning and limitations | The three depth laws as one account of information loss |

## Phase I: background and preliminaries

<a id="m01"></a>

### M01. States and the maximally mixed target

**Central question.** What does it mean for a quantum register to have forgotten its input?

**Understanding target.** Interpret a density operator as the object that determines measurement probabilities. Identify the maximally mixed state $`\tau_n=I/2^n`$ and the replacement channel $`\mathcal R_n(X)=\mathrm{Tr}(X)\tau_n`$. Separate a specified target state from a claim that a physical process reaches it for every input.

**Dependencies and story role.** None. This establishes the physical object and target before introducing dynamics or accuracy.

**Conceptual connection.** Forgetting is a property of the input-output map. A single output that happens to equal $`\tau_n`$ does not establish that the channel discards all input information.

**Source pointers.** Watrous [§2.1.2][w2] on states and [§2.2.3, equations (2.152)–(2.155)][w2] on the completely depolarizing channel and maximally mixed state; [whole-register error](../science/model.md#whole-register-error).

<a id="m02"></a>

### M02. Pauli coordinates and operator support

**Central question.** How can the location of quantum information be represented algebraically?

**Understanding target.** Read a tensor-product Pauli as an operator on the whole register, with identity factors on inactive sites. Use Pauli weight to count its nonidentity factors, and recognize Pauli strings as a complete orthogonal operator basis. A small set of Pauli expectations describes only part of a general state.

**Dependencies and story role.** [M01](#m01). This provides local coordinates that can later be followed through noise and control.

**Conceptual connection.** Operator support connects an algebraic expansion to the physical sites on which local noise acts. Completeness of the basis is what permits an eventual statement about every input.

**Source pointers.** Watrous [§1.1.2][w1] on operators and tensor products, and [§4.1.2][w4] on Weyl operators and covariant maps; [Pauli conventions](../science/channel_distance.md#pauli-conventions).

<a id="m03"></a>

### M03. Composite systems and retained correlations

**Central question.** Can a register look mixed while still carrying information in its correlations?

**Understanding target.** Distinguish a joint state from its reduced states and identify an inaccessible reference as part of the input specification. Understand why the desired joint output is $`\tau_n\otimes\rho_R`$, with the reference marginal unchanged. Recognize that initially entangled inputs are included.

**Dependencies and story role.** [M01](#m01), [M02](#m02). This enlarges the target from one register's marginal state to the information held by a composite system.

**Conceptual connection.** Partial trace describes what one subsystem reveals, while the joint state records correlations that a marginal alone can miss. Complete mixing must remove both forms of input dependence.

**Source pointers.** Watrous [§§2.1.2–2.1.3][w2] on reduced states and purifications; [whole-register error](../science/model.md#whole-register-error).

<a id="m04"></a>

### M04. Channels, adjoints, and the fixed state

**Central question.** Which mathematical maps represent the allowed physical dynamics?

**Understanding target.** Interpret complete positivity and trace preservation, and understand why positivity must persist when a reference is present. Distinguish the channel acting on states from its adjoint acting on observables. Explain why a unital channel preserves the maximally mixed state and why trace preservation makes the adjoint unital.

**Dependencies and story role.** [M01](#m01), [M03](#m03). This supplies the physical and algebraic framework for composing noisy rounds and later constructing witnesses.

**Conceptual connection.** The same input-output probabilities can be calculated by evolving the state forward or the observable through the adjoint. Unitality identifies the target that all allowed rounds share.

**Source pointers.** Watrous [§§2.2.1–2.2.2, Definition 2.13 and Theorems 2.22 and 2.26][w2]; [the charged-round model](../science/model.md#register-noise-and-one-charged-round).

<a id="m05"></a>

### M05. Local depolarization and the cost of support

**Central question.** Why does a high-weight Pauli decay faster under the same local noise?

**Understanding target.** Interpret $`\eta`$ as a retention factor, so a larger value means weaker noise. Derive the action $`\mathcal N_\eta(P)=\eta^{w(P)}P`$ from independent one-qubit channels. Distinguish repeated noise on a fixed support from noise acting while control changes that support.

**Dependencies and story role.** [M02](#m02), [M04](#m04). This identifies the local mechanism that the constructions will exploit and the converse will limit.

**Conceptual connection.** Tensor-product noise multiplies the retention factors on the sites where an operator is nontrivial. Spreading support therefore changes the amount of attenuation without changing the one-site bath.

**Source pointers.** Watrous [§2.2.3][w2] on depolarizing channels and [§4.1.1][w4] on mixed-unitary channels; [noise convention](../science/model.md#register-noise-and-one-charged-round) and [noisy Clifford reduction](../science/channel_distance.md#lemma-noisy-clifford-reduction).

<a id="m06"></a>

### M06. Local control and noisy operator trajectories

**Central question.** What can a charged layer of reversible control do to operator support?

**Understanding target.** Read a circuit as disjoint one- or two-qubit gates followed by noise on every site, including idle sites. Distinguish nearest-neighbor geometry from unrestricted pair connectivity. Understand that a Clifford maps each Pauli to one Pauli up to phase, making its accumulated noisy trajectory exact, whereas arbitrary unitaries remain allowed in the converse.

**Dependencies and story role.** [M02](#m02), [M04](#m04), [M05](#m05). This connects the algebraic noise rule to the execution resource and interaction architecture.

**Conceptual connection.** Reversible control can redistribute support. The bath produces the irreversible attenuation, and the number of charged layers limits how quickly that redistribution occurs.

**Source pointers.** Watrous [§2.2.1][w2] on unitary channels and their composition; [architectures and optimization](../science/model.md#architectures-and-optimization), [full syntactic cones](../science/causal_bound.md#full-syntactic-causal-cones), and [noisy Clifford reduction](../science/channel_distance.md#lemma-noisy-clifford-reduction).

<a id="m07"></a>

### M07. Measurement, trace distance, and distinguishability

**Central question.** How does a residual observable difference certify that mixing is incomplete?

**Understanding target.** Interpret a POVM as a physical measurement and half-trace distance as optimal state distinguishability. Understand that any chosen measurement gives a lower bound on that distance through its outcome distributions. Recognize total variation as the corresponding classical quantity and data processing as the reason a measurement cannot increase distinguishability.

**Dependencies and story role.** [M01](#m01), [M03](#m03), [M04](#m04). This turns observable calculations into operational evidence about information that remains.

**Conceptual connection.** A converse need not solve the full optimal measurement problem. A valid measurement with distinguishable outcomes already rules out complete mixing below that error.

**Source pointers.** Watrous [§§2.3.1–2.3.2][w2] on measurements and [§3.1.1, Theorem 3.4 and Proposition 3.5][w3] on discrimination and measurement contraction; [the converse's physical measurement](../science/causal_bound.md#proof-a-physical-measurement-that-retains-bias).

<a id="m08"></a>

### M08. Norm bounds that turn observables into measurements

**Central question.** When does an algebraically constructed observable define a physical test?

**Understanding target.** Distinguish trace norm from operator norm and use their duality to connect states with observables. For a Hermitian $`A`$ with $`\|A\|_\infty\le K`$, explain why $`(I\pm A/K)/2`$ are valid measurement effects. Understand the operator-norm contraction of positive unital maps that underlies the later inverse-noise estimate.

**Dependencies and story role.** [M04](#m04), [M07](#m07). This supplies the normalization step needed to make a mathematical witness experimentally meaningful.

**Conceptual connection.** An inverse linear map need not be a physical operation. Its output can still define a physical observable after a proven norm bound is imposed.

**Source pointers.** Watrous [§1.1.3, equations (1.173)–(1.174)][w1] on norm duality and Hölder inequalities, and [§4.2.2][w4] on norms of unital maps; [bounded inverse observables](../science/causal_bound.md#proof-bounded-inverse-observables).

<a id="m09"></a>

### M09. Complete channel error

**Central question.** What accuracy criterion controls every input and every reference at once?

**Understanding target.** Interpret $`\delta(\Psi)=\tfrac12\|\Psi-\mathcal R_n\|_\diamond`$ as the worst output half-trace distance with an input reference. Explain why a reference as large as the input suffices and why a difference of channels can be optimized over input states. Keep the factor of one half explicit.

**Dependencies and story role.** [M03](#m03), [M04](#m04), [M07](#m07). This defines the global success criterion that both constructions and lower bounds must address.

**Conceptual connection.** Channel distance strengthens a statement about particular states into a statement about the entire physical process, including correlations with systems that the protocol never controls.

**Source pointers.** Watrous [§§3.3.2–3.3.3, Definition 3.43 and Theorems 3.46 and 3.51][w3]; [whole-register error](../science/model.md#whole-register-error).

<a id="m10"></a>

### M10. Pauli channels and their exact complete distance

**Central question.** When can a quantum channel distance be calculated from classical error probabilities?

**Understanding target.** Describe a Pauli channel as a probability mixture of Pauli conjugations. Explain how the normalized Choi state encodes those probabilities in orthogonal Bell states and why complete positivity makes them nonnegative. Understand the exact equality between Pauli-channel half-diamond distance and total variation of the error distributions.

**Dependencies and story role.** [M02](#m02), [M04](#m04), [M09](#m09). This gives the upper bounds a complete-channel calculation with no unaccounted reference factor.

**Conceptual connection.** A maximally entangled input distinguishes the orthogonal Pauli errors. The resulting classical formula is exact because it matches the general upper bound from the triangle inequality.

**Source pointers.** Watrous [§2.2.2, Theorem 2.22][w2] on Choi positivity and [§4.1.1, Definition 4.2][w4] on mixed-unitary maps; [Pauli-channel distance](../science/channel_distance.md#lemma-pauli-channel-distance).

<a id="m11"></a>

### M11. Fourier coefficients and the full Pauli count

**Central question.** Why is damping each individual Pauli insufficient unless their number is also counted?

**Understanding target.** Connect Pauli-channel eigenvalues with the finite Fourier transform of the error distribution. Interpret the identity $`\chi^2(p\|u)=\sum_{P\ne I}a_P^2`$ and the bound $`\tfrac12\|p-u\|_1\le\tfrac12\sqrt{\chi^2(p\|u)}`$. Retain the $`4^n-1`$ nonidentity coefficients when passing from a uniform attenuation estimate to a channel estimate.

**Dependencies and story role.** [M02](#m02), [M10](#m10). This exposes the quantitative cost of controlling every operator, rather than a selected set.

**Conceptual connection.** Orthogonality turns a global probability discrepancy into a sum of squared mode amplitudes. The local damping mechanism must overcome the total number of modes.

**Source pointers.** Watrous [§4.1.2][w4] for the Weyl-covariant framework; the project's [Fourier chi-square identity](../science/channel_distance.md#lemma-fourier-chi-square-identity) supplies the normalization and derivation used here.

<a id="m12"></a>

### M12. Parallel blocks and one global accuracy budget

**Central question.** How do small errors on independent channel blocks combine on an entangled input?

**Understanding target.** Distinguish a tensor product of channels from an assumption that their input state is a product. Use $`1+\chi^2(p\|u)=\prod_j(1+\chi^2(p_j\|u_j))`$ for product Pauli-error distributions. Explain why block error must decrease as the number of blocks grows if the complete register is to meet a fixed error target.

**Dependencies and story role.** [M03](#m03), [M09](#m09), [M11](#m11). This combines local estimates into the global bookkeeping needed by both upper bounds.

**Conceptual connection.** Channel factorization is compatible with arbitrary correlations in the input. The diamond-norm reduction and the classical tensorization identity together preserve that guarantee.

**Source pointers.** Watrous [§2.2.1][w2] on channels on composite systems and [§3.3.2][w3] on the completely bounded trace norm; [chi-square tensorization](../science/channel_distance.md#lemma-chi-square-tensorization).

<a id="m13"></a>

### M13. Background synthesis: the exact optimization problem

**Central question.** Which experiment and resource count do the depth laws describe?

**Understanding target.** Assemble the model: $`n`$ arbitrary input qubits, a fixed architecture, one unitary layer followed by local depolarization per charged round, all outputs retained, and half-diamond error at most $`\epsilon`$. Identify the absence of auxiliary initialization, measurement, reset, and fresh random control. Separate reference systems used in the accuracy definition from physical resources available to the circuit.

**Dependencies and story role.** [M05](#m05), [M06](#m06), [M08](#m08), [M09](#m09), [M12](#m12). This closes the background phase by joining the physical model, analytic tools, and global target.

**Conceptual connection.** The same resource contract must govern a proposed construction, its lower bound, and the passive comparison. Changing the scored outputs or the allowed initial states changes the optimization problem.

**Source pointers.** Watrous [§§2.1.3 and 2.2.1][w2] and [§§3.3.2–3.3.3][w3] for the composite-channel framework; [the complete model](../science/model.md) and [what has been counted](../science/interpretation.md#what-has-been-counted).

## Phase II: narrative and innovation

<a id="m14"></a>

### M14. The passive global benchmark

**Central question.** Why does an uncoupled register take logarithmically many rounds to mix completely?

**Understanding target.** Set $`a=\eta^D`$ and connect passive evolution to the exact total variation distance between $`\mathrm{Bin}(n,(1+3a)/4)`$ and $`\mathrm{Bin}(n,1/4)`$. Explain how many weak residual biases remain globally detectable. Recover the scale $`D_{\mathrm{pass}}=(\log n)/(2\lambda)+O_{\eta,\epsilon}(1)`$ from matching finite bounds.

**Dependencies and story role.** [M05](#m05), [M10](#m10), [M12](#m12), [M13](#m13). This establishes the baseline under the same register, bath, and error criterion as the controlled protocols.

**Conceptual connection.** A one-qubit relaxation scale can remain constant while the time needed to suppress the collective evidence from an increasing number of qubits grows.

**Source pointers.** Watrous [§3.1.1][w3] for distinguishability and [§4.1.1][w4] for the channel representation; [exact passive error](../science/passive.md#exact-complete-channel-error), [finite bounds](../science/passive.md#finite-upper-bound), and [passive cutoff scale](../science/passive.md#the-passive-cutoff-scale).

<a id="m15"></a>

### M15. An inverse observable that survives arbitrary control

**Central question.** How can a converse follow residual information without assuming Clifford gates?

**Understanding target.** Follow the inverse-adjoint recursion from an input Pauli $`X_i`$ to a final Hermitian observable $`A_i`$ satisfying $`\Psi_D^\dagger(A_i)=X_i`$. Explain why the inverse noise is an analytical map and why each supported site contributes at most $`\kappa=2/\eta-1`$ to the operator-norm bound. Interpret $`\kappa^{V_i(D)}`$ as the price of undoing attenuation over a cone history.

**Dependencies and story role.** [M06](#m06), [M08](#m08), [M13](#m13). This constructs the local witness from which the universal converse is built.

**Conceptual connection.** A forward dissipative channel can erase an observable only as quickly as its bounded-support inverse witness becomes too large to normalize effectively.

**Source pointers.** Watrous [§2.2.2][w2] for adjoints and [§4.2.2][w4] for unital norm contraction; [bounded inverse observables](../science/causal_bound.md#proof-bounded-inverse-observables).

<a id="m16"></a>

### M16. Disjoint histories and independent readout bits

**Central question.** Why do the converse's measurements factor even when final spatial regions are correlated?

**Understanding target.** Use full syntactic forward cones, including every wire reached by an allowed gate, to identify disjoint histories. Explain the exact product identity for inverse observables on those histories. On the chosen product input, derive independent biased measurement outcomes without assuming that the corresponding output regions form a product state.

**Dependencies and story role.** [M06](#m06), [M07](#m07), [M15](#m15). This combines many local witnesses while retaining a rigorous probability model.

**Conceptual connection.** Independence of these particular outcomes follows from an algebraic identity for all their moments. It is a more specific property than absence of correlations in the full output state.

**Source pointers.** Watrous [§§2.3.1–2.3.2][w2] for measurement probabilities; [products on disjoint histories](../science/causal_bound.md#proof-products-on-disjoint-histories), [the physical readout](../science/causal_bound.md#proof-a-physical-measurement-that-retains-bias), and [the correlated-region example](../science/finite_examples.md#inverse-witness-check).

<a id="m17"></a>

### M17. From surviving biases to a universal converse

**Central question.** How does a collection of weak witnesses force a lower bound on complete mixing error?

**Understanding target.** Combine the biased-bit product distribution with the Bhattacharyya coefficient and measurement data processing. Interpret the bound

```math
\delta(\Psi_D)\ge
1-\exp\!\left[-\frac18\sum_{i\in S}\kappa^{-2V_i(D)}\right]
```

for a set $`S`$ of sites with disjoint cone histories. Explain why one valid input and measurement suffice to lower-bound the channel error, although the task itself quantifies over every input and reference.

**Dependencies and story role.** [M07](#m07), [M09](#m09), [M16](#m16). This turns local information survival into an architecture-independent theorem.

**Conceptual connection.** Many small biases become distinguishable collectively. The cone history controls each bias, and the number of disjoint histories controls how much evidence can be combined.

**Source pointers.** Watrous [§3.2, Definition 3.11 and Proposition 3.16][w3] for unsquared fidelity and its tensor product, and [§3.2.3, Theorem 3.33][w3] for the fidelity-distance inequality; [the causal-cone theorem](../science/causal_bound.md#theorem-causal-cone-bound).

<a id="m18"></a>

### M18. Architecture turns the converse into depth laws

**Central question.** How do geometric propagation and bounded fan-in impose different minimum depths?

**Understanding target.** Relate cone volume and the number of disjoint cones to the interaction graph. On a fixed-dimensional lattice, explain the cumulative upper envelope $`V_i(D)=O_d(D^{d+1})`$ and the resulting $`\Omega((\log n)^{1/(d+1)})`$ depth. Under unrestricted pair connectivity, use exponential cone growth to obtain $`\Omega(\log\log n)`$. These are lower bounds for arbitrary allowed unitaries.

**Dependencies and story role.** [M06](#m06), [M17](#m17). This makes the universal witness theorem quantitative for the two architectures.

**Conceptual connection.** Space and time enter together because the local bath acts throughout the history. Geometry limits the maximum history size; it does not require every circuit to fill that maximum.

**Source pointers.** Watrous [§3.1.1][w3] supplies the operational distinguishability framework; the architecture estimates are in [the lattice corollary](../science/causal_bound.md#corollary-lattice-depth) and [the unrestricted corollary](../science/causal_bound.md#corollary-unrestricted-connectivity).

<a id="m19"></a>

### M19. Pauli branch weight replaces a final-weight requirement

**Central question.** How can a unitary expose every nonidentity Pauli to substantial support?

**Understanding target.** Explain why a Clifford permutation cannot send every nonidentity Pauli to high final weight. Use the weaker requirement $`w(P)+w(V_mPV_m^\dagger)\ge\alpha m`$ for every $`P\ne I`$. Understand how a count of low-weight Paulis and a union bound establish the existence of such a fixed line Clifford, with $`\alpha=1/10`$ sufficient.

**Dependencies and story role.** [M02](#m02), [M06](#m06), [M13](#m13). This introduces the local construction ingredient that can meet the converse without initializing any part of the register.

**Conceptual connection.** Noise can act at several stages of a reversible trajectory. The required exposure can therefore be shared between the input and output weights of a unitary.

**Source pointers.** Watrous [§4.1.2][w4] for the unitary-error-basis background; [line branch-weight existence](../science/geometric_construction.md#lemma-line-branch-weight) and [the exact three-qubit example](../science/finite_examples.md#exact-line-example).

<a id="m20"></a>

### M20. Compiling a line Clifford into charged local rounds

**Central question.** Does the branch-weight construction survive an honest accounting of its implementation?

**Understanding target.** Identify the imported nearest-neighbor synthesis result and distinguish its two-qubit depth from total charged depth. Explain how collecting single-qubit layers gives an $`O(m)`$ bound without auxiliary qubits. Follow why noise during every compiled layer only attenuates the same ideal Clifford trajectory in this discrete model.

**Dependencies and story role.** [M05](#m05), [M06](#m06), [M19](#m19). This converts an abstract unitary into an admissible local protocol with a controlled cost.

**Conceptual connection.** A mathematical spreading map yields a physical depth bound only after its gates, idle sites, and intermediate noise have all been included.

**Source pointers.** Watrous [§2.2.1][w2] for channel composition; [linear depth on a line](../science/geometric_construction.md#linear-depth-on-a-line) and [Maslov and Yang, Lemma 4](../references/RELATED_WORK.md#maslov2023). The compiler is an imported theorem, not a result supplied by Watrous.

<a id="m21"></a>

### M21. Recursive checkpoints fill a geometric block

**Central question.** How can one-dimensional branch weight become a guarantee on every Pauli in a higher-dimensional block?

**Understanding target.** Read the recursive stage sequence: a lower-dimensional construction, a layer of lines along the remaining axis, then the lower-dimensional construction again. Explain the induction using active hyperplanes on either side of the middle stage. Account for the disjoint checkpoint sets and obtain $`W_d(P)\ge\alpha^d b`$ for a rectangular block of volume $`b`$.

**Dependencies and story role.** [M19](#m19), [M20](#m20). This builds a whole-block exposure guarantee from local line operations.

**Conceptual connection.** The recursion does not require support to increase at every stage. It guarantees that the sum over selected stages is large, which is the quantity needed when noise is inserted at those stages.

**Source pointers.** Watrous [§1.1.2][w1] supplies the tensor-product background; [coordinate-line recursion](../science/geometric_construction.md#coordinate-line-recursion), [checkpoint-weight lemma](../science/geometric_construction.md#lemma-checkpoint-weight), and [finite recursive examples](../science/finite_examples.md#recursive-checkpoints).

<a id="m22"></a>

### M22. Checkpoint noise produces a complete block estimate

**Central question.** How does accumulated support overcome the number of possible input operators?

**Understanding target.** Insert $`t`$ charged noise rounds at each checkpoint and obtain $`a_P\le e^{-\lambda t\alpha^d b}`$. Include the full $`4^b-1`$ coefficient count in the chi-square bound. Explain why choosing $`t`$ proportional to block side length produces an exponent proportional to the block's spacetime volume. Understand that the inverse ideal Clifford is used only in the analysis of the channel distance.

**Dependencies and story role.** [M05](#m05), [M06](#m06), [M10](#m10), [M11](#m11), [M21](#m21). This converts a support certificate into complete mixing of a finite geometric block.

**Conceptual connection.** A trajectory bound becomes a channel bound only after all Pauli modes are counted and the resulting map is connected to an operational distance.

**Source pointers.** Watrous [§§3.3.2–3.3.3][w3] supplies the channel-distance framework; [block mixing](../science/geometric_construction.md#proposition-block-mixing) and [noisy Clifford reduction](../science/channel_distance.md#lemma-noisy-clifford-reduction).

<a id="m23"></a>

### M23. Tiling the register and attaining the geometric optimum

**Central question.** How does a good block protocol mix an entire filled lattice without spare qubits?

**Understanding target.** Partition every coordinate interval into lengths between $`m`$ and $`2m-1`$, so every input site belongs to a block. Explain depth synchronization by charged idle rounds and combine block errors through chi-square tensorization. Choose $`m=\Theta((\log n)^{1/(d+1)})`$ and combine the upper bound with the arbitrary-unitary converse to obtain the geometric optimum.

**Dependencies and story role.** [M12](#m12), [M18](#m18), [M20](#m20), [M22](#m22). This completes the geometric argument from local ingredients to one global channel.

**Conceptual connection.** The block size balances useful noise exposure against the need to make every block's residual error small enough for the full register.

**Source pointers.** Watrous [§3.3.2, Corollary 3.40][w3] supplies trace-norm contraction. The exact Clifford-path argument in [tiling](../science/geometric_construction.md#tiling-the-physical-register) accounts for stage-internal padding; [parallel-block error](../science/geometric_construction.md#complete-error-of-the-parallel-blocks) completes [the geometric theorem](../science/geometric_construction.md#theorem-geometric-mixing-depth).

<a id="m24"></a>

### M24. A normalized spreading tail gives a shallow simultaneous guarantee

**Central question.** What additional ingredient permits a good branch-weight circuit in logarithmic block depth?

**Understanding target.** Identify the fixed-input Pauli tail in Anand et al., Theorem 3.4, and its hypotheses for random matching Clifford circuits. Explain why the factor $`[3^{w(P)}\binom b{w(P)}]^{-1}`$ in the polynomial tail must be retained when summing over all low-weight inputs. Understand how the union bound produces one fixed circuit that works for every nonidentity Pauli.

**Dependencies and story role.** [M06](#m06), [M19](#m19). This supplies the architecture-specific construction ingredient needed to match the unrestricted converse.

**Conceptual connection.** A probability bound for each input becomes a simultaneous all-input statement only when its dependence on the number of inputs is strong enough. Random selection establishes existence; execution can use the selected circuit deterministically.

**Source pointers.** Watrous [§4.1.2][w4] for the Pauli/Weyl background; [the exact external statement](../science/unrestricted_connectivity.md#external-spreading-theorem), [the branch-number derivation](../science/unrestricted_connectivity.md#lemma-logarithmic-depth-branch-number), and [Anand et al., Theorem 3.4](../references/RELATED_WORK.md#anand2026).

<a id="m25"></a>

### M25. Attaining the unrestricted-connectivity optimum

**Central question.** Why are logarithmic-size blocks enough to reach complete mixing in double-logarithmic depth?

**Understanding target.** Place a fixed number of noise rounds before and after the shallow branch-weight circuit, and show that the block chi-square error is exponentially small in its size. Combine blocks of size $`\Theta(\log n)`$, including the even-size constraint and an optional odd input wire. Account for all padding and combine this upper bound with the bounded-fan-in lower bound to obtain $`\Theta(\log\log n)`$.

**Dependencies and story role.** [M12](#m12), [M18](#m18), [M22](#m22), [M24](#m24). This completes the second architecture's matching construction on precisely the physical input register.

**Conceptual connection.** Faster support growth reduces the cost of constructing a useful block. The complete-error budget still determines how large that block must be.

**Source pointers.** Watrous [§§3.3.2–3.3.3][w3] for complete channel distance; [block mixing](../science/unrestricted_connectivity.md#lemma-block-mixing), [arbitrary register sizes](../science/unrestricted_connectivity.md#arbitrary-register-sizes), and [the unrestricted theorem](../science/unrestricted_connectivity.md#theorem-unrestricted-connectivity).

<a id="m26"></a>

### M26. Finite examples as independent proof diagnostics

**Central question.** Which parts of the argument can exact enumeration and dense channel calculations check?

**Understanding target.** Relate the three-qubit branch certificate, rectangular checkpoint sums, and dense normalized Choi calculation to the claims they test. Use the non-Clifford example to distinguish independent witness outcomes from correlated output regions. Separate exhaustive enumeration, sampled checks, floating-point corroboration, and mathematical proof of an arbitrary-size family.

**Dependencies and story role.** [M10](#m10), [M16](#m16), [M21](#m21), [M22](#m22), [M25](#m25). This connects the abstract arguments to finite channels whose full behavior can be independently inspected.

**Conceptual connection.** Different checks probe different failure modes: Pauli signs and support, checkpoint indexing, probability normalization, reference behavior, and inverse-witness factorization.

**Source pointers.** Watrous [§2.2.2][w2] for Choi representations and [§3.1.1][w3] for measurement distinguishability; [finite examples](../science/finite_examples.md) and [verification instructions](../verification/README.md).

<a id="m27"></a>

### M27. Physical meaning of global mixing

**Central question.** How can reversible control accelerate irreversible information loss under a fixed bath?

**Understanding target.** Explain how control changes the supports exposed to noise while preserving the state's spectrum during each unitary step. Connect accumulated support to the dimensional exponent. Distinguish complete mixing from local relaxation, uniform outcomes in a chosen basis, and efficient sampling of a circuit's output distribution.

**Dependencies and story role.** [M05](#m05), [M09](#m09), [M14](#m14), [M18](#m18), [M23](#m23), [M25](#m25). This joins the mechanisms and performance laws into a physical account of the task.

**Conceptual connection.** The bath removes information, control changes its exposure, and the global distance measures the evidence that remains anywhere in the output or its reference correlations.

**Source pointers.** Watrous [§§3.1.1 and 3.3.2][w3] for operational distinguishability; [why control accelerates the bath](../science/interpretation.md#why-control-can-accelerate-a-fixed-bath), [the dimensional exponent](../science/interpretation.md#the-causal-origin-of-the-dimensional-exponent), and [global accuracy](../science/interpretation.md#global-accuracy-and-a-local-relaxation-time).

<a id="m28"></a>

### M28. Resource and parameter boundaries

**Central question.** Which changes to the setting would require a different theorem?

**Understanding target.** Keep fixed $`d`$, $`\eta`$, and $`\epsilon`$ separate from limits in which those parameters vary. Identify the filled-box requirement for the geometric upper bound and the broader occupancy scope of the converse. Distinguish discrete unitary-then-noise rounds from simultaneous continuous-time control, and maximally mixed replacement from pure-state reset or a thermodynamic work-cost claim. Separate offline circuit selection from execution depth.

**Dependencies and story role.** [M13](#m13), [M23](#m23), [M25](#m25), [M27](#m27). This fixes the boundary of the combined interpretation without weakening the established statements.

**Conceptual connection.** An asymptotic depth law has content only together with its geometry, allowed resources, target channel, and fixed-parameter convention.

**Source pointers.** Watrous [§2.2.1][w2] and [§3.3.2][w3] for channels and their comparison; [model boundaries](../science/model.md#mechanism-and-boundaries), [geometric scope](../science/geometric_construction.md#scope-and-inherited-ingredients), and [limits of the statement](../science/interpretation.md#limits-of-the-statement).

<a id="m29"></a>

### M29. Inherited mechanisms and the matching contribution

**Central question.** Which ingredients are established inputs, and what connects them into these optima?

**Understanding target.** Attribute scrambling-enhanced noisy mixing to the existing literature, linear-depth line compilation to Maslov and Yang, and the normalized random-matching tail to Anand et al. Identify the connecting arguments: the arbitrary-unitary inverse-cone converse, recursive checkpoint exposure, and complete-channel accounting on all physical input qubits. Recognize that the geometric theorem has independent proof dependencies from the unrestricted upper bound.

**Dependencies and story role.** [M18](#m18), [M20](#m20), [M23](#m23), [M24](#m24), [M25](#m25), [M28](#m28). This locates the complete result within its mathematical and physical antecedents.

**Conceptual connection.** A familiar mechanism can support a different quantitative theorem when the resource model, universal converse, and operational error criterion are all made compatible.

**Source pointers.** Watrous [§§3.3.2–3.3.3][w3] provides the foundational distance framework; [related work and proof dependencies](../references/RELATED_WORK.md), especially [Quek et al.](../references/RELATED_WORK.md#quek2024), [Maslov and Yang](../references/RELATED_WORK.md#maslov2023), and [Anand et al.](../references/RELATED_WORK.md#anand2026).

<a id="m30"></a>

### M30. Final synthesis: three depth laws, one information-loss problem

**Central question.** How do the lower bounds, constructions, and passive benchmark fit into a single answer?

**Understanding target.** Explain the three asymptotic laws under the same complete-channel target and resource contract:

```math
\begin{aligned}
D_{\mathrm{pass}}
&=\frac{\log n}{2\lambda}+O_{\eta,\epsilon}(1),\\
D_{\min}([L]^d,\eta,\epsilon)
&=\Theta_{d,\eta,\epsilon}\!\left((\log n)^{1/(d+1)}\right),
\qquad n=L^d,\\
D_{\min}(K_n,\eta,\epsilon)
&=\Theta_{\eta,\epsilon}(\log\log n).
\end{aligned}
```

Connect the lower bounds to limits on cumulative causal support and the upper bounds to circuits that expose every Pauli to enough local noise. Distinguish what is asymptotically optimal from unoptimized constants, finite examples, and imported ingredients.

**Dependencies and story role.** [M14](#m14), [M18](#m18), [M23](#m23), [M25](#m25), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29). This closes the narrative phase by integrating the full problem, both matching proofs, and their operational meaning.

**Conceptual connection.** The bath is unchanged across the three settings. The attainable history of operator support changes, and the global information-loss criterion turns that difference into the stated depth laws.

**Source pointers.** Watrous [§§3.1.1 and 3.3.2–3.3.3][w3] supplies the shared state and channel interpretation; [the main statements](../science/model.md#theorem-g-the-geometric-optimum), [causal converse](../science/causal_bound.md), [geometric construction](../science/geometric_construction.md), [unrestricted construction](../science/unrestricted_connectivity.md), [passive benchmark](../science/passive.md), and [physical interpretation](../science/interpretation.md).

## Source route

The [Watrous bridge](WATROUS_BRIDGE.md) provides the notation translation and a focused route through the single selected anchor. The milestone sources identify only the sections used for their concepts; the book is not a prerequisite to be read in full. The [science pages](../science/model.md) retain the complete proofs, and [verification](../verification/README.md) records the finite checks and their limits. This map organizes the central understanding targets without claiming to cover every technical detail or neighboring topic.

[w1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[w2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[w3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[w4]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf
