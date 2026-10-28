# Reproducible finite verification

This directory checks finite instances of the complete-mixing proofs. It contains exact integer Pauli calculations and independent dense matrix calculations. The tests complement the [causal-cone proof](../science/causal_bound.md) and [geometric construction](../science/geometric_construction.md); they do not establish an asymptotic theorem by numerical extrapolation.

The explained examples and principal results are in [science/finite_examples.md](../science/finite_examples.md). The complete machine-readable reference output is [expected_results.json](expected_results.json).

## Run

Use Python 3.11 or newer and the pinned NumPy dependency:

```sh
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The command checks every assertion and compares the resulting report with the committed reference. It exits nonzero on failure. To retain or inspect the full report:

```sh
python verification/run_all.py --output /tmp/quantum_mixing_results.json
python verification/run_all.py --json
```

The recorded run used Python 3.12.14 and NumPy 2.3.5. With one BLAS thread it completed in approximately 2.5 seconds in the development environment. Runtime is machine dependent. If a BLAS installation starts many threads for the small dense matrices, this optional invocation avoids that overhead:

```sh
OPENBLAS_NUM_THREADS=1 python verification/run_all.py
```

All integer results must match exactly. Floating values use relative tolerance $`10^{-9}`$ and absolute tolerance $`2\times10^{-11}`$ when compared with the reference. Independent mathematical assertions use the stated absolute tolerance. The observed dense residuals were below $`2.2\times10^{-14}`$.

## Checks and coverage

| Check | Method | Coverage |
|---|---|---|
| Line branch weight | Exact bit arithmetic; permutation and symplectic checks | Every Pauli on two and three qubits |
| Three-qubit line implementation | Independent dense unitary matrices | All 64 Pauli matrices, including phases |
| Recursive checkpoint weight | Exact coordinate-line maps | Every nonidentity Pauli on a $`2\times3`$ rectangle, $`3\times3`$ square, and $`2\times2\times2`$ cube |
| Larger 3D recursion | Exact arithmetic on an explicitly limited test set | 5,399 Paulis on $`3\times3\times3`$ sites, not exhaustive |
| Actual noisy Clifford circuit | Exact Pauli path weights and dense channel evolution | Three data qubits, eight-dimensional reference, two noise strengths |
| Complete error and chi-square | Pauli Fourier transform, direct normalized Choi matrix, product distributions | Single three-qubit block and two-block probability distribution |
| Non-Clifford converse witnesses | Dense unitary/noise and inverse-adjoint evolution | Two disjoint forward cones in a four-qubit circuit whose final regions are correlated |
| Passive error formula | Explicit $`4^n`$ Pauli probabilities versus binomial probabilities | Four finite choices with $`n\le4`$ |

There are 331,773 exhaustive recursive checkpoint inputs. The separate 27-qubit sample contains all weight-one and weight-two Paulis, homogeneous line and hyperplane patterns, the three homogeneous full-register patterns, and 2,048 fixed-seed pseudorandom nonidentity Paulis, with duplicates removed. The output marks that case `exhaustive: false`.

## Fixed fixtures and conventions

The three-qubit line circuit is fixed in `LINE3`; the two-qubit fixture is fixed in `LINE2`. No random circuit is selected during a verification run. Pseudorandomness with seed `20261028` only supplements the larger 3D test set. It is not an operation in any mixing protocol.

A phase-free Pauli is represented by two bit masks $`(x,z)`$. Site 0 is the least significant computational-basis bit. A displayed Pauli word lists sites 0, 1, and onward from left to right. These conventions are different from reading a dense matrix Kronecker product from its most significant factor, so the dense routines construct matrix entries directly. The independent matrix comparison includes the real signs that phase-free integer arithmetic suppresses.

For a rectangle with side lengths $`m_1,\ldots,m_d`$, the site index is

```math
q=x_1+m_1x_2+m_1m_2x_3+\cdots.
```

The recursive stage-axis sequence is $`(0,1,0)`$ in two dimensions and $`(0,1,0,2,0,1,0)`$ in three. Checkpoint weights include the state before the first stage and after every stage. There are exactly $`2^d`$ checkpoints.

## Reference output maintenance

`expected_results.json` records the checked finite results. Updating it is an explicit authoring operation:

```sh
python verification/run_all.py --write-expected
```

This option still runs every mathematical assertion, but replaces the numerical regression reference. It should be used only after reviewing an intentional change to the fixtures or checks. The ordinary run never silently creates or updates a missing reference.

## Limits

The exhaustive line and checkpoint results are finite integer certificates for the stated fixtures. They do not prove the existence of a good line circuit at every growing size, the imported linear-depth synthesis theorem, or the asymptotic optimum. Those claims are justified in the scientific proofs and their cited primary sources.

The 27-qubit test is a sample and does not certify its global minimum. The dense checks use floating-point arithmetic rather than interval arithmetic. The direct Choi trace distance equals the diamond error here because the analytically decoded channel is a Pauli channel; this equality is not assumed for arbitrary channels. The non-Clifford example tests inverse witnesses and a specific valid input, not its entire diamond norm.

No benchmark of a continuously driven noisy Hamiltonian, experimental hardware, practical compiler, or typical random-circuit mixing is performed.
