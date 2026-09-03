# Data Sources — MedTrack_DV

## Source used for Milestone 1

**Type:** Real, relational, synthetic HMIS dataset (Kaggle download, user-provided)
**Structure:** 18 linked CSV files under `raw_source/`
**Scale:** 45,000 admissions · 30,000 patients · 11 departments · 27 wards ·
415 beds · 500 employees
**Date range:** 2020-01-01 to 2025-12-31

### Files in `raw_source/`
| File | Rows | Key fields |
|---|---|---|
| `admission.csv` | 45,000 | admission_id, admission_date, discharge_date, patient_id, department_id, ward_id, bed_id, disease_id |
| `patient.csv` | 30,000 | patient_id, gender, date_of_birth, blood_group, city |
| `department.csv` | 11 | department_id, department_name, department_type |
| `ward.csv` | 27 | ward_id, ward_name, ward_type, **total_beds** (real capacity) |
| `bed.csv` | 415 | bed_id, bed_number, bed_status, ward_id |
| `disease.csv` | 20 | disease_id, disease_name, disease_category |
| `employee.csv` | 500 | employee_id, role, department_id |
| `doctor.csv` | 98 | doctor_id, employee_id, specialization |
| `staff_assignment.csv` | 207 | employee_id, ward_id, shift |
| `billing.csv` | 45,000 | admission_id, total_amount, payment_status |
| (+ drug, drug_inventory, drug_manufacturer, diagnostic_test, patient_diagnostic, patient_insurance, insurance_provider, billing_detail, prescription) | | supporting tables, not used in Milestone 1 core tables |

### Why this source
It contains genuine primary/foreign-key relationships across admissions,
departments, wards, beds, and staff — matching the relational structure
the project brief calls for, rather than a single flat patient CSV.
Critically, `ward.csv` provides **real total bed capacity**, which makes
Occupancy Rate and Bed Utilization Rate genuinely calculable (not every
hospital dataset includes this).

### Known gaps (documented, not hidden)
- No multi-step patient movement/transfer log (each admission has one
  department/ward/bed, not a sequence of transfers)
- No per-date staff roster (staff_assignment has no date column)
- No equipment/resource data beyond beds and staff
