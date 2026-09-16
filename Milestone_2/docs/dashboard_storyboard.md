# MedTrack_DV – Dashboard Storyboard
## Milestone 2 | Infosys Springboard Virtual Internship

---

## Overview

This document is the complete blueprint for all 4 Tableau dashboards before development begins. Each dashboard section describes: purpose, KPIs shown, charts, filters, and interactions.

---

## Navigation Bar (Common to All Dashboards)

Every dashboard must have a navigation bar at the top:

```
┌──────────────────────────────────────────────────────────┐
│  🏥 MedTrack_DV  │  Home  │  Patient Flow  │  Departments  │  Resources  │
└──────────────────────────────────────────────────────────┘
```

Each button links to its respective dashboard using Tableau navigation actions.

---

## Global Filters (Applied to All Dashboards)

These filters appear on every dashboard and update all charts:

| Filter | Field | Values |
|---|---|---|
| Hospital | hospital_name | MedTrack General Hospital |
| Department | service / dept_name | ICU, Emergency, General Medicine, Surgery, All |
| Year | admission_year | 2019, 2020, 2021, 2022, 2023, 2024 |
| Month | admission_month | January – December, All |

---

## Dashboard 1 – Hospital Overview

**Purpose:** "How is the hospital performing overall?"
**Source Dataset:** hospital_overview_dataset.csv + resource_utilization_dataset.csv

---

### Layout

```
┌──────────────────────────────────────────────────────────────────┐
│  NAVIGATION BAR                                                   │
├──────────────────────────────────────────────────────────────────┤
│  FILTERS:  Hospital ▼   Department ▼   Year ▼   Month ▼          │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │
│  │ Total    │ │Occupancy │ │  Avg LOS │ │Readmission│ │  Bed   │ │
│  │Admissions│ │  Rate    │ │  (days)  │ │   Rate   │ │  Util  │ │
│  │  56,500  │ │  92.7%   │ │  5.13    │ │  12.7%   │ │  92.7% │ │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └────────┘ │
│                                                                   │
│  ┌────────────────────────────┐  ┌──────────────────────────────┐│
│  │  Monthly Admission Trend   │  │  Admissions vs Discharges    ││
│  │      (Line Chart)          │  │      (Dual Bar Chart)        ││
│  │  Jan──Feb──Mar──...        │  │  ██ Admissions  ░░ Discharges││
│  └────────────────────────────┘  └──────────────────────────────┘│
│                                                                   │
│  ┌────────────────────────────┐  ┌──────────────────────────────┐│
│  │  Occupancy Trend by Week   │  │  Dept Efficiency Score       ││
│  │     (Area Chart)           │  │     (Horizontal Bar)         ││
│  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │  │  ICU          92.15 ████████ ││
│  └────────────────────────────┘  │  Surgery       88.69 ███████ ││
│                                  │  Gen Med       81.53 ██████  ││
│                                  │  Emergency     65.82 █████   ││
│                                  └──────────────────────────────┘│
└──────────────────────────────────────────────────────────────────┘
```

### Charts Detail

| Chart | Type | X-Axis | Y-Axis | Color |
|---|---|---|---|---|
| KPI Cards | Text/Number | — | KPI value | Green/Red based on target |
| Monthly Admission Trend | Line Chart | Month Name | COUNT(admission_id) | Blue |
| Admissions vs Discharges | Dual Bar | Month | Count | Blue / Orange |
| Occupancy Trend | Area Chart | Week | bed_utilization_pct | Teal |
| Dept Efficiency Score | Horizontal Bar | dept name | efficiency_score | Green gradient |

### Tableau Calculated Fields
```
Total Admissions:    COUNTD([Admission Id])
Occupancy Rate:      SUM([Patients Admitted]) / SUM([Available Beds]) * 100
Avg LOS:             AVG([Length Of Stay Days])
Readmission Rate:    SUM([Readmission Flag]) / COUNT([Patient Id]) * 100
Bed Utilization:     SUM([Patients Admitted]) / SUM([Available Beds]) * 100
```

---

## Dashboard 2 – Patient Flow

**Purpose:** "How are patients moving through the hospital?"
**Source Dataset:** patient_flow_dataset.csv

---

### Layout

