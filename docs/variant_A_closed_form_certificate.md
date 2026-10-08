# Analytical Certificate — Additive Allocation Structure

## Result
The equal-sector additive Variant A is not merely observed to lie on a straight numerical path. For the corrected v3 model, its global optimum can be certified analytically for every `0 <= d <= d*`.

The same transformation also explains the piecewise concentration observed in the household-floor additive variant.

## 1. Key transformation
Let:

- `M = K^-1`
- `z` = normalized final-demand coverage
- `y = M z`
- `J` = D35

Because `A >= 0` and the verified spectral radius is `0.522878 < 1`, the Leontief inverse is nonnegative. Hence:

`M = diag(x0)^-1 (I-A)^-1 diag(f0) >= 0`.

Also `K·1 = 1`, so `M·1 = 1`. Thus M is row-stochastic in this normalization: its entries are nonnegative and every row sums to one.

For any `0 <= z <= 1`, this implies automatically:

`0 <= y = M z <= M 1 = 1`.

Therefore, after transforming into z-space, the output box constraints introduce no additional restriction.

## 2. Capacity constraint becomes a continuous knapsack
Let `r` be row J of M:

`r_i = M[J,i]`.

Then:

`y_J = r^T z <= 1-d`.

Since `r^T 1 = 1`, define coverage loss `l = 1-z`. The D35 capacity requirement becomes:

`r^T l >= d`.

For positive objective weights `w`, maximizing `w^T z` is exactly equivalent to minimizing:

`w^T l`

subject to the required capacity relief and `0 <= l_i <= 1` (plus any declared floor-derived loss caps).

This is a continuous/fractional knapsack problem. Loss is allocated in descending order of the leverage-to-cost ratio:

`r_i / w_i`.

This is the precise mechanism behind the concentrated additive solutions.

## 3. Variant A — equal-sector objective
For equal-sector weights, `w_i = 1`, so the ordering is simply by `r_i`.

The largest entries of row J are:

- D35: 0.225443825545
- F: 0.143974996424
- L68B: 0.068366903223
- C13-C15: 0.060582853602
- C10-C12: 0.042441230322
- G47: 0.038563116662
- I: 0.037101103892
- Q86: 0.029916824417

In particular:
- `r_J = 0.225443825545 = d*`
- second-largest coefficient is `F` with `0.143974996424`
- D35 is the **unique** largest coefficient.

For any feasible loss vector:

`d <= r^T l <= r_J * sum(l_i)`,

so:

`sum(l_i) >= d/r_J`.

The candidate:

- `l_J = d/r_J`
- `l_i = 0` for `i != J`

achieves this lower bound whenever `d <= r_J = d*`.

Therefore it is globally optimal, and because D35 is the unique largest coefficient it is unique for `d>0`.

Thus, for all `0 <= d <= d*`:

`z_i = 1` for all `i != J`

`z_J = 1 - d/d*`

and

`y = 1 - (d/d*) M e_J`.

At the three frozen severities, the maximum numerical discrepancy in `z_D35` from this formula is `1.660e-10`.

**Status: PROVEN ANALYTICALLY for the equal-sector Variant A.**

## 4. Why Variant A is also insensitive to the monetary convention
Under monetary weighting, the relevant ranking is `r_i / w_i`.

Largest ratios:

- D35: 0.338694496298
- L68B: 0.069974980720
- C23: 0.034765451427
- E36: 0.033170702917
- J61: 0.027335250753
- B: 0.022324510571
- C13-C15: 0.020998974962
- C22: 0.019283889352

D35 is again the unique largest ratio. Consequently the same D35-only loss ray is optimal under the frozen monetary weighting for `0 <= d <= d*`.

This analytically explains why equal-sector and monetary Variant A differ only at solver-noise scale (~1e-11) in the frozen results.

## 5. Household-floor additive variant
The household floor restricts D35 loss to:

`l_J <= 1 - hh_J/f0_J = 0.015196215519`.

D35 can therefore provide only:

`r_J * l_J,max = 0.003425892961`

of the required capacity relief before its loss cap binds.

Under equal-sector weights, the next-largest leverage is Construction (`F`):

`r_F = 0.143974996424`.

Hence, after the D35 floor binds, construction is the next exact marginal absorber. Its loss reaches one at:

`d_F = r_J*(1-floor) + r_F = 0.147400889384`.

So the previously approximate `d≈0.147` statement can be upgraded:

**Construction coverage reaches zero at d = 0.147400889 under the equal-sector household-floor additive rule, before any later absorber is required.**

The frozen `d=0.05`, `0.10`, and `0.20` solutions agree with this piecewise knapsack mechanism. At `d=0.20`, construction is exhausted and the next equal-weight leverage sector, `L68B`, absorbs the remaining coverage loss.

## 6. Claim boundary
This certificate applies to the **additive** objective(s) in corrected v3. It does not turn the lexicographic max-min comparator into a knapsack problem and does not imply that real economies allocate shortages according to these leverage rankings.
