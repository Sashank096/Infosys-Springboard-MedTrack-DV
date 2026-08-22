# DATA_QUALITY_REPORT.md — MedTrack_DV | Milestone 1

All values below are calculated directly from the actual raw and cleaned datasets (see `hospital_cleaning.ipynb`, Sections 4, 5, and 10).

| Dataset | Rows Before | Rows After | Missing Before | Missing After | Duplicates Before | Duplicates After | Completeness |
|---|---:|---:|---:|---:|---:|---:|---:|
| Hospital Operations | 2,565 | 2,555 | 24 | 0 | 10 | 0 | 100.00% |
| Patient Admissions | 10,542 | 10,500 | 104 | 0 | 41 | 0 | 100.00% |
| Department Data | 71 | 70 | 2 | 0 | 1 | 0 | 100.00% |
| Resource Utilization | 5,220 | 5,200 | 52 | 0 | 20 | 0 | 100.00% |

## Milestone 1 Targets vs. Actuals

| Target | Threshold | Actual (all datasets) | Status |
|---|---|---|---|
| Dataset completeness | > 95% | 100.00% | ✅ Met |
| Missing values after cleaning | < 2% | 0.00% | ✅ Met |

## Additional Quality Checks

| Check | Result |
|---|---|
| `Hospital_ID` validity (all datasets) | 100% — all values within `H001`–`H007` |
| `Department_ID` validity (all datasets) | 100% — all values within `D001`–`D010` |
| `Patient_ID` uniqueness (cleaned) | 100% unique (42 duplicates resolved) |
| Foreign-key relationship validation | 0 orphan `Hospital_ID`/`Department_ID` combinations across all four datasets |
| Date validity (cleaned) | 0 null/unparseable dates in `Date`, `Admission_Date`, `Discharge_Date` |
| Numeric rule violations (cleaned) | 0 — `Occupied_Beds <= Total_Beds`, `Equipment_In_Use <= Equipment_Count`, `Staff_Allocated <= Staff_Available`, `Emergency_Admissions <= Total_Admissions`, `Staff_Count >= Doctors_Count + Nurses_Count` all hold |

Milestone 1 data quality criteria are satisfied for all four datasets.
