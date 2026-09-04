# Data Cleaning — MedTrack_DV

## Steps applied (in `build_datasets.py`)

1. **Deduplication** — `admission.drop_duplicates()`. Result: 0 duplicate
   rows found in the raw admission table.
2. **Outlier / validity checks** — checked for negative length-of-stay
   (discharge_date < admission_date). Result: 0 invalid rows.
3. **Date standardization** — `admission_date` and `discharge_date` parsed
   to proper datetime; `date_of_birth` parsed for age calculation.
4. **ID standardization** — `patient_id`, `admission_id`, `department_id`,
   `ward_id`, `bed_id`, `employee_id` are all native integer keys in the
   source; no renaming/remapping needed since they were already
   consistent (verified no mixed-format IDs like "P001" vs "p001").
5. **Derived fields** (all formulas documented, none fabricated):
   - `length_of_stay_days` = discharge_date − admission_date
   - `patient_age` = (admission_date − date_of_birth) in years
   - `readmission_flag` = "Yes" if the same patient's admission_date falls
     within 30 days of their own previous discharge_date, else "No"
     (standard 30-day readmission definition)
   - `department_efficiency_score` = weighted composite of normalized
     average LOS and normalized readmission rate (50/50) — see
     `docs_validation/KPI_DEFINITIONS.md`
   - `occupancy_rate_pct` = occupied beds (via date-range interval sweep
     over admissions) ÷ `ward.total_beds` summed per department
6. **Missing values** — 0% missing across `hospital_operations_cleaned.csv`,
   `patient_admissions_cleaned.csv`, `department_data_cleaned.csv`;
   0.05% missing in `resource_utilization_cleaned.csv` (explained: static
   staff-count rows have no applicable date/capacity field, flagged via
   the `note` column rather than silently left blank).

## What was intentionally NOT done
- No `fillna(0)` on any field — every missing value was investigated
  first (see step 6).
- No invented columns to satisfy a KPI that the source doesn't support
  (e.g. equipment downtime — simply not present, not backfilled).
