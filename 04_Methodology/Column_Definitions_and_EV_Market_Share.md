# 15-Year Longitudinal Automotive Study: Column Definitions, EV Market Share Clarification & Source Standards

This document provides definitive, academically rigorous definitions for all column headers and variables present in `Automotive_15Year_Study_Master.xlsx` (specifically across the `Wide Dataset` and `Master Panel Dataset`), with an exhaustive clarification of **what "EV Market Share" represents in this study** versus related metrics.

---

## 1. Core Focus: What is "EV Market Share" Here?

A common source of confusion in automotive transition research is conflating **internal electrification rate** with **external market share**. In this study, these concepts are strictly delineated across three distinct variables:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              POWERTRAIN METRIC TAXONOMY                                │
├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│ Metric Name              │ Column / Variable ID        │ Conceptual Scope              │
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ EV Sales Penetration     │ EV Penetration (V21)        │ Company Internal Transition   │
│ EV Market Share          │ EV Market Share (V23)       │ External EV Segment Position  │
│ Total PV Market Share    │ ICE/PV Market Share (V14)   │ Macro Industry Market Position│
└──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

### 1.1 "EV Market Share" (Column: `EV Market Share`, ID: `V23`)
* **Definition**: The company's sales volume of pure battery electric passenger vehicles (BEVs) expressed as a percentage of the **total electric passenger vehicle market volume sold by all manufacturers within the company's primary reference geography**.
* **Formula**:
  $$\text{EV Market Share}_t = \left( \frac{\text{Company EV PV Sales}_t}{\text{Total Industry EV PV Sales in Reference Market}_t} \right) \times 100$$
* **Reference Geographies Used in this Dataset**:
  1. **Indian OEMs (Tata Motors, Mahindra & Mahindra, JSW MG Motor India)**:
     - **Reference Geography**: **Domestic Indian Passenger Vehicle Market**.
     - **Denominator**: Total electric passenger vehicles (e-PV) registered/dispatched in India during the financial year (April 1 to March 31).
     - **Interpretation**: When Tata Motors registers **87.2%** in FY2021-22, it means **87.2 out of every 100 electric passenger cars sold in India** were manufactured by Tata Motors (driven by Nexon EV and Tigor EV). When JSW MG Motor India records **25.5%** in FY2024-25, it means JSW MG commanded over a quarter of all electric cars sold in India (via Comet, ZS EV, and Windsor).
  2. **Global OEMs (Toyota Motor Corporation, Honda Motor Co., Hyundai Motor Company)**:
     - **Reference Geography**: **Global Passenger Vehicle Market**.
     - **Denominator**: Total global light-duty battery electric vehicles (BEVs) sold worldwide during the reporting year (benchmarked against IEA Global EV Outlook and MarkLines).
     - **Interpretation**: When Toyota records **1.2%** in FY2024-25, it means Toyota's 1,45,000 BEV sales constituted 1.2% of the approximately 11.5 Million pure electric cars sold worldwide.
* **Sources & Citation Lineage**:
  - Primary corporate annual reports (MD&A and operational performance sections citing domestic market shares).
  - Society of Indian Automobile Manufacturers (SIAM) Annual Performance Circulars.
  - Ministry of Road Transport and Highways (MoRTH) Vahan National Registration Portal.
  - International Energy Agency (IEA) *Global EV Outlook*.

---

### 1.2 How "EV Market Share" Differs from "EV Penetration" and "Total PV Market Share"

#### A. EV Penetration (Column: `EV Penetration`, ID: `V21`)
* **What it measures**: **The company's own internal transition pace**.
* **Formula**:
  $$\text{EV Penetration}_t = \left( \frac{\text{Company EV PV Sales}_t}{\text{Company Total PV Sales}_t} \right) \times 100$$
* **Key Example**: In FY2024-25, JSW MG Motor India had an **EV Penetration of 41.90%** (meaning 41.9% of all MG cars sold were electric), but an **EV Market Share of 25.50%** (meaning MG captured 25.5% of the total Indian electric car industry).

#### B. Total Passenger Vehicle Market Share (Column: `ICE/PV Market Share`, ID: `V14`)
* **What it measures**: **The company's overall market share across all passenger car powertrains (ICE + Hybrid + EV)**.
* **Formula**:
  $$\text{PV Market Share}_t = \left( \frac{\text{Company Total PV Sales}_t}{\text{Total Industry PV Sales Across All Powertrains}_t} \right) \times 100$$
* **Key Example**: In FY2024-25, Tata Motors held a **14.1% share of the total Indian passenger vehicle market**, but commanded a **68.5% share of the Indian EV segment**.

