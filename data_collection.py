"""
data_collection.py
-------------------
MedTrack_DV — Milestone 1: Data Collection and Preparation

This script LOADS the four synthetic raw datasets (already generated
separately by scripts/generate_synthetic_data.py), VALIDATES their
structure, and EXPORTS the raw/integrated data required for the
downstream cleaning workflow (hospital_cleaning.ipynb).

This script does NOT generate synthetic data. It only collects,
validates, and prepares what already exists in data/raw/.

Data policy: all datasets used here are SYNTHETIC datasets generated for
educational and internship project development purposes. They do not
represent real patient records or confidential healthcare information.

Outputs:
    - data/raw/hospital_raw_data.csv   (integrated/concatenated raw export,
      required Milestone 1 deliverable)
    - Console validation report

Usage:
    python data_collection.py
"""

import os
import sys
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

REQUIRED_FILES = {
    "hospital_operations.csv": [
        "Hospital_ID", "Hospital_Name", "Date", "Total_Beds", "Occupied_Beds",
        "Available_Beds", "Total_Admissions", "Total_Discharges",
        "Emergency_Admissions", "Outpatient_Visits",
    ],
    "patient_admissions.csv": [
        "Patient_ID", "Hospital_ID", "Department_ID", "Admission_Date",
        "Discharge_Date", "Admission_Type", "Diagnosis", "Treatment_Type",
        "Length_of_Stay", "Readmission_Flag", "Patient_Status",
    ],
    "department_data.csv": [
        "Hospital_ID", "Department_ID", "Department_Name", "Department_Type",
        "Department_Capacity", "Staff_Count", "Doctors_Count", "Nurses_Count",
        "Monthly_Target", "Department_Status",
    ],
    "resource_utilization.csv": [
        "Hospital_ID", "Department_ID", "Date", "Total_Beds", "Occupied_Beds",
        "Available_Beds", "Equipment_Count", "Equipment_In_Use",
        "Staff_Available", "Staff_Allocated", "Resource_Status",
    ],
}

MASTER_HOSPITAL_IDS = {f"H{str(i).zfill(3)}" for i in range(1, 8)}
MASTER_DEPARTMENT_IDS = {f"D{str(i).zfill(3)}" for i in range(1, 11)}


def load_datasets():
    """Load the four raw CSV files into a dict of DataFrames."""
    datasets = {}
    for filename in REQUIRED_FILES:
        path = os.path.join(RAW_DIR, filename)
        if not os.path.exists(path):
            print(f"[ERROR] Missing required raw file: {filename}")
            sys.exit(1)
        datasets[filename] = pd.read_csv(path)
    return datasets


def validate_structure(datasets):
    """Check that each dataset has the required columns."""
    print("\n--- Structure Validation ---")
    all_ok = True
    for filename, required_cols in REQUIRED_FILES.items():
        df = datasets[filename]
        missing_cols = set(required_cols) - set(df.columns)
        status = "OK" if not missing_cols else f"MISSING COLUMNS: {missing_cols}"
        if missing_cols:
            all_ok = False
        print(f"  {filename}: {status}  (rows={len(df)}, cols={len(df.columns)})")
    return all_ok


def check_missing_values(datasets):
    """Report missing value counts/percentages per dataset."""
    print("\n--- Missing Value Check ---")
    for filename, df in datasets.items():
        total_cells = df.shape[0] * df.shape[1]
        missing_cells = df.isna().sum().sum()
        pct = (missing_cells / total_cells * 100) if total_cells else 0
        print(f"  {filename}: {missing_cells} missing cells ({pct:.2f}%)")


def check_duplicates(datasets):
    """Report duplicate row counts per dataset."""
    print("\n--- Duplicate Check ---")
    for filename, df in datasets.items():
        dup_count = df.duplicated().sum()
        print(f"  {filename}: {dup_count} duplicate rows")


