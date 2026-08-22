"""
generate_synthetic_data.py
---------------------------
Generates the four raw synthetic datasets for MedTrack_DV Milestone 1:
    - hospital_operations.csv
    - patient_admissions.csv
    - department_data.csv
    - resource_utilization.csv

These are SYNTHETIC datasets created for educational / internship project
development. They do not represent real patient records or confidential
healthcare information.

Intentional, small, realistic data-quality issues are injected into the RAW
files only (missing values, duplicates, inconsistent department-name casing,
inconsistent categorical formatting, a few date-format inconsistencies) so
that the cleaning notebook (hospital_cleaning.ipynb) has real problems to
detect and fix.
"""

import random
import numpy as np
import pandas as pd
from datetime import date, timedelta

RNG_SEED = 42
random.seed(RNG_SEED)
np.random.seed(RNG_SEED)

RAW_DIR = "/home/claude/medtrack_dv/data/raw"

# ---------------------------------------------------------------------------
# MASTER KEYS
# ---------------------------------------------------------------------------

HOSPITALS = [
    ("H001", "MedCare General Hospital"),
    ("H002", "CityCare Medical Center"),
    ("H003", "LifeLine Hospital"),
    ("H004", "HealthFirst Medical Institute"),
    ("H005", "PrimeCare Hospital"),
    ("H006", "Sunrise Community Hospital"),
    ("H007", "Unity Wellness Hospital"),
]

DEPARTMENTS = [
    ("D001", "Cardiology", "Specialty"),
    ("D002", "Neurology", "Specialty"),
    ("D003", "Orthopedics", "Surgical"),
    ("D004", "Pediatrics", "Medical"),
    ("D005", "General Medicine", "Medical"),
    ("D006", "Emergency", "Emergency"),
    ("D007", "Oncology", "Specialty"),
    ("D008", "Dermatology", "Medical"),
    ("D009", "ENT", "Surgical"),
    ("D010", "Gastroenterology", "Diagnostic"),
]

DEPT_NAME_BY_ID = {d_id: name for d_id, name, _ in DEPARTMENTS}
DEPT_TYPE_BY_ID = {d_id: dtype for d_id, name, dtype in DEPARTMENTS}

START_DATE = date(2025, 1, 1)
END_DATE = date(2025, 12, 31)
ALL_DATES = pd.date_range(START_DATE, END_DATE, freq="D")

DIAGNOSES = [
    "Cardiac Condition", "Neurological Disorder", "Orthopedic Condition",
    "Respiratory Condition", "Gastrointestinal Condition", "Infection",
    "Routine Pediatric Care", "Dermatological Condition", "ENT Condition",
    "General Medical Condition",
]
ADMISSION_TYPES = ["Emergency", "Routine", "Referral", "Transfer"]
TREATMENT_TYPES = ["Medication", "Surgery", "Therapy", "Observation", "Diagnostic Procedure"]
READMISSION_FLAGS = ["Yes", "No"]
PATIENT_STATUSES = ["Discharged", "Admitted", "Transferred", "Under Treatment"]
RESOURCE_STATUSES = ["Normal", "High Utilization", "Limited", "Critical"]
DEPT_STATUSES = ["Active", "Limited", "Under Maintenance"]

# Messy-casing variants used ONLY to corrupt a small % of raw rows
DEPT_NAME_VARIANTS = {
    name: [name, name.upper(), name.lower(), name.title()]
    for _, name, _ in DEPARTMENTS
}


def messy_date(d: date) -> str:
    """Return the date in one of a few inconsistent raw formats."""
    fmt = random.choice(["%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%Y/%m/%d"])
    return d.strftime(fmt)


# ---------------------------------------------------------------------------
# DATASET 1 — HOSPITAL OPERATIONS
# ---------------------------------------------------------------------------

def generate_hospital_operations():
    rows = []
    # Daily records for all hospitals across the year -> 7 * 365 = 2555 rows
    for h_id, h_name in HOSPITALS:
        total_beds = random.randint(150, 500)
        for d in ALL_DATES:
            occupancy_rate = np.clip(np.random.normal(0.72, 0.12), 0.35, 0.98)
            occupied_beds = int(total_beds * occupancy_rate)
            available_beds = total_beds - occupied_beds
            total_admissions = max(0, int(np.random.normal(25, 8)))
            emergency_admissions = min(total_admissions, max(0, int(np.random.normal(9, 4))))
            total_discharges = max(0, int(np.random.normal(24, 8)))
            outpatient_visits = max(0, int(np.random.normal(120, 40)))

            rows.append({
                "Hospital_ID": h_id,
                "Hospital_Name": h_name,
                "Date": d.date(),
                "Total_Beds": total_beds,
                "Occupied_Beds": occupied_beds,
                "Available_Beds": available_beds,
                "Total_Admissions": total_admissions,
                "Total_Discharges": total_discharges,
                "Emergency_Admissions": emergency_admissions,
                "Outpatient_Visits": outpatient_visits,
            })

    df = pd.DataFrame(rows)

    # --- inject small, realistic raw-data issues -------------------------
    n = len(df)
    rng = np.random.default_rng(RNG_SEED)

    # ~1% missing values scattered across a few nullable-ish columns
    for col in ["Outpatient_Visits", "Emergency_Admissions", "Total_Discharges", "Hospital_Name"]:
        idx = rng.choice(n, size=max(1, int(n * 0.01 / 4)), replace=False)
        df.loc[idx, col] = np.nan

    # small number of duplicate rows
    dup_idx = rng.choice(n, size=max(1, int(n * 0.004)), replace=False)
    df = pd.concat([df, df.loc[dup_idx]], ignore_index=True)

    # a few date-format inconsistencies (store Date as mixed-format string)
    date_str = df["Date"].apply(lambda x: x.isoformat() if pd.notna(x) else x)
    messy_idx = rng.choice(len(df), size=max(1, int(len(df) * 0.01)), replace=False)
    date_str_list = date_str.tolist()
    for i in messy_idx:
        d_val = df.loc[i, "Date"]
        if pd.notna(d_val):
            date_str_list[i] = messy_date(d_val)
    df["Date"] = date_str_list

    df = df.sample(frac=1, random_state=RNG_SEED).reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# DATASET 2 — PATIENT ADMISSIONS