```
┌──────────────────────────────────────────────────────────────────┐
│  NAVIGATION BAR                                                   │
├──────────────────────────────────────────────────────────────────┤
│  FILTERS:  Admission Type ▼   Year ▼   Month ▼   Condition ▼     │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │              Admission Trend Over Time (Line Chart)          │ │
│  │  2019────2020────2021────2022────2023────2024               │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─────────────────────┐  ┌───────────────────────────────────┐  │
│  │  Admission Type      │  │   Avg LOS by Medical Condition    │  │
│  │  (Donut Chart)       │  │   (Horizontal Bar Chart)          │  │
│  │                      │  │   Asthma        15.70 ███████████ │  │
│  │  Elective  33.6%     │  │   Arthritis     15.52 ██████████  │  │
│  │  Urgent    33.5%     │  │   Cancer        15.50 ██████████  │  │
│  │  Emergency 32.9%     │  │   Hypertension  15.46 █████████   │  │
│  └─────────────────────┘  └───────────────────────────────────┘  │
│                                                                   │
│  ┌─────────────────────┐  ┌───────────────────────────────────┐  │
│  │  Patient Volume by   │  │   Test Results Distribution       │  │
│  │  Day of Week (Bar)   │  │   (Bar Chart)                     │  │
│  │  Mon Tue Wed Thu ... │  │   Normal / Abnormal / Inconclusive│  │
│  └─────────────────────┘  └───────────────────────────────────┘  │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │          Discharge Trend Over Time (Line Chart)              │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

### Charts Detail

| Chart | Type | X-Axis | Y-Axis | Color |
|---|---|---|---|---|
| Admission Trend | Line Chart | date_of_admission | COUNT | Blue |
| Admission Type | Donut Chart | admission_type | COUNT / % | Multi-color |
| Avg LOS by Condition | Horizontal Bar | medical_condition | AVG(los) | Orange |
| Day of Week Volume | Bar Chart | day_of_week | COUNT | Teal |
| Test Results | Bar Chart | test_results | COUNT | Multi-color |
| Discharge Trend | Line Chart | discharge_date | COUNT | Green |

---

## Dashboard 3 – Department Analytics

**Purpose:** "Which departments are performing well and which need attention?"
**Source Dataset:** department_analytics_dataset.csv

---

### Layout

```
┌──────────────────────────────────────────────────────────────────┐
│  NAVIGATION BAR                                                   │
├──────────────────────────────────────────────────────────────────┤
│  FILTERS:  Department ▼   Month ▼   Week ▼                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌────────────────────────────┐  ┌──────────────────────────────┐│
│  │  Admissions by Department  │  │  Dept Efficiency Score        ││
│  │  (Bar Chart)               │  │  (Sorted Horizontal Bar)      ││
│  │  Gen Med  ███████████ 2332 │  │  ICU          92.15 ████████  ││
│  │  Surgery  ████████   1686  │  │  Surgery      88.69 ███████   ││
│  │  Emergency████     1185    │  │  Gen Med      81.53 ██████    ││
│  │  ICU      ████      648    │  │  Emergency    65.82 █████     ││
│  └────────────────────────────┘  └──────────────────────────────┘│
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │        Weekly Occupancy Heatmap (Dept × Week)                │ │
│  │                                                              │ │
│  │        Wk1  Wk2  Wk3  Wk4  Wk5  ...                        │ │
│  │  ICU   ▓▓▓  ▓▓▓  ▓▓   ▓▓▓  ▓▓▓                            │ │
│  │  Emrg  ░    ░░   ░    ░░   ░                               │ │
│  │  GMed  ▓░   ▓░   ░▓   ▓░   ▓░                              │ │
│  │  Surg  ▓▓   ▓▓   ▓▓   ▓▓   ▓▓                              │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌────────────────────────────┐  ┌──────────────────────────────┐│
│  │  Patients Refused by Dept  │  │  Patient Satisfaction Score   ││
│  │  (Bar Chart)               │  │  (Bar Chart)                  ││
│  │  Emergency ████████ 5008   │  │  ICU      81.6 ████████       ││
│  │  Gen Med   ████     1938   │  │  Gen Med  81.2 ████████       ││
│  │  Surgery   ██        555   │  │  Surgery  79.3 ███████        ││
│  │  ICU       █         141   │  │  Emergency77.9 ███████        ││
│  └────────────────────────────┘  └──────────────────────────────┘│
└──────────────────────────────────────────────────────────────────┘
```

### Charts Detail

| Chart | Type | X-Axis | Y-Axis | Color |
|---|---|---|---|---|
| Admissions by Dept | Bar Chart | service | patients_admitted | Blue |
| Efficiency Score | Horizontal Bar (sorted) | service | efficiency_score | Green gradient |
| Weekly Heatmap | Heatmap | week | service | Red-Green scale |
| Refused Patients | Bar Chart | service | patients_refused | Red |
| Satisfaction Score | Bar Chart | service | avg(patient_satisfaction) | Orange |

### Dashboard Action
- **Click any department bar** → Filters Dashboard 2 (Patient Flow) to that department
- **Click any department bar** → Filters Dashboard 4 (Resource Utilization) to that department

---

## Dashboard 4 – Resource Utilization

**Purpose:** "How efficiently are hospital resources being used?"
**Source Dataset:** resource_utilization_dataset.csv

---

### Layout

```
┌──────────────────────────────────────────────────────────────────┐
│  NAVIGATION BAR                                                   │
├──────────────────────────────────────────────────────────────────┤
│  FILTERS:  Department ▼   Week ▼   Month ▼                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │  Total   │ │ Occupied │ │Available │ │ Shortage │            │
│  │  Beds    │ │   Beds   │ │  Beds    │ │  Flag    │            │
│  │   500    │ │   463    │ │    37    │ │  3 Depts │            │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘            │
│                                                                   │
│  ┌────────────────────────────┐  ┌──────────────────────────────┐│
│  │  Bed Utilization by Dept   │  │  Available vs Occupied Beds   ││
│  │  (Horizontal Bar)          │  │  (Stacked Bar)                ││
│  │  ICU       92.7% ████████  │  │  ICU  ████████░░             ││
│  │  Surgery   75.2% ███████   │  │  Surg ████████░░░            ││
│  │  Gen Med   54.6% █████     │  │  GMed ██████░░░░░            ││
│  │  Emergency 19.1% ██        │  │  Emrg ██░░░░░░░░░            ││
│  └────────────────────────────┘  └──────────────────────────────┘│
│                                                                   │
│  ┌────────────────────────────┐  ┌──────────────────────────────┐│
│  │  Weekly Resource Trend     │  │  Shortage Flag Heatmap        ││
│  │  (Line Chart)              │  │  (Highlight Table)            ││
│  │  ─────────────────────     │  │  Dept × Week                  ││
│  │  Wk1──Wk2──Wk3──Wk4──...  │  │  🔴 Shortage  🟢 No Shortage  ││
│  └────────────────────────────┘  └──────────────────────────────┘│
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │          Staff Utilization by Department (Bar Chart)         │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

