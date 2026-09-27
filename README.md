# 15-Year Longitudinal Automotive Industry Study (2010 – 2025)

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Complete](https://img.shields.io/badge/Status-Audited_and_Reconciled-success.svg)]()

A comprehensive 15-year empirical data extraction, validation, and econometric panel study on the automotive industry covering **six major global and Indian automotive manufacturers** over **15 consecutive financial/calendar years** across **25 standardized variables**.

---

## 📌 Research Overview & Scope

* **Observation Period**: 15 consecutive completed reporting years
  * **Indian & Japanese OEMs**: FY2010-11 to FY2024-25 (April 1 to March 31)
  * **South Korean OEM**: CY2010 to CY2024 (January 1 to December 31)
* **Companies Analyzed**:
  1. **Tata Motors Limited** (TML - India / Global)
  2. **Mahindra & Mahindra Limited** (M&M - India)
  3. **Toyota Motor Corporation** (TMC - Japan / Global)
  4. **Honda Motor Co., Ltd.** (HMC - Japan / Global)
  5. **Hyundai Motor Company** (HMC - South Korea / Global)
  6. **JSW Motors / JSW MG Motor India** (JSW Group - India)
* **Dataset Scale**:
  * **Master Long Panel**: 2,250 observations (6 companies $\times$ 15 years $\times$ 25 variables)
  * **Wide Dataset**: 90 company-year rows with 25 side-by-side metrics
  * **Qualitative Disclosures**: 310 strategic disclosures on EV, hydrogen, R&D, and partnerships
  * **Audit Traceability**: 100% of observations linked to unique `Reference ID` citations and audited statutory annual report pages.

---

## 📊 15-Year Longitudinal Trajectory Matrix

| Strategic Dimension | Tata Motors | Mahindra & Mahindra | Toyota Motor Corp | Honda Motor Co | Hyundai Motor Co | JSW Motors / MG India |
|:---|:---|:---|:---|:---|:---|:---|
| **R&D Expenditure** | ₹4,591 Cr → ₹26,100 Cr *(Consolidated + JLR)* | ₹724 Cr → ₹5,450 Cr *(Auto + Farm MRV)* | ¥730B → ¥1,250B *(₹39,013 Cr → ₹68,500 Cr)* | ¥472B → ¥940B *(₹25,220 Cr → ₹51,512 Cr)* | KRW 1.45T → 4.35T *(₹5,716 Cr → ₹26,600 Cr)* | *NA (FY11-23)* → ₹420 Cr *(FY25)* |
| **Patent Applications** | 112 → 435 / yr *(Stock: 3,860)* | 48 → 410 / yr *(Stock: 2,280)* | 4,820 → 7,200 / yr *(Stock: 72,800)* | 3,210 → 5,380 / yr *(Stock: 50,800)* | 3,850 → 8,450 / yr *(Stock: 71,500)* | *NA* → 28 / yr *(Stock: 70)* |
| **Capital Structure (D/E)** | 1.64x → 0.78x *(Net auto debt cleared)* | 1.01x → 0.62x *(Post SsangYong exit)* | 1.19x → 1.03x *(Auto finance backed)* | 0.96x → 0.88x *(Motorcycle cash buffer)* | 0.95x → 1.11x *(Receivables leverage)* | 0.69x *(FY25 JV)* |
| **ROCE Trajectory** | 21.8% → -8.5% *(FY19)* → 20.8% | 18.5% → 3.8% *(FY20)* → 22.1% | 3.8% → 12.8% *(FY24)* → 11.6% | 6.8% → 3.6% → 5.6% | 11.2% → 2.5% *(CY20)* → 12.8% | 2.8% *(FY25)* |
| **ICE PV Sales** | 3.20L → 5.15L units | 1.69L → 4.85L units | 7.31M → 9.50M units | 3.51M → 4.19M units | 3.61M → 4.02M units | *NA* → 39,800 units |
| **EV PV Sales (BEV)** | 0 → 76,500 units *(Share: 12.9%)* | 450 → 26,500 units *(Share: 5.2%)* | 100 → 1,45,000 units *(Share: 1.5%)* | 50 → 58,000 units *(Share: 1.4%)* | 30 → 2,60,000 units *(Share: 6.1%)* | *NA* → 28,700 units *(Share: 41.9%)* |
| **EV Platform Blueprint** | Ziptron, Acti.ev & Avinya | INGLO Born Electric (BE.05) | e-TNGA & BEV Factory | Honda 0 Series & e:Architecture | E-GMP (800V) & IMA | Modular EV & BaaS (Windsor) |
| **Hydrogen Commercialization** | Commercial FCEV buses (IOCL); Prima H.2 | H2-ICE tractor prototypes (IIT Madras) | Mirai I & II; Hydrogen Factory; BMW JV | Clarity; CR-V e:FCEV; FCSM JV (GM) | Tucson FCEV, Nexo; HTWO; XCIENT FCEV | MG Euniq 7; industrial freight studies |
| **Total Workforce** | 52,244 → 91,500 | 28,500 → 51,500 | 3,17,716 → 3,85,000 | 1,79,060 → 1,96,000 | 95,200 → 1,25,500 | *NA* → 4,600 |

---

## 📁 Repository Directory Structure

```
Automotive 15-Year Study/
├── 01_Annual Reports/                  # Year-by-year filing metadata & archive cards
│   ├── Honda/                          # FY2011 to FY2025 archive receipts
│   ├── Hyundai/                        # CY2010 to CY2024 archive receipts
│   ├── JSW Motors/                     # Transition & JV filings
│   ├── Mahindra/                       # FY2011 to FY2025 archive receipts
│   ├── Tata Motors/                    # FY2011 to FY2025 archive receipts
│   └── Toyota/                         # FY2011 to FY2025 archive receipts
├── 02_Datasets/                        # Master datasets and code pipeline
│   ├── Automotive_15Year_Study_Master.xlsx  # Multi-tab formatted Excel workbook
│   ├── Master_Panel_Dataset.csv        # Long format: 2,250 observations
│   ├── Wide_Dataset.csv                # Wide format: 90 company-years
│   ├── Qualitative_Disclosure_Dataset.csv   # 310 verified qualitative records
│   ├── Missing_Data_Matrix.csv         # Econometric data quality audit flags
│   ├── compile_study.py                # Python pipeline to regenerate all data
│   └── data_*.py                       # Underlying raw data modules per company
├── 03_References/                      # Audit trails & supplementary registries
│   ├── Master_References.xlsx          # Master reference index in Excel
│   ├── Master_References.csv           # 90 unique Reference IDs with filing URLs
│   ├── Source_Audit.csv                # Full audit trail mapping variables to pages
│   └── Supplementary_Sources.md        # Official RBI, IMF, SIAM, JAMA, USPTO sources
├── 04_Methodology/                     # Methodological and econometric documentation
│   ├── Data_Dictionary.md              # Detailed definitions of all 25 variables
│   ├── Calculation_Methodology.md      # Mathematical and accounting formulas
│   ├── Currency_Conversion_Methodology.md # Historical JPY/INR & KRW/INR matrices
│   └── Comparability_Notes.md          # Segment scopes and JSW boundary definitions
└── 05_Analysis/                        # Analytical reports & anomaly audits
    ├── Company_Summaries.md            # Comprehensive 10-dimension descriptive report
    ├── Year_over_Year_Anomalies.md     # Institutional explanation of 21 structural shifts
    └── Year_over_Year_Anomalies.csv    # Raw anomaly detection output
```

---

## 📐 The 25 Standardized Variables

### 1. Innovation Capability
* **V01: R&D Expenditure**: Standardized in ₹ Crore (original JPY/KRW preserved).
* **V02: R&D Intensity**: $(\text{R\&D Expenditure} / \text{Revenue}) \times 100$.
* **V03: Patent Applications**: Annual patent filings.
* **V04: Cumulative Patent Stock**: Active patents held at fiscal year-end.
* **V05: Patents Granted**: Annual patent grants awarded.
* **V06: Number of R&D Centres**: Dedicated technical research and proving ground facilities.

### 2. Financial Capability
* **V07: Cash Ratio to Total Assets**: $(\text{Cash \& Cash Equivalents} / \text{Total Assets}) \times 100$.
* **V08: Debt-to-Equity**: $\text{Total Debt} / \text{Total Equity}$.
* **V09: Operating Cash Flow / Total Assets**: $(\text{OCF} / \text{Total Assets}) \times 100$.
* **V10: Capex Intensity**: $(\text{Capex} / \text{Revenue}) \times 100$.
* **V11: ROCE**: Reported or calculated as $\text{EBIT} / (\text{Total Assets} - \text{Current Liabilities}) \times 100$.

### 3. Legacy Technology Exposure
* **V12: ICE PV Sales**: Annual volume of internal-combustion passenger vehicles sold.
* **V13: ICE Sales Share**: $(\text{ICE PV Sales} / \text{Total PV Sales}) \times 100$.
* **V14: ICE/PV Market Share**: Domestic passenger vehicle market share.

### 4. Strategic Positioning
* **V15: EV-Specific R&D Intensity**: $(\text{Clean R\&D} / \text{Total R\&D}) \times 100$.
* **V16: EV-Specific Capex Intensity**: $(\text{Clean Capex} / \text{Total Capex}) \times 100$.
* **V17: EV Investment Commitment**: Dedicated capital envelopes announced for electrification.
* **V18: EV Production Capacity**: Annual manufacturing run-rate capacity in units/year.
* **V19: Technology Partnerships**: Strategic technology partnerships count & binary indicator.

### 5. EV Adoption
* **V20: EV PV Sales**: Annual battery electric passenger vehicle (BEV) sales volume.
* **V21: EV Sales Penetration**: $(\text{EV PV Sales} / \text{Total PV Sales}) \times 100$.
* **V22: EV Sales Growth**: YoY percentage change in EV passenger vehicle sales.
* **V23: EV Market Share**: Share of passenger electric vehicle market in core reference territory.

### 6. Hydrogen Experimentation
* **V24: Hydrogen R&D / Technology Investment**: Dedicated expenditure and qualitative activity flags.

### 7. Company Resources & Capabilities
* **V25: Employee Base / Workforce Size**: Consolidated year-end regular employee headcount.

---

## 🛠️ Data Quality & Academic Reproducibility

Every data point in the panel is strictly categorized into one of six quality classifications:
* `✓` **Reported**: Directly verified from audited financial statements, segmental notes, or statutory annexures.
* `C` **Calculated**: Computed deterministically via explicit accounting equations.
* `D` **Derived**: Inferred via accounting identities (e.g. $\text{Total PV} - \text{EV PV}$).
* `Q` **Qualitative Only**: Verbatim strategic disclosure where no currency amount is provided.
* `NR` **Not Reported**: Unreported in corporate disclosures despite operational relevance.
* `NA` **Not Applicable**: Entity had no legal or operational activity in the sector (e.g. JSW pre-2024).

### To Regenerate All Datasets:
```powershell
python "02_Datasets/compile_study.py"
```

---

## 📜 Citation & License

This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. When using this panel for econometric modeling, thesis work, or policy analysis, please cite:

```bibtex
@dataset{jha_automotive_15year_study_2026,
  author       = {Jha, Adway},
  title        = {Longitudinal Automotive Industry Dataset: 15-Year Panel Study on Innovation, Electrification, and Capital Capabilities (2010--2025)},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/adw0y/Automotive-15-Year-Study}
}
```
