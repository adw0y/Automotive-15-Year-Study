# 15-Year Longitudinal Automotive Study: Calculation Methodology

This document outlines the formal computational formulas, accounting definitions, and reconciliation rules applied to compute all derived variables across the panel dataset.

---

## 1. Innovation Metrics

### 1.1 R&D Intensity (%)
$$\text{R\&D Intensity}_t = \left( \frac{\text{Total Consolidated R\&D Expenditure}_t}{\text{Total Consolidated Revenue from Operations}_t} \right) \times 100$$
- **Numerator**: Total R&D expenses recognized in the Statement of Profit and Loss plus capitalized development costs recognized in Intangible Assets during the period (where separately disclosed under Ind AS 38 / IFRS / US GAAP / J-GAAP).
- **Denominator**: Total Revenue from Operations (Net Sales + Operating Revenue), excluding other non-operating income.

### 1.2 EV-Specific R&D Intensity (%)
$$\text{EV R\&D Intensity}_t = \left( \frac{\text{EV and Clean Technology R\&D Expenditure}_t}{\text{Total R\&D Expenditure}_t} \right) \times 100$$
- Where companies report aggregate R&D without functional clean-tech breakdown, this metric is coded as `ND` (Qualitatively Disclosed) if electrification programs are described, or `NR` (Not Reported).

---

## 2. Financial Capability Ratios

### 2.1 Cash Ratio to Total Assets (%)
$$\text{Cash Ratio}_t = \left( \frac{\text{Cash and Cash Equivalents}_t + \text{Current Bank Balances / Marketable Securities}_t}{\text{Total Consolidated Assets}_t} \right) \times 100$$
- Captures unrestricted cash, demand deposits, and liquid money-market equivalents reported on the consolidated balance sheet date.

### 2.2 Debt-to-Equity Ratio (x)
$$\text{Debt-to-Equity}_t = \frac{\text{Total Debt}_t}{\text{Total Equity}_t}$$
- **Total Debt**: Sum of Long-Term Borrowings, Non-Current Lease Liabilities, Short-Term Borrowings, and Current Maturities of Long-Term Debt. Operating payables and deferred tax liabilities are excluded.
- **Total Equity**: Total equity attributable to shareholders of the parent company plus non-controlling interests (Total Net Worth).

### 2.3 Operating Cash Flow to Total Assets (%)
$$\text{OCF / Total Assets}_t = \left( \frac{\text{Net Cash Flow from Operating Activities}_t}{\text{Total Consolidated Assets}_t} \right) \times 100$$
- Extracted directly from the audited Consolidated Statement of Cash Flows after working capital adjustments and taxes paid.

### 2.4 Capex Intensity (%)
$$\text{Capex Intensity}_t = \left( \frac{\text{Capital Expenditure}_t}{\text{Total Consolidated Revenue}_t} \right) \times 100$$
- **Capital Expenditure**: Cash outflows for purchase of Property, Plant, and Equipment (PPE), capital work-in-progress (CWIP), and capital additions to intangible assets from the Investing Activities section of the Cash Flow statement. Multi-year commitments or MOUs are excluded from annual capex.

### 2.5 Return on Capital Employed (ROCE) (%)
$$\text{ROCE}_t = \left( \frac{\text{EBIT}_t}{\text{Capital Employed}_t} \right) \times 100$$
Where:
- $\text{EBIT} = \text{Profit Before Finance Costs and Tax}$ (Operating Profit).
- $\text{Capital Employed} = \text{Total Assets} - \text{Current Liabilities}$ (equivalent to $\text{Total Equity} + \text{Total Debt}$).
- If the company publishes an official ROCE figure in its Management Discussion & Analysis (MD&A) or Key Financial Highlights, the reported figure is preserved with priority, and any divergence from the standard formula is noted.

---

## 3. Legacy Technology Exposure and EV Adoption

### 3.1 ICE Passenger-Vehicle Sales (Units)
$$\text{ICE PV Sales}_t = \text{Total PV Sales}_t - \text{EV PV Sales}_t$$
- **Passenger Vehicles (PV)**: Includes hatchbacks, sedans, utility vehicles (SUVs), multi-purpose vehicles (MPVs), and crossovers. Light commercial vehicles (LCVs), medium/heavy commercial vehicles (M&HCVs), buses, and 2/3-wheelers are strictly excluded.
- **Hybrid Treatment**: For OEMs with significant hybrid adoption (Toyota, Honda):
  - Pure Battery Electric Vehicles (BEVs) are classified under `EV PV Sales`.
  - Non-plug-in Strong Hybrid Electric Vehicles (HEVs) and Mild Hybrids are classified within legacy/hybrid combustion fleets unless explicit disaggregation is analyzed, with explanatory notes. Plug-in Hybrids (PHEVs) are reported separately where tracked.

### 3.2 ICE Sales Share (%)
$$\text{ICE Sales Share}_t = \left( \frac{\text{ICE PV Sales}_t}{\text{Total PV Sales}_t} \right) \times 100$$

### 3.3 EV Sales Penetration (%)
$$\text{EV Sales Penetration}_t = \left( \frac{\text{EV PV Sales}_t}{\text{Total PV Sales}_t} \right) \times 100$$

### 3.4 EV Sales Growth (YoY %)
$$\text{EV Sales Growth}_t = \left( \frac{\text{EV PV Sales}_t - \text{EV PV Sales}_{t-1}}{\text{EV PV Sales}_{t-1}} \right) \times 100$$
- If $\text{EV PV Sales}_{t-1} = 0$ or is unavailable (first year of launch), growth is marked `NA` to avoid division by zero.
