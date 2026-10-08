# Max-min Distribution Audit

Question: Is the statement “max-min spreads shortfalls across 62 non-D35 sectors” a tolerance artifact?

**Answer: No. It is substantive in all three frozen scenarios.** The 62 sectors are not merely at 0.999999.

| d | count z<1-1e-6 | z<.999 | z<.99 | z<.95 | z<.90 | min | median | p90 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 62 | 62 | 62 | 62 | 0 | 0.939870 | 0.939870 | 0.939870 |
| 0.10 | 62 | 62 | 62 | 62 | 62 | 0.875317 | 0.875317 | 0.875317 |
| 0.20 | 62 | 62 | 62 | 62 | 62 | 0.746211 | 0.746211 | 0.746211 |

At d=0.05, all 62 affected non-D35 sectors are below 0.95 (around 0.93987), so the count is economically visible rather than solver noise.
At d=0.10 and d=0.20, all 62 are below 0.90 (around 0.87532 and 0.74621 respectively).
The sole non-D35 sector remaining at full coverage is `T` in all three max-min scenarios.

The near-equality among the 62 affected sectors is expected from the max-min objective: stage 1 lifts the minimum coverage to t*, and the lexicographic second stage retains that guarantee while maximizing aggregate coverage.

## Ten lowest-covered non-D35 sectors

### d=0.05

| rank | sector | z |
|---:|---|---:|
| 1 | C29 | 0.939869941 |
| 2 | C25 | 0.939869941 |
| 3 | H50 | 0.939869942 |
| 4 | C27 | 0.939869942 |
| 5 | A02 | 0.939869942 |
| 6 | A03 | 0.939869942 |
| 7 | J59_J60 | 0.939869942 |
| 8 | E36 | 0.939869942 |
| 9 | C24 | 0.939869942 |
| 10 | H52 | 0.939869942 |

### d=0.10

| rank | sector | z |
|---:|---|---:|
| 1 | C29 | 0.875316844 |
| 2 | C25 | 0.875316844 |
| 3 | H50 | 0.875316845 |
| 4 | C27 | 0.875316845 |
| 5 | A02 | 0.875316845 |
| 6 | A03 | 0.875316845 |
| 7 | J59_J60 | 0.875316845 |
| 8 | E36 | 0.875316845 |
| 9 | C24 | 0.875316845 |
| 10 | H52 | 0.875316845 |

### d=0.20

| rank | sector | z |
|---:|---|---:|
| 1 | C29 | 0.746210650 |
| 2 | C25 | 0.746210650 |
| 3 | H50 | 0.746210650 |
| 4 | C27 | 0.746210650 |
| 5 | A02 | 0.746210650 |
| 6 | A03 | 0.746210650 |
| 7 | J59_J60 | 0.746210650 |
| 8 | E36 | 0.746210650 |
| 9 | C24 | 0.746210650 |
| 10 | H52 | 0.746210650 |

## Final wording
Safe wording:
> The lexicographic max-min solution spreads nontrivial coverage shortfalls across 62 of 63 non-D35 sectors at each frozen severity, while protecting the worst-covered sector.

Do not describe the 62-sector count as a tolerance artifact.