### Charts Detail

| Chart | Type | X-Axis | Y-Axis | Color |
|---|---|---|---|---|
| KPI Cards | Text/Number | — | Value | Blue/Red |
| Bed Utilization | Horizontal Bar | service | bed_utilization_pct | Red-Green scale |
| Available vs Occupied | Stacked Bar | service | available/admitted | Blue/Orange |
| Weekly Resource Trend | Line Chart | week | bed_utilization_pct | Teal |
| Shortage Heatmap | Highlight Table | week | service | Red/Green |
| Staff Utilization | Bar Chart | service | staff_utilization_pct | Purple |

---

## Cross-Dashboard Interaction Map

```
Dashboard 1 (Hospital Overview)
        ↓ Click Department
Dashboard 3 (Department Analytics)
        ↓ Click Department Name
        ↓────────────────────────────────┐
Dashboard 2 (Patient Flow)        Dashboard 4 (Resource Utilization)
Shows patient data for             Shows resource data for
selected department                selected department
```

---

## Color Scheme

| Color | Used For |
|---|---|
| 🔵 Blue | Admissions, Patient counts |
| 🟠 Orange | Discharges, LOS |
| 🟢 Green | Good performance, Efficiency |
| 🔴 Red | Shortage, Refused patients, High risk |
| 🟣 Purple | Staff metrics |
| 🩵 Teal | Trends, Resource utilization |

---

## Dashboard Design Rules

1. Every dashboard has the navigation bar at the top
2. Filters are placed below the navigation bar
3. KPI cards always appear in the top section
4. Charts fill the remaining space in a 2-column grid
5. Color coding is consistent across all dashboards
6. Font: Tableau default (Tableau Book)
7. Background: White (#FFFFFF)
8. All numbers are formatted with commas (56,500 not 56500)
9. Percentages shown with 1 decimal place (92.7%)
