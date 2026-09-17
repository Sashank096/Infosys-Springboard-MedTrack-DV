# MedTrack_DV – Power BI Setup Guide
## Milestone 3 | Infosys Springboard Virtual Internship

---

## Step 1 – Download Power BI Desktop

1. Go to: https://powerbi.microsoft.com/desktop
2. Click **Download Free**
3. Install it on your computer
4. Open Power BI Desktop

---

## Step 2 – Load the 4 Datasets

1. Click **Home** → **Get Data** → **Text/CSV**
2. Load these 4 files one by one from `Milestone_1/data/processed/`:

| File | Load As |
|---|---|
| hospital_overview_dataset.csv | hospital_overview_dataset |
| patient_flow_dataset.csv | patient_flow_dataset |
| department_analytics_dataset.csv | department_analytics_dataset |
| resource_utilization_dataset.csv | resource_utilization_dataset |

3. Also load:
   - `normalized_readmission.csv` (for readmission rate KPI)

---

## Step 3 – Transform Data (Power Query)

After loading each file, click **Transform Data** to open Power Query Editor.

### For hospital_overview_dataset:
- Check `admission_date` column → Change Type → **Date**
- Check `discharge_date` column → Change Type → **Date**
- Check `length_of_stay_days` → Change Type → **Whole Number**
- Close & Apply

### For patient_flow_dataset:
- `date_of_admission` → Change Type → **Date**
- `discharge_date` → Change Type → **Date**
- `billing_amount` → Change Type → **Decimal Number**
- `length_of_stay_days` → Change Type → **Whole Number**
- Close & Apply

### For department_analytics_dataset:
- `bed_utilization_rate` → Change Type → **Decimal Number**
- `department_efficiency_score` → Change Type → **Decimal Number**
- `patient_satisfaction` → Change Type → **Decimal Number**
- Close & Apply

### For resource_utilization_dataset:
- `bed_utilization_pct` → Change Type → **Decimal Number**
- `shortage_flag` → Change Type → **True/False**
- Close & Apply

---

## Step 4 – Create Relationships

Go to **Model View** (icon on the left sidebar that looks like 3 boxes).

Create these relationships:

| From Table | From Field | To Table | To Field | Cardinality |
|---|---|---|---|---|
| hospital_overview_dataset | dept_name | department_analytics_dataset | service | Many to Many |
| department_analytics_dataset | service | resource_utilization_dataset | service | Many to Many |
| department_analytics_dataset | week | resource_utilization_dataset | week | Many to Many |

**Note:** patient_flow_dataset stays separate (different grain — do NOT connect it to the others)

---

## Step 5 – Add All DAX Measures

See `docs/dax_measures.md` for all 28 measures.

To add a measure:
1. Click on the table name in the Fields pane (right side)
2. Click **Home** → **New Measure**
3. Paste the DAX formula
4. Press Enter

---

## Step 6 – Build Dashboard 1 (Hospital Overview)

### Page Setup:
- Right click on Page 1 at bottom → **Rename** → type `Hospital Overview`
- Go to **View** → **Page Size** → **16:9**

### Add Navigation Buttons (Top):
1. Click **Insert** → **Buttons** → **Blank**
2. Create 4 buttons: Home | Patient Flow | Departments | Resources
3. Format each button with text, border, background color
4. For navigation: select button → **Action** → **Page Navigation** → select target page

### Add KPI Cards:
1. Click **Visualizations** → **Card** visual
2. Drag your measure into the **Fields** well

Create these 6 cards:
| Card | Measure | Format |
|---|---|---|
| Total Admissions | Total Admissions | Whole number, comma |
| Occupancy Rate | Occupancy Rate % | 1 decimal, add % |
| Avg LOS | Avg Length of Stay | 2 decimals, add " days" |
| Readmission Rate | Readmission Rate % | 1 decimal, add % |
| Bed Utilization | Bed Utilization Rate % | 1 decimal, add % |
| Total Beds | Total Available Beds | Whole number |

### Add Monthly Trend Chart:
1. Click **Line Chart** visual
2. X-axis: `admission_month_name` from hospital_overview_dataset
3. Y-axis: `Total Admissions` measure
4. Sort by month number (add `admission_month` as sort column)

### Add Admissions vs Discharges (Clustered Bar):
1. Click **Clustered Bar Chart**
2. Y-axis: `admission_month_name`
3. X-axis: `Total Admissions` measure
4. Add second bar for discharge count

### Add Dept Efficiency Score (Horizontal Bar):
1. Click **Bar Chart**
2. Y-axis: `service` from department_analytics_dataset
3. X-axis: `Avg Efficiency Score` measure
4. Sort descending by score
5. Add conditional formatting → use `Efficiency Color` measure

