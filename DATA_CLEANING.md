# DATA_CLEANING.md — MedTrack_DV | Milestone 1

This document summarizes the cleaning process performed in `hospital_cleaning.ipynb` on the four raw synthetic datasets.

## Problems Found in Raw Data

Intentional, small-scale, realistic data-quality issues were present in the raw files:

1. **Missing values** — scattered nulls (~0.1–0.3% of cells) across select numeric and categorical columns in all four datasets (e.g. `Outpatient_Visits`, `Treatment_Type`, `Monthly_Target`, `Equipment_Count`).
2. **Duplicate rows** — a small number of exact duplicate records in each dataset, plus 42 duplicate `Patient_ID` values in Patient Admissions.
3. **Inconsistent department-name formatting** — `Department_Name` in Department Data appeared in mixed casing (`Cardiology`, `CARDIOLOGY`, `cardiology`, `Cardiology`-title-case) for ~15% of rows.
4. **Inconsistent categorical formatting** — mixed-case values in `Admission_Type` (Patient Admissions) and `Resource_Status` (Resource Utilization).
5. **Date-format inconsistencies** — `Date` / `Admission_Date` columns contained a mix of `YYYY-MM-DD`, `DD-MM-YYYY`, `MM/DD/YYYY`, and `YYYY/MM/DD` formats for ~1% of rows.

## Missing Values — Handling Approach

- **Hospital Operations**: `Hospital_Name` gaps filled via `Hospital_ID` lookup; numeric gaps (`Outpatient_Visits`, `Emergency_Admissions`, `Total_Discharges`) filled with the per-hospital median.
- **Patient Admissions**: categorical gaps (`Treatment_Type`, `Diagnosis`) filled with `"Unknown"`; `Readmission_Flag` defaulted to `"No"`; `Length_of_Stay` recomputed from `Admission_Date`/`Discharge_Date` where possible, otherwise filled with the dataset median.
- **Department Data**: `Monthly_Target` filled with the per-department median; `Department_Status` defaulted to `"Active"` (the dataset mode).
- **Resource Utilization**: `Equipment_Count` and `Staff_Available` filled with per-department medians; `Resource_Status` recomputed from the bed-occupancy ratio where missing.

## Duplicates — Handling Approach

- Exact duplicate rows dropped from all four datasets.
- Duplicate `Patient_ID` values resolved by keeping the first occurrence, preserving the uniqueness contract required by the spec.

## Standardization

- **Department names** mapped to the master `Department_ID` → name lookup (`D001` = Cardiology, `D002` = Neurology, … `D010` = Gastroenterology), eliminating all casing inconsistencies.
- **Categorical fields** (`Admission_Type`, `Resource_Status`) normalized to Title Case.
- **Dates** parsed with a mixed-format parser and standardized to `YYYY-MM-DD` (`datetime64`) across all four datasets.

## Key Validation

- `Hospital_ID` and `Department_ID` values validated against the master key lists — 100% valid in both raw and cleaned data (no orphan keys were ever introduced).
- `Patient_ID` uniqueness enforced by de-duplication (42 duplicate IDs resolved).

## Data Transformations (Business Rules Enforced)

- `Occupied_Beds` capped at `Total_Beds`; `Available_Beds` recomputed as `Total_Beds − Occupied_Beds` (Hospital Operations and Resource Utilization).
- `Emergency_Admissions` capped at `Total_Admissions`.
- `Total_Admissions`, `Total_Discharges`, `Outpatient_Visits` clipped to be non-negative.
- `Discharge_Date` swapped with `Admission_Date` where the discharge preceded admission (Patient Admissions); `Length_of_Stay` recalculated from the corrected dates.
- `Staff_Count` in Department Data enforced to be `>= Doctors_Count + Nurses_Count`.
- `Equipment_In_Use` capped at `Equipment_Count`; `Staff_Allocated` capped at `Staff_Available` (Resource Utilization).

## Before / After Results

| Dataset | Rows Before | Rows After | Missing Before | Missing After | Duplicates Before | Duplicates After |
|---|---:|---:|---:|---:|---:|---:|
| Hospital Operations | 2,565 | 2,555 | 24 (0.09%) | 0 | 10 | 0 |
| Patient Admissions | 10,542 | 10,500 | 104 (0.09%) | 0 | 41 | 0 |
| Department Data | 71 | 70 | 2 (0.28%) | 0 | 1 | 0 |
| Resource Utilization | 5,220 | 5,200 | 52 (0.09%) | 0 | 20 | 0 |

Row counts after cleaning reflect duplicate removal only — no records were dropped simply to reach the quality targets. Final completeness across all four datasets is **100%**, well within the Milestone 1 targets of completeness > 95% and missing values < 2%.
