# Relationship & Key Validation Report — MedTrack_DV (v2)

```
======================================================================
RELATIONSHIP & KEY VALIDATION REPORT (v2 — real relational HMIS source)
======================================================================

--- 1. Grain integrity ---
hospital_overview: 45000 rows, admission_id unique: True
patient_flow: 45000 rows, admission_id unique: True
department_analytics grain duplicates: 0
resource_utilization (Bed) grain duplicates: 0

--- 2. Orphan key checks ---
department_ids in overview but not in department_analytics: None
admission_ids in patient_flow but not in hospital_overview: 0
admission_ids in hospital_overview but not in patient_flow: 0

--- 3. Date consistency ---
hospital_overview.admission_date: 0 unparseable
patient_flow.admission_date: 0 unparseable
department_analytics.date: 0 unparseable

--- 4. Occupancy sanity (must be 0-100%) ---
occupancy_rate_pct > 100%: 0; < 0%: 0

--- 5. hospital_id consistency ---
overview: ['H1']
flow: ['H1']
dept: ['H1']
res: ['H1']

--- 6. Summary ---
PASS: no orphaned keys, no grain duplicates, no invalid dates, no occupancy values outside 0-100%, hospital_id consistent.
```
