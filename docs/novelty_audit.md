# Novelty Audit

## Executive conclusion

**Do not claim that this study is the first to show that allocation/rationing assumptions matter in constrained input-output models. That claim is not supportable.**

The closest literature already contains:
- explicit IO allocation systems (Ghosh, 1958);
- disaster IO models with rationing/adaptation (Hallegatte, 2008);
- IO linear-programming models for energy resilience (He, Ng & Su, 2015; 2019);
- optimization-based post-disruption allocation (Oosterhaven & Bouwmeester, 2016);
- direct evidence that predictions under simultaneous supply/demand constraints depend strongly on rationing assumptions (Pichler & Farmer, 2022).

Pichler & Farmer is particularly important: their published abstract states that economic impacts depend strongly on input bottlenecks and that the rationing assumption is a key variable in predictions. Therefore the broad slogan **“allocation conventions, not technology alone, matter” is not by itself a novel discovery.**

## What is still defensibly distinct in this project

The contribution can be framed as a **focused methodological decomposition and reproducible Turkish case study**, combining several elements that the literature search did not reveal as a standard packaged analysis:

1. **Dimensionless single-capacity formulation.**  
   The model writes the domestic Leontief balance as `K y = z`, making normalized output and normalized final-demand coverage directly comparable.

2. **Analytical feasibility threshold.**  
   The D35 non-D35-full-coverage threshold is obtained directly as `d* = (K^-1 e_J)_J = 0.2254438255`.

3. **Analytical reduction of the additive allocation problem.**  
   Because `M=K^-1` is nonnegative with `M1=1`, the additive problem reduces to a continuous knapsack in coverage-loss space. This gives an exact mechanism for the concentrated solutions and proves the Variant-A ray.

4. **Same feasible set, explicitly different normative selectors.**  
   The project compares:
   - equal-sector additive coverage,
   - monetary-weighted additive coverage,
   - lexicographic max-min,
   - max-output as a diagnostic reference.

5. **Local robustness versus structural convention sensitivity.**  
   The frozen household-floor d=.10 solution is nearly unchanged under large random perturbations around equal weights, yet can differ by a full unit of coverage when the weighting convention is changed to monetary weights. This makes a precise distinction between **parameter-neighbourhood robustness** and **model-convention robustness**.

6. **Current Turkish A64 application with full reproducibility.**  
   The entire numerical case is anchored to the 2023 domestic product-by-product TÜİK table with source hash and frozen outputs.

## How strong is that novelty?

**Assessment: incremental but real, if framed narrowly.**

This is not a new theory of input-output economics and not the first constrained IO optimization model. Its strongest publishable angle is a transparent methodological note/case study showing exactly how the feasible technology and normative selection rule separate, with an analytical reduction that makes the mechanism inspectable instead of black-box numerical.

The project becomes weak if it is framed as:
- “we discovered that rationing rules matter”;
- “we introduce IO linear programming for energy resilience”;
- “we are the first to model supply constraints in IO”;
- “Turkey’s electricity cuts would actually be allocated this way.”

It becomes stronger if framed as:
> A reproducible decomposition of capacity-constrained Leontief allocation into a technology-defined feasible set and convention-defined selection, with an analytical knapsack characterization of additive rules and an explicit contrast between local weight robustness and structural allocation-convention sensitivity.

## Closest literature and relationship

### Pichler & Farmer (2022)
Closest conceptual overlap. They model binding supply and demand constraints, introduce optimization for best-case feasible allocation, and show that rationing assumptions are important.  
**Implication:** broad allocation-sensitivity novelty is already occupied.

### He, Ng & Su (2015; 2019)
Direct IO-LP energy-resilience precedent.  
**Implication:** “IO + LP + energy disruption” is not novel.

### Hallegatte (2008)
Rationing and adaptation are explicit in disaster IO.  
**Implication:** a paper must acknowledge that post-shock allocation rules have long been modeled.

### Oosterhaven & Bouwmeester (2016)
Optimization-based approach to disruptive-event impacts.  
**Implication:** optimization itself is not the contribution.

### Ghosh (1958) / Yagi et al. (2020)
Historical supply/allocation traditions and the plausibility problems of naïve supply-driven quantity interpretations.  
**Implication:** the current paper is better positioned as a constrained demand-coverage allocation problem rather than a revival of the Ghosh quantity model.

## Recommended novelty sentence

Safe:
> We provide a transparent, dimensionless capacity-constrained Leontief case study in which additive allocation rules admit an analytical loss-allocation characterization, and use it to distinguish local weight perturbation robustness from sensitivity to structurally different allocation conventions.

Avoid:
> We are the first to show that allocation rules determine outcomes under supply constraints.
