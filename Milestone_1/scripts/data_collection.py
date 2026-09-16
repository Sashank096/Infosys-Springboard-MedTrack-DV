"""
MedTrack_DV – Milestone 1
Script: data_collection.py
Purpose: Document and verify all 4 approved dataset sources
Internship: Infosys Springboard Virtual Internship
"""

import os
import pandas as pd

RAW_PATH = '../data/raw/'

# ============================================================
# APPROVED DATASET SOURCES
# ============================================================

DATASETS = {
    "Dataset 1 – Hospital Management System (CORE)": {
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/mshamoonbutt/hospital-management-system",
        "file": "Hospital_Management_System.xlsx",
        "type": "Excel (Multi-sheet)",
        "purpose": "Core HMIS dataset – Patients, Admissions, Departments, Wards, Beds, Doctors, Nurses",
        "dashboards": ["Hospital Overview", "Patient Flow", "Department Analytics", "Resource Utilization"]
    },
    "Dataset 2 – Hospital Beds Management (RESOURCE)": {
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/jaderz/hospital-beds-management",
        "files": ["beds_patients.csv", "beds_services_weekly.csv", "beds_staff.csv", "beds_staff_schedule.csv"],
        "type": "CSV (4 files)",
        "purpose": "Resource and capacity dataset – Bed allocation, staffing, service demand",
        "dashboards": ["Resource Utilization", "Department Analytics"]
    },
    "Dataset 3 – Hospital Readmission (PATIENT/OUTCOME)": {
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/ashishsahani/hospital-admissions-data",
        "files": ["readmission_admission_data.csv", "readmission_mortality_data.csv"],
        "type": "CSV (2 files)",
        "purpose": "Patient readmission and outcomes – LOS, discharge status, readmission rate",
        "dashboards": ["Patient Flow", "Hospital Overview"]
    },
    "Dataset 4 – Healthcare Dataset (INPATIENT)": {
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/prasad22/healthcare-dataset",
        "file": "healthcare_dataset.csv",
        "type": "CSV (1 file)",
        "purpose": "Inpatient records – Admissions, discharges, billing, doctor, hospital",
        "dashboards": ["Hospital Overview", "Patient Flow"]
    }
}


def verify_files():
    """Verify all raw data files are present"""
    print("=" * 60)
    print("MEDTRACK_DV – DATA COLLECTION VERIFICATION")
    print("=" * 60)

    expected_files = [
        "Hospital_Management_System.xlsx",
        "beds_patients.csv",
        "beds_services_weekly.csv",
        "beds_staff.csv",
        "beds_staff_schedule.csv",
        "readmission_admission_data.csv",
        "readmission_mortality_data.csv",
        "healthcare_dataset.csv"
    ]

    all_present = True
    for fname in expected_files:
        fpath = os.path.join(RAW_PATH, fname)
        exists = os.path.exists(fpath)
        status = "✅" if exists else "❌ MISSING"
        print(f"  {status} {fname}")
        if not exists:
            all_present = False

    print()
    if all_present:
        print("✅ All raw data files are present!")
    else:
        print("❌ Some files are missing. Please download and place them in data/raw/")

    return all_present


def print_dataset_info():
    """Print dataset source information"""
    print("\n" + "=" * 60)
    print("APPROVED DATASET SOURCES")
    print("=" * 60)
    for name, info in DATASETS.items():
        print(f"\n{name}")
        print(f"  Source:   {info['source']}")
        print(f"  URL:      {info['url']}")
        print(f"  Purpose:  {info['purpose']}")
        print(f"  Used for: {', '.join(info['dashboards'])}")


def get_basic_stats():
    """Load and print basic stats of all raw files"""
    print("\n" + "=" * 60)
    print("RAW DATASET STATISTICS")
    print("=" * 60)

    # Dataset 1
    try:
        xl = pd.read_excel(RAW_PATH + 'Hospital_Management_System.xlsx', sheet_name=None)
        total_rows = sum(df.shape[0] for df in xl.values())
        print(f"\nDataset 1 – HMIS: {len(xl)} sheets | {total_rows:,} total rows")
        for sheet, df in xl.items():
            print(f"    {sheet}: {df.shape[0]} rows x {df.shape[1]} cols")
    except Exception as e:
        print(f"Dataset 1 error: {e}")

    # Dataset 2
    for fname in ['beds_patients.csv', 'beds_services_weekly.csv', 'beds_staff.csv', 'beds_staff_schedule.csv']:
        try:
            df = pd.read_csv(RAW_PATH + fname)
            print(f"\nDataset 2 – {fname}: {df.shape[0]:,} rows x {df.shape[1]} cols")
        except Exception as e:
            print(f"{fname} error: {e}")

    # Dataset 3
    for fname in ['readmission_admission_data.csv', 'readmission_mortality_data.csv']:
        try:
            df = pd.read_csv(RAW_PATH + fname)
            print(f"\nDataset 3 – {fname}: {df.shape[0]:,} rows x {df.shape[1]} cols")
        except Exception as e:
            print(f"{fname} error: {e}")

    # Dataset 4
    try:
        df = pd.read_csv(RAW_PATH + 'healthcare_dataset.csv')
        print(f"\nDataset 4 – healthcare_dataset.csv: {df.shape[0]:,} rows x {df.shape[1]} cols")
    except Exception as e:
        print(f"Dataset 4 error: {e}")


if __name__ == '__main__':
    print_dataset_info()
    verify_files()
    get_basic_stats()
    print("\n✅ Data collection script complete!")
