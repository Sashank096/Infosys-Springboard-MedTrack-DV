# MedTrack_DV – Power BI DAX Measures
## Milestone 3 | Infosys Springboard Virtual Internship

---

## How to Add These Measures in Power BI

1. Open Power BI Desktop
2. Go to **Home** → **New Measure**
3. Copy and paste each formula below
4. Press Enter to save

---

## Table 1 — Hospital Overview Measures
**Source Table:** hospital_overview_dataset

### Measure 1 – Total Admissions
```DAX
Total Admissions =
DISTINCTCOUNT('hospital_overview_dataset'[admission_id])
```

### Measure 2 – Total Patients
```DAX
Total Patients =
DISTINCTCOUNT('hospital_overview_dataset'[patient_id])
```

### Measure 3 – Average Length of Stay
```DAX
Avg Length of Stay =
AVERAGE('hospital_overview_dataset'[length_of_stay_days])
```

### Measure 4 – Total Male Patients
```DAX
Total Male =
CALCULATE(
    DISTINCTCOUNT('hospital_overview_dataset'[patient_id]),
    'hospital_overview_dataset'[gender] = "Male"
)
```

### Measure 5 – Total Female Patients
```DAX
Total Female =
CALCULATE(
    DISTINCTCOUNT('hospital_overview_dataset'[patient_id]),
    'hospital_overview_dataset'[gender] = "Female"
)
```

### Measure 6 – Total Departments
```DAX
Total Departments =
DISTINCTCOUNT('hospital_overview_dataset'[dept_name])
```

---

## Table 2 — Resource Utilization Measures
**Source Table:** resource_utilization_dataset

### Measure 7 – Occupancy Rate
```DAX
Occupancy Rate % =
DIVIDE(
    SUM('resource_utilization_dataset'[patients_admitted]),
    SUM('resource_utilization_dataset'[available_beds]),
    0
) * 100
```

### Measure 8 – Bed Utilization Rate
```DAX
Bed Utilization Rate % =
DIVIDE(
    SUM('resource_utilization_dataset'[patients_admitted]),
    SUM('resource_utilization_dataset'[available_beds]),
    0
) * 100
```

### Measure 9 – Total Available Beds
```DAX
Total Available Beds =
SUM('resource_utilization_dataset'[available_beds])
```

### Measure 10 – Total Occupied Beds
```DAX
Total Occupied Beds =
SUM('resource_utilization_dataset'[patients_admitted])
```

### Measure 11 – Total Beds Remaining
```DAX
Beds Remaining =
[Total Available Beds] - [Total Occupied Beds]
```

### Measure 12 – Total Patients Refused
```DAX
Total Patients Refused =
SUM('resource_utilization_dataset'[patients_refused])
```

### Measure 13 – Shortage Departments Count
```DAX
Shortage Departments =
CALCULATE(
    DISTINCTCOUNT('resource_utilization_dataset'[service]),
    'resource_utilization_dataset'[shortage_flag] = TRUE()
)
```

### Measure 14 – Staff Utilization Rate
```DAX
Staff Utilization Rate % =
DIVIDE(
    SUM('resource_utilization_dataset'[staff_present]),
    SUM('resource_utilization_dataset'[total_staff]),
    0
) * 100
```

---

## Table 3 — Department Analytics Measures
**Source Table:** department_analytics_dataset

### Measure 15 – Average Efficiency Score
```DAX
Avg Efficiency Score =
AVERAGE('department_analytics_dataset'[department_efficiency_score])
```

### Measure 16 – Average Patient Satisfaction
```DAX
Avg Patient Satisfaction =
AVERAGE('department_analytics_dataset'[patient_satisfaction])
```

### Measure 17 – Average Staff Morale
```DAX
Avg Staff Morale =
AVERAGE('department_analytics_dataset'[staff_morale])
```

### Measure 18 – Department Bed Utilization
```DAX
Dept Bed Utilization % =
AVERAGE('department_analytics_dataset'[bed_utilization_rate])
```

### Measure 19 – Total Admitted by Department
```DAX
Total Dept Admissions =
SUM('department_analytics_dataset'[patients_admitted])
```

### Measure 20 – Total Refused by Department
```DAX
Total Dept Refused =
SUM('department_analytics_dataset'[patients_refused])
```

### Measure 21 – Refusal Rate
```DAX
Refusal Rate % =
DIVIDE(
    SUM('department_analytics_dataset'[patients_refused]),
    SUM('department_analytics_dataset'[patients_admitted]) + SUM('department_analytics_dataset'[patients_refused]),
    0
) * 100
```

---

## Table 4 — Patient Flow Measures
**Source Table:** patient_flow_dataset

### Measure 22 – Readmission Rate
```DAX
Readmission Rate % =
DIVIDE(
    CALCULATE(
        COUNT('normalized_readmission'[patient_id]),
        'normalized_readmission'[readmission_flag] = 1
    ),
    COUNT('normalized_readmission'[patient_id]),
    0
) * 100
```

### Measure 23 – Patient Flow Avg LOS
```DAX
Patient Flow Avg LOS =
AVERAGE('patient_flow_dataset'[length_of_stay_days])
```

### Measure 24 – Total Billing Amount
```DAX
Total Billing Amount =
SUM('patient_flow_dataset'[billing_amount])
```

### Measure 25 – Average Billing Amount
```DAX
Avg Billing Amount =
AVERAGE('patient_flow_dataset'[billing_amount])
```

### Measure 26 – Emergency Admissions
```DAX
Emergency Admissions =
CALCULATE(
    COUNT('patient_flow_dataset'[admission_type]),
    'patient_flow_dataset'[admission_type] = "Emergency"
)
```

### Measure 27 – Elective Admissions
```DAX
Elective Admissions =
CALCULATE(
    COUNT('patient_flow_dataset'[admission_type]),
    'patient_flow_dataset'[admission_type] = "Elective"
)
```

### Measure 28 – Weekend Admissions
```DAX
Weekend Admissions =
CALCULATE(
    COUNT('patient_flow_dataset'[admission_type]),
    'patient_flow_dataset'[is_weekend] = TRUE()
)
```

---

## KPI Color Coding Rules (Conditional Formatting in Power BI)

Use these rules to color KPI cards:

### Occupancy Rate
```DAX
Occupancy Color =
IF([Occupancy Rate %] >= 90, "#E24B4A",
   IF([Occupancy Rate %] >= 75, "#EF9F27",
      "#1D9E75"))
```
- 🔴 Red = Above 90% (overcapacity)
- 🟠 Orange = 75–90% (healthy range)
- 🟢 Green = Below 75% (underutilized)

### Efficiency Score
```DAX
Efficiency Color =
IF([Avg Efficiency Score] >= 85, "#1D9E75",
   IF([Avg Efficiency Score] >= 70, "#EF9F27",
      "#E24B4A"))
```
- 🟢 Green = 85–100 (Excellent)
- 🟠 Orange = 70–84 (Good)
- 🔴 Red = Below 70 (Needs attention)

### Readmission Rate
```DAX
Readmission Color =
IF([Readmission Rate %] >= 20, "#E24B4A",
   IF([Readmission Rate %] >= 15, "#EF9F27",
      "#1D9E75"))
```
- 🟢 Green = Below 15% (Good)
- 🟠 Orange = 15–20% (Watch)
- 🔴 Red = Above 20% (Critical)
