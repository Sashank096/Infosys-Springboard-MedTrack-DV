# Milestone 1 – Data Preparation
## MedTrack_DV | Hospital Operations & Patient Analytics Dashboard
### Infosys Springboard Virtual Internship

---

## Objective

Milestone 1 covers the complete data preparation phase of the MedTrack_DV project. This includes dataset selection, data collection, data profiling, cleaning, normalization, validation, and KPI engineering. The output is 4 final analytical datasets ready for Tableau dashboard development in Milestone 2.

---

## Milestone 1 Checklist

| Task | Status |
|---|---|
| ✅ Dataset selection and justification | Complete |
| ✅ Data collection from Kaggle | Complete |
| ✅ Data profiling (shape, dtypes, nulls, duplicates) | Complete |
| ✅ Data cleaning (duplicates, missing values, outliers) | Complete |
| ✅ ID standardization (patient, dept, ward, bed) | Complete |
| ✅ Department name standardization | Complete |
| ✅ Date format standardization | Complete |
| ✅ Gender and categorical value standardization | Complete |
| ✅ Dataset validation and mapping sheet | Complete |
| ✅ 4 final analytical datasets created | Complete |
| ✅ 6 KPIs calculated and documented | Complete |
| ✅ Data dictionary created | Complete |
| ✅ Dataset sources documented | Complete |

---

## Folder Structure

```
Milestone_1/
│
├── data/
│   ├── raw/                              ← Original downloaded datasets (DO NOT MODIFY)
│   │   ├── Hospital_Management_System.xlsx
│   │   ├── beds_patients.csv
│   │   ├── beds_services_weekly.csv
│   │   ├── beds_staff.csv
│   │   ├── beds_staff_schedule.csv
│   │   ├── readmission_admission_data.csv
│   │   ├── readmission_mortality_data.csv
│   │   └── healthcare_dataset.csv
│   │
│   └── processed/                        ← Cleaned and final datasets
│       ├── normalized_patients.csv
│       ├── normalized_bed_records.csv
│       ├── normalized_departments.csv
│       ├── normalized_doctors.csv
│       ├── normalized_nurses.csv
│       ├── normalized_wards.csv
│       ├── normalized_beds.csv
│       ├── normalized_staff_shifts.csv
│       ├── normalized_beds_patients.csv
│       ├── normalized_beds_services.csv
│       ├── normalized_readmission.csv
│       ├── normalized_healthcare.csv
│       ├── hospital_overview_dataset.csv       ← Final → Tableau Dashboard 1
│       ├── patient_flow_dataset.csv            ← Final → Tableau Dashboard 2
│       ├── department_analytics_dataset.csv    ← Final → Tableau Dashboard 3
│       └── resource_utilization_dataset.csv    ← Final → Tableau Dashboard 4
│
├── notebooks/
│   ├── 01_data_loading.ipynb             ← Load and inspect all 4 datasets
│   ├── 02_data_cleaning.ipynb            ← Remove duplicates, fix nulls, fix types
│   ├── 03_data_normalization.ipynb       ← Standardize IDs, names, dates, categories
│   ├── 04_data_validation.ipynb          ← Validate keys, relationships, quality targets
│   └── 05_kpi_engineering.ipynb          ← Calculate 6 KPIs, build 4 final datasets
│
├── scripts/
│   ├── data_collection.py                ← Dataset sources, file verification
│   └── generate_hospital_kpis.py         ← Full ETL pipeline and KPI calculation
│
├── docs/
│   ├── dataset_sources.md                ← All 4 Kaggle sources documented
│   ├── data_dictionary.md                ← Column definitions for all final datasets
│   ├── kpi_definitions.md                ← Formulas, sources, and interpretation
│   └── dataset_validation_mapping.md     ← Field-level validation and mapping
│
└── README.md                             ← This file
```

---

## Approved Datasets

| # | Dataset | Source | Role |
|---|---|---|---|
| 1 | Hospital Management System | [Kaggle](https://www.kaggle.com/datasets/mshamoonbutt/hospital-management-system) | CORE / HMIS |
| 2 | Hospital Beds Management | [Kaggle](https://www.kaggle.com/datasets/jaderz/hospital-beds-management) | RESOURCE |
| 3 | Hospital Readmission Data | [Kaggle](https://www.kaggle.com/datasets/ashishsahani/hospital-admissions-data) | PATIENT / OUTCOME |
| 4 | Healthcare Dataset | [Kaggle](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) | INPATIENT / DISCHARGE |

---

## 6 Mandatory KPIs

| # | KPI | Formula | Source Dataset |
|---|---|---|---|
| 1 | Total Admissions | COUNT DISTINCT (admission_id) | hospital_overview_dataset.csv |
| 2 | Occupancy Rate | Admitted / Available Beds × 100 | resource_utilization_dataset.csv |
| 3 | Average Length of Stay | AVG (discharge_date – admission_date) | hospital_overview_dataset.csv |
| 4 | Readmission Rate | Readmitted / Total Patients × 100 | normalized_readmission.csv |
| 5 | Bed Utilization Rate | Beds in Use / Available Beds × 100 | resource_utilization_dataset.csv |
| 6 | Department Efficiency Score | 40% Occupancy + 40% Satisfaction + 20% Staff Morale | department_analytics_dataset.csv |

---

## Final Analytical Datasets (for Tableau)

| File | Grain | Dashboard |
|---|---|---|
| hospital_overview_dataset.csv | One row = One admission | Dashboard 1 – Hospital Overview |
| patient_flow_dataset.csv | One row = One patient event | Dashboard 2 – Patient Flow |
| department_analytics_dataset.csv | One row = One dept per week | Dashboard 3 – Department Analytics |
| resource_utilization_dataset.csv | One row = One dept per week (resource) | Dashboard 4 – Resource Utilization |

---

## How to Run

### Step 1 – Run Notebooks in Order
```
01_data_loading.ipynb
02_data_cleaning.ipynb
03_data_normalization.ipynb
04_data_validation.ipynb
05_kpi_engineering.ipynb
```

### Step 2 – Or Run the Full Pipeline Script
```bash
cd scripts/
python generate_hospital_kpis.py
```

### Requirements
```bash
pip install pandas numpy openpyxl
```

---

## Data Flow

```
RAW DATA (data/raw/)
        ↓
01_data_loading.ipynb      → Load & inspect
        ↓
02_data_cleaning.ipynb     → Remove duplicates, fix nulls, fix types
        ↓
03_data_normalization.ipynb → Standardize IDs, names, dates
        ↓
04_data_validation.ipynb   → Validate keys, relationships, quality
        ↓
05_kpi_engineering.ipynb   → Calculate KPIs, build 4 final datasets
        ↓
PROCESSED DATA (data/processed/)
        ↓
    TABLEAU (Milestone 2 & 3)
```

---

## Data Quality Results

| Target | Requirement | Result |
|---|---|---|
| Dataset Completeness | > 95% | ✅ Achieved |
| Missing Values After Cleaning | < 2% | ✅ Achieved |
| Duplicate Records | 0 | ✅ Removed |
| Primary Key Uniqueness | 100% | ✅ Validated |
| Foreign Key Match Rate | > 95% | ✅ Validated |

---

## Next Step → Milestone 2

Milestone 2 covers KPI validation, dashboard storyboarding, Tableau data model creation, and initial dashboard prototyping.
