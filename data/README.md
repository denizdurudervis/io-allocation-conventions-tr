# Data acquisition and provenance

Raw TÜİK input-output workbooks are intentionally excluded from this repository.

## Official source

Türkiye İstatistik Kurumu (TÜİK)

**Release:** *Arz ve Kullanım Tabloları, Girdi-Çıktı Tabloları, 2023*  
**Haber Bülteni:** 57943  
**Publication date:** 1 September 2025  
**Official page:** https://veriportali.tuik.gov.tr/tr/press/57943

The official methodological note states that the 2023 supply-use and symmetric input-output tables were prepared at 64-industry / 64-product level and that product-by-product 2023 IO tables were generated from the supply-use tables.

## Frozen source identity

Original study workbook:

`Yurtiçi Üretim Girdi - Çıktı Tablosu, 2023 (Temel Fiyatlarla) [Cari Fiyatlarla]`

SHA-256:

`572d4e0f3cb4288f62d0249e3d8514a61ec40e5888ea9ac323ca740c9ce2378e`

## Exact source geometry used by corrected v3

Sheet: `T9`

| Quantity | Excel range |
|---|---|
| sector codes | `B10:B73` |
| sector names | `C10:C73` |
| domestic intermediate-use matrix `Z0` | `D10:BO73` |
| baseline output `x0` | `D86:BO86` |
| household final use `hh` | `BQ10:BQ73` |
| total final consumption `fc` | `BT10:BT73` |
| gross capital formation `gcf` | `BW10:BW73` |
| exports `exp` | `BX10:BX73` |

Corrected v3 defines modeled baseline final use as:

`f0 = fc + gcf + exp`

The shocked product group is `D35`.

## Local reproduction note

The official source is distributed as legacy `.xls`. The repository code reads `.xlsx` using `openpyxl`.

For reproduction:

1. retain the original `.xls` unchanged;
2. verify its SHA-256 against the frozen hash above;
3. use Excel/compatible software to save an unchanged `.xlsx` copy;
4. do not modify cells;
5. place both files under `data/raw/`.

`data/raw/` is ignored by Git.
