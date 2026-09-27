# 15-Year Longitudinal Automotive Study: Currency Conversion Methodology

This document outlines the exchange-rate framework, source benchmarks, and translation formulas used to standardize financial metrics to Indian Rupees (₹ Crore) while preserving reported local currencies.

---

## 1. Principles of Currency Standardization

1. **Dual Currency Preservation**:
   - The primary dataset records every monetary variable in two forms:
     - `Original Value` and `Original Currency` (JPY in Millions/Billions, KRW in Millions/Billions, or GBP/USD where relevant).
     - Standardized `Value` in `₹ Crore` (1 Crore = 10,000,000 INR = 10 Million INR).
2. **Flow vs. Stock Conversion**:
   - **Flow metrics** (Revenue, R&D Expenditure, Capital Expenditure, Operating Cash Flow, EBIT): Converted using the **Fiscal Year Financial Average Exchange Rate** for the respective reporting period.
   - **Stock metrics** (Total Assets, Cash & Cash Equivalents, Total Debt, Total Equity): Converted using the **Fiscal Year-End Closing Reference Rate** (as of March 31 or December 31).
3. **Reference Rate Source**:
   - Benchmark rates are obtained from official publications of the **Reserve Bank of India (RBI Reference Rates / FBIL)** and the **International Monetary Fund (IMF International Financial Statistics)**.

---

## 2. Historical Exchange Rate Series (FY2010-11 to FY2024-25 / CY2010 to CY2024)

### 2.1 Japanese Yen (JPY) to Indian Rupee (INR)
*Rates expressed per 100 JPY (₹ / 100 JPY)*

| Fiscal Year | Period | Annual Average (Flows) | Year-End Closing (Stocks) |
|:---|:---|:---:|:---:|
| **FY2010-11** | Apr 2010 – Mar 2011 | 53.42 | 53.88 |
| **FY2011-12** | Apr 2011 – Mar 2012 | 60.54 | 62.15 |
| **FY2012-13** | Apr 2012 – Mar 2013 | 65.86 | 57.78 |
| **FY2013-14** | Apr 2013 – Mar 2014 | 60.48 | 58.40 |
| **FY2014-15** | Apr 2014 – Mar 2015 | 55.67 | 52.12 |
| **FY2015-16** | Apr 2015 – Mar 2016 | 54.45 | 58.96 |
| **FY2016-17** | Apr 2016 – Mar 2017 | 61.82 | 57.92 |
| **FY2017-18** | Apr 2017 – Mar 2018 | 58.32 | 61.34 |
| **FY2018-19** | Apr 2018 – Mar 2019 | 62.81 | 62.42 |
| **FY2019-20** | Apr 2019 – Mar 2020 | 65.05 | 69.65 |
| **FY2020-21** | Apr 2020 – Mar 2021 | 69.87 | 66.25 |
| **FY2021-22** | Apr 2021 – Mar 2022 | 66.24 | 62.12 |
| **FY2022-23** | Apr 2022 – Mar 2023 | 59.48 | 61.85 |
| **FY2023-24** | Apr 2023 – Mar 2024 | 56.42 | 55.18 |
| **FY2024-25** | Apr 2024 – Mar 2025 | 54.80 | 54.10 |

### 2.2 South Korean Won (KRW) to Indian Rupee (INR)
*Rates expressed per 1 KRW (₹ / KRW) or per 1,000 KRW*

| Calendar Year | Period | Annual Average (₹ / 1,000 KRW) | Year-End Closing (₹ / 1,000 KRW) |
|:---|:---|:---:|:---:|
| **CY2010** | Jan 2010 – Dec 2010 | 39.42 | 39.75 |
| **CY2011** | Jan 2011 – Dec 2011 | 41.80 | 46.02 |
| **CY2012** | Jan 2012 – Dec 2012 | 47.35 | 51.10 |
| **CY2013** | Jan 2013 – Dec 2013 | 53.60 | 58.70 |
| **CY2014** | Jan 2014 – Dec 2014 | 57.90 | 57.50 |
| **CY2015** | Jan 2015 – Dec 2015 | 56.80 | 56.40 |
| **CY2016** | Jan 2016 – Dec 2016 | 57.70 | 56.25 |
| **CY2017** | Jan 2017 – Dec 2017 | 57.65 | 60.80 |
| **CY2018** | Jan 2018 – Dec 2018 | 62.10 | 62.30 |
| **CY2019** | Jan 2019 – Dec 2019 | 60.40 | 61.60 |
| **CY2020** | Jan 2020 – Dec 2020 | 62.80 | 67.20 |
| **CY2021** | Jan 2021 – Dec 2021 | 64.60 | 62.70 |
| **CY2022** | Jan 2022 – Dec 2022 | 61.20 | 65.40 |
| **CY2023** | Jan 2023 – Dec 2023 | 63.20 | 64.10 |
| **CY2024** | Jan 2024 – Dec 2024 | 61.15 | 58.90 |

---

## 3. Mathematical Translation Formulas

### 3.1 Flow Conversion (e.g. R&D Expenditure)
$$\text{Amount (₹ Crore)} = \frac{\text{Amount in Original Foreign Currency} \times \text{Average Exchange Rate}}{\text{Scale Factor}}$$

- **For JPY Millions to ₹ Crore**:
  $$\text{Value (₹ Crore)} = \frac{\text{JPY (Millions)} \times 1,000,000 \times \left( \frac{\text{Rate per 100 JPY}}{100} \right)}{10,000,000} = \text{JPY (Millions)} \times \left( \frac{\text{Rate per 100 JPY}}{1,000} \right)$$
- **For KRW Billions to ₹ Crore**:
  $$\text{Value (₹ Crore)} = \frac{\text{KRW (Billions)} \times 1,000,000,000 \times \left( \frac{\text{Rate per 1,000 KRW}}{1,000} \right)}{10,000,000} = \text{KRW (Billions)} \times \left( \frac{\text{Rate per 1,000 KRW}}{10} \right)$$
