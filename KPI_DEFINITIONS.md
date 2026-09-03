# KPI Definitions — MedTrack_DV

All six mandatory KPIs, with exact formula, source fields, and grain.

## 1. Total Admissions
`COUNTD(admission_id)` from `hospital_overview_dataset.csv`.
Filterable by department, date range, admission_type.

## 2. Occupancy Rate
```
occupancy_rate_pct = occupied_beds / total_bed_capacity * 100
```
- `occupied_beds`: count of admissions whose [admission_date, discharge_date]
  interval covers the given day, per department (computed via an interval
  sweep, not a snapshot).
- `total_bed_capacity`: sum of `ward.total_beds` for all wards in that department.
- Source table: `resource_utilization_dataset.csv` (resource_type = "Bed").
- Grain: hospital + department + day.

## 3. Average Length of Stay
```
avg_length_of_stay_days = AVG(discharge_date - admission_date)
```
Computed at admission grain in `hospital_overview_dataset.csv`, aggregated
by department/day in `department_analytics_dataset.csv`.

## 4. Readmission Rate
**Definition used:** a 30-day readmission — an admission counts as a
readmission if the same patient has a prior admission whose discharge
date is within 30 days before this admission's start date.

```
readmission_flag = "Yes" if (admission_date - previous_discharge_date_for_same_patient) <= 30 days else "No"
readmission_rate_pct = COUNT(readmission_flag == "Yes") / COUNT(admission_id) * 100
```

Measured overall rate: 2.49%. This is a standard clinical definition
(matches CMS's commonly used 30-day readmission window) — documented here
so it can be defended if questioned, and can be changed to a different
window (e.g. 90 days) by editing `scripts/build_four_tables.py` if the
mentor specifies a different definition.

## 5. Bed Utilization Rate
Same underlying calculation as Occupancy Rate (see #2) — the source
dataset does not distinguish "beds occupied" from "beds in active clinical
use" as separate concepts, so both KPIs are reported from the same
`occupancy_rate_pct` field. This is stated explicitly rather than
inventing an artificial second definition to make the two KPIs look
different.

## 6. Department Efficiency Score
A documented composite score, 0–100, per department:

```
los_score      = 100 - min-max normalize(avg_length_of_stay_days)   # lower LOS -> higher score
readmit_score  = 100 - min-max normalize(readmission_rate_pct)      # lower readmission -> higher score
department_efficiency_score = (los_score * 0.5) + (readmit_score * 0.5)
```

**Components:** average length of stay, readmission rate (equal weight,
50/50).
**Why only two components:** the source dataset has no equipment-downtime
or capacity-shortage field, so a fuller composite (as the guidance doc
suggests: occupancy + LOS + readmission + downtime) cannot be built
without inventing a downtime number. If a downtime/capacity-shortage field
becomes available, add it as a third weighted component and rebalance
weights — the formula is written to make that change straightforward.
**Interpretation:** higher score = shorter stays and fewer readmissions,
relative to other departments in this dataset. Scores are *relative*
(min-max normalized across departments in this dataset), not
absolute/benchmarked against external hospital standards.
