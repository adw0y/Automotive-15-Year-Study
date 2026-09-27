"""
15-Year Longitudinal Automotive Study: Dataset Generation, Validation & Export Engine
Generates:
1. Master Panel Dataset (Long format, 2,250 observations)
2. Wide Dataset (90 company-year rows)
3. Qualitative Disclosure Dataset
4. Source Audit Table
5. Missing-Data Matrix
6. Master Excel Workbook with all tabs
7. Year-over-Year Validation & Anomalies Report
8. Company Summaries Analytical Report
"""

import os
import sys
import pandas as pd
import numpy as np

# Ensure working directory
base_dir = r"C:\Users\AJhaIIT\Downloads\Automotive 15-Year Study"
os.chdir(base_dir)

# Exchange rates (FY11 to FY25 / CY10 to CY24)
# JPY to INR per 100 JPY (Flow average, Stock closing)
jpy_rates = {
    "FY11": {"avg": 53.42, "close": 53.88},
    "FY12": {"avg": 60.54, "close": 62.15},
    "FY13": {"avg": 65.86, "close": 57.78},
    "FY14": {"avg": 60.48, "close": 58.40},
    "FY15": {"avg": 55.67, "close": 52.12},
    "FY16": {"avg": 54.45, "close": 58.96},
    "FY17": {"avg": 61.82, "close": 57.92},
    "FY18": {"avg": 58.32, "close": 61.34},
    "FY19": {"avg": 62.81, "close": 62.42},
    "FY20": {"avg": 65.05, "close": 69.65},
    "FY21": {"avg": 69.87, "close": 66.25},
    "FY22": {"avg": 66.24, "close": 62.12},
    "FY23": {"avg": 59.48, "close": 61.85},
    "FY24": {"avg": 56.42, "close": 55.18},
    "FY25": {"avg": 54.80, "close": 54.10},
}

# KRW to INR per 1000 KRW
krw_rates = {
    "CY10": {"avg": 39.42, "close": 39.75},
    "CY11": {"avg": 41.80, "close": 46.02},
    "CY12": {"avg": 47.35, "close": 51.10},
    "CY13": {"avg": 53.60, "close": 58.70},
    "CY14": {"avg": 57.90, "close": 57.50},
    "CY15": {"avg": 56.80, "close": 56.40},
    "CY16": {"avg": 57.70, "close": 56.25},
    "CY17": {"avg": 57.65, "close": 60.80},
    "CY18": {"avg": 62.10, "close": 62.30},
    "CY19": {"avg": 60.40, "close": 61.60},
    "CY20": {"avg": 62.80, "close": 67.20},
    "CY21": {"avg": 64.60, "close": 62.70},
    "CY22": {"avg": 61.20, "close": 65.40},
    "CY23": {"avg": 63.20, "close": 64.10},
    "CY24": {"avg": 61.15, "close": 58.90},
}

print("Base setup initialized successfully.")
