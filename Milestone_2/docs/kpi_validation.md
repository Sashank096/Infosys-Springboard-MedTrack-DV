# MedTrack_DV – KPI Validation Report
## Milestone 2 | Infosys Springboard Virtual Internship

---

## Purpose

This document validates all 6 mandatory KPIs by calculating them in Python (Pandas) and cross-checking them against Tableau. Every KPI formula is documented with its source fields and actual calculated values.

---

## KPI 1 – Total Admissions

| Item | Details |
|---|---|
| **Formula** | COUNT DISTINCT (admission_id) across all datasets |
| **Source** | HMIS BedRecords + Healthcare Dataset |
| **Python Value** | **56,500** |
| **Breakdown** | HMIS BedRecords: 1,000 admissions + Healthcare Dataset: 55,500 admissions |
| **Tableau Value** | _(fill after building dashboard)_ |
| **Match** | _(fill after verifying)_ |

**Python Calculation:**
```python
kpi1 = df_bed_records['admission_id'].nunique() + len(df_healthcare)
# Result: 1000 + 55500 = 56,500
```

---

## KPI 2 – Occupancy Rate

| Item | Details |
|---|---|
| **Formula** | (Total Patients Admitted / Total Available Beds) × 100 |
| **Source** | beds_services_weekly.csv |
| **Source Fields** | patients_admitted, available_beds |
| **Python Value** | **92.7%** |
| **Interpretation** | ⚠️ Above 90% — Hospital is operating at near-full capacity. Shortage risk exists. |
| **Tableau Value** | _(fill after building dashboard)_ |
| **Match** | _(fill after verifying)_ |

**Python Calculation:**
```python
occ = df_beds_services['patients_admitted'].sum() / df_beds_services['available_beds'].sum() * 100
# Result: 92.7%
```

**Department-wise Occupancy:**
| Department | Admitted | Refused | Available Beds (avg) | Occupancy |
|---|---|---|---|---|
| ICU | 648 | 141 | 14.8 | 82.1% |
| Emergency | 1,185 | 5,008 | 22.8 | 19.1% |
| General Medicine | 2,332 | 1,938 | 46.2 | 54.6% |
| Surgery | 1,686 | 555 | 37.5 | 75.2% |

---

## KPI 3 – Average Length of Stay

| Item | Details |
|---|---|
| **Formula** | AVG (discharge_date – admission_date) in days |
| **Source** | HMIS BedRecords, Readmission Dataset, Healthcare Dataset |
| **Python Value (HMIS)** | **5.13 days** |
| **Python Value (Healthcare)** | **15.51 days** |
| **Python Value (Readmission)** | **6.42 days** |
| **Tableau Value** | _(fill after building dashboard)_ |
| **Match** | _(fill after verifying)_ |

**Python Calculation:**
```python
avg_los_hmis = df_bed_records['length_of_stay_days'].mean()  # 5.13 days
avg_los_hc   = df_healthcare['length_of_stay_days'].mean()   # 15.51 days
avg_los_re   = df_readmission['duration_of_stay'].mean()     # 6.42 days
```

**LOS by Medical Condition (Healthcare Dataset):**
| Condition | Avg LOS (days) |
|---|---|
| Arthritis | 15.52 |
| Asthma | 15.70 |
| Cancer | 15.50 |
| Diabetes | 15.42 |
| Hypertension | 15.46 |
| Obesity | 15.46 |

---

## KPI 4 – Readmission Rate

| Item | Details |
|---|---|
| **Formula** | (Readmitted Patients / Total Eligible Patients) × 100 |
| **Source** | readmission_admission_data.csv |
| **Readmission Definition** | Outcome = DAMA (Discharged Against Medical Advice) or EXPIRY |
| **Total Patients** | 15,757 |
| **Readmitted Patients** | 2,001 |
| **Python Value** | **12.7%** |
| **Interpretation** | ✅ Below 15% industry benchmark — acceptable readmission rate |
| **Tableau Value** | _(fill after building dashboard)_ |
| **Match** | _(fill after verifying)_ |