---

## 2. Complete Definitions for All 28 Dataset Columns

Below is the definitive catalog for all column headers present in `Wide Dataset` and `Master Panel Dataset`.

```
Classification Categories:
- Reported: Extracted directly from audited financial statements, notes, or directors' reports.
- Calculated: Deterministically derived using a standard mathematical/accounting formula from reported numbers.
- Derived: Accounting identity derivation (e.g. Total PV minus EV PV).
- Qualitative: Substantive strategic disclosure in narrative text.
- NA / NR: Not Applicable (entity had no operations) / Not Reported.
```

### Metadata Columns
1. **`Company`**: Official corporate legal entity name analyzed (Tata Motors Limited, Mahindra & Mahindra Limited, Toyota Motor Corporation, Honda Motor Co., Ltd., Hyundai Motor Company, JSW Motors / JSW MG Motor India).
2. **`Year`**: Standardized longitudinal reporting cycle (FY2010-11 through FY2024-25 for Indian and Japanese OEMs; CY2010 through CY2024 for Hyundai).
3. **`Reporting Period`**: Exact statutory calendar date span covered by the audited financial statements (e.g. `Apr 2024 - Mar 2025` or `Jan 2024 - Dec 2024`).

---

### Innovation Capability Columns
4. **`R&D` (Variable ID: `V01`)**
   - **Full Name**: Total Research and Development Expenditure.
   - **Unit**: ₹ Crore (original JPY and KRW values preserved in Master Panel).
   - **Definition**: The total gross capital deployed in technological research, product design, engineering, and platform development during the period. Includes both R&D expenses recognized in the Statement of Profit and Loss and capitalized development costs added to Intangible Assets under Development.
   - **Classification**: Reported.
   - **Statutory Source**: Notes to Consolidated Financial Statements (*Research and Development Expenditure* / Intangible Assets note per Ind AS 38 / IAS 38 / US GAAP ASC 730).

5. **`R&D Intensity` (Variable ID: `V02`)**
   - **Full Name**: Research and Development Intensity.
   - **Unit**: %
   - **Definition**: The proportion of firm turnover reinvested into research and technological advancement.
   - **Formula**: $(\text{Total Consolidated R\&D Expenditure} / \text{Total Consolidated Revenue from Operations}) \times 100$.
   - **Classification**: Calculated.
   - **Statutory Source**: Derived from audited P&L Revenue and R&D Notes.

6. **`Patent Applications` (Variable ID: `V03`)**
   - **Full Name**: Annual Patent Applications Filed.
   - **Unit**: Count
   - **Definition**: Total number of priority and national/international patent applications officially submitted by the group's automotive entities to intellectual property authorities during the reporting year.
   - **Classification**: Reported.
   - **Statutory Source**: Directors' Report Annexure on Technology Absorption; Annual ESG / Intellectual Property Reports; corroboration with USPTO, JPO, KIPO, and Indian Patent Office (IPO).

7. **`Cumulative Patent Stock` (Variable ID: `V04`)**
   - **Full Name**: Total Active Patent Portfolio / Patent Stock.
   - **Unit**: Count
   - **Definition**: Total number of active, enforceable patents held in the company's intellectual property portfolio at the end of the financial year.
   - **Classification**: Reported / Derived.
   - **Statutory Source**: Corporate Intellectual Property Disclosures; WIPO PatentScope / USPTO PTMT Database.

8. **`Patents Granted` (Variable ID: `V05`)**
   - **Full Name**: Annual Patents Granted.
   - **Unit**: Count
   - **Definition**: Total number of patents officially approved and issued to the corporate entity by patent offices worldwide during the twelve-month reporting period.
   - **Classification**: Reported.
   - **Statutory Source**: Directors' Report IP Annexure; Corporate Factbooks.

9. **`R&D Centres` (Variable ID: `V06`)**
   - **Full Name**: Number of Dedicated Global R&D Centres and Engineering Facilities.
   - **Unit**: Count
   - **Definition**: Total number of dedicated technical research centers, proving grounds, vehicle design studios, and advanced engineering hubs operated by the firm worldwide.
   - **Classification**: Reported / Qualitative.
   - **Statutory Source**: Corporate Profile & Facilities Overview in Annual Integrated Report.

---

