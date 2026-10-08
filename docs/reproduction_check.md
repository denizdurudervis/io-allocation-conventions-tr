# Reproduction Check — corrected v3

Date: 19 Aug 2026

## Provenance
Original TÜİK `.xls` SHA-256:

`572d4e0f3cb4288f62d0249e3d8514a61ec40e5888ea9ac323ca740c9ce2378e`

Expected frozen hash:

`572d4e0f3cb4288f62d0249e3d8514a61ec40e5888ea9ac323ca740c9ce2378e`

**Result: exact match.**

## Numerical gates
- d=0 regression: max|q| = `7.731e-10` (< 1e-9)
- max|K·1 - 1| = `3.135e-13`
- rank(K) = `64/64`
- cond2(K) = `76.946830`
- spectral radius(A) = `0.522878223923` (< 1)
- analytical d* = `0.225443825545`

## Frozen-output reproduction
The corrected formulation was recomputed from the verified source. The following regenerated Python objects matched the included frozen JSON **exactly**, including all stored floating-point values and Monte Carlo shares:

- `variants`
- `weighting_convention`
- `local_perturbation`
- `comparator`
- `d_feas_analytic`

Therefore the three supplied frozen outputs are reproduced without numerical discrepancy at their stored precision.

## Historical model status
- v1: withdrawn because of scaling/numerical invalidity.
- v2: superseded.
- corrected v3: sole technical authority for this project.

## Background checks explaining why D35 was pursued
Using the same verified A64 table:
- D35 Type-I output multiplier = `2.383902854441`, rank `1/64` (highest).
- A[D35,D35] = `0.506017394305`, diagonal rank `1/64` (highest sector-self technical coefficient).
