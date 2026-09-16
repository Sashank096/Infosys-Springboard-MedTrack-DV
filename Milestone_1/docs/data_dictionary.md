# MedTrack_DV – Data Dictionary
## Milestone 1 | Infosys Springboard Virtual Internship

---

## Final Analytical Datasets

These 4 datasets are the final output of Milestone 1 and are used directly in Tableau.

---

## 1. hospital_overview_dataset.csv
**Grain:** One row = One patient admission  
**Source:** HMIS BedRecords + Patients + Ward + Department

| Column | Type | Description | Example |
|---|---|---|---|
| admission_id | String | Unique admission identifier | ADM00001 |
| patient_id | String | Unique patient identifier | P001 |
| full_name | String | Patient full name | John Smith |
| gender | String | Patient gender (Male/Female/Unknown) | Male |
| date_of_birth | Date | Patient date of birth | 1985-06-15 |
| admission_date | Date | Date of hospital admission | 2023-01-10 |
| discharge_date | Date | Date of discharge | 2023-01-15 |
| length_of_stay_days | Integer | Days between admission and discharge | 5 |
| bed_no | String | Assigned bed number | B101 |
| ward_no | String | Ward number | W01 |
| ward_name | String | Ward name | General Ward |
| dept_id | String | Department identifier | D001 |
| dept_name | String | Department name | Cardiology |
| mode_of_payment | String | Payment method | Insurance |
| hospital_id | String | Hospital identifier | H001 |
| hospital_name | String | Hospital name | MedTrack General Hospital |
| admission_year | Integer | Year of admission | 2023 |
| admission_month | Integer | Month number of admission | 1 |
| admission_month_name | String | Month name of admission | January |
| admission_quarter | Integer | Quarter of admission | 1 |
| day_of_week | String | Day of week of admission | Tuesday |

---

## 2. patient_flow_dataset.csv
**Grain:** One row = One patient admission/movement event  
**Source:** Healthcare Dataset (Dataset 4)

| Column | Type | Description | Example |
|---|---|---|---|
| name | String | Patient name | Jane Doe |
| age | Integer | Patient age at admission | 45 |
| gender | String | Patient gender | Female |
| medical_condition | String | Primary diagnosis | Diabetes |
| date_of_admission | Date | Admission date | 2023-03-12 |
| discharge_date | Date | Discharge date | 2023-03-18 |
| admission_type | String | Type of admission | Emergency / Elective / OPD |
| hospital | String | Hospital name | City Medical Center |
| doctor | String | Attending doctor | Dr. Alice Brown |
| billing_amount | Float | Total billing amount | 12500.00 |
| length_of_stay_days | Integer | Length of hospital stay | 6 |
| admission_year | Integer | Year of admission | 2023 |
| admission_month | String | Month name | March |
| test_results | String | Test result outcome | Normal / Abnormal / Inconclusive |
| day_of_week | String | Day of admission | Sunday |
| admission_quarter | Integer | Quarter | 1 |
| is_weekend | Boolean | Whether admission was on weekend | True |

---

## 3. department_analytics_dataset.csv
**Grain:** One row = One department per week  
**Source:** Beds Services Weekly + Department Efficiency Scores

| Column | Type | Description | Example |
|---|---|---|---|
| week | Integer | Week number | 1 |
| month | String | Month name | January |
| service | String | Department / Service name | Cardiology |
| available_beds | Integer | Total beds available | 20 |
| patients_admitted | Integer | Patients admitted that week | 15 |
| patients_refused | Integer | Patients refused due to capacity | 2 |
| patient_satisfaction | Float | Average satisfaction score | 7.8 |
| staff_morale | Float | Average staff morale score | 7.2 |
| event | String | Notable event during that week | None |
| hospital_id | String | Hospital identifier | H001 |
| hospital_name | String | Hospital name | MedTrack General Hospital |
| bed_utilization_rate | Float | % beds in use | 75.00 |
| refusal_rate | Float | % patients refused | 11.76 |
| occupancy_score | Float | Occupancy component of efficiency | 88.24 |
| satisfaction_score | Float | Satisfaction component (0–100) | 82.50 |
| department_efficiency_score | Float | Composite efficiency score (0–100) | 85.10 |

---

## 4. resource_utilization_dataset.csv
**Grain:** One row = One department per week (resource focus)  
**Source:** Beds Services + Staff Schedule

| Column | Type | Description | Example |
|---|---|---|---|
| week | Integer | Week number | 1 |
| month | String | Month name | January |
| service | String | Department / Service name | ICU |
| available_beds | Integer | Total available beds | 10 |
| patients_admitted | Integer | Patients occupying beds | 9 |
| patients_refused | Integer | Patients turned away | 1 |
| patient_satisfaction | Float | Average satisfaction score | 8.1 |
| staff_morale | Float | Average staff morale | 7.5 |
| total_staff | Integer | Total staff assigned | 12 |
| staff_present | Integer | Staff who were present | 10 |
| hospital_id | String | Hospital identifier | H001 |
| hospital_name | String | Hospital name | MedTrack General Hospital |
| bed_utilization_pct | Float | % beds utilized | 90.00 |
| staff_utilization_pct | Float | % staff present | 83.33 |
| shortage_flag | Boolean | True if patients were refused | True |

---

## Normalized Supporting Tables (from HMIS)

### normalized_patients.csv
| Column | Type | Description |
|---|---|---|
| patient_id | String | Unique patient ID |
| fname | String | First name |
| lname | String | Last name |
| full_name | String | Full name (derived) |
| gender | String | Gender (Male/Female/Unknown) |
| date_of_birth | Date | Date of birth |

### normalized_departments.csv
| Column | Type | Description |
|---|---|---|
| dept_id | String | Department ID |
| dept_name | String | Standardized department name |

### normalized_wards.csv
| Column | Type | Description |
|---|---|---|
| ward_no | String | Ward number |
| ward_name | String | Ward name |
| dept_id | String | Linked department ID |

### normalized_doctors.csv
| Column | Type | Description |
|---|---|---|
| doct_id | String | Doctor ID |
| full_name | String | Doctor full name |
| gender | String | Gender |
| surgeon_type | String | Specialization |
| dept_id | String | Linked department ID |

---

## Standardization Rules Applied

| Field | Standardization Rule |
|---|---|
| Gender | M/Male → Male, F/Female → Female, others → Unknown |
| Department Names | ER/Emergency Room → Emergency Department, ICU/Intensive Care → ICU |
| Admission Types | Emergency/OPD/Elective/Urgent standardized |
| Date Formats | All dates converted to YYYY-MM-DD using pd.to_datetime() |
| Text Fields | .strip().title() applied to all name/category columns |
| IDs | .strip().lower() applied, surrogate IDs created where missing |
| Hospital ID | H001 assigned to all HMIS records |
