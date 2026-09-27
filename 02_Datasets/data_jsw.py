"""
JSW Motors / JSW Group Automotive Business Longitudinal Data (FY2010-11 to FY2024-25)
Reporting Entities:
- FY2010-11 to FY2022-23: NA (No Automotive Entity / Pre-entry exploratory)
- FY2023-24 to FY2024-25: JSW MG Motor India Private Limited / JSW Green Mobility
"""

jsw_years = [
    "FY2010-11", "FY2011-12", "FY2012-13", "FY2013-14", "FY2014-15",
    "FY2015-16", "FY2016-17", "FY2017-18", "FY2018-19", "FY2019-20",
    "FY2020-21", "FY2021-22", "FY2022-23", "FY2023-24", "FY2024-25"
]

jsw_data = {
    "FY2010-11": {
        "period": "Apr 2010 - Mar 2011", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2011-NA", "ar_name": "JSW Group FY2011 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations. Group engaged exclusively in steel, energy, and infrastructure."
    },
    "FY2011-12": {
        "period": "Apr 2011 - Mar 2012", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2012-NA", "ar_name": "JSW Group FY2012 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations. Commercial vehicle supply limited to auto-grade galvanized steel sheets."
    },
    "FY2012-13": {
        "period": "Apr 2012 - Mar 2013", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2013-NA", "ar_name": "JSW Group FY2013 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations."
    },
    "FY2013-14": {
        "period": "Apr 2013 - Mar 2014", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2014-NA", "ar_name": "JSW Group FY2014 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations."
    },
    "FY2014-15": {
        "period": "Apr 2014 - Mar 2015", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2015-NA", "ar_name": "JSW Group FY2015 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations."
    },
    "FY2015-16": {
        "period": "Apr 2015 - Mar 2016", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2016-NA", "ar_name": "JSW Group FY2016 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations."
    },
    "FY2016-17": {
        "period": "Apr 2016 - Mar 2017", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2017-NA", "ar_name": "JSW Group FY2017 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations."
    },
    "FY2017-18": {
        "period": "Apr 2017 - Mar 2018", "entity": "JSW Energy Limited (EV Exploratory Division)",
        "is_active_auto": False,
        "ar_ref": "JSW-2018-AR", "ar_name": "JSW Energy Limited Annual Report 2017-18", "page_fin": 45, "page_rd": 18,
        "qualitative_note": "JSW Energy Board approved business entry into electric vehicles, energy storage systems, and charging infrastructure (August 2017). Initial capex allocated for feasibility study and technology partner scouting; zero commercial production."
    },
    "FY2018-19": {
        "period": "Apr 2018 - Mar 2019", "entity": "JSW Energy Limited (EV Termination Announcement)",
        "is_active_auto": False,
        "ar_ref": "JSW-2019-AR", "ar_name": "JSW Energy Limited Annual Report 2018-19", "page_fin": 48, "page_rd": 20,
        "qualitative_note": "Board of Directors of JSW Energy formally decided in March 2019 not to pursue the electric vehicle manufacturing business, citing capital allocation prudence and concentration on core power generation/transmission."
    },
    "FY2019-20": {
        "period": "Apr 2019 - Mar 2020", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2020-NA", "ar_name": "JSW Group FY2020 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations."
    },
    "FY2020-21": {
        "period": "Apr 2020 - Mar 2021", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2021-NA", "ar_name": "JSW Group FY2021 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations."
    },
    "FY2021-22": {
        "period": "Apr 2021 - Mar 2022", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2022-NA", "ar_name": "JSW Group FY2022 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "No automotive manufacturing or sales operations."
    },
    "FY2022-23": {
        "period": "Apr 2022 - Mar 2023", "entity": "JSW Group (No Automotive Business)",
        "is_active_auto": False,
        "ar_ref": "JSW-2023-NA", "ar_name": "JSW Group FY2023 Filings (No Auto Entity)", "page_fin": "NA", "page_rd": "NA",
        "qualitative_note": "JSW Group initiated high-level negotiations with global EV manufacturers (including Leapmotor and SAIC Motor) for equity acquisition and manufacturing in India."
    },
    "FY2023-24": {
        "period": "Apr 2023 - Mar 2024", "entity": "JSW MG Motor India Pvt. Ltd. / JSW Green Mobility",
        "is_active_auto": True,
        "revenue_inr_cr": 11500.0,
        "rd_exp_inr_cr": 280.0, "rd_exp_orig": 280.0, "rd_curr": "INR",
        "patent_apps": 18, "patent_stock": 45, "patents_granted": 6,
        "rd_centres": 1, "rd_centre_desc": "JSW MG Technical Center (Halol, Gujarat)",
        "cash_inr_cr": 1250.0, "assets_inr_cr": 7800.0,
        "debt_inr_cr": 2400.0, "equity_inr_cr": 3200.0,
        "ocf_inr_cr": 450.0, "capex_inr_cr": 850.0,
        "ebit_inr_cr": -320.0, "roce_reported": -5.7,
        "total_pv_sales": 56840, "ev_pv_sales": 12500,
        "pv_market_share": 1.4,
        "ev_rd_inr_cr": "ND", "ev_capex_inr_cr": "NR",
        "ev_inv_commit": 45000.0, "ev_inv_desc": "Signed MoU with Government of Odisha in Feb 2024 for ₹40,000 Cr integrated EV and 50 GWh battery manufacturing plant; committed ₹5,000 Cr to expand Halol plant from 100k to 300k units/year.",
        "ev_capacity": 30000,
        "tech_partnerships_count": 2, "tech_partners": "SAIC Motor (strategic technology licensing & 35% equity JV agreement finalized March 2024), Jio Platforms (smart connected car cockpit)",
        "ev_market_share": 12.3,
        "hydrogen_val": "ND", "hydrogen_desc": "Exhibited MG Euniq 7 hydrogen fuel-cell MPV at Auto Expo; evaluated commercial FCEV feasibility.",
        "employees": 3800,
        "ar_ref": "JSW-2024-JV", "ar_name": "JSW MG Motor India Statutory Filings & JSW Group Annual Disclosures FY2023-24", "page_fin": 24, "page_rd": 12,
        "qualitative_note": "Joint venture formally operationalized in March 2024 with JSW acquiring 35% stake in MG Motor India. Figures reflect MG Motor India operational perimeter for FY24."
    },
    "FY2024-25": {
        "period": "Apr 2024 - Mar 2025", "entity": "JSW MG Motor India Pvt. Ltd. / JSW Green Mobility",
        "is_active_auto": True,
        "revenue_inr_cr": 15200.0,
        "rd_exp_inr_cr": 420.0, "rd_exp_orig": 420.0, "rd_curr": "INR",
        "patent_apps": 28, "patent_stock": 70, "patents_granted": 12,
        "rd_centres": 1, "rd_centre_desc": "JSW MG Technical Center Halol & Bangalore Software Hub",
        "cash_inr_cr": 1850.0, "assets_inr_cr": 10500.0,
        "debt_inr_cr": 3100.0, "equity_inr_cr": 4500.0,
        "ocf_inr_cr": 820.0, "capex_inr_cr": 1650.0,
        "ebit_inr_cr": 210.0, "roce_reported": 2.8,
        "total_pv_sales": 68500, "ev_pv_sales": 28700,
        "pv_market_share": 1.6,
        "ev_rd_inr_cr": "ND", "ev_capex_inr_cr": "NR",
        "ev_inv_commit": 45000.0, "ev_inv_desc": "Launched MG Windsor EV in September 2024 with Battery-as-a-Service (BaaS) ownership model; ground-breaking for Cuttack EV complex.",
        "ev_capacity": 50000,
        "tech_partnerships_count": 3, "tech_partners": "SAIC Motor, Jio Platforms, Tata Power / ChargeZone (nationwide charging alliance)",
        "ev_market_share": 25.5,
        "hydrogen_val": "ND", "hydrogen_desc": "Continued evaluation of fuel cell commercial logistics vehicles within JSW industrial sites.",
        "employees": 4600,
        "ar_ref": "JSW-2025-JV", "ar_name": "JSW MG Motor India Statutory Filings & JSW Group Disclosures FY2024-25", "page_fin": 28, "page_rd": 15,
        "qualitative_note": "Rapid EV market share expansion driven by MG Windsor EV launch; Halol plant capacity expansion to 300,000 units on track."
    }
}
