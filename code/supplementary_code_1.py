#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Supplementary Code 1
Photonic information capacity benchmark and reassembly fidelity simulation

This script reproduces the numerical results and Figure 3 of the manuscript:
"什么是信息处理：最细微的光量子为何成为信息处理的主流载体"
("What is information processing, and why do the most subtle photonic quanta
become the mainstay of information processing?")

Author: Xiaohui Li
Repository: https://github.com/xiaohui-li-lab/
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==================== Configuration ====================
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Information requirement range (bits)
I = np.linspace(0, 200, 401)

# Per-carrier depolarizing error (2%)
EPSILON = 0.02

# Carrier definitions: name -> capacity in bits
CARRIERS = {
    "Classical bit":   {"C": 1.00,  "linestyle": "-",  "color": "#1f77b4"},
    "Molecular state": {"C": 3.32,  "linestyle": "--", "color": "#ff7f0e"},
    "Photon qudit":    {"C": 8.00,  "linestyle": ":",  "color": "#2ca02c"},
}

# ==================== Table 2: Capacity benchmark ====================
def build_capacity_table() -> pd.DataFrame:
    """
    Reproduce Table 2 of the manuscript.
    Effective number of states and Shannon capacity per carrier.
    """
    table = pd.DataFrame({
        "Carrier": [
            "Ideal classical bit",
            "Electronic switch (charge ensemble)",
            "Molecular vibronic state",
            "Photon (pol + OAM + path + time)",
        ],
        "Effective_states_d": [2, 2, 10, 256],
        "Decoherence_time_310K": [
            "Indefinite (classical)",
            "ns to µs",
            "fs to ps",
            "µs to ms (guided/free-space)",
        ],
    })
    table["Capacity_log2d_bits"] = np.log2(table["Effective_states_d"])
    return table

# ==================== Simulation core ====================
def success_probability(information: np.ndarray,
                        capacity: float,
                        error: float) -> np.ndarray:
    """
    Compute the probability of successful reassembly of a message of size
    `information` bits, given per-carrier depolarizing error `error`
    and per-carrier capacity `capacity`.

    Parameters
    ----------
    information : np.ndarray
        Array of required information sizes in bits.
    capacity : float
        Shannon capacity per carrier in bits.
    error : float
        Depolarizing error probability per carrier.

    Returns
    -------
    np.ndarray
        Success probability for each information size.
    """
    if not 0 <= error <= 1:
        raise ValueError("Error probability must be in [0, 1].")
    if capacity <= 0:
        raise ValueError("Capacity must be positive.")
    return (1.0 - error) ** (information / capacity)

# ==================== Figure generation ====================
def generate_figure(table: pd.DataFrame) -> plt.Figure:
    """
    Generate Figure 3: capacity benchmark bar chart (top) and reassembly
    fidelity curves (bottom).
    """
    fig, axes = plt.subplots(2, 1, figsize=(9, 9), dpi=150)
    fig.patch.set_facecolor("white")

    # --- Top panel: capacity per carrier ---
    ax1 = axes[0]
    carriers_sorted = table.sort_values("Capacity_log2d_bits")
    bars = ax1.barh(
        carriers_sorted["Carrier"],
        carriers_sorted["Capacity_log2d_bits"],
        color=["#7f7f7f", "#ffbb78", "#ff7f0e", "#2ca02c"],
    )
    ax1.set_xlabel("Capacity per carrier (bits)", fontsize=11)
    ax1.set_title(
        "Information capacity of elementary carriers (Table 2)",
        fontsize=12, fontweight="bold",
    )
    ax1.set_xlim(0, 10)
    ax1.grid(axis="x", linestyle="--", alpha=0.4)

    # Annotate bar values
    for bar in bars:
        width = bar.get_width()
        ax1.text(
            width + 0.15, bar.get_y() + bar.get_height() / 2,
            f"{width:.2f}", va="center", fontsize=9,
        )

    # --- Bottom panel: success probability vs information ---
    ax2 = axes[1]
    for name, props in CARRIERS.items():
        P = success_probability(I, props["C"], EPSILON)
        ax2.plot(
            I, P,
            linestyle=props["linestyle"],
            color=props["color"],
            linewidth=2.2,
            label=f"{name} (C = {props['C']:.2f} bits)",
        )

    ax2.set_xlabel("Required information $I$ (bits)", fontsize=11)
    ax2.set_ylabel("Success probability $P_{\\mathrm{success}}$", fontsize=11)
    ax2.set_title(
        "Reassembly fidelity under 2% depolarizing noise per carrier",
        fontsize=12, fontweight="bold",
    )
    ax2.set_xlim(0, 200)
    ax2.set_ylim(0, 1.05)
    ax2.legend(loc="lower left", fontsize=9)
    ax2.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    return fig

# ==================== Main entry point ====================
def main():
    print("=" * 60)
    print("Supplementary Code 1: Photonic capacity benchmark")
    print("=" * 60)

    # Print Table 2 to console
    table = build_capacity_table()
    print("\nTable 2: Capacity benchmark")
    print(table.round(2).to_string(index=False))

    # Generate Figure 3
    fig = generate_figure(table)
    output_path = OUTPUT_DIR / "figure3_capacity_benchmark.pdf"
    fig.savefig(output_path, bbox_inches="tight")
    fig.savefig(output_path.with_suffix(".png"), bbox_inches="tight", dpi=300)
    plt.close(fig)

    print(f"\nFigure saved to: {output_path}")
    print("PNG version also saved for quick preview.")

if __name__ == "__main__":
    main()
