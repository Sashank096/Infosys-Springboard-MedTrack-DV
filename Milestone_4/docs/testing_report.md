# MedTrack_DV – Testing Report
## Milestone 4 | Infosys Springboard Virtual Internship

---

## 1. Data Testing Results

### Row Count Verification

| Dataset | Expected Rows | Actual Rows | Status |
|---|---|---|---|
| hospital_overview_dataset.csv | 1,000+ | _(fill after running notebook)_ | ⏳ |
| patient_flow_dataset.csv | 55,500 | _(fill after running notebook)_ | ⏳ |
| department_analytics_dataset.csv | 208 | _(fill after running notebook)_ | ⏳ |
| resource_utilization_dataset.csv | 208 | _(fill after running notebook)_ | ⏳ |
| normalized_readmission.csv | 15,757 | _(fill after running notebook)_ | ⏳ |

### Missing Value Check

| Dataset | Missing % | Target | Status |
|---|---|---|---|
| hospital_overview_dataset.csv | _(fill)_ | < 2% | ⏳ |
| patient_flow_dataset.csv | _(fill)_ | < 2% | ⏳ |
| department_analytics_dataset.csv | _(fill)_ | < 2% | ⏳ |
| resource_utilization_dataset.csv | _(fill)_ | < 2% | ⏳ |

### Duplicate Check

| Dataset | Duplicates Found | Status |
|---|---|---|
| hospital_overview_dataset.csv | _(fill)_ | ⏳ |
| patient_flow_dataset.csv | _(fill)_ | ⏳ |
| department_analytics_dataset.csv | _(fill)_ | ⏳ |
| resource_utilization_dataset.csv | _(fill)_ | ⏳ |

---

## 2. KPI Validation – Python vs Power BI

| KPI | Python Value | Power BI Value | Match? |
|---|---|---|---|
| Total Admissions | 56,500 | _(fill)_ | ⏳ |
| Occupancy Rate | 92.7% | _(fill)_ | ⏳ |
| Avg Length of Stay | 5.13 days | _(fill)_ | ⏳ |
| Readmission Rate | 12.7% | _(fill)_ | ⏳ |
| Bed Utilization Rate | 92.7% | _(fill)_ | ⏳ |
| ICU Efficiency Score | 92.15 | _(fill)_ | ⏳ |
| Surgery Efficiency Score | 88.69 | _(fill)_ | ⏳ |
| Gen Med Efficiency Score | 81.53 | _(fill)_ | ⏳ |
| Emergency Efficiency Score | 65.82 | _(fill)_ | ⏳ |

---

## 3. Dashboard Functional Testing

### Dashboard 1 – Hospital Overview

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Total Admissions card shows | 56,500 | _(fill)_ | ⏳ |
| Occupancy Rate card shows | 92.7% | _(fill)_ | ⏳ |
| Avg LOS card shows | 5.13 days | _(fill)_ | ⏳ |
| Readmission Rate card shows | 12.7% | _(fill)_ | ⏳ |
| Bed Utilization card shows | 92.7% | _(fill)_ | ⏳ |
| Monthly trend line chart loads | Chart visible | _(fill)_ | ⏳ |
| Dept efficiency bar chart loads | 4 departments shown | _(fill)_ | ⏳ |
| Donut chart loads | 3 admission types | _(fill)_ | ⏳ |

### Dashboard 2 – Patient Flow

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Admission trend loads | Line chart visible | _(fill)_ | ⏳ |
| Admission type donut loads | Emergency/Elective/Urgent | _(fill)_ | ⏳ |
| LOS by condition loads | 6 conditions shown | _(fill)_ | ⏳ |
| Day of week chart loads | Mon–Sun bars visible | _(fill)_ | ⏳ |
| Test results chart loads | Normal/Abnormal/Inconclusive | _(fill)_ | ⏳ |

### Dashboard 3 – Department Analytics

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Dept admissions chart loads | 4 departments | _(fill)_ | ⏳ |
| Efficiency score ranking loads | ICU top, Emergency bottom | _(fill)_ | ⏳ |
| Weekly heatmap loads | Grid visible | _(fill)_ | ⏳ |
| Refused patients chart loads | Emergency highest | _(fill)_ | ⏳ |
| Satisfaction score chart loads | Scores visible | _(fill)_ | ⏳ |

### Dashboard 4 – Resource Utilization

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Total beds card shows | 500 | _(fill)_ | ⏳ |
| Bed utilization chart loads | 4 departments | _(fill)_ | ⏳ |
| Stacked bar chart loads | Available vs occupied | _(fill)_ | ⏳ |
| Weekly trend loads | Line chart visible | _(fill)_ | ⏳ |
| Shortage heatmap loads | Red/green matrix | _(fill)_ | ⏳ |

---

## 4. Navigation Testing

| Test | Expected Result | Status |
|---|---|---|
| Home button → Hospital Overview | Opens page 1 | ⏳ |
| Patient Flow button → Page 2 | Opens page 2 | ⏳ |
| Departments button → Page 3 | Opens page 3 | ⏳ |
| Resources button → Page 4 | Opens page 4 | ⏳ |
| Back navigation works | Returns to previous page | ⏳ |

---

## 5. Slicer / Filter Testing

| Slicer | Test Action | Expected Result | Status |
|---|---|---|---|
| Hospital filter | Select a hospital | All charts update | ⏳ |
| Department filter | Select ICU | All charts filter to ICU | ⏳ |
| Year filter | Select 2023 | Only 2023 data shown | ⏳ |
| Month filter | Select January | Only January data shown | ⏳ |
| Reset filters | Click reset | All data shown again | ⏳ |
| Slicer sync | Change filter on page 1 | Same filter on all pages | ⏳ |

---

## 6. Cross-Dashboard Interaction Testing

| Test | Expected Result | Status |
|---|---|---|
| Click dept in Dashboard 3 | Dashboard 2 filters to that dept | ⏳ |
| Click dept in Dashboard 3 | Dashboard 4 filters to that dept | ⏳ |
| Drill-through works | Detail page opens | ⏳ |

---

## 7. Final Testing Summary

| Category | Tests Passed | Tests Failed | Status |
|---|---|---|---|
| Data Testing | _(fill)_ | _(fill)_ | ⏳ |
| KPI Validation | _(fill)_ | _(fill)_ | ⏳ |
| Dashboard Testing | _(fill)_ | _(fill)_ | ⏳ |
| Navigation Testing | _(fill)_ | _(fill)_ | ⏳ |
| Filter Testing | _(fill)_ | _(fill)_ | ⏳ |
| **Overall** | _(fill)_ | _(fill)_ | ⏳ |

---

## 8. Issues Found & Fixed

| Issue | Dashboard | Fix Applied | Status |
|---|---|---|---|
| _(fill any issues found)_ | _(fill)_ | _(fill)_ | ⏳ |

---

## Sign Off

| Item | Details |
|---|---|
| Tested by | _(your name)_ |
| Date | _(fill date)_ |
| Power BI File | MedTrack_DV.pbix |
| Final Status | ⏳ Pending |