---

## Step 7 – Build Dashboard 2 (Patient Flow)

- Rename page: `Patient Flow`

### Visuals to add:

| Visual | Type | Fields |
|---|---|---|
| Admission Trend | Line Chart | date_of_admission (X), count of rows (Y) |
| Admission Type | Donut Chart | admission_type (Legend), count (Values) |
| Avg LOS by Condition | Horizontal Bar | medical_condition (Y), Patient Flow Avg LOS (X) |
| Day of Week Volume | Column Bar | day_of_week (X), count (Y) |
| Test Results | Pie / Bar | test_results (Legend), count (Values) |
| Billing Trend | Line Chart | date_of_admission (X), Total Billing Amount (Y) |

---

## Step 8 – Build Dashboard 3 (Department Analytics)

- Rename page: `Department Analytics`

### Visuals to add:

| Visual | Type | Fields |
|---|---|---|
| Dept Admissions | Bar Chart | service (Y), Total Dept Admissions (X) |
| Efficiency Score Ranking | Bar Chart (sorted) | service (Y), Avg Efficiency Score (X) |
| Weekly Heatmap | Matrix | service (Rows), week (Columns), bed_utilization_rate (Values) |
| Refused Patients | Bar Chart | service (Y), Total Dept Refused (X) |
| Satisfaction Score | Bar Chart | service (Y), Avg Patient Satisfaction (X) |
| Staff Morale Trend | Line Chart | week (X), Avg Staff Morale (Y), service (Legend) |

### Add Department Drill-through:
1. Click on Dept Admissions bar chart
2. Right pane → **Drill through** → add `service` field
3. This lets user click a department and go to its detail

---

## Step 9 – Build Dashboard 4 (Resource Utilization)

- Rename page: `Resource Utilization`

### Add Summary Cards (top row):

| Card | Measure |
|---|---|
| Total Beds | Total Available Beds |
| Occupied Beds | Total Occupied Beds |
| Available Beds | Beds Remaining |
| Shortage Depts | Shortage Departments |

### Visuals to add:

| Visual | Type | Fields |
|---|---|---|
| Bed Utilization by Dept | Horizontal Bar | service (Y), Bed Utilization Rate % (X) |
| Available vs Occupied | Stacked Bar | service (Y), available_beds + patients_admitted (X) |
| Weekly Trend | Line Chart | week (X), Bed Utilization Rate % (Y), service (Legend) |
| Shortage Heatmap | Matrix | service (Rows), week (Cols), shortage_flag (Values) |
| Staff Utilization | Bar Chart | service (Y), Staff Utilization Rate % (X) |

---

## Step 10 – Add Global Filters (Slicers)

On EVERY page, add these slicers:

1. Click **Slicer** visual
2. Add these one by one:

| Slicer | Field | Style |
|---|---|---|
| Hospital | hospital_name | Dropdown |
| Department | service / dept_name | Dropdown |
| Year | admission_year | Dropdown |
| Month | admission_month_name | Dropdown |

To sync slicers across all pages:
- Click **View** → **Sync Slicers**
- Select the slicer → check all 4 pages in the sync panel

---

## Step 11 – Cross-Page Interactions

### Set up Drill-through (Department click → Patient Flow):
1. Go to Patient Flow page
2. Fields pane → Drill through section → drag `medical_condition`
3. Now right-click any department bar → Drill through → Patient Flow

### Set up Bookmarks for Navigation:
1. Click **View** → **Bookmarks**
2. Create one bookmark per page
3. Assign bookmark to each navigation button

---

## Step 12 – Format and Design

### Color Theme:
| Element | Color |
|---|---|
| Good/Success | #1D9E75 (Teal) |
| Warning | #EF9F27 (Amber) |
| Danger/Alert | #E24B4A (Red) |
| Primary | #378ADD (Blue) |
| Secondary | #7F77DD (Purple) |
| Background | #F8F9FA (Light Gray) |
| Card Background | #FFFFFF (White) |

### Font:
- Title: Segoe UI Semibold, 14px
- Labels: Segoe UI, 11px
- Values: Segoe UI Bold, 24px (KPI cards)

### Apply to all pages:
- Background: Light gray (#F8F9FA)
- All cards: White background, light border
- All chart titles: Bold, 12px

---

## Step 13 – Final Export

1. **Save** the file as `MedTrack_DV.pbix`
2. Place it in `Milestone_3/dashboard/`
3. Take screenshots of all 4 dashboard pages
4. Save screenshots in `Milestone_3/screenshots/`
   - `01_hospital_overview.png`
   - `02_patient_flow.png`
   - `03_department_analytics.png`
   - `04_resource_utilization.png`
5. Push everything to GitHub