### Financial Capability Columns
10. **`Cash/Assets` (Variable ID: `V07`)**
    - **Full Name**: Cash and Cash Equivalents to Total Assets Ratio.
    - **Unit**: %
    - **Definition**: The liquidity cushion available to the firm relative to its total economic asset base.
    - **Formula**: $[(\text{Cash and Cash Equivalents} + \text{Current Bank Balances \& Marketable Securities}) / \text{Total Assets}] \times 100$.
    - **Classification**: Calculated.
    - **Statutory Source**: Consolidated Balance Sheet (Current Assets: Cash and Cash Equivalents).

11. **`Debt/Equity` (Variable ID: `V08`)**
    - **Full Name**: Total Debt to Shareholders' Equity Ratio.
    - **Unit**: Ratio (x)
    - **Definition**: Solvency metric measuring the degree to which company assets are financed through borrowed debt versus equity capital.
    - **Formula**: $\text{Total Debt} / \text{Total Equity}$, where Total Debt comprises Long-Term Borrowings, Short-Term Borrowings, and Current Maturities of Long-Term Debt (lease liabilities excluded from debt numerator unless stated).
    - **Classification**: Calculated.
    - **Statutory Source**: Consolidated Balance Sheet (Non-Current & Current Financial Liabilities: Borrowings) and Statement of Changes in Equity.

12. **`OCF/Assets` (Variable ID: `V09`)**
    - **Full Name**: Operating Cash Flow to Total Assets Ratio.
    - **Unit**: %
    - **Definition**: Cash generation productivity of the firm's total capital assets before financing decisions.
    - **Formula**: $(\text{Net Cash Flow from Operating Activities} / \text{Total Assets}) \times 100$.
    - **Classification**: Calculated.
    - **Statutory Source**: Consolidated Statement of Cash Flows (Cash Flow from Operating Activities).

13. **`Capex/Revenue` (Variable ID: `V10`)**
    - **Full Name**: Capital Expenditure Intensity.
    - **Unit**: %
    - **Definition**: The percentage of top-line revenue reinvested into tangible and intangible productive infrastructure.
    - **Formula**: $(\text{Gross Capital Expenditure} / \text{Total Revenue from Operations}) \times 100$.
    - **Classification**: Calculated.
    - **Statutory Source**: Consolidated Statement of Cash Flows (Investing Activities: Purchase of Property, Plant, Equipment, and Intangible Assets).

14. **`ROCE` (Variable ID: `V11`)**
    - **Full Name**: Return on Capital Employed.
    - **Unit**: %
    - **Definition**: Core operational profitability metric showing efficiency in generating operating returns from capital base.
    - **Formula**: $[\text{EBIT} / (\text{Total Assets} - \text{Current Liabilities})] \times 100$, or reported official ROCE from MD&A.
    - **Classification**: Reported / Calculated.
    - **Statutory Source**: Management Discussion and Analysis (MD&A) Key Financial Ratios / Audited Financial Statements.

---

### Legacy Powertrain & Incumbent Exposure Columns
15. **`ICE PV Sales` (Variable ID: `V12`)**
    - **Full Name**: Internal Combustion Engine Passenger Vehicle Sales Volume.
    - **Unit**: Units (Vehicles Sold)
    - **Definition**: Annual wholesale volume of passenger cars, SUVs, and MPVs powered by internal combustion engines (petrol, diesel, CNG). Non-plug-in mild/strong hybrids (HEVs) are categorized under this baseline unless separately delineated.
    - **Formula**: $\text{Total PV Sales} - \text{EV PV Sales}$.
    - **Classification**: Derived.
    - **Statutory Source**: Operational Disclosures in Directors' Report; SIAM Flash Reports; JAMA / KAMA registries.

16. **`ICE Sales Share` (Variable ID: `V13`)**
    - **Full Name**: ICE Passenger Vehicle Sales Share.
    - **Unit**: %
    - **Definition**: The percentage of the company's passenger vehicle portfolio still dependent on conventional combustion engines.
    - **Formula**: $(\text{ICE PV Sales} / \text{Total PV Sales}) \times 100 = 100 - \text{EV Penetration}$.
    - **Classification**: Calculated.

17. **`ICE/PV Market Share` (Variable ID: `V14`)**
    - **Full Name**: Overall Passenger Vehicle Market Share.
    - **Unit**: %
    - **Definition**: The firm's market share of the total passenger vehicle industry in its core home market across all powertrains.
    - **Classification**: Reported.
    - **Statutory Source**: MD&A Industry Review; SIAM Official Industry Dispatches.

---

### Strategic Positioning Columns
18. **`EV R&D Intensity` (Variable ID: `V15`)**
    - **Full Name**: EV-Specific Research & Development Intensity.
    - **Unit**: %
    - **Definition**: Dedicated EV/clean mobility R&D spending expressed as a percentage of total corporate R&D spending.
    - **Classification**: Qualitative (`ND` / `NR`).
    - **Statutory Source**: Corporate Sustainability / ESG Reports (noted where disaggregated).

