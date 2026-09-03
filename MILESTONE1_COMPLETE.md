# MedTrack_DV — Milestone 1 Completion

## Status: Complete

| Checklist item | Status | Where |
|---|---|---|
| Dataset selection & justification | ✅ | `DATA_SOURCES.md` |
| Data collection | ✅ | `raw_source/` (18 linked CSVs) |
| Data profiling | ✅ | `DATA_QUALITY_REPORT.md` |
| Data cleaning | ✅ | `DATA_CLEANING.md`, `build_datasets.py` |
| ID / date / department standardization | ✅ | `DATA_CLEANING.md` |
| Missing-value & duplicate handling | ✅ | 0% missing (3 of 4 tables), 0 duplicates anywhere |
| Four-table construction | ✅ | `hospital_operations_cleaned.csv`, `patient_admissions_cleaned.csv`, `department_data_cleaned.csv`, `resource_utilization_cleaned.csv` |
| Relationship validation | ✅ | `docs_validation/relationship_validation_report.md` — full PASS |
| KPI formulas defined | ✅ | `docs_validation/KPI_DEFINITIONS.md` — all 6 KPIs, all calculable |

## How to reproduce
```
python3 build_datasets.py       # builds the 4 tables from raw_source/
python3 validate_datasets.py    # validates keys/relationships across them
```

## Note on source provenance
This dataset was sourced from Kaggle by hand (not auto-downloaded — Kaggle
requires authenticated access). It is a genuinely relational synthetic
HMIS dataset with real admission/discharge dates and real ward bed
capacity, which is what makes all six KPIs calculable rather than
partially blocked. See `DATA_SOURCES.md` for the full field inventory.

## Next: Milestone 2
KPI validation against the formulas in `docs_validation/KPI_DEFINITIONS.md`,
dashboard storyboarding, and the Tableau data model — not started yet.
