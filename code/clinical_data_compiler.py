#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Template for compiling and summarizing the 29 far-infrared clinical reports
referenced in the manuscript (Supplementary Data 1).

Usage:
1. Fill the CSV file data/far_infrared_clinical_reports.csv with real entries.
2. Run: python code/clinical_data_compiler.py
3. Inspect the printed summary and update Table 1 of the manuscript.
"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_FILE = DATA_DIR / "far_infrared_clinical_reports.csv"

def create_template():
    """
    Create an empty template CSV with the columns used for coding.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    template = pd.DataFrame(columns=[
        "study_id",           # e.g. PMID or DOI
        "first_author",
        "year",
        "country",
        "condition",          # target system/condition
        "sample_size",
        "wavelength_um",      # wavelength range in micrometres
        "power_density_mw_cm2",
        "duration_min",       # per session
        "sessions_n",
        "outcome_direction",  # positive / mixed / negative
        "main_finding",
        "notes",
    ])
    template.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
    print(f"Template created: {DATA_FILE}")
    print("Please fill it with the 29 clinical reports.")

def summarize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize the compiled reports by condition and outcome direction.
    """
    summary = df.groupby(["condition", "outcome_direction"]).size().unstack(
        fill_value=0
    )
    summary["total"] = summary.sum(axis=1)
    return summary

def main():
    if not DATA_FILE.exists():
        print("No data file found. Creating template...")
        create_template()
        return

    df = pd.read_csv(DATA_FILE)

    # Basic validation
    required = ["condition", "outcome_direction"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"CSV missing required columns: {missing}")

    print(f"Loaded {len(df)} clinical reports from {DATA_FILE}\n")

    # Overall counts
    print("Overall outcome distribution:")
    print(df["outcome_direction"].value_counts())
    print()

    # By condition
    print("Summary by condition:")
    print(summarize(df))
    print()

    # Export summary
    summary_path = DATA_DIR / "clinical_summary.csv"
    summarize(df).to_csv(summary_path, encoding="utf-8-sig")
    print(f"Summary saved to: {summary_path}")

if __name__ == "__main__":
    main()