**Python Calculation:**
```python
readmitted    = df_readmission['outcome'].str.upper().isin(['DAMA','EXPIRY']).sum()
readm_rate    = readmitted / len(df_readmission) * 100
# Result: 2001 / 15757 * 100 = 12.7%
```

---

## KPI 5 – Bed Utilization Rate

| Item | Details |
|---|---|
| **Formula** | (Beds in Use / Total Available Beds) × 100 |
| **Source** | beds_services_weekly.csv |
| **Source Fields** | patients_admitted, available_beds |
| **Python Value** | **92.7%** |
| **Total Beds (HMIS)** | 500 beds |
| **Interpretation** | ⚠️ Very high utilization — capacity planning needed |
| **Tableau Value** | _(fill after building dashboard)_ |
| **Match** | _(fill after verifying)_ |

**Department-wise Bed Utilization:**
| Department | Admitted | Available | Utilization |
|---|---|---|---|
| ICU | 648 | 789 total | 82.1% |
| Emergency | 1,185 | 6,193 total | 19.1% |
| General Medicine | 2,332 | 4,270 total | 54.6% |
| Surgery | 1,686 | 2,241 total | 75.2% |

---

## KPI 6 – Department Efficiency Score

| Item | Details |
|---|---|
| **Formula** | (40% × Occupancy Score) + (40% × Satisfaction Score) + (20% × Staff Morale Score) |
| **Source** | beds_services_weekly.csv |
| **Scale** | 0 to 100 |
| **Tableau Value** | _(fill after building dashboard)_ |

**Calculated Scores by Department:**
| Department | Occupancy Score | Satisfaction Score | Staff Morale Score | **Efficiency Score** |
|---|---|---|---|---|
| ICU | 82.13 | 100.00 | 96.50 | **92.15** ✅ Excellent |
| Surgery | 75.23 | 97.13 | 98.75 | **88.69** ✅ Excellent |
| General Medicine | 54.61 | 99.53 | 99.37 | **81.53** ✅ Good |
| Emergency | 19.13 | 95.43 | 100.00 | **65.82** ⚠️ Average |

**Python Calculation:**
```python
dept_eff['eff_score'] = (
    0.40 * dept_eff['occ_score'] +
    0.40 * dept_eff['sat_score']  +
    0.20 * dept_eff['staff_score']
)
```

---

## Admission Type Distribution

| Type | Count | Percentage |
|---|---|---|
| Elective | 18,655 | 33.6% |
| Urgent | 18,576 | 33.5% |
| Emergency | 18,269 | 32.9% |

---

## Complete KPI Summary

| # | KPI | Value | Status |
|---|---|---|---|
| 1 | Total Admissions | **56,500** | ✅ Calculated |
| 2 | Occupancy Rate | **92.7%** | ✅ Calculated |
| 3 | Average Length of Stay | **5.13 days (HMIS) / 15.51 days (Healthcare)** | ✅ Calculated |
| 4 | Readmission Rate | **12.7%** | ✅ Calculated |
| 5 | Bed Utilization Rate | **92.7%** | ✅ Calculated |
| 6 | Department Efficiency Score | **ICU: 92.15 / Surgery: 88.69 / Gen Med: 81.53 / Emergency: 65.82** | ✅ Calculated |

---

## Tableau Cross-Check Table
_(Fill this in after building Tableau dashboards)_

| KPI | Python Value | Tableau Value | Difference | Match? |
|---|---|---|---|---|
| Total Admissions | 56,500 | | | |
| Occupancy Rate | 92.7% | | | |
| Avg LOS (HMIS) | 5.13 days | | | |
| Readmission Rate | 12.7% | | | |
| Bed Utilization | 92.7% | | | |
| ICU Efficiency Score | 92.15 | | | |
| Surgery Efficiency Score | 88.69 | | | |
| Gen Med Efficiency Score | 81.53 | | | |
| Emergency Efficiency Score | 65.82 | | | |
