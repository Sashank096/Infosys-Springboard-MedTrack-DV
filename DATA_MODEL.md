# DATA_MODEL.md — MedTrack_DV | Milestone 1

## Overview

MedTrack_DV's Milestone 1 data is organized as **four separate, related datasets** rather than one large flat table. This preserves a clean relational structure for the eventual Tableau data model (to be designed in a later milestone).

```text
                 HOSPITAL
                    │
                    │ Hospital_ID
        ┌───────────┼────────────┐
        ▼           ▼            ▼
   OPERATIONS   PATIENTS     RESOURCES
                    │            ▲
                    │            │
             Department_ID       │
                    │            │
                    ▼            │
               DEPARTMENT ───────┘
                 Hospital_ID
              + Department_ID
```

## Datasets

1. **Hospital Operations** (`hospital_operations.csv`) — daily hospital-level activity: beds, admissions, discharges, outpatient visits.
2. **Patient Admissions** (`patient_admissions.csv`) — individual synthetic patient admission/discharge records, one row per patient.
3. **Department Data** (`department_data.csv`) — per-hospital, per-department staffing and capacity information.
4. **Resource Utilization** (`resource_utilization.csv`) — daily per-hospital, per-department bed/equipment/staff usage.

## Relationships

| # | From | To | Key(s) | Meaning |
|---|---|---|---|---|
| 1 | Hospital Operations | Patient Admissions | `Hospital_ID` | A hospital can have many patient admissions. |
| 2 | Patient Admissions | Department Data | `Hospital_ID` + `Department_ID` | A patient admission belongs to a department within a hospital. |
| 3 | Department Data | Resource Utilization | `Hospital_ID` + `Department_ID` | Resource utilization belongs to a particular department within a hospital. |
| 4 | Hospital Operations | Resource Utilization | `Hospital_ID` + `Date` | Hospital operational activity and resource utilization can be compared by hospital and date. |

## Master Key Reference

- **Hospital_ID**: `H001`–`H007`
- **Department_ID**: `D001` = Cardiology, `D002` = Neurology, `D003` = Orthopedics, `D004` = Pediatrics, `D005` = General Medicine, `D006` = Emergency, `D007` = Oncology, `D008` = Dermatology, `D009` = ENT, `D010` = Gastroenterology
- **Patient_ID**: unique per patient admission record, format `P00001`…
- **Date**: `YYYY-MM-DD`, range 2025-01-01 to 2025-12-31

All foreign-key relationships were validated during cleaning (Section 8 of `hospital_cleaning.ipynb`) and confirmed to have zero orphan records — every `Hospital_ID` and `Department_ID` reference in the downstream datasets resolves to a valid record in its parent dataset.

Dashboard-level relationship design (blending/joins in Tableau) is out of scope for Milestone 1 and will be addressed in a later milestone.
