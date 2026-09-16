# MedTrack_DV – Dataset Validation & Mapping Sheet
## Milestone 1 | Infosys Springboard Virtual Internship

---

## Purpose

As required by the project mentor, this document validates every dataset before merging. For every dataset, it documents fields, common keys, actions taken, and data quality results.

---

## Dataset 1 – Hospital Management System (HMIS)

| Field | Available? | Common Key? | Action |
|---|---|---|---|
| Hospital ID | No (added) | Yes (surrogate H001) | Created hospital_id = H001 |
| Patient ID | Yes (patient_id) | Yes | Used as-is |
| Admission ID | Yes (admission_id in BedRecords) | Yes | Used as-is |
| Department ID | Yes (dept_id) | Yes | Used for joining Doctor, Nurse, Ward |
| Ward ID | Yes (ward_no) | Yes | Used for joining BedRecords |
| Bed ID | Yes (bed_no) | Yes | Used for occupancy calculation |
| Staff ID | Yes (doct_id, nurse_id) | Yes | Used in StaffShift |
| Admission Date | Yes (admission_date) | — | Converted to datetime, derived year/month/quarter |
| Discharge Date | Yes (discharge_date) | — | Converted to datetime, LOS derived |
| Readmission | No | — | Not available in HMIS |
| Available Beds | Partial (Bed table) | — | Count of bed records |

**Data Quality:**
- Rows: Multiple sheets (see dataset_sources.md)
- Missing Values: < 2% after cleaning
- Duplicates: Removed on primary keys
- Status: ✅ VALIDATED

---

## Dataset 2 – Hospital Beds Management

| Field | Available? | Common Key? | Action |
|---|---|---|---|
| Hospital ID | No (added) | Yes (surrogate H001) | Created hospital_id = H001 |
| Patient ID | Yes (patient_id) | Yes (Beds Patients) | Used as-is |
| Admission ID | No | No | Not applicable (grain = weekly service) |
| Department ID | No | No | Service name used as department proxy |
| Service/Dept Name | Yes (service) | Yes | Standardized to match HMIS dept_name |
| Ward ID | No | No | Not available |
| Bed ID | No | No | Available beds count used instead |
| Staff ID | Yes (staff_id) | Yes | Used in staff_schedule join |
| Admission Date | Yes (arrival_date in beds_patients.csv) | — | Converted to datetime |
| Discharge Date | Yes (departure_date) | — | Converted to datetime |
| Readmission | No | — | Not available |
| Available Beds | Yes (available_beds) | — | Used for KPI 2 and KPI 5 |
| Patients Admitted | Yes (patients_admitted) | — | Core resource metric |
| Patients Refused | Yes (patients_refused) | — | Used for shortage flag |
| Patient Satisfaction | Yes (patient_satisfaction) | — | Used in KPI 6 |
| Staff Morale | Yes (staff_morale) | — | Used in KPI 6 |

**Data Quality:**
- beds_patients.csv: 1,000 rows | 7 columns
- beds_services_weekly.csv: 208 rows | 10 columns
- beds_staff.csv: 110 rows | 4 columns
- beds_staff_schedule.csv: 6,552 rows | 6 columns
- Missing Values: < 2% after cleaning
- Duplicates: Removed
- Status: ✅ VALIDATED

---

## Dataset 3 – Hospital Readmission Data

| Field | Available? | Common Key? | Action |
|---|---|---|---|
| Hospital ID | No | No | Not available in this dataset |
| Patient ID | Yes (mrd_no) | Yes | Renamed to patient_id |
| Admission ID | No | No | mrd_no used as patient identifier |
| Department ID | No | No | Not available |
| Ward ID | Yes (ward) | Partial | Ward name available (text) |
| Bed ID | Partial (sr_b_available, sr_b_occupied) | No | Used for bed analytics only |
| Admission Date | Yes (d_o_a) | — | Renamed to admission_date, converted to datetime |
| Discharge Date | Yes (d_o_d) | — | Renamed to discharge_date, converted to datetime |
| Length of Stay | Yes (duration_of_stay) | — | Validated: no negative values |
| Readmission | Yes (outcome: DAMA/EXPIRY) | — | readmission_flag derived |
| Age | Yes | — | Validated: 0–120 range |
| Gender | Yes | — | Standardized to Male/Female/Unknown |
| Admission Type | Yes (type_of_admission) | — | Emergency/OPD standardized |

