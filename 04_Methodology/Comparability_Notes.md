# 15-Year Longitudinal Automotive Study: Comparability Notes & Structural Boundaries

This document formalizes cross-sectional and temporal comparability nuances across the six subject companies over the 15-year observation window (FY2011 to FY2025).

---

## 1. JSW Group / JSW Motors Reporting Entity Resolution

### 1.1 Structural Background
The JSW Group (Jindal South West), historically an industrial conglomerate anchored in steel (JSW Steel), energy (JSW Energy), infrastructure (JSW Infrastructure), and paints, had **no active commercial passenger vehicle manufacturing or automotive retail sales operations prior to FY2023-24**.

### 1.2 Chronology of Automotive Initiatives
- **2017–2019 (Exploratory / Shelved)**: JSW Energy evaluated entering electric vehicles and energy storage systems via an electric commercial vehicle project. In early 2019, the board formally announced the termination of the electric vehicle plan to preserve capital for core energy assets.
- **November 2023 (Strategic Joint Venture Agreement)**: JSW Group entered into a definitive strategic partnership with Shanghai Automotive Industry Corporation (SAIC Motor) to acquire a 35% equity stake in MG Motor India Pvt. Ltd.
- **March 2024 (Operational Formation)**: The joint venture entity **JSW MG Motor India Private Limited** was formally unveiled, with JSW holding 35%, Indian financial institutions holding ~8%, employees/dealers ~8%, and SAIC retaining 49%.
- **February 2024 (Odisha EV & Battery Ecosystem Project)**: JSW Group signed an MoU with the Government of Odisha for a ₹40,000 Crore integrated EV and EV battery manufacturing project in Cuttack and Paradip under JSW Neo Energy / JSW Green Mobility.

### 1.3 Longitudinal Coding Rules for JSW
1. **FY2010-11 to FY2022-23 (Years 1 to 13)**: Coded as `NA` (Not Applicable) for all operational vehicle variables (sales, EV penetration, plant capacity, automotive ROCE). Qualitative historical milestones (the 2017 exploratory entry and 2019 exit) are documented in the Qualitative Disclosures dataset. Unrelated JSW Steel / JSW Energy balance sheets are **not** substituted to avoid biasing econometric automotive panel estimations.
2. **FY2023-24 to FY2024-25 (Years 14 and 15)**: Reporting entity is **JSW MG Motor India Pvt. Ltd.** (supplemented by JSW Group disclosed EV capex commitments). Metrics reflect MG Motor India operations consolidated from the effective date of partnership.

---

## 2. Multi-Segment Disentanglement & Scope Boundaries

### 2.1 Tata Motors Limited (TML)
- **Consolidated Scope**: Includes Tata Commercial Vehicles (CV), Tata Passenger Vehicles (PV), Jaguar Land Rover (JLR), and vehicle financing. Group-level financial metrics (Revenue, Capex, ROCE, Total Debt) reflect this full perimeter.
- **PV-Specific Scope**: Metrics for ICE PV Sales, EV PV Sales, EV Penetration, and Indian Market Share track Tata Motors Passenger Vehicles Ltd (TMPVL) and Tata Passenger Electric Mobility Ltd (TPEML). JLR volumes are documented separately in source notes.

### 2.2 Mahindra & Mahindra Limited (M&M)
- **Consolidated Scope**: Combines Automotive (SUVs, LCVs, 3W, electric 3W/4W), Farm Equipment Sector (FES - tractors), Financial Services, and Tech Mahindra.
- **Automotive Segment Scope**: R&D expenditure and capex are tracked at the Auto + Farm aggregate per statutory segmental notes, while PV sales strictly isolate the Passenger Vehicle (Utility Vehicles + Passenger Cars) portfolio.

### 2.3 Honda Motor Co., Ltd.
- **Consolidated Scope**: Encompasses four operating segments: Motorcycle Business, Automobile Business, Financial Services, and Power Products / Other.
- **Automobile Isolation**: Segmental sales volume and automobile-specific revenue/capex are reported to ensure comparability with pure passenger car OEMs.

### 2.4 Toyota Motor Corporation
- **Consolidated Scope**: Encompasses Automotive, Financial Services, and All Other. Includes Daihatsu (mini-vehicles) and Hino (trucks).
- **PV Scope**: Production and sales metrics isolate Toyota and Lexus passenger vehicles.

### 2.5 Hyundai Motor Company
- **Reporting Periodicity**: Follows Calendar Year (Jan 1 to Dec 31). CY2010 to CY2024 represents the 15-year sequence.
- **Consolidated Scope**: Includes automotive operations, finance, and other manufacturing affiliates.

---

## 3. Technology Taxonomy: Powertrain Classification

1. **Battery Electric Vehicles (BEVs)**: Exclusively powered by on-board traction batteries recharged via external grid electricity. Counted under `EV PV Sales` across all OEMs.
2. **Plug-in Hybrid Electric Vehicles (PHEVs)**: Combines combustion engine with externally rechargeable battery allowing 30–80 km pure electric range. Separately delineated where disclosed.
3. **Hybrid Electric Vehicles (HEVs / Mild Hybrids)**: Self-charging internal combustion vehicles with battery regeneration (e.g. Toyota Prius, Camry Hybrid; Honda e:HEV). Classified under legacy/hybrid combustion architecture for sales share calculations, with clear comparability tags.
4. **Fuel Cell Electric Vehicles (FCEVs)**: Hydrogen-powered electric vehicles (e.g. Toyota Mirai, Hyundai Nexo). Tracked under Hydrogen Experimentation (`V24`).
