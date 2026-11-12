#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master script: generate all figures for the manuscript.

Run this from the repository root or from the code/ directory:
    python code/generate_all_figures.py
"""

import subprocess
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
FIGURES_DIR = CODE_DIR.parent / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

SCRIPTS = [
    "generate_figure1.py",
    "generate_figure2.py",
    "supplementary_code_1.py",
]

def main():
    print("Generating all manuscript figures...")
    for script in SCRIPTS:
        path = CODE_DIR / script
        print(f"\n>>> Running {script}")
        result = subprocess.run(
            [sys.executable, str(path)],
            cwd=CODE_DIR,
            text=True,
            capture_output=True,
        )
        print(result.stdout, end="")
        if result.returncode != 0:
            print(f"ERROR in {script}:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            sys.exit(result.returncode)
    print("\nAll figures generated successfully.")
    print(f"Output directory: {FIGURES_DIR}")

if __name__ == "__main__":
    main()
