# Milestone 2 – KPI Engineering & Dashboard Planning
## MedTrack_DV | Hospital Operations & Patient Analytics Dashboard
### Infosys Springboard Virtual Internship

---

## Objective

Milestone 2 covers KPI validation with real calculated values, complete dashboard storyboarding with layouts, Tableau data model design, and documentation before Tableau development begins in Milestone 3.

---

## Milestone 2 Checklist

| Task | Status |
|---|---|
| ✅ 6 KPI formulas defined and documented | Complete |
| ✅ All 6 KPIs calculated from real data (Python) | Complete |
| ✅ KPI validation report created | Complete |
| ✅ Dashboard storyboard with layouts created | Complete |
| ✅ Tableau data model designed | Complete |
| ✅ Field mapping documented | Complete |
| ✅ Tableau calculated fields defined | Complete |
| ⏳ Initial Tableau prototype | Add after building |

---

## Folder Structure

```
Milestone_2/
│
├── docs/
│   ├── kpi_validation.md          ← All 6 KPIs with actual values
│   ├── dashboard_storyboard.md    ← Layout blueprint for all 4 dashboards
│   └── tableau_data_model.md      ← How to load and connect data in Tableau
│
├── dashboard/
│   └── MedTrack_DV_prototype.twbx ← Add after building Tableau prototype
│
└── README.md                      ← This file
```

---

## 6 KPIs – Actual Calculated Values

| # | KPI | Formula | Calculated Value |
|---|---|---|---|
| 1 | Total Admissions | COUNT DISTINCT(admission_id) | **56,500** |
| 2 | Occupancy Rate | Admitted / Available × 100 | **92.7%** |
| 3 | Average Length of Stay | AVG(discharge - admission) | **5.13 days (HMIS)** |
| 4 | Readmission Rate | Readmitted / Total × 100 | **12.7%** |
| 5 | Bed Utilization Rate | In Use / Available × 100 | **92.7%** |
| 6 | Dept Efficiency Score | 40% Occ + 40% Sat + 20% Staff | **ICU: 92.15 / Surgery: 88.69** |

---

## Department Efficiency Scores

| Department | Score | Status |
|---|---|---|
| ICU | 92.15 | ✅ Excellent |
| Surgery | 88.69 | ✅ Excellent |
| General Medicine | 81.53 | ✅ Good |
| Emergency | 65.82 | ⚠️ Needs Attention |

---

## 4 Dashboard Summary

| Dashboard | Purpose | Primary Dataset |
|---|---|---|
| Dashboard 1 – Hospital Overview | Overall performance KPIs | hospital_overview_dataset.csv |
| Dashboard 2 – Patient Flow | Patient movement and trends | patient_flow_dataset.csv |
| Dashboard 3 – Department Analytics | Dept performance comparison | department_analytics_dataset.csv |
| Dashboard 4 – Resource Utilization | Beds, staff, capacity | resource_utilization_dataset.csv |

---

## Tableau Data Model Summary

- Load 4 CSV files from `Milestone_1/data/processed/`
- Use **Relationships** (NOT Joins) to connect datasets
- patient_flow_dataset.csv = separate data source (different grain)
- Connect hospital_overview ↔ department_analytics via `dept_name = service`
- Connect department_analytics ↔ resource_utilization via `service + week`

---

## Next Step → Milestone 3

Build all 4 Tableau dashboards following the storyboard layouts in `docs/dashboard_storyboard.md` and the data model in `docs/tableau_data_model.md`.
