# Data Model — MedTrack_DV

## Four analytical tables (Milestone 1 deliverable)

| Table | Grain (what one row means) | Rows |
|---|---|---|
| `hospital_operations_cleaned.csv` | One admission | 45,000 |
| `patient_admissions_cleaned.csv` | One admission's department/ward/bed assignment | 45,000 |
| `department_data_cleaned.csv` | One hospital + department + day | 12,474 |
| `resource_utilization_cleaned.csv` | One hospital + department + day + resource_type (Bed or Staff) | 13,138 |

## Relationships

```
patient.csv ──┐
              ├──> admission.csv (admission_id, patient_id, department_id, ward_id, bed_id, disease_id)
department.csv ──┤
ward.csv ─────────┤   (ward.total_beds gives real capacity per department)
bed.csv ──────────┤
disease.csv ──────┤
billing.csv ──────┘  (joined on admission_id)

admission.csv
   │
   ├──> hospital_operations_cleaned.csv   (1 row per admission, all attributes)
   ├──> patient_admissions_cleaned.csv    (1 row per admission's dept/ward/bed assignment)
   ├──> department_data_cleaned.csv       (aggregated: department + day)
   └──> resource_utilization_cleaned.csv  (aggregated: department + day + resource_type,
                                            occupancy computed via date-range interval sweep
                                            against ward.total_beds)
```

## Why not one flat merged table
Admissions, department-day aggregates, and resource-day aggregates are at
different grains. Flattening them into one table would either duplicate
admission-level fields across every department-day row, or lose the
department/day aggregation entirely. Keeping four tables at their correct
grain, linked by `hospital_id` + `department_id` + `date` where
applicable, avoids this — consistent with the project brief's instruction
not to blindly merge tables of different grain.

## Validated relationships (see `docs_validation/relationship_validation_report.md`)
- 0 duplicate `admission_id` across both admission-level tables
- 0 orphaned `department_id` between admission-level and department-level tables
- 0 orphaned `admission_id` between the two admission-grain tables
- Occupancy values bounded 0–100% (sanity-checked against real ward capacity)