19. **`EV Capex Intensity` (Variable ID: `V16`)**
    - **Full Name**: EV-Specific Capital Expenditure Intensity.
    - **Unit**: %
    - **Definition**: Proportion of annual capital additions dedicated exclusively to EV production facilities and battery assembly.
    - **Classification**: Not Reported (`NR`) per standard segment accounting.

20. **`EV Investment` (Variable ID: `V17`)**
    - **Full Name**: Dedicated EV Investment Commitment.
    - **Unit**: ₹ Crore
    - **Definition**: Multi-year formal capital envelopes committed for electric platforms, gigafactories, and EV subsidiary capitalization.
    - **Classification**: Reported / Qualitative.
    - **Statutory Source**: Statutory Corporate Announcements, Investor Day Presentations, State Government MOUs (e.g. Odisha IPICOL).

21. **`EV Capacity` (Variable ID: `V18`)**
    - **Full Name**: Dedicated / Flexible EV Manufacturing Capacity.
    - **Unit**: Units / Year
    - **Definition**: Annualized run-rate nameplate manufacturing capacity for electric passenger vehicles.
    - **Classification**: Reported.
    - **Statutory Source**: Directors' Report Manufacturing Review.

22. **`Technology Partnerships` (Variable ID: `V19`)**
    - **Full Name**: Strategic Technology Alliances and Partnerships in Clean Tech.
    - **Unit**: Binary / Count
    - **Definition**: Formal joint ventures, licensing agreements, and technical alliances in battery cell manufacturing, electric drivetrains, and software architectures.
    - **Classification**: Reported.
    - **Statutory Source**: Business Alliances section in Directors' Report.

---

### EV Adoption Columns
23. **`EV PV Sales` (Variable ID: `V20`)**
    - **Full Name**: Electric Passenger Vehicle Wholesale Volume.
    - **Unit**: Units (Vehicles Sold)
    - **Definition**: Total annual sales of highway-capable, pure battery electric passenger vehicles (BEVs). Commercial trucks, buses, and 2/3-wheelers are strictly excluded.
    - **Classification**: Reported.
    - **Statutory Source**: Audited Operational Review in Annual Report / Form 20-F; SIAM / Vahan.

24. **`EV Penetration` (Variable ID: `V21`)**
    - **Full Name**: EV Sales Penetration Rate.
    - **Unit**: %
    - **Definition**: The share of electric vehicles within the company's own passenger car sales portfolio.
    - **Formula**: $(\text{EV PV Sales} / \text{Total PV Sales}) \times 100$.
    - **Classification**: Calculated.

25. **`EV Growth` (Variable ID: `V22`)**
    - **Full Name**: Year-over-Year EV Sales Growth.
    - **Unit**: %
    - **Definition**: Annual compound percentage expansion of the firm's electric vehicle volume.
    - **Formula**: $[(\text{EV Sales}_t - \text{EV Sales}_{t-1}) / \text{EV Sales}_{t-1}] \times 100$.
    - **Classification**: Calculated (coded `NA` for initial commercial launch years).

26. **`EV Market Share` (Variable ID: `V23`)**
    - **Full Name**: Electric Vehicle Segment Market Share.
    - **Unit**: %
    - **Definition**: Share of the external electric passenger car market in the reference market captured by the firm (detailed in Section 1 above).
    - **Classification**: Reported / Calculated against official industry benchmarks.

---

### Alternative Powertrains & Enterprise Resources
27. **`Hydrogen Investment` (Variable ID: `V24`)**
    - **Full Name**: Hydrogen Fuel Cell R&D / Strategic Tech Investment.
    - **Unit**: Status / ₹ Crore
    - **Definition**: Status and financial commitment to hydrogen fuel cell electric vehicles (FCEVs) and hydrogen combustion engine technologies.
    - **Classification**: Reported / Qualitative.
    - **Statutory Source**: Clean Mobility & Alternate Powertrain Disclosures in Annual Reports.

28. **`Employees` (Variable ID: `V25`)**
    - **Full Name**: Total Regular Workforce Headcount.
    - **Unit**: Headcount
    - **Definition**: Total regular, permanent employees on corporate payroll at financial year-end.
    - **Classification**: Reported.
    - **Statutory Source**: Human Resources Disclosures / Business Responsibility and Sustainability Report (BRSR) / Form 20-F Item 6.D.