# ---------------------------------------------------------------------------

def generate_patient_admissions(n_rows=10500):
    rows = []
    for i in range(1, n_rows + 1):
        patient_id = f"P{i:05d}"
        h_id, _ = random.choice(HOSPITALS)
        d_id, dept_name, _ = random.choice(DEPARTMENTS)

        admit_offset = random.randint(0, (END_DATE - START_DATE).days - 1)
        admission_date = START_DATE + timedelta(days=admit_offset)
        stay_length = max(0, int(np.random.exponential(3.5)))
        stay_length = min(stay_length, 30)
        discharge_date = admission_date + timedelta(days=stay_length)
        if discharge_date > END_DATE:
            discharge_date = END_DATE
            stay_length = (discharge_date - admission_date).days

        status = random.choices(
            PATIENT_STATUSES, weights=[0.75, 0.10, 0.05, 0.10]
        )[0]

        rows.append({
            "Patient_ID": patient_id,
            "Hospital_ID": h_id,
            "Department_ID": d_id,
            "Admission_Date": admission_date,
            "Discharge_Date": discharge_date if status == "Discharged" or True else pd.NaT,
            "Admission_Type": random.choice(ADMISSION_TYPES),
            "Diagnosis": random.choice(DIAGNOSES),
            "Treatment_Type": random.choice(TREATMENT_TYPES),
            "Length_of_Stay": stay_length,
            "Readmission_Flag": random.choices(READMISSION_FLAGS, weights=[0.12, 0.88])[0],
            "Patient_Status": status,
        })

    df = pd.DataFrame(rows)
    n = len(df)
    rng = np.random.default_rng(RNG_SEED + 1)

    # ~1% missing values across a few columns
    for col in ["Treatment_Type", "Diagnosis", "Length_of_Stay", "Readmission_Flag"]:
        idx = rng.choice(n, size=max(1, int(n * 0.01 / 4)), replace=False)
        df.loc[idx, col] = np.nan

    # duplicate records
    dup_idx = rng.choice(n, size=max(1, int(n * 0.004)), replace=False)
    df = pd.concat([df, df.loc[dup_idx]], ignore_index=True)

    # inconsistent categorical formatting (Admission_Type casing)
    messy_idx = rng.choice(len(df), size=max(1, int(len(df) * 0.008)), replace=False)
    for i in messy_idx:
        val = df.loc[i, "Admission_Type"]
        if isinstance(val, str):
            df.loc[i, "Admission_Type"] = random.choice([val.upper(), val.lower()])

    # date-format inconsistencies on Admission_Date
    df["Admission_Date"] = df["Admission_Date"].apply(lambda x: x.isoformat() if pd.notna(x) else x)
    df["Discharge_Date"] = df["Discharge_Date"].apply(lambda x: x.isoformat() if pd.notna(x) else x)
    messy_idx2 = rng.choice(len(df), size=max(1, int(len(df) * 0.01)), replace=False)
    admit_list = df["Admission_Date"].tolist()
    for i in messy_idx2:
        v = admit_list[i]
        if isinstance(v, str):
            admit_list[i] = messy_date(date.fromisoformat(v))
    df["Admission_Date"] = admit_list

    df = df.sample(frac=1, random_state=RNG_SEED).reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# DATASET 3 — DEPARTMENT DATA
# ---------------------------------------------------------------------------