**Data Quality:**
- readmission_admission_data.csv: 56 columns of clinical data
- Missing Values: < 5% in some clinical columns (acceptable)
- Duplicates: Removed on mrd_no
- Status: ✅ VALIDATED

---

## Dataset 4 – Healthcare Dataset

| Field | Available? | Common Key? | Action |
|---|---|---|---|
| Hospital ID | No | No | Hospital name used as identifier |
| Patient ID | No | No | Name + admission date used as composite key |
| Admission ID | No | No | Row index used |
| Department ID | No | No | medical_condition used as proxy |
| Ward ID | No | No | Not available |
| Bed ID | No | No | Not available |
| Admission Date | Yes (date_of_admission) | — | Converted to datetime |
| Discharge Date | Yes (discharge_date) | — | Converted to datetime |
| Length of Stay | Derived | — | discharge_date - date_of_admission |
| Readmission | No | No | Not directly available |
| Age | Yes | — | Validated: 0–120 range |
| Gender | Yes | — | Standardized |
| Admission Type | Yes (admission_type) | — | Emergency/Elective/Urgent standardized |
| Billing Amount | Yes | — | Validated: no negative values |
| Test Results | Yes | — | Normal/Abnormal/Inconclusive |

**Data Quality:**
- healthcare_dataset.csv: 55,500 rows | 15 columns
- Missing Values: < 1%
- Duplicates: Removed
- Status: ✅ VALIDATED

---

## Cross-Dataset Key Matching Summary

| Key | Dataset 1 (HMIS) | Dataset 2 (Beds) | Dataset 3 (Readmission) | Dataset 4 (Healthcare) | Join Type |
|---|---|---|---|---|---|
| hospital_id | H001 (surrogate) | H001 (surrogate) | Not available | Not available | Surrogate |
| patient_id | ✅ patient_id | ✅ patient_id | ✅ mrd_no (renamed) | ❌ Not available | Direct / None |
| admission_id | ✅ admission_id | ❌ Not available | ❌ Not available | ❌ Not available | Direct only in HMIS |
| department_id | ✅ dept_id | ✅ service (text) | ❌ Not available | ❌ Not available | Text-based match |
| ward_id | ✅ ward_no | ❌ Not available | Partial (ward text) | ❌ Not available | HMIS only |
| admission_date | ✅ | ✅ arrival_date | ✅ d_o_a | ✅ date_of_admission | All present |
| discharge_date | ✅ | ✅ departure_date | ✅ d_o_d | ✅ discharge_date | All present |

---

## Data Architecture Decision

The 4 datasets are **NOT directly merged** into one flat file. They are kept as separate analytical tables following their natural grain:

```
hospital_overview_dataset.csv   → Grain: One admission
patient_flow_dataset.csv        → Grain: One patient movement
department_analytics_dataset.csv → Grain: One dept per week
resource_utilization_dataset.csv → Grain: One dept per week (resource)
```

They are linked in Tableau through common fields: `hospital_id`, `service/dept_name`, `week/date`, and `patient_id` where available.

---

## Validation Status

| Dataset | Completeness | Missing % | Duplicates | Status |
|---|---|---|---|---|
| HMIS Patients | > 95% | < 2% | Removed | ✅ |
| HMIS BedRecords | > 95% | < 2% | Removed | ✅ |
| HMIS Departments | 100% | 0% | None | ✅ |
| Beds Patients | > 98% | < 2% | Removed | ✅ |
| Beds Services | > 99% | < 1% | None | ✅ |
| Readmission Data | > 90% | < 10% clinical | Removed | ✅ |
| Healthcare Dataset | > 99% | < 1% | Removed | ✅ |
