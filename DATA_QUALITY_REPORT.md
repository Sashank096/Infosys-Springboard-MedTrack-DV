# Data Quality Report — MedTrack_DV

## hospital_operations_cleaned.csv
- Rows: 45000
- Columns: 20
- Duplicate rows: 0
- Missing values (%):
```
admission_id           0.0
patient_id             0.0
hospital_id            0.0
hospital_name          0.0
department_id          0.0
department_name        0.0
ward_id                0.0
ward_name              0.0
bed_id                 0.0
admission_date         0.0
discharge_date         0.0
admission_type         0.0
length_of_stay_days    0.0
patient_age            0.0
patient_gender         0.0
disease_name           0.0
disease_category       0.0
treatment_cost         0.0
payment_status         0.0
readmission_flag       0.0
```

## patient_admissions_cleaned.csv
- Rows: 45000
- Columns: 15
- Duplicate rows: 0
- Missing values (%):
```
admission_id           0.0
patient_id             0.0
hospital_id            0.0
department_id          0.0
department_name        0.0
ward_id                0.0
ward_name              0.0
bed_id                 0.0
admission_date         0.0
discharge_date         0.0
admission_type         0.0
length_of_stay_days    0.0
year                   0.0
month                  0.0
day_of_week            0.0
```

## department_data_cleaned.csv
- Rows: 12474
- Columns: 12
- Duplicate rows: 0
- Missing values (%):
```
hospital_id                    0.0
department_id                  0.0
department_name                0.0
date                           0.0
patients_admitted_count        0.0
readmission_count              0.0
avg_length_of_stay_days        0.0
avg_treatment_cost             0.0
readmission_rate_pct           0.0
patients_discharged_count      0.0
total_staff_in_department      0.0
department_efficiency_score    0.0
```

## resource_utilization_cleaned.csv
- Rows: 13138
- Columns: 9
- Duplicate rows: 0
- Missing values (%):
```
hospital_id           0.00
department_id         0.00
department_name       0.00
date                  0.05
resource_type         0.00
units_in_use          0.00
total_capacity        0.05
occupancy_rate_pct    0.05
note                  0.00
```