def generate_department_data():
    rows = []
    for h_id, _ in HOSPITALS:
        for d_id, dept_name, dept_type in DEPARTMENTS:
            capacity = random.randint(20, 80)
            doctors = random.randint(4, 20)
            nurses = random.randint(8, 40)
            staff_count = doctors + nurses + random.randint(0, 6)  # extra support staff
            monthly_target = random.randint(80, 400)
            status = random.choices(DEPT_STATUSES, weights=[0.85, 0.10, 0.05])[0]

            rows.append({
                "Hospital_ID": h_id,
                "Department_ID": d_id,
                "Department_Name": dept_name,
                "Department_Type": dept_type,
                "Department_Capacity": capacity,
                "Staff_Count": staff_count,
                "Doctors_Count": doctors,
                "Nurses_Count": nurses,
                "Monthly_Target": monthly_target,
                "Department_Status": status,
            })

    df = pd.DataFrame(rows)
    n = len(df)
    rng = np.random.default_rng(RNG_SEED + 2)

    # ~1% missing values
    for col in ["Monthly_Target", "Department_Status"]:
        idx = rng.choice(n, size=max(1, int(n * 0.01 / 2)), replace=False)
        df.loc[idx, col] = np.nan

    # a couple of duplicates
    dup_idx = rng.choice(n, size=max(1, int(n * 0.02)), replace=False)
    df = pd.concat([df, df.loc[dup_idx]], ignore_index=True)

    # inconsistent department-name casing (the classic Cardiology/CARDIOLOGY/cardiology issue)
    messy_idx = rng.choice(len(df), size=max(1, int(len(df) * 0.15)), replace=False)
    for i in messy_idx:
        name = df.loc[i, "Department_Name"]
        if isinstance(name, str):
            df.loc[i, "Department_Name"] = random.choice(DEPT_NAME_VARIANTS[name])

    df = df.sample(frac=1, random_state=RNG_SEED).reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# DATASET 4 — RESOURCE UTILIZATION
# ---------------------------------------------------------------------------

def generate_resource_utilization(n_rows=5200):
    rows = []
    combos = [(h, d) for h, _ in HOSPITALS for d, _, _ in DEPARTMENTS]
    for i in range(n_rows):
        h_id, d_id = random.choice(combos)
        offset = random.randint(0, (END_DATE - START_DATE).days)
        d = START_DATE + timedelta(days=offset)

        total_beds = random.randint(10, 60)
        occupied_beds = random.randint(0, total_beds)
        available_beds = total_beds - occupied_beds

        equipment_count = random.randint(5, 40)
        equipment_in_use = random.randint(0, equipment_count)

        staff_available = random.randint(5, 30)
        staff_allocated = random.randint(0, staff_available)

        util_ratio = occupied_beds / total_beds if total_beds else 0
        if util_ratio >= 0.9:
            status = "Critical"
        elif util_ratio >= 0.75:
            status = "High Utilization"
        elif util_ratio <= 0.3:
            status = "Limited"
        else:
            status = "Normal"

        rows.append({
            "Hospital_ID": h_id,
            "Department_ID": d_id,
            "Date": d,
            "Total_Beds": total_beds,
            "Occupied_Beds": occupied_beds,
            "Available_Beds": available_beds,
            "Equipment_Count": equipment_count,
            "Equipment_In_Use": equipment_in_use,
            "Staff_Available": staff_available,
            "Staff_Allocated": staff_allocated,
            "Resource_Status": status,
        })

    df = pd.DataFrame(rows)
    n = len(df)
    rng = np.random.default_rng(RNG_SEED + 3)

    # ~1% missing values
    for col in ["Equipment_Count", "Staff_Available", "Resource_Status"]:
        idx = rng.choice(n, size=max(1, int(n * 0.01 / 3)), replace=False)
        df.loc[idx, col] = np.nan

    # duplicates
    dup_idx = rng.choice(n, size=max(1, int(n * 0.004)), replace=False)
    df = pd.concat([df, df.loc[dup_idx]], ignore_index=True)

    # inconsistent categorical formatting on Resource_Status
    messy_idx = rng.choice(len(df), size=max(1, int(len(df) * 0.01)), replace=False)
    for i in messy_idx:
        val = df.loc[i, "Resource_Status"]
        if isinstance(val, str):
            df.loc[i, "Resource_Status"] = val.lower()

    # date-format inconsistencies
    df["Date"] = df["Date"].apply(lambda x: x.isoformat() if pd.notna(x) else x)
    messy_idx2 = rng.choice(len(df), size=max(1, int(len(df) * 0.01)), replace=False)
    date_list = df["Date"].tolist()
    for i in messy_idx2:
        v = date_list[i]
        if isinstance(v, str):
            date_list[i] = messy_date(date.fromisoformat(v))
    df["Date"] = date_list

    df = df.sample(frac=1, random_state=RNG_SEED).reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    hosp_ops = generate_hospital_operations()
    patient_adm = generate_patient_admissions()
    dept_data = generate_department_data()
    resource_util = generate_resource_utilization()

    hosp_ops.to_csv(f"{RAW_DIR}/hospital_operations.csv", index=False)
    patient_adm.to_csv(f"{RAW_DIR}/patient_admissions.csv", index=False)
    dept_data.to_csv(f"{RAW_DIR}/department_data.csv", index=False)
    resource_util.to_csv(f"{RAW_DIR}/resource_utilization.csv", index=False)

    print("Hospital Operations:", hosp_ops.shape)
    print("Patient Admissions :", patient_adm.shape)
    print("Department Data    :", dept_data.shape)
    print("Resource Utilization:", resource_util.shape)
