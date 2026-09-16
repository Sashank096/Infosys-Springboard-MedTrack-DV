# MedTrack_DV – Dataset Sources
## Milestone 1 | Infosys Springboard Virtual Internship

---

## Overview

The MedTrack_DV project uses **4 approved datasets** from Kaggle covering all required hospital analytics areas: admissions, patient flow, department performance, bed utilization, staff allocation, and readmission.

---

## Dataset 1 – Hospital Management System (CORE/HMIS)

| Field | Details |
|---|---|
| **Name** | Hospital Management System |
| **Source** | Kaggle |
| **URL** | https://www.kaggle.com/datasets/mshamoonbutt/hospital-management-system |
| **Type** | Excel (.xlsx) – Multi-sheet relational dataset |
| **Role** | PRIMARY / CORE dataset |

### Sheets Available
| Sheet | Description | Key Column |
|---|---|---|
| Patients | Patient demographics | patient_id |
| BedRecords | Admission & discharge records | admission_id |
| Department | Hospital departments | dept_id |
| Ward | Ward details | ward_no |
| Bed | Bed inventory | bed_no |
| Doctor | Doctor profiles | doct_id |
| Nurse | Nurse profiles | nurse_id |
| Helpers | Support staff | helper_id |
| StaffShift | Staff shift schedule | shift_id |
| Appointment | Patient appointments | appt_id |
| MedicalRecord | Medical records | record_id |
| SurgeryRecord | Surgery records | surgery_id |
| Room | Room inventory | room_no |
| RoomRecords | Room allocation | room_record_id |

### Used For
- Hospital Overview Dashboard
- Patient Flow Dashboard
- Department Analytics Dashboard
- Resource Utilization Dashboard

---

## Dataset 2 – Hospital Beds Management (RESOURCE)

| Field | Details |
|---|---|
| **Name** | Hospital Beds Management |
| **Source** | Kaggle |
| **URL** | https://www.kaggle.com/datasets/jaderz/hospital-beds-management |
| **Type** | CSV (4 files) |
| **Role** | RESOURCE / CAPACITY dataset |

### Files Available
| File | Description | Rows |
|---|---|---|
| beds_patients.csv | Patient admissions with satisfaction | 1,000 |
| beds_services_weekly.csv | Weekly service demand and bed stats | 208 |
| beds_staff.csv | Staff list with roles and services | 110 |
| beds_staff_schedule.csv | Weekly staff attendance | 6,552 |

### Key Columns
- `available_beds`, `patients_admitted`, `patients_refused`
- `patient_satisfaction`, `staff_morale`
- `service`, `week`, `month`

### Used For
- Resource Utilization Dashboard
- Department Analytics Dashboard
- KPI 5: Bed Utilization Rate
- KPI 6: Department Efficiency Score

---

## Dataset 3 – Hospital Readmission Data (PATIENT/OUTCOME)

| Field | Details |
|---|---|
| **Name** | Hospital Data for Patient Readmission Prediction |
| **Source** | Kaggle |
| **URL** | https://www.kaggle.com/datasets/ashishsahani/hospital-admissions-data |
| **Type** | CSV (2 files) |
| **Role** | PATIENT / OUTCOME dataset |

### Files Available
| File | Description |
|---|---|
| readmission_admission_data.csv | Patient admissions with 56 clinical columns |
| readmission_mortality_data.csv | Mortality outcome data |

### Key Columns
- `mrd_no` (patient ID), `d_o_a` (admission date), `d_o_d` (discharge date)
- `duration_of_stay`, `age`, `gender`, `outcome`
- `type_of_admission` (Emergency / OPD)

### Used For
- Patient Flow Dashboard
- Hospital Overview Dashboard
- KPI 3: Average Length of Stay
- KPI 4: Readmission Rate

---

## Dataset 4 – Healthcare Dataset (INPATIENT/DISCHARGE)

| Field | Details |
|---|---|
| **Name** | Healthcare Dataset |
| **Source** | Kaggle |
| **URL** | https://www.kaggle.com/datasets/prasad22/healthcare-dataset |
| **Type** | CSV (1 file) |
| **Role** | INPATIENT / DISCHARGE dataset |

### Key Columns
- `name`, `age`, `gender`, `medical_condition`
- `date_of_admission`, `discharge_date`, `admission_type`
- `hospital`, `doctor`, `billing_amount`, `test_results`

### Used For
- Hospital Overview Dashboard
- Patient Flow Dashboard
- KPI 1: Total Admissions
- KPI 3: Average Length of Stay

---

## Dataset Coverage Matrix

| Requirement | Dataset 1 (HMIS) | Dataset 2 (Beds) | Dataset 3 (Readmission) | Dataset 4 (Healthcare) |
|---|---|---|---|---|
| Hospital Operations | ✅ | ✅ | — | ✅ |
| Patient Admissions | ✅ | ✅ | ✅ | ✅ |
| Departments | ✅ | ✅ | — | — |
| Wards | ✅ | — | — | — |
| Beds | ✅ | ✅ | — | — |
| Staff | ✅ | ✅ | — | — |
| Patient Flow | ✅ | ✅ | ✅ | ✅ |
| Readmission | — | — | ✅ | — |
| Length of Stay | ✅ | ✅ | ✅ | ✅ |
| Resource Utilization | ✅ | ✅ | — | — |
| Capacity Planning | — | ✅ | — | — |
