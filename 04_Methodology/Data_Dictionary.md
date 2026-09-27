# 15-Year Longitudinal Automotive Study: Data Dictionary

This document defines the 25 core variables tracked across the 15-year panel (FY2010-11 to FY2024-25 / CY2010 to CY2024) across seven strategic dimensions.

---

## Variable Specifications

### 1. Innovation Capability

| ID | Variable Name | Unit | Primary Scope | Classification | Description & Rules |
|:---|:---|:---|:---|:---|:---|
| **V01** | **R&D Expenditure** | ₹ Crore (original JPY/KRW preserved) | Consolidated | Reported | Total research and development expenditures expensed and/or capitalized in the financial year. Converted to ₹ crore using annual average exchange rates. |
| **V02** | **R&D Intensity** | % | Consolidated | Calculated | Calculated as $(\text{R&D Expenditure} / \text{Revenue}) \times 100$. Captures strategic commitment to technological advancement relative to firm turnover. |
| **V03** | **Patent Applications** | Count | Group / Auto | Reported | Total patent applications filed during the reporting year. Excludes pending carryovers from previous years where disclosed. |
| **V04** | **Cumulative Patent Stock** | Count | Group / Auto | Reported / Derived | Total active patents/patent portfolio held at year-end. If not directly reported, recorded as NR unless explicit cumulative additions can be tracked without attrition distortion. |
| **V05** | **Patents Granted** | Count | Group / Auto | Reported | Number of patents officially granted to the company during the financial year by patent offices (USPTO, JPO, KIPO, IPO, EPO, etc.). |
| **V06** | **Number of R&D Centres** | Count | Group / Auto | Reported / Qualitative | Number of dedicated technical centres, engineering centres, proving grounds, and research facilities worldwide. Terminology used by the firm is documented. |

---

### 2. Financial Capability

| ID | Variable Name | Unit | Primary Scope | Classification | Description & Rules |
|:---|:---|:---|:---|:---|:---|
| **V07** | **Cash Ratio to Assets** | % | Consolidated | Calculated | Calculated as $(\text{Cash \& Cash Equivalents} / \text{Total Assets}) \times 100$. Measures liquid financial buffer. |
| **V08** | **Debt-to-Equity** | Ratio (x) | Consolidated | Calculated | Calculated as $\text{Total Debt} / \text{Total Equity}$. Total debt includes short-term borrowings, current maturities of long-term debt, and long-term borrowings. |
| **V09** | **OCF / Total Assets** | % | Consolidated | Calculated | Calculated as $(\text{Cash Flow from Operating Activities} / \text{Total Assets}) \times 100$. Measures internal cash generation power relative to asset base. |
| **V10** | **Capex Intensity** | % | Consolidated | Calculated | Calculated as $(\text{Capital Expenditure} / \text{Revenue}) \times 100$. Capex reflects gross cash additions to property, plant, and equipment (PPE) and intangible assets. |
| **V11** | **ROCE** | % | Consolidated | Reported / Calculated | Return on Capital Employed: $\text{EBIT} / (\text{Total Assets} - \text{Current Liabilities}) \times 100$. Directly reported values are prioritized; otherwise standard formula is applied. |

---

### 3. Legacy / Incumbent Technology Exposure

| ID | Variable Name | Unit | Primary Scope | Classification | Description & Rules |
|:---|:---|:---|:---|:---|:---|
| **V12** | **ICE PV Sales** | Units | Passenger Vehicles | Reported / Derived | Annual volume of pure internal-combustion-engine passenger vehicles sold. Unless separately delineated, standard non-plug-in mild/strong hybrids (HEVs) are categorized per company reporting conventions with explicit notes. |
| **V13** | **ICE Sales Share** | % | Passenger Vehicles | Calculated | Calculated as $(\text{ICE PV Sales} / \text{Total PV Sales}) \times 100$. Reflects legacy lock-in and vulnerability to transition risk. |
| **V14** | **ICE/PV Market Share** | % | Passenger Vehicles | Reported | Passenger-vehicle market share in core home market (India for Tata/Mahindra; Japan/Global for Toyota/Honda; South Korea/Global for Hyundai). Market and geography clearly specified. |

---

### 4. Strategic Positioning

