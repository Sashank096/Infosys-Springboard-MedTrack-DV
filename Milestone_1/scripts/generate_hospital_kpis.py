"""
MedTrack_DV – Milestone 1
Script: generate_hospital_kpis.py
Purpose: Calculate all 6 mandatory KPIs and export the 4 final analytical datasets
Internship: Infosys Springboard Virtual Internship
"""

import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

PROCESSED = '../data/processed/'

# ============================================================
# LOAD NORMALIZED DATASETS
# ============================================================

def load_data():
    print("Loading normalized datasets...")
    data = {
        'patients':       pd.read_csv(PROCESSED + 'normalized_patients.csv'),
        'bed_records':    pd.read_csv(PROCESSED + 'normalized_bed_records.csv',
                                      parse_dates=['admission_date', 'discharge_date']),
        'department':     pd.read_csv(PROCESSED + 'normalized_departments.csv'),
        'doctor':         pd.read_csv(PROCESSED + 'normalized_doctors.csv'),
        'nurse':          pd.read_csv(PROCESSED + 'normalized_nurses.csv'),
        'ward':           pd.read_csv(PROCESSED + 'normalized_wards.csv'),
        'beds_patients':  pd.read_csv(PROCESSED + 'normalized_beds_patients.csv'),
        'beds_services':  pd.read_csv(PROCESSED + 'normalized_beds_services.csv'),
        'beds_schedule':  pd.read_csv(PROCESSED + 'normalized_staff_shifts.csv'),
        'readmission':    pd.read_csv(PROCESSED + 'normalized_readmission.csv'),
        'healthcare':     pd.read_csv(PROCESSED + 'normalized_healthcare.csv',
                                      parse_dates=['date_of_admission', 'discharge_date'])
    }
    print("✅ All datasets loaded!")
    return data


# ============================================================
# KPI CALCULATIONS
# ============================================================

def calculate_kpis(data):
    kpis = {}

    # KPI 1: Total Admissions
    kpis['total_admissions_hmis'] = data['bed_records']['admission_id'].nunique()
    kpis['total_admissions_hc']   = len(data['healthcare'])
    kpis['total_admissions']      = kpis['total_admissions_hmis'] + kpis['total_admissions_hc']

    # KPI 2: Occupancy Rate
    total_beds = len(data['bed_records']['bed_no'].unique()) if 'bed_no' in data['bed_records'].columns else 500
    occupied   = data['beds_services']['patients_admitted'].sum()
    available  = data['beds_services']['available_beds'].sum()
    kpis['occupancy_rate'] = round(occupied / available * 100, 2) if available > 0 else 0

    # KPI 3: Average Length of Stay
    kpis['avg_los_hmis']       = round(data['bed_records']['length_of_stay_days'].dropna().mean(), 2)
    kpis['avg_los_healthcare'] = round(data['healthcare']['length_of_stay_days'].dropna().mean(), 2)

    duration_col = next((c for c in ['duration_of_stay', 'length_of_stay_days'] if c in data['readmission'].columns), None)
    kpis['avg_los_readmission'] = round(data['readmission'][duration_col].dropna().mean(), 2) if duration_col else 'N/A'

    # KPI 4: Readmission Rate
    total_patients = len(data['readmission'])
    if 'outcome' in data['readmission'].columns:
        readmitted = data['readmission']['outcome'].str.strip().str.upper().isin(['DAMA', 'EXPIRY']).sum()
    else:
        readmitted = 0
    kpis['readmission_rate'] = round(readmitted / total_patients * 100, 2) if total_patients > 0 else 0

    # KPI 5: Bed Utilization Rate
    kpis['bed_utilization_rate'] = round(
        data['beds_services']['patients_admitted'].sum() /
        data['beds_services']['available_beds'].sum() * 100, 2
    )

    # KPI 6: Department Efficiency Score
    dept_eff = data['beds_services'].groupby('service').agg(
        total_admitted   = ('patients_admitted', 'sum'),
        total_refused    = ('patients_refused', 'sum'),
        avg_satisfaction = ('patient_satisfaction', 'mean'),
        avg_staff_morale = ('staff_morale', 'mean')
    ).reset_index()

    dept_eff['occupancy_score'] = (
        dept_eff['total_admitted'] /
        (dept_eff['total_admitted'] + dept_eff['total_refused']) * 100
    ).round(2)
    dept_eff['satisfaction_score'] = (
        dept_eff['avg_satisfaction'] / dept_eff['avg_satisfaction'].max() * 100
    ).round(2)
    dept_eff['staff_score'] = (
        dept_eff['avg_staff_morale'] / dept_eff['avg_staff_morale'].max() * 100
    ).round(2)
    dept_eff['department_efficiency_score'] = (
        0.40 * dept_eff['occupancy_score'] +
        0.40 * dept_eff['satisfaction_score'] +
        0.20 * dept_eff['staff_score']
    ).round(2)

    kpis['dept_efficiency'] = dept_eff

    return kpis


# ============================================================
# BUILD FINAL 4 ANALYTICAL DATASETS
# ============================================================

