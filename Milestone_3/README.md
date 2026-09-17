# Milestone 3 – Dashboard Development
## MedTrack_DV | Hospital Operations & Patient Analytics Dashboard
### Infosys Springboard Virtual Internship

---

## Objective

Milestone 3 is where you build all 4 dashboards in **Power BI Desktop** using the 4 cleaned CSV datasets from Milestone 1. The final output is a single `MedTrack_DV.pbix` file containing all 4 connected dashboards.

---

## Milestone 3 Checklist

| Task | Status |
|---|---|
| ✅ Power BI setup guide created | Complete |
| ✅ All 28 DAX measures documented | Complete |
| ✅ Dashboard layouts planned (Milestone 2 storyboard) | Complete |
| ✅ Color theme and design rules defined | Complete |
| ⏳ Dashboard 1 – Hospital Overview | Build in Power BI |
| ⏳ Dashboard 2 – Patient Flow | Build in Power BI |
| ⏳ Dashboard 3 – Department Analytics | Build in Power BI |
| ⏳ Dashboard 4 – Resource Utilization | Build in Power BI |
| ⏳ Navigation buttons across all pages | Build in Power BI |
| ⏳ Global slicers (Hospital, Dept, Year, Month) | Build in Power BI |
| ⏳ Cross-dashboard interactions | Build in Power BI |
| ⏳ Final MedTrack_DV.pbix exported | Add to dashboard/ folder |
| ⏳ 4 Screenshots taken | Add to screenshots/ folder |

---

## Folder Structure

```
Milestone_3/
│
├── README.md                          ← This file
│
├── docs/
│   ├── powerbi_setup_guide.md         ← Step by step Power BI instructions
│   └── dax_measures.md                ← All 28 DAX measures with formulas
│
├── dashboard/
│   └── MedTrack_DV.pbix               ← ADD THIS after building in Power BI
│
└── screenshots/
    ├── 01_hospital_overview.png        ← ADD THIS after building
    ├── 02_patient_flow.png             ← ADD THIS after building
    ├── 03_department_analytics.png     ← ADD THIS after building
    └── 04_resource_utilization.png     ← ADD THIS after building
```

---

## Data Files to Load in Power BI

All files are in `Milestone_1/data/processed/`

| File | Dashboard |
|---|---|
| hospital_overview_dataset.csv | Dashboard 1 – Hospital Overview |
| patient_flow_dataset.csv | Dashboard 2 – Patient Flow |
| department_analytics_dataset.csv | Dashboard 3 – Department Analytics |
| resource_utilization_dataset.csv | Dashboard 4 – Resource Utilization |
| normalized_readmission.csv | KPI 4 – Readmission Rate |

---

## 4 Dashboards to Build

### Dashboard 1 – Hospital Overview
**Purpose:** Overall hospital performance at a glance

**KPI Cards:**
- Total Admissions → 56,500
- Occupancy Rate → 92.7%
- Avg Length of Stay → 5.13 days
- Readmission Rate → 12.7%
- Bed Utilization → 92.7%
- Total Beds → 500

**Charts:**
- Monthly Admission Trend (Line Chart)
- Admissions vs Discharges (Clustered Bar)
- Occupancy Rate Trend (Line Chart)
- Department Efficiency Score (Horizontal Bar)
- Admission Type Split (Donut Chart)

---

### Dashboard 2 – Patient Flow
**Purpose:** How patients move through the hospital

**Charts:**
- Admission Trend Over Time (Line Chart)
- Admission Type Breakdown (Donut Chart)
- Avg LOS by Medical Condition (Horizontal Bar)
- Patient Volume by Day of Week (Column Bar)
- Test Results Distribution (Bar Chart)
- Discharge Trend (Line Chart)
- Billing Amount Trend (Line Chart)

---

### Dashboard 3 – Department Analytics
**Purpose:** Which departments are performing well

