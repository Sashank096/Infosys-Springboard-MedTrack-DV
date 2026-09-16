# MedTrack_DV – Tableau Data Model
## Milestone 2 | Infosys Springboard Virtual Internship

---

## Overview

This document explains exactly how to load the 4 final datasets into Tableau and how to connect them correctly. The most important rule from the mentor's document is:

> **Do NOT join all 4 datasets into one flat table. Use Tableau Relationships to preserve grain integrity.**

---

## Step 1 – Load the 4 Final Datasets into Tableau

Open Tableau Desktop → Connect → Text File (CSV)

Load these 4 files from `Milestone_1/data/processed/`:

| # | File | Grain |
|---|---|---|
| 1 | hospital_overview_dataset.csv | One row = One admission |
| 2 | patient_flow_dataset.csv | One row = One patient event |
| 3 | department_analytics_dataset.csv | One row = One dept per week |
| 4 | resource_utilization_dataset.csv | One row = One dept per week |

---

## Step 2 – Understand Why We Use Relationships (NOT Joins)

The 4 datasets have **different grains** (different levels of detail):

```
hospital_overview_dataset   → admission level (1000+ rows)
patient_flow_dataset        → patient level  (55,500 rows)
department_analytics_dataset → weekly dept   (208 rows)
resource_utilization_dataset → weekly dept   (208 rows)
```

If you do a direct JOIN between admission-level and weekly-level data, Tableau will **multiply rows** and give wrong totals. This is called a **fan-out problem**.

**Solution:** Use Tableau **Relationships** (the default in Tableau 2020.2+), not Joins.

---

## Step 3 – Data Model Structure in Tableau

In Tableau's Data Source tab, set up relationships like this:

```
┌─────────────────────────────────┐
│   hospital_overview_dataset     │  ← Primary table
│   (admission level)             │
└────────────┬────────────────────┘
             │
             │ dept_name = service
             │
      ┌──────┴──────────────────────┐
      │  department_analytics_dataset│
      │  (weekly dept level)         │
      └──────┬──────────────────────┘
             │
             │ service = service
             │ week = week
             │
      ┌──────┴──────────────────────┐
      │  resource_utilization_dataset│
      │  (weekly dept level)         │
      └─────────────────────────────┘

┌─────────────────────────────────┐
│   patient_flow_dataset          │  ← Separate logical table
│   (patient level)               │    (different grain – do not
└─────────────────────────────────┘     join to the above)
```

**patient_flow_dataset** is kept as a **separate logical table** because it has a completely different grain (patient-level) compared to the weekly department tables.

---

## Step 4 – How to Create Relationships in Tableau

1. Open Tableau Desktop
2. Click **Data** → **New Data Source**
3. Connect to `hospital_overview_dataset.csv` → drag it to the canvas
4. Drag `department_analytics_dataset.csv` next to it
5. Tableau will ask you to define the relationship field:
   - From hospital_overview: `dept_name`
   - From department_analytics: `service`
   - Click OK
6. Drag `resource_utilization_dataset.csv` next to department_analytics
7. Define relationship:
   - From department_analytics: `service`
   - From resource_utilization: `service`
   - Click OK
8. Create a **second data source** for `patient_flow_dataset.csv` (separate)

---

## Step 5 – Field Mapping Table

These fields link the datasets together:

| Field in hospital_overview | Field in department_analytics | Notes |
|---|---|---|
| dept_name | service | Department name |
| hospital_name | hospital_name | Hospital name |
| admission_month_name | month | Month name |

| Field in department_analytics | Field in resource_utilization | Notes |
|---|---|---|
| service | service | Department name |
| week | week | Week number |
| hospital_name | hospital_name | Hospital name |

---

## Step 6 – Rename Fields in Tableau (For Clarity)

After loading, rename these fields in Tableau for cleaner dashboard labels:

| Original Field | Rename To |
|---|---|
| patients_admitted | Patients Admitted |
| available_beds | Available Beds |
| patients_refused | Patients Refused |
| bed_utilization_pct | Bed Utilization % |
| department_efficiency_score | Efficiency Score |
| length_of_stay_days | Length of Stay (Days) |
| admission_month_name | Month |
| patient_satisfaction | Patient Satisfaction Score |
| staff_morale | Staff Morale Score |
| shortage_flag | Shortage Flag |

---

## Step 7 – Create Calculated Fields in Tableau

Create these calculated fields in Tableau after loading data:

### Occupancy Rate
```
SUM([Patients Admitted]) / SUM([Available Beds]) * 100
```

### Avg Length of Stay
```
AVG([Length Of Stay Days])
```

### Readmission Rate
```
SUM([Readmission Flag]) / COUNTD([Patient Id]) * 100
```

### Bed Utilization Rate
```
SUM([Patients Admitted]) / SUM([Available Beds]) * 100
```

### Shortage Count
```
COUNTD(IF [Shortage Flag] = TRUE THEN [Service] END)
```

### Occupied Beds
```
SUM([Available Beds]) - (SUM([Available Beds]) - SUM([Patients Admitted]))
```

### Available Beds Remaining
```
SUM([Available Beds]) - SUM([Patients Admitted])
```

---

## Step 8 – Data Model Validation Checklist

Before building dashboards, verify these in Tableau:

| Check | How to Verify | Expected |
|---|---|---|
| Total Admissions | Drag admission_id to Text, use COUNTD | 56,500 |
| Total Depts | Drag service to Text, use COUNTD | 4 |
| Occupancy Rate | Calculated field | 92.7% |
| No row multiplication | Check row count after relationship | Same as CSV |
| Avg LOS | Drag length_of_stay_days to Text, use AVG | ~5.13 (HMIS) |
| Bed Utilization | Calculated field | 92.7% |

---

## Common Mistakes to Avoid

| Mistake | Why It's Wrong | Correct Approach |
|---|---|---|
| Creating a flat JOIN across all 4 tables | Causes row multiplication and wrong totals | Use Relationships |
| Joining patient_flow with hospital_overview | Different grain → wrong counts | Keep as separate data source |
| Using SUM instead of AVG for LOS | Gives total days, not average | Use AVG([Length Of Stay Days]) |
| Counting rows instead of COUNTD for admissions | Counts duplicates | Use COUNTD([Admission Id]) |
| Naming fields the same across datasets | Tableau may merge them incorrectly | Use unique, clear field names |
