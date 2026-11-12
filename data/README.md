# Data folder

This directory contains the clinical data compilation used in the manuscript.

## Files

- `far_infrared_clinical_reports.csv`: Raw coding sheet for the 29 far-infrared clinical reports.
  Columns: study_id, first_author, year, country, condition, sample_size,
  wavelength_um, power_density_mw_cm2, duration_min, sessions_n,
  outcome_direction, main_finding, notes.

- `clinical_summary.csv`: Auto-generated summary produced by
  `code/clinical_data_compiler.py`.

## Data sources

The 29 reports were identified by querying PubMed/Medline and CNKI using the
keywords: "far-infrared therapy", "far-infrared radiation", "远红外线",
"biological effect".

## Status

Currently a template. Real bibliographic data must be entered before submission.
