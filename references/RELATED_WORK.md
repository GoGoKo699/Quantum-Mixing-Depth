# Related work and proof dependencies

The task here is to minimize the number of local gate/noise rounds needed to approximate the maximally mixed replacement channel in half-diamond distance. Every input qubit may be entangled with a reference, every physical output is retained, and every control layer is charged. The [model](../science/model.md) fixes the noise convention and the permitted resources.

Scrambling-induced sensitivity to local noise is an established mechanism. The results developed here concern the matching minimum depth for complete mixing under those resource and distance conventions. The following sources supply the closest comparisons and the external ingredients used by the proofs. Bibliographic records, including the versions cited below, are in [references.bib](references.bib).

| Source | Statement used or compared | Role in this repository |
| --- | --- | --- |
| [Quek et al. (2024)](#quek2024) | Rapid noisy mixing through high-weight Pauli spreading; shallow and geometric constructions | Closest mechanistic and performance comparison |
| [Maslov and Yang (2023)](#maslov2023) | Linear-nearest-neighbor Clifford synthesis in linear entangling depth | Compiler used by the geometric upper bound |
| [Anand et al. (2026)](#anand2026) | A normalized Pauli-weight tail after logarithmically many random matching rounds | External input to the unrestricted-connectivity upper bound |
| [Wills et al. (2026)](#wills2026) | Good CSS codes with logarithmic-depth, linear-size encoders | Related alternative when mixed check qubits are supplied |
| [Dive et al. (2016)](#dive2016) | Constraints on coherent control of fixed dissipation | Control-theoretic context |
| [Dalzell et al. (2024)](#dalzell2024) | White-noise approximation for measured outputs of random noisy circuits | Comparison of noise regime and operational distance |
| [Nelson and collaborators (2026)](#nelson2026) | Local mixing structure and efficient classical sampling | Distinction between sampling complexity and complete mixing |
| [Watrous (2018)](#watrous2018) | Channels, trace distance, and completely bounded trace norm | Foundational channel and norm conventions |

<a id="quek2024"></a>

## Quek et al.: rapid noisy mixing and error mitigation

Yihui Quek, Daniel Stilck França, Sumeet Khatri, Johannes Jakob Meyer, and Jens Eisert, *Exponentially tighter bounds on limitations of quantum error mitigation*, **Nature Physics 20**, 1648–1658 (2024). [Published article and DOI](https://doi.org/10.1038/s41567-024-02536-7). Detailed statements cited here use [arXiv:2210.11505v3](https://arxiv.org/pdf/2210.11505v3), dated March 29, 2024.

The paper explicitly connects high-weight Pauli spreading to accelerated damping and constructs rapidly mixing circuits at $`\mathrm{poly}(\log\log n)`$ depth. Supplementary Section III, equations (43)–(44), controls an average computational-input relative entropy against the noisy maximally mixed reference. Lemma 4 implements exact Clifford two-designs using pure auxiliary qubits. Section III.E and Theorem 4 give smaller-block and geometrically local variants.

These results establish the physical mechanism and rapid-mixing premise used here. The present [causal-cone bound](../science/causal_bound.md) addresses the minimum achievable complete-channel mixing depth for arbitrary unitary controls; the [constructions](../science/geometric_construction.md) attain the corresponding scaling on the input register itself. An average state-ensemble estimate does not by itself furnish that reference-stable, whole-register optimum.

<a id="maslov2023"></a>

## Maslov and Yang: the nearest-neighbor compiler

Dmitri Maslov and Willers Yang, *CNOT circuits need little help to implement arbitrary Hadamard-free Clifford transformations they generate*, **npj Quantum Information 9**, 96 (2023). [Published article and DOI](https://doi.org/10.1038/s41534-023-00760-2). [arXiv:2210.16195v2](https://arxiv.org/pdf/2210.16195v2), dated January 24, 2023.

Lemma 4 implements any Clifford transformation on a line of $`m`$ qubits without auxiliary qubits, with two-qubit depth at most $`7m-4`$. This is an entangling-depth statement. Collecting the single-qubit operations between consecutive entangling layers gives $`O(m)`$ total charged depth in the model used here; the geometric construction includes this conversion explicitly.

The compiler is an inherited ingredient. The [geometric upper bound](../science/geometric_construction.md) combines it with a recursive sequence of coordinate-line operations and counted noise intervals. The resulting checkpoint-weight and attenuation arguments are given in that proof.

<a id="anand2026"></a>

## Anand et al.: logarithmic-depth Pauli spreading

Emile Anand, Elia Gorokhovsky, Jennifer Hritz, and Jingtong Sun, *Good Stabilizer Codes from Shallow Clifford Circuits with Random Matchings*, [arXiv:2608.18536v1](https://arxiv.org/abs/2608.18536v1), August 19, 2026. [Versioned full text](https://arxiv.org/html/2608.18536v1). [DOI](https://doi.org/10.48550/arXiv.2608.18536).

Theorem 3.4 bounds the probability that a fixed Pauli of weight $`w`$ reaches low weight after $`O(\log b)`$ matching rounds on $`b`$ sites. Its polynomial error is divided by $`3^w\binom bw`$. The [unrestricted-connectivity proof](../science/unrestricted_connectivity.md#external-spreading-theorem) states that bound with its quantifiers and verifies its hypotheses for uniform two-qubit Cliffords.

The subsequent union bound preserves that normalization and produces a fixed circuit with linear Pauli branch number. Counted noise before and after the circuit then yields the complete mixing estimate. This upper bound depends on the stated theorem in the cited preprint version. The causal-cone converse and geometric construction have separate proofs and dependencies.

<a id="wills2026"></a>

## Wills et al.: a related encoding route

Adam Wills, Ting-Chun Lin, Rachel Yun Zhang, and Min-Hsiu Hsieh, *Linear-Time Encodable and Decodable Quantum Error-Correcting Codes*, [arXiv:2603.04543v2](https://arxiv.org/abs/2603.04543v2), June 22, 2026. [Full text](https://arxiv.org/pdf/2603.04543v2). [DOI](https://doi.org/10.48550/arXiv.2603.04543).

Theorems 1–2 give asymptotically good CSS codes with logarithmic-depth, linear-size unitary encoders, at any fixed rate. Their encoders use CNOT gates.

For a modified input model with independent maximally mixed check qubits, such an encoder also provides a mixing construction: every nonidentity input Pauli tensored with identity on the checks becomes a nontrivial logical Pauli of at least the code distance. A constant number of final noise rounds suppresses the full Pauli coefficient count on logarithmic-size blocks. This observation gives constant width overhead and linear gate count in that modified model. The unrestricted theorem in this repository instead acts on an arbitrary state of every physical input qubit and uses the preceding all-Pauli branch-number argument.

<a id="dive2016"></a>

## Dive, Burgarth, and Mintert: control of dissipation

Benjamin Dive, Daniel Burgarth, and Florian Mintert, *Isotropy and control of dissipative quantum dynamics*, **Physical Review A 94**, 012119 (2016). [Published article and DOI](https://doi.org/10.1103/PhysRevA.94.012119). [arXiv:1509.07163v2](https://arxiv.org/pdf/1509.07163v2), August 5, 2016.

This work derives reachability and evolution-time constraints for a fixed dissipative generator under universal coherent control. Its determinant and singular-value constraints describe how control can redistribute dissipative contraction rates. It supplies established control-theoretic context for using reversible control to alter relaxation.

The spatial gate restrictions and global error criterion here add a different resource question: how much operator support can be exposed to a fixed local bath within a charged number of rounds? The discrete causal-cone argument resolves that question in the stated circuit model. It does not assert a continuous-time extension of either framework.

<a id="dalzell2024"></a>

## Dalzell, Hunter-Jones, and Brandão: random-circuit white noise

Alexander M. Dalzell, Nicholas Hunter-Jones, and Fernando G. S. L. Brandão, *Random Quantum Circuits Transform Local Noise into Global White Noise*, **Communications in Mathematical Physics 405**, 78 (2024). [Published full text and DOI](https://doi.org/10.1007/s00220-024-04958-z). The earlier preprint is [arXiv:2111.14907v1](https://arxiv.org/abs/2111.14907v1).

The published model studies measured output distributions of random circuits with weak local unital noise. It proves a white-noise approximation with an ensemble-averaged total-variation error in a regime where the inverse local error rate grows with system size. The discussion explicitly distinguishes uniform measurement outcomes from a maximally mixed density operator.

The present problem fixes a nonzero noise strength as $`n`$ grows and optimizes a channel distance over arbitrary quantum inputs and references. These changes in noise regime, quantifiers, and operational distance are why a measured-output white-noise estimate cannot directly establish the depth law here.

<a id="nelson2026"></a>
<a id="nelson2026local"></a>

## Nelson and collaborators: local structure and classical sampling

Jon Nelson, Joel Rajakumar, and Michael J. Gullans, *Limitations of Noisy Geometrically Local Quantum Circuits*, [arXiv:2510.06346v2](https://arxiv.org/abs/2510.06346v2), September 18, 2026. [Versioned full text](https://arxiv.org/html/2510.06346v2). [DOI](https://doi.org/10.48550/arXiv.2510.06346).

This work treats geometrically local noisy circuits initialized in product states. Corollary 3.3 gives relative-entropy decay for spatially separated local regions, and the paper develops classical sampling and Pauli-truncation consequences. Local regions can become approximately mixed before the entire register does.

<a id="nelson2026sampling"></a>

Jon Nelson, Joel Rajakumar, Chao Yin, Yifan F. Zhang, and Michael J. Gullans, *A polynomial-time classical sampler for noisy quantum circuits from statistical mechanics*, [arXiv:2610.00548v2](https://arxiv.org/abs/2610.00548v2), October 5, 2026. [Versioned full text](https://arxiv.org/html/2610.00548v2). [DOI](https://doi.org/10.48550/arXiv.2610.00548).

Theorem 1.1 gives a polynomial-time approximate sampler for geometrically local unital circuits above a noise-dependent depth independent of register size, with a fixed product initialization. The sampler reproduces the circuit's output distribution; it need not output uniformly random bits.

Both papers clarify that classical simulability and local mixing can occur without complete replacement of arbitrary quantum information. Their sampling objectives are compatible with the [lower bound](../science/causal_bound.md) on the fastest full-register diamond-norm mixing protocol.

<a id="watrous2018"></a>

## Watrous: channel and norm foundations

John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018). [DOI](https://doi.org/10.1017/9781316848142). [Author's official book page](https://cs.uwaterloo.ca/~watrous/TQI/).

Chapters 2–4 provide the channel, trace-distance, completely bounded trace-norm, and unital-map framework used in the [model](../science/model.md) and [channel-distance arguments](../science/channel_distance.md). The Pauli-channel and tensorization identities needed for the constructions are proved directly in the latter file.