def build_final_datasets(data, kpis):

    # 1. Hospital Overview Dataset
    hospital_overview = data['bed_records'].merge(
        data['patients'][['patient_id', 'gender', 'date_of_birth', 'full_name']],
        on='patient_id', how='left'
    ).merge(
        data['ward'][['ward_no', 'ward_name', 'dept_id']],
        on='ward_no', how='left'
    ).merge(
        data['department'][['dept_id', 'dept_name']],
        on='dept_id', how='left'
    )
    hospital_overview['hospital_id']   = 'H001'
    hospital_overview['hospital_name'] = 'MedTrack General Hospital'

    # 2. Patient Flow Dataset
    patient_flow = data['healthcare'][[
        'name', 'age', 'gender', 'medical_condition', 'date_of_admission',
        'discharge_date', 'admission_type', 'hospital', 'doctor',
        'billing_amount', 'length_of_stay_days', 'admission_year',
        'admission_month', 'test_results'
    ]].copy()
    patient_flow['day_of_week']       = pd.to_datetime(patient_flow['date_of_admission']).dt.day_name()
    patient_flow['admission_quarter'] = pd.to_datetime(patient_flow['date_of_admission']).dt.quarter
    patient_flow['is_weekend']        = pd.to_datetime(patient_flow['date_of_admission']).dt.weekday >= 5

    # 3. Department Analytics Dataset
    dept_analytics = data['beds_services'].merge(
        kpis['dept_efficiency'][['service', 'occupancy_score', 'satisfaction_score', 'department_efficiency_score']],
        on='service', how='left'
    )
    dept_analytics['hospital_id']          = 'H001'
    dept_analytics['hospital_name']        = 'MedTrack General Hospital'
    dept_analytics['bed_utilization_rate'] = (
        dept_analytics['patients_admitted'] / dept_analytics['available_beds'] * 100
    ).round(2)
    dept_analytics['refusal_rate'] = (
        dept_analytics['patients_refused'] /
        (dept_analytics['patients_admitted'] + dept_analytics['patients_refused']) * 100
    ).round(2)

    # 4. Resource Utilization Dataset
    if 'week' in data['beds_schedule'].columns and 'service' in data['beds_schedule'].columns:
        schedule_agg = data['beds_schedule'].groupby(['week', 'service']).agg(
            total_staff   = ('staff_id', 'count') if 'staff_id' in data['beds_schedule'].columns else ('shift_id', 'count'),
            staff_present = ('present', 'sum') if 'present' in data['beds_schedule'].columns else ('shift_date', 'count')
        ).reset_index()
        resource_util = data['beds_services'].merge(schedule_agg, on=['week', 'service'], how='left')
    else:
        resource_util = data['beds_services'].copy()
        resource_util['total_staff']   = 0
        resource_util['staff_present'] = 0

    resource_util['hospital_id']           = 'H001'
    resource_util['hospital_name']         = 'MedTrack General Hospital'
    resource_util['bed_utilization_pct']   = (
        resource_util['patients_admitted'] / resource_util['available_beds'] * 100
    ).round(2)
    resource_util['shortage_flag'] = resource_util['patients_refused'] > 0

    # Save all 4 datasets
    hospital_overview.to_csv(PROCESSED + 'hospital_overview_dataset.csv', index=False)
    patient_flow.to_csv(PROCESSED + 'patient_flow_dataset.csv', index=False)
    dept_analytics.to_csv(PROCESSED + 'department_analytics_dataset.csv', index=False)
    resource_util.to_csv(PROCESSED + 'resource_utilization_dataset.csv', index=False)

    print("✅ All 4 final datasets saved!")
    return hospital_overview, patient_flow, dept_analytics, resource_util


# ============================================================
# PRINT KPI SUMMARY
# ============================================================

def print_kpi_summary(kpis):
    print("\n" + "=" * 55)
    print("   MEDTRACK_DV – FINAL KPI SUMMARY")
    print("=" * 55)
    print(f"KPI 1 – Total Admissions:       {kpis['total_admissions']:,}")
    print(f"KPI 2 – Occupancy Rate:         {kpis['occupancy_rate']}%")
    print(f"KPI 3 – Avg Length of Stay:     {kpis['avg_los_hmis']} days")
    print(f"KPI 4 – Readmission Rate:       {kpis['readmission_rate']}%")
    print(f"KPI 5 – Bed Utilization Rate:   {kpis['bed_utilization_rate']}%")
    print(f"KPI 6 – Dept Efficiency Score:  See department breakdown")
    print()
    print("Department Efficiency Scores:")
    print(kpis['dept_efficiency'][['service', 'department_efficiency_score']].to_string(index=False))
    print("=" * 55)


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    data    = load_data()
    kpis    = calculate_kpis(data)
    ho, pf, da, ru = build_final_datasets(data, kpis)
    print_kpi_summary(kpis)

    print("\nFinal Datasets:")
    print(f"  hospital_overview_dataset.csv:      {ho.shape[0]:,} rows")
    print(f"  patient_flow_dataset.csv:           {pf.shape[0]:,} rows")
    print(f"  department_analytics_dataset.csv:   {da.shape[0]:,} rows")
    print(f"  resource_utilization_dataset.csv:   {ru.shape[0]:,} rows")
    print("\n✅ KPI generation complete! Ready for Tableau.")
