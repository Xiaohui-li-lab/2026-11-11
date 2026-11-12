#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Figure 2: Cardio-Photonic Hypothesis

Schematic showing the heart distributing far-infrared (FIR) photons via blood
to the brain and peripheral organs.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def draw_hypothesis():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=150)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # Organ boxes
    organ_style = dict(
        boxstyle="round,pad=0.5",
        linewidth=2.5,
        facecolor="#F8F9FA",
        edgecolor="#212529",
    )

    # Heart
    ax.text(
        1.5, 3.5, "Heart",
        fontsize=14, fontweight="bold", ha="center", va="center",
        bbox={**organ_style, "facecolor": "#FADBD8", "edgecolor": "#C0392B"},
    )

    # Blood
    ax.text(
        5.0, 3.5, "Blood",
        fontsize=13, fontweight="bold", ha="center", va="center",
        bbox={**organ_style, "facecolor": "#D6EAF8", "edgecolor": "#2874A6"},
    )

    # Brain
    ax.text(
        8.5, 5.5, "Brain",
        fontsize=13, fontweight="bold", ha="center", va="center",
        bbox={**organ_style, "facecolor": "#E8DAEF", "edgecolor": "#8E44AD"},
    )

    # Peripheral organs
    ax.text(
        8.5, 1.5, "Peripheral\nOrgans",
        fontsize=12, fontweight="bold", ha="center", va="center",
        bbox={**organ_style, "facecolor": "#D5F5E3", "edgecolor": "#27AE60"},
    )

    # Arrows
    ax.annotate(
        "", xy=(3.5, 3.5), xytext=(2.3, 3.5),
        arrowprops=dict(arrowstyle="->", color="#C0392B", lw=3),
    )
    ax.text(2.9, 3.75, "pump", fontsize=10, ha="center", color="#C0392B")

    # FIR photons to brain
    ax.annotate(
        "", xy=(7.5, 5.3), xytext=(6.0, 3.9),
        arrowprops=dict(arrowstyle="->", color="#E67E22", lw=2.5, ls="--"),
    )
    ax.text(6.6, 4.85, "FIR photons", fontsize=9, color="#E67E22", fontweight="bold", rotation=35)

    # FIR photons to organs
    ax.annotate(
        "", xy=(7.5, 1.7), xytext=(6.0, 3.1),
        arrowprops=dict(arrowstyle="->", color="#E67E22", lw=2.5, ls="--"),
    )
    ax.text(6.6, 2.15, "FIR photons", fontsize=9, color="#E67E22", fontweight="bold", rotation=-35)

    # Sub-labels
    ax.text(8.5, 4.6, "neural modulation\n(skull penetration window)", fontsize=9, ha="center", color="#666666")
    ax.text(8.5, 0.6, "tissue-level quantum modulation", fontsize=9, ha="center", color="#666666")

    # Title
    ax.text(
        5.5, 6.6,
        "Cardio-Photonic Information Hypothesis",
        fontsize=15, fontweight="bold", ha="center",
    )
    ax.text(
        5.5, 6.15,
        "The heart distributes metabolic far-infrared photons to modulate quantum states",
        fontsize=10, ha="center", color="#555555",
    )

    plt.tight_layout()
    return fig

def main():
    fig = draw_hypothesis()
    out_pdf = OUTPUT_DIR / "figure2_cardio_photonic_hypothesis.pdf"
    fig.savefig(out_pdf, bbox_inches="tight")
    fig.savefig(out_pdf.with_suffix(".png"), bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Figure 2 saved to: {out_pdf}")

if __name__ == "__main__":
    main()
