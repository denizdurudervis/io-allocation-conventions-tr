# Results

`results/frozen/` is the numerical authority for corrected v3.

## Files

- `25_frozen_results.json` — model metadata, analytical threshold, variant summaries, weighting-convention sensitivity, perturbation experiment and comparator results.
- `24_variants.csv` — residual and household-floor additive summaries.
- `26_comparator.csv` — additive vs lexicographic max-min plus max-output reference.
- `sector_level_solutions.csv` — full 64-sector deterministic solution vectors for the frozen scenarios.
- `D35_capacity_relief_leverage.csv` — transformed D35 capacity-relief leverage ordering used in the analytical audit.

Do not replace these files with results from v1 or v2.

Regenerated files should be written to `results/generated/`, which is Git-ignored.