def validate_keys(datasets):
    """Validate Hospital_ID / Department_ID / Patient_ID against master lists."""
    print("\n--- Key Validation ---")

    hosp_ops = datasets["hospital_operations.csv"]
    patient_adm = datasets["patient_admissions.csv"]
    dept_data = datasets["department_data.csv"]
    resource_util = datasets["resource_utilization.csv"]

    def pct_valid(series, master_set):
        clean = series.dropna()
        if len(clean) == 0:
            return 100.0
        valid = clean.isin(master_set).sum()
        return valid / len(clean) * 100

    print(f"  Hospital_ID validity (Hospital Operations): "
          f"{pct_valid(hosp_ops['Hospital_ID'], MASTER_HOSPITAL_IDS):.2f}%")
    print(f"  Hospital_ID validity (Patient Admissions):  "
          f"{pct_valid(patient_adm['Hospital_ID'], MASTER_HOSPITAL_IDS):.2f}%")
    print(f"  Department_ID validity (Patient Admissions): "
          f"{pct_valid(patient_adm['Department_ID'], MASTER_DEPARTMENT_IDS):.2f}%")
    print(f"  Hospital_ID validity (Department Data):     "
          f"{pct_valid(dept_data['Hospital_ID'], MASTER_HOSPITAL_IDS):.2f}%")
    print(f"  Department_ID validity (Department Data):   "
          f"{pct_valid(dept_data['Department_ID'], MASTER_DEPARTMENT_IDS):.2f}%")
    print(f"  Hospital_ID validity (Resource Utilization): "
          f"{pct_valid(resource_util['Hospital_ID'], MASTER_HOSPITAL_IDS):.2f}%")
    print(f"  Department_ID validity (Resource Utilization): "
          f"{pct_valid(resource_util['Department_ID'], MASTER_DEPARTMENT_IDS):.2f}%")

    dup_patients = patient_adm["Patient_ID"].duplicated().sum()
    print(f"  Duplicate Patient_ID values: {dup_patients}")


def validate_relationships(datasets):
    """Confirm foreign-key values exist across related datasets."""
    print("\n--- Relationship Validation ---")

    hosp_ops = datasets["hospital_operations.csv"]
    patient_adm = datasets["patient_admissions.csv"]
    dept_data = datasets["department_data.csv"]
    resource_util = datasets["resource_utilization.csv"]

    hosp_ids_ops = set(hosp_ops["Hospital_ID"].dropna().unique())
    hosp_ids_dept = set(dept_data["Hospital_ID"].dropna().unique())

    orphan_patient_hosp = set(patient_adm["Hospital_ID"].dropna().unique()) - hosp_ids_ops
    print(f"  Patient Admissions -> Hospital Operations: "
          f"{'OK, all Hospital_IDs recognized' if not orphan_patient_hosp else f'{len(orphan_patient_hosp)} unmatched Hospital_IDs'}")

    dept_keys = set(zip(dept_data["Hospital_ID"], dept_data["Department_ID"]))
    patient_keys = set(zip(patient_adm["Hospital_ID"], patient_adm["Department_ID"]))
    orphan_patient_dept = patient_keys - dept_keys
    print(f"  Patient Admissions -> Department Data: "
          f"{'OK, all Hospital+Department combinations recognized' if not orphan_patient_dept else f'{len(orphan_patient_dept)} unmatched combinations'}")

    resource_keys = set(zip(resource_util["Hospital_ID"], resource_util["Department_ID"]))
    orphan_resource_dept = resource_keys - dept_keys
    print(f"  Resource Utilization -> Department Data: "
          f"{'OK, all Hospital+Department combinations recognized' if not orphan_resource_dept else f'{len(orphan_resource_dept)} unmatched combinations'}")

    resource_hosp_ids = set(resource_util["Hospital_ID"].dropna().unique())
    orphan_resource_hosp = resource_hosp_ids - hosp_ids_ops
    print(f"  Resource Utilization -> Hospital Operations: "
          f"{'OK, all Hospital_IDs recognized' if not orphan_resource_hosp else f'{len(orphan_resource_hosp)} unmatched Hospital_IDs'}")


def export_integrated_raw(datasets):
    """
    Export a single combined raw export (hospital_raw_data.csv) that tags
    each row with its source dataset, satisfying the Milestone 1 deliverable
    requirement while preserving the underlying relational structure in the
    separate per-dataset raw CSV files.
    """
    tagged_frames = []
    for filename, df in datasets.items():
        tagged = df.copy()
        tagged.insert(0, "Source_Dataset", filename.replace(".csv", ""))
        tagged_frames.append(tagged)

    combined = pd.concat(tagged_frames, ignore_index=True, sort=False)
    out_path = os.path.join(RAW_DIR, "hospital_raw_data.csv")
    combined.to_csv(out_path, index=False)
    print(f"\n--- Export ---\n  Combined raw export written to: {out_path}  (rows={len(combined)})")
    return combined


def main():
    print("=" * 60)
    print("MedTrack_DV | Milestone 1 | Data Collection & Validation")
    print("=" * 60)
    print("NOTE: All datasets are SYNTHETIC, generated for educational /")
    print("internship project development. No real patient data is used.")

    datasets = load_datasets()
    validate_structure(datasets)
    check_missing_values(datasets)
    check_duplicates(datasets)
    validate_keys(datasets)
    validate_relationships(datasets)
    export_integrated_raw(datasets)

    print("\nData collection and validation complete.")
    print("Proceed to hospital_cleaning.ipynb for the cleaning workflow.")


if __name__ == "__main__":
    main()
