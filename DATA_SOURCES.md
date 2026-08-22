# DATA_SOURCES.md — MedTrack_DV | Milestone 1

## Data Policy

> The datasets used in this project are synthetic datasets generated for educational and internship project development purposes. They do not represent real patient records or confidential healthcare information.

No real patient information, names, addresses, phone numbers, medical record numbers, or other personally identifiable information is used anywhere in this project.

**Generation date:** 2025-01-01 to 2025-12-31 data range; datasets generated for Milestone 1 on the project build date.
**Generator:** `scripts/generate_synthetic_data.py` (random seed = 42, for reproducibility)

---

## Dataset 1 — Hospital Operations

| Field | Value |
|---|---|
| File | `data/raw/hospital_operations.csv` |
| Synthetic-data status | 100% synthetic |
| Purpose | Daily hospital-level operational activity; supports the future Hospital Overview dashboard |
| Rows | 2,565 |
| Columns | 10 |
| Key fields | `Hospital_ID`, `Date` |
| Relationships | `Hospital_ID` → Patient Admissions; `Hospital_ID` + `Date` → Resource Utilization |

## Dataset 2 — Patient Admissions

| Field | Value |
|---|---|
| File | `data/raw/patient_admissions.csv` |
| Synthetic-data status | 100% synthetic |
| Purpose | Synthetic patient admission/discharge activity; supports future Patient Flow analysis |
| Rows | 10,542 |
| Columns | 11 |
| Key fields | `Patient_ID` (unique), `Hospital_ID`, `Department_ID` |
| Relationships | `Hospital_ID` → Hospital Operations; `Hospital_ID` + `Department_ID` → Department Data |

## Dataset 3 — Department Data

| Field | Value |
|---|---|
| File | `data/raw/department_data.csv` |
| Synthetic-data status | 100% synthetic |
| Purpose | Hospital department-level operational information; supports future Department Analytics |
| Rows | 71 |
| Columns | 10 |
| Key fields | `Hospital_ID`, `Department_ID` |
| Relationships | `Hospital_ID` + `Department_ID` → Patient Admissions and Resource Utilization |

## Dataset 4 — Resource Utilization

| Field | Value |
|---|---|
| File | `data/raw/resource_utilization.csv` |
| Synthetic-data status | 100% synthetic |
| Purpose | Daily hospital/department resource usage; supports future Resource Utilization analysis |
| Rows | 5,220 |
| Columns | 11 |
| Key fields | `Hospital_ID`, `Department_ID`, `Date` |
| Relationships | `Hospital_ID` + `Department_ID` → Department Data; `Hospital_ID` + `Date` → Hospital Operations |

---

## Master Keys

- **Hospital_ID**: `H001`–`H007` (7 synthetic hospitals — MedCare General Hospital, CityCare Medical Center, LifeLine Hospital, HealthFirst Medical Institute, PrimeCare Hospital, Sunrise Community Hospital, Unity Wellness Hospital)
- **Department_ID**: `D001`–`D010` (Cardiology, Neurology, Orthopedics, Pediatrics, General Medicine, Emergency, Oncology, Dermatology, ENT, Gastroenterology)
- **Patient_ID**: `P00001`–`P10542` (unique per admission record)
- **Date range**: 2025-01-01 to 2025-12-31, standard format `YYYY-MM-DD`

No external URLs or third-party data sources were used — all four datasets were generated programmatically.
