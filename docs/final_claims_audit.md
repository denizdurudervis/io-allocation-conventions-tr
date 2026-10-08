# Final Claims Audit

Labels:
- **PROVEN ANALYTICALLY**
- **NUMERICALLY SUPPORTED IN FROZEN SCENARIOS**
- **INTERPRETIVE / QUALIFIED**
- **MUST NOT CLAIM**

| Claim | Evidence | Status |
|---|---|---|
| D35 has the highest Type-I output multiplier in the verified A64 table | multiplier `2.383903`, rank 1/64 | **NUMERICALLY SUPPORTED IN FROZEN DATA** |
| D35 has the largest sector-self technical coefficient | `A_JJ=0.506017`, diagonal rank 1/64 | **NUMERICALLY SUPPORTED IN FROZEN DATA** |
| `d*=0.2254438255` is the maximum D35 capacity loss compatible with full non-D35 coverage | transformed model and `M=K^-1` | **PROVEN ANALYTICALLY** |
| Additive allocation can be rewritten as a continuous knapsack in coverage-loss space | `M>=0`, `M1=1`, capacity row `r^T l>=d` | **PROVEN ANALYTICALLY** |
| Equal-sector Variant A follows `z_J=1-d/d*`, all non-D35 z=1 for `0<=d<=d*` | D35 is unique largest `r_i`; lower-bound proof in certificate | **PROVEN ANALYTICALLY** |
| Residual monetary Variant A follows the same ray | D35 is unique largest `r_i/w_i` under frozen monetary weights | **PROVEN ANALYTICALLY** |
| Household-floor equal-sector rule makes Construction the next absorber after D35 floor binds | D35 first, F second in leverage ordering | **PROVEN ANALYTICALLY for this additive formulation** |
| Construction reaches zero coverage at `d=0.147400889` | exact loss-cap + leverage calculation | **PROVEN ANALYTICALLY within the household-floor equal-sector additive rule** |
| At d=.20 the next equal-sector absorber is L68B | exact leverage order and sector-level frozen solution | **NUMERICALLY SUPPORTED; mechanism analytically explained** |
| Max-min spreads shortfalls across 62 non-D35 sectors | all 62 are <.95 at d=.05 and <.90 at d=.10/.20 | **NUMERICALLY SUPPORTED; not a tolerance artifact** |
| Max-min protects the worst-covered non-D35 sector | .6765→.9399, .3292→.8753, 0→.7462 | **NUMERICALLY SUPPORTED IN FROZEN SCENARIOS** |
| Max-min has higher OWL than additive at all three frozen d values | frozen comparator | **NUMERICALLY SUPPORTED IN THESE SCENARIOS** |
| Additive objective minimizes output loss | max-output reference is much lower | **MUST NOT CLAIM (false)** |
| Equal-sector household-floor d=.10 marginal absorber is locally stable to random weight noise | F is 100% through ±30%, 99.33% at ±60% | **NUMERICALLY SUPPORTED FOR THIS SCENARIO** |
| Structural weighting convention can matter much more than local perturbation | household-floor max|Δz|=.681/1/1 while local absorber stable | **NUMERICALLY SUPPORTED, household-floor only** |
| Weighting convention generally matters in all constrained IO models | Variant A is invariant between tested equal/monetary rules | **MUST NOT CLAIM** |
| If two tested conventions agree, the outcome is a property of the system | other untested conventions could disagree | **MUST NOT CLAIM** |
| Equal→monetary weighting causes a discontinuity | no continuous path/bifurcation analysis was run | **MUST NOT CLAIM; say “changes sharply”** |
| “Every distributional statement changes when the rule changes” | residual equal/monetary are effectively identical | **MUST NOT CLAIM; narrow to tested household-floor comparisons** |
| Construction is intrinsically fragile in Turkey | it is selected by the stated rule/leverage ordering | **MUST NOT CLAIM** |
| Household floor reflects actual Turkish rationing priorities | no behavioral/institutional evidence | **MUST NOT CLAIM** |
| Model forecasts realized electricity-rationing outcomes | static counterfactual feasible-allocation model only | **MUST NOT CLAIM** |
| 62-sector max-min pattern is merely LP tolerance noise | distribution audit rejects this | **MUST NOT CLAIM** |
| Concentration is “just generic LP vertex geometry” | more precise mechanism is the fractional-knapsack leverage ranking | **INTERPRETIVE / QUALIFIED — use the specific mechanism instead** |

## Frozen central claim

A technically defensible central statement is:

> With the domestic Leontief technology held fixed, a binding D35 capacity restriction defines a feasible set rather than a unique distributional incidence. In the corrected formulation, additive allocation rules can be characterized analytically by coverage-loss leverage ratios, while alternative normative selectors such as lexicographic max-min choose materially different points of the same feasible set. In the household-floor case, the equal-sector solution is locally stable to large random weight perturbations yet sharply sensitive to a structurally different monetary weighting convention.

## Novelty boundary
Do not claim that the general fact “rationing/allocation assumptions matter” is new; closely related literature already establishes this. The contribution is the transparent analytical decomposition, robustness distinction, reproducible Turkish case, and specific comparison set.
