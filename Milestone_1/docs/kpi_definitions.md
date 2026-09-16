# MedTrack_DV – KPI Definitions
## Milestone 1 | Infosys Springboard Virtual Internship

---

## Overview

The MedTrack_DV project requires **6 mandatory KPIs** as specified in the project document. Each KPI is defined below with its formula, source dataset, source fields, and interpretation.

---

## KPI 1 – Total Admissions

| Item | Details |
|---|---|
| **Definition** | Total number of distinct patient admissions across the hospital |
| **Formula** | COUNT DISTINCT (admission_id) |
| **Source Dataset** | hospital_overview_dataset.csv |
| **Source Fields** | admission_id |
| **Grain** | One admission = one row |
| **Tableau Calculation** | `COUNTD([Admission Id])` |
| **Target** | Track monthly and yearly trends |
| **Interpretation** | Higher admissions indicate higher patient load; used for capacity planning |

---

## KPI 2 – Occupancy Rate

| Item | Details |
|---|---|
| **Definition** | Percentage of available beds that are currently occupied by patients |
| **Formula** | (Patients Admitted / Available Beds) × 100 |
| **Source Dataset** | resource_utilization_dataset.csv |
| **Source Fields** | patients_admitted, available_beds |
| **Grain** | One row per department per week |
| **Tableau Calculation** | `SUM([Patients Admitted]) / SUM([Available Beds]) * 100` |
| **Target Range** | 75% – 85% is considered optimal |
| **Interpretation** | Below 75% = underutilization; above 90% = overcapacity risk |

---

## KPI 3 – Average Length of Stay (Avg LOS)

| Item | Details |
|---|---|
| **Definition** | Average number of days a patient stays in the hospital from admission to discharge |
| **Formula** | AVG (discharge_date – admission_date) in days |
| **Source Dataset** | hospital_overview_dataset.csv, patient_flow_dataset.csv |
| **Source Fields** | length_of_stay_days |
| **Grain** | One admission = one row |
| **Tableau Calculation** | `AVG([Length Of Stay Days])` |
| **Target** | Lower LOS generally indicates better operational efficiency |
| **Interpretation** | High LOS in certain departments may indicate complexity or discharge delays |

---

## KPI 4 – Readmission Rate

| Item | Details |
|---|---|
| **Definition** | Percentage of patients who are readmitted (or have adverse outcome) out of total eligible patients |
| **Formula** | (Readmitted Patients / Total Eligible Patients) × 100 |
| **Source Dataset** | normalized_readmission.csv |
| **Source Fields** | outcome (DAMA or EXPIRY = readmission risk flag) |
| **Grain** | One patient record = one row |
| **Tableau Calculation** | `SUM([Readmission Flag]) / COUNT([Patient Id]) * 100` |
| **Denominator Definition** | All patients discharged in the selected period |
| **Target** | Industry standard target is below 15% |
| **Interpretation** | High readmission rate may indicate inadequate care or early discharge |

---

## KPI 5 – Bed Utilization Rate

| Item | Details |
|---|---|
| **Definition** | Percentage of total bed capacity that is actively being used |
| **Formula** | (Beds in Use / Total Available Beds) × 100 |
| **Source Dataset** | resource_utilization_dataset.csv, department_analytics_dataset.csv |
| **Source Fields** | patients_admitted, available_beds |
| **Grain** | One row per department per week |
| **Tableau Calculation** | `SUM([Patients Admitted]) / SUM([Available Beds]) * 100` |
| **Target Range** | 70% – 85% is considered healthy utilization |
| **Interpretation** | Above 90% = shortage risk; below 60% = resource wastage |

---

## KPI 6 – Department Efficiency Score

| Item | Details |
|---|---|
| **Definition** | A composite score measuring overall departmental performance on a scale of 0–100 |
| **Formula** | (0.40 × Occupancy Score) + (0.40 × Satisfaction Score) + (0.20 × Staff Morale Score) |
| **Source Dataset** | department_analytics_dataset.csv |
| **Source Fields** | bed_utilization_rate, patient_satisfaction, staff_morale |
| **Grain** | One row per department per week |
| **Tableau Calculation** | `AVG([Department Efficiency Score])` |
| **Scale** | 0 to 100 (higher = better) |

### Component Breakdown

| Component | Weight | Calculation | Source Field |
|---|---|---|---|
| Occupancy Score | 40% | admitted / (admitted + refused) × 100 | patients_admitted, patients_refused |
| Satisfaction Score | 40% | satisfaction / max_satisfaction × 100 | patient_satisfaction |
| Staff Morale Score | 20% | morale / max_morale × 100 | staff_morale |

### Interpretation
| Score Range | Meaning |
|---|---|
| 85 – 100 | Excellent performance |
| 70 – 84 | Good performance |
| 55 – 69 | Average – needs attention |
| Below 55 | Poor – immediate review required |

---

## KPI Summary Table

| # | KPI | Formula | Source | Tableau Field |
|---|---|---|---|---|
| 1 | Total Admissions | COUNT DISTINCT(admission_id) | hospital_overview_dataset.csv | COUNTD([Admission Id]) |
| 2 | Occupancy Rate | Admitted / Available × 100 | resource_utilization_dataset.csv | SUM([Patients Admitted]) / SUM([Available Beds]) * 100 |
| 3 | Avg Length of Stay | AVG(discharge - admission) | hospital_overview_dataset.csv | AVG([Length Of Stay Days]) |
| 4 | Readmission Rate | Readmitted / Total × 100 | normalized_readmission.csv | SUM([Readmission Flag]) / COUNT([Patient Id]) * 100 |
| 5 | Bed Utilization Rate | In Use / Available × 100 | resource_utilization_dataset.csv | SUM([Patients Admitted]) / SUM([Available Beds]) * 100 |
| 6 | Dept Efficiency Score | Composite (0–100) | department_analytics_dataset.csv | AVG([Department Efficiency Score]) |