| ID | Variable Name | Unit | Primary Scope | Classification | Description & Rules |
|:---|:---|:---|:---|:---|:---|
| **V15** | **EV-Specific R&D Intensity** | % | Group / Auto | Calculated | Calculated as $(\text{EV/Green R&D Expenditure} / \text{Total R&D Expenditure}) \times 100$. Recorded only when EV R&D is explicitly disaggregated in notes/ESG disclosures; otherwise marked ND or NR. |
| **V16** | **EV-Specific Capex Intensity** | % | Group / Auto | Calculated | Calculated as $(\text{EV Capex} / \text{Total Capex}) \times 100$. Only computed where annual EV manufacturing/tooling capex is disaggregated from multi-year commitments. |
| **V17** | **EV Investment Commitment** | ₹ Crore (original preserved) | Group / Auto | Reported / Qualitative | Multi-year dedicated investment envelopes announced for electrification, battery gigafactories, and EV platforms. Year of announcement and target horizon documented. |
| **V18** | **EV Production Capacity** | Units / Year | Passenger Vehicles | Reported / Qualitative | Dedicated or flexible annual manufacturing run-rate capacity for electric vehicles. |
| **V19** | **Technology Partnerships** | Binary & Count | Group / Auto | Qualitative / Derived | Strategic alliances, joint ventures, and technology partnerships in battery cells, software-defined vehicle (SDV) architectures, autonomous driving, and power electronics. Binary indicator (1/0) + partner names. |

---

### 5. EV Adoption

| ID | Variable Name | Unit | Primary Scope | Classification | Description & Rules |
|:---|:---|:---|:---|:---|:---|
| **V20** | **EV PV Sales** | Units | Passenger Vehicles | Reported | Annual sales volume of battery electric passenger vehicles (BEVs). Plug-in hybrid (PHEV) volumes are delineated where reported. Commercial vehicles and 2/3-wheelers strictly excluded. |
| **V21** | **EV Sales Penetration** | % | Passenger Vehicles | Calculated | Calculated as $(\text{EV PV Sales} / \text{Total PV Sales}) \times 100$. |
| **V22** | **EV Sales Growth** | % | Passenger Vehicles | Calculated | Calculated as $[(\text{EV Sales}_t - \text{EV Sales}_{t-1}) / \text{EV Sales}_{t-1}] \times 100$. If prior year sales were zero or unavailable, reported as `NA`. |
| **V23** | **EV Market Share** | % | Passenger Vehicles | Reported | Company's share of the passenger electric vehicle market in specified reference geography. |

---

### 6. Hydrogen Experimentation

| ID | Variable Name | Unit | Primary Scope | Classification | Description & Rules |
|:---|:---|:---|:---|:---|:---|
| **V24** | **Hydrogen R&D / Tech Investment** | Binary (0/1) / ₹ Crore / Qualitative | Group / Auto | Reported / Qualitative | R&D spending, fuel cell vehicle (FCEV) pilot fleets, hydrogen combustion engine development, and hydrogen ecosystem alliances. If monetary spending is undisclosed, captures qualitative narrative. |

---

### 7. Company Resources & Capabilities

| ID | Variable Name | Unit | Primary Scope | Classification | Description & Rules |
|:---|:---|:---|:---|:---|:---|
| **V25** | **Employee Base / Workforce Size** | Headcount | Consolidated | Reported | Total year-end regular workforce. Permanent, contract, and temporary worker breakdowns noted where disclosed in statutory annexures (e.g. BRSR / Form 20-F). |

---

## Coding Taxonomy for Data Types

- **Reported (`✓`)**: Direct numerical disclosure in audited financial statements, notes, or directors' report.
- **Calculated (`C`)**: Ratio or metric derived via deterministic arithmetic formula from two or more reported numbers.
- **Derived (`D`)**: Metric inferred through accounting identities (e.g. Total PV minus EV PV).
- **Qualitative Only (`Q` / `ND`)**: Substantive strategic disclosure present in narrative text, but unquantified in currency/units.
- **Not Reported (`NR`)**: Metric not disclosed despite entity having relevant operational activity.
- **Not Applicable (`NA`)**: Entity had no relevant operations or legal existence in the sector during the reporting period.
