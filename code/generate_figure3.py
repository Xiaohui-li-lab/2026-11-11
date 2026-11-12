#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standalone script to generate Figure 3 only.

This is a thin wrapper around supplementary_code_1, kept for modularity.
"""

from supplementary_code_1 import build_capacity_table, generate_figure
from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    table = build_capacity_table()
    fig = generate_figure(table)
    out_pdf = OUTPUT_DIR / "figure3_capacity_benchmark.pdf"
    fig.savefig(out_pdf, bbox_inches="tight")
    fig.savefig(out_pdf.with_suffix(".png"), bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Figure 3 saved to: {out_pdf}")

if __name__ == "__main__":
    main()
