# Milestone 4 – Testing & Validation
## MedTrack_DV | Hospital Operations & Patient Analytics Dashboard
### Infosys Springboard Virtual Internship

---

## Objective

Milestone 4 covers complete testing of the MedTrack_DV Power BI dashboard system before final GitHub submission. This includes data testing, KPI validation, dashboard functional testing, and final checklist completion.

---

## Milestone 4 Checklist

| Task | Status |
|---|---|
| ✅ Testing report template created | Complete |
| ✅ Validation checklist created | Complete |
| ⏳ Data Testing completed | Fill after testing |
| ⏳ KPI Testing – Python vs Power BI cross-check | Fill after testing |
| ⏳ Dashboard functional testing | Fill after testing |
| ⏳ Navigation testing | Fill after testing |
| ⏳ Filter/Slicer testing | Fill after testing |
| ⏳ Final validation checklist signed off | Fill after testing |
| ⏳ GitHub repository final review | Fill after testing |
| ⏳ Final submission completed | Fill after testing |

---

## Folder Structure

```
Milestone_4/
│
├── README.md                    ← This file
│
└── docs/
    ├── testing_report.md        ← Fill after testing dashboards
    └── validation_checklist.md  ← Fill after final review
```

---

## What to Test

### 1. Data Testing
Run `Milestone_1/notebooks/04_data_validation.ipynb` and check:
- Row counts match expected values
- No nulls in key columns
- No duplicate records
- All KPI values match Python output

### 2. Power BI Dashboard Testing
After building all 4 dashboards:
- All 6 KPI cards show correct values
- All charts load without errors
- All slicers filter data correctly
- Navigation buttons work on all pages
- Cross-dashboard interactions work

### 3. GitHub Testing
- All 4 milestone folders present
- Each milestone has README.md
- All notebooks run without errors
- All CSV files present in processed folder
- .pbix file present in Milestone_3/dashboard/

---

## Expected KPI Values

Use these to verify your Power BI dashboard is correct:

| KPI | Expected Value |
|---|---|
| Total Admissions | 56,500 |
| Occupancy Rate | 92.7% |
| Avg Length of Stay | 5.13 days |
| Readmission Rate | 12.7% |
| Bed Utilization Rate | 92.7% |
| ICU Efficiency Score | 92.15 |
| Surgery Efficiency Score | 88.69 |
| General Medicine Efficiency Score | 81.53 |
| Emergency Efficiency Score | 65.82 |

---

## Next Step

Fill in `docs/testing_report.md` and `docs/validation_checklist.md` after completing all dashboard testing, then do final GitHub push.
