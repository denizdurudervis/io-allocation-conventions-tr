# io-allocation-conventions-tr

**Technical status:** complete and frozen  
**Manuscript status:** in preparation.

A reproducible case study of how allocation conventions shape sectoral final-demand coverage under a binding capacity restriction in a fixed domestic Leontief input-output system, using the 2023 Türkiye A64 domestic product-by-product table.

## Research question

When one sector is capacity-constrained, does the input-output technology uniquely determine which sectors bear the final-demand shortfall?

This project separates:

- the **technology-defined feasible set**, and
- the **allocation convention** used to select one feasible solution.

The numerical case restricts D35 (electricity, gas, steam and air conditioning) and compares:

- equal-sector additive coverage,
- monetary-weighted additive coverage,
- lexicographic max-min,
- max-output as a diagnostic reference,
- with and without a D35 household final-use floor.

## Main technical findings

These are claims supported by the frozen technical audit, not forecasts of realized Turkish electricity rationing.

1. The additive allocation problem admits an analytical loss-allocation interpretation in transformed coverage space.
2. For residual Variant A, the equal-sector optimum is analytically characterized for `0 <= d <= d*`, with:
   - `d* = 0.2254438255`
   - full non-D35 final-demand coverage
   - D35 final-use coverage `z_D35 = 1 - d/d*`.
3. With the D35 household floor imposed, the equal-sector additive rule next assigns coverage loss to Construction (`F`) according to the frozen leverage ordering; its coverage reaches zero at `d = 0.1474008894`.
4. Lexicographic max-min substantially raises the worst-covered non-D35 sector while spreading nontrivial shortfalls across 62 of 63 non-D35 sectors in the frozen scenarios.
5. Local random perturbations around equal-sector weights can leave the marginal sector highly stable even when a structurally different monetary weighting convention produces large sector-level changes.
6. The broad statement “rationing/allocation assumptions matter” is **not** claimed as novel. The contribution is the transparent analytical decomposition, explicit convention comparison, local-versus-structural robustness distinction, and reproducible Türkiye 2023 case.

See `docs/final_claims_audit.md` before quoting any result.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── src/
│   ├── run_corrected_v3.py
│   └── validate_frozen.py
├── results/
│   ├── README.md
│   └── frozen/
│       ├── 24_variants.csv
│       ├── 25_frozen_results.json
│       ├── 26_comparator.csv
│       ├── D35_capacity_relief_leverage.csv
│       └── sector_level_solutions.csv
├── figures/
│   ├── figure_1.png
│   ├── figure_2.png
│   ├── figure_3.png
│   ├── figure_4.png
│   └── figure_captions.md
└── docs/
    ├── technical_completion_report.md
    ├── reproduction_check.md
    ├── variant_A_closed_form_certificate.md
    ├── maxmin_distribution_audit.md
    ├── final_claims_audit.md
    ├── novelty_audit.md
    └── verified_references.md
```

## Data

The raw TÜİK workbooks are **not redistributed** in this repository.

Official release:

> Türkiye İstatistik Kurumu (TÜİK). *Arz ve Kullanım Tabloları, Girdi-Çıktı Tabloları, 2023.* Haber Bülteni No. 57943, 1 September 2025.

Official release page:

`https://veriportali.tuik.gov.tr/tr/press/57943`

The exact original `.xls` used in the frozen study has SHA-256:

```text
572d4e0f3cb4288f62d0249e3d8514a61ec40e5888ea9ac323ca740c9ce2378e
```

See `data/README.md` for the exact sheet and cells.

## Reproduction

### 1. Create an environment

Python used for the technical freeze:

```text
Python 3.13.5
numpy 2.3.5
scipy 1.17.0
openpyxl 3.1.5
matplotlib 3.10.8
```

Install:

```bash
python -m pip install -r requirements.txt
```

### 2. Obtain the TÜİK workbook

Download the official 2023 domestic input-output workbook.

The original frozen source is a legacy `.xls`. Save an **unchanged copy** as `.xlsx` so `openpyxl` can read it. Do not edit cells.

Suggested local layout:

```text
data/raw/
    tuik_2023_domestic_io_original.xls
    tuik_2023_domestic_io.xlsx
```

Raw files are ignored by Git.

### 3. Run corrected v3

```bash
python src/run_corrected_v3.py \
  --input-xlsx data/raw/tuik_2023_domestic_io.xlsx \
  --original-xls data/raw/tuik_2023_domestic_io_original.xls \
  --outdir results/generated
```

The original `.xls` hash is checked if `--original-xls` is supplied.

### 4. Validate the regenerated frozen JSON

```bash
python src/validate_frozen.py \
  --generated results/generated/25_frozen_results.json \
  --frozen results/frozen/25_frozen_results.json
```

Expected message:

```text
PASS: regenerated JSON matches frozen numerical authority within tolerance.
```

## Interpretation boundaries

This repository does **not** claim that:

- Türkiye would actually ration electricity according to any modeled rule;
- Construction is intrinsically the most vulnerable real-world sector;
- the household floor represents Turkish institutional policy;
- max-min is “fair” or additive allocation is “efficient”;
- agreement between two tested conventions proves a result is technology-determined;
- allocation/rationing sensitivity is a new discovery in input-output economics.

The study is a static feasible-allocation analysis under fixed domestic Leontief coefficients.

## Version history

Only **corrected v3** is authoritative.

- v1: withdrawn because of invalid numerical scaling.
- v2: superseded.
- corrected v3: frozen numerical authority in this repository.

## Manuscript

A manuscript based on this study is in preparation.

## License

Code and repository-authored documentation are released under the MIT License.

The underlying TÜİK data are not part of this license and are not redistributed here.