**Charts:**
- Admissions by Department (Bar Chart)
- Department Efficiency Score Ranking (Horizontal Bar)
- Weekly Occupancy Heatmap (Matrix)
- Patients Refused by Department (Bar Chart)
- Patient Satisfaction Score (Bar Chart)
- Staff Morale Trend (Line Chart)

---

### Dashboard 4 – Resource Utilization
**Purpose:** How efficiently are beds, staff and resources used

**KPI Cards:**
- Total Beds
- Occupied Beds
- Available Beds
- Departments with Shortage

**Charts:**
- Bed Utilization by Department (Horizontal Bar)
- Available vs Occupied Beds (Stacked Bar)
- Weekly Resource Trend (Line Chart)
- Shortage Flag Heatmap (Matrix)
- Staff Utilization by Department (Bar Chart)

---

## All 28 DAX Measures (Quick Reference)

See full formulas in `docs/dax_measures.md`

| # | Measure Name | Table |
|---|---|---|
| 1 | Total Admissions | hospital_overview_dataset |
| 2 | Total Patients | hospital_overview_dataset |
| 3 | Avg Length of Stay | hospital_overview_dataset |
| 4 | Total Male | hospital_overview_dataset |
| 5 | Total Female | hospital_overview_dataset |
| 6 | Total Departments | hospital_overview_dataset |
| 7 | Occupancy Rate % | resource_utilization_dataset |
| 8 | Bed Utilization Rate % | resource_utilization_dataset |
| 9 | Total Available Beds | resource_utilization_dataset |
| 10 | Total Occupied Beds | resource_utilization_dataset |
| 11 | Beds Remaining | resource_utilization_dataset |
| 12 | Total Patients Refused | resource_utilization_dataset |
| 13 | Shortage Departments | resource_utilization_dataset |
| 14 | Staff Utilization Rate % | resource_utilization_dataset |
| 15 | Avg Efficiency Score | department_analytics_dataset |
| 16 | Avg Patient Satisfaction | department_analytics_dataset |
| 17 | Avg Staff Morale | department_analytics_dataset |
| 18 | Dept Bed Utilization % | department_analytics_dataset |
| 19 | Total Dept Admissions | department_analytics_dataset |
| 20 | Total Dept Refused | department_analytics_dataset |
| 21 | Refusal Rate % | department_analytics_dataset |
| 22 | Readmission Rate % | normalized_readmission |
| 23 | Patient Flow Avg LOS | patient_flow_dataset |
| 24 | Total Billing Amount | patient_flow_dataset |
| 25 | Avg Billing Amount | patient_flow_dataset |
| 26 | Emergency Admissions | patient_flow_dataset |
| 27 | Elective Admissions | patient_flow_dataset |
| 28 | Weekend Admissions | patient_flow_dataset |

---

## Color Theme

| Color | Hex Code | Used For |
|---|---|---|
| 🟢 Green | #1D9E75 | Good performance, success |
| 🟠 Orange | #EF9F27 | Warning, medium range |
| 🔴 Red | #E24B4A | Danger, shortage, high alert |
| 🔵 Blue | #378ADD | Admissions, primary charts |
| 🟣 Purple | #7F77DD | Secondary charts, staff |
| ⬜ Background | #F8F9FA | Page background |
| ⬛ Cards | #FFFFFF | Card background |

---

## Step by Step Instructions

Follow `docs/powerbi_setup_guide.md` for complete step-by-step instructions including:
- How to load data
- How to create relationships
- How to add DAX measures
- How to build each chart
- How to add navigation buttons
- How to sync slicers across pages
- How to export final .pbix file

---

## Next Step → Milestone 4

After completing all 4 dashboards:
1. Save as `MedTrack_DV.pbix`
2. Place in `Milestone_3/dashboard/`
3. Take 4 screenshots → place in `Milestone_3/screenshots/`
4. Push to GitHub
5. Proceed to Milestone 4 (Testing & Validation)
