#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Figure 1: Decomposition-Assembly Model

Schematic of the quantum decomposition-assembly model of information processing:
Macroscopic input M -> Decomposition D -> Elementary carriers -> Quantum U -> Assembly A -> Output M'
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def draw_model():
    fig, ax = plt.subplots(figsize=(10, 8), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # Box style
    box_kwargs = dict(
        boxstyle="round,pad=0.4",
        facecolor="#E8F4F8",
        edgecolor="#2C5F7C",
        linewidth=2,
    )

    # Diamond style
    diamond_kwargs = dict(
        boxstyle="diamond,pad=0.5",
        facecolor="#FFF4E6",
        edgecolor="#D35400",
        linewidth=2,
    )

    # Helper to add text box
    def add_box(x, y, text, kind="box", fontsize=11):
        style = box_kwargs if kind == "box" else diamond_kwargs
        ax.text(
            x, y, text,
            ha="center", va="center",
            fontsize=fontsize, fontweight="bold",
            bbox=style,
        )

    # Nodes
    add_box(5, 9.0, "Macroscopic input\n$\\mathbf{M}$", kind="box")
    add_box(5, 7.2, "Decomposition\n$\\mathcal{D}$", kind="diamond")
    add_box(5, 5.0, "Elementary quantum carriers\n(photons · phonons · electrons)", kind="box")
    add_box(5, 2.8, "Quantum processing\n$\\mathcal{U}$", kind="diamond")
    add_box(5, 1.0, "Assembly\n$\\mathcal{A}$", kind="diamond")
    add_box(5, -1.0, "Macroscopic output\n$\\mathbf{M}'$", kind="box")

    # Arrows
    arrow_style = dict(arrowstyle="->", color="#2C5F7C", lw=2.5)
    for y1, y2 in [(8.5, 7.8), (6.6, 5.5), (4.5, 3.3), (2.3, 1.5), (0.5, -0.5)]:
        ax.annotate("", xy=(5, y2), xytext=(5, y1), arrowprops=arrow_style)

    # Environment decoherence arrow
    ax.annotate(
        "environment",
        xy=(6.7, 2.5), xytext=(8.0, 4.5),
        fontsize=10, color="#7F8C8D", ha="center",
        arrowprops=dict(arrowstyle="->", color="#7F8C8D", lw=1.5, ls="--"),
    )

    # Title
    ax.text(
        5, 10.2,
        "Quantum Decomposition--Assembly Model of Information Processing",
        fontsize=14, fontweight="bold", ha="center",
    )

    plt.tight_layout()
    return fig

def main():
    fig = draw_model()
    out_pdf = OUTPUT_DIR / "figure1_decomposition_assembly.pdf"
    fig.savefig(out_pdf, bbox_inches="tight")
    fig.savefig(out_pdf.with_suffix(".png"), bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Figure 1 saved to: {out_pdf}")

if __name__ == "__main__":
    main()
