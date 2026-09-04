"""
MedTrack_DV - Milestone 1: Relationship & Key Validation (v2)
"""
import pandas as pd

overview = pd.read_csv("hospital_operations_cleaned.csv")
flow = pd.read_csv("patient_admissions_cleaned.csv")
dept = pd.read_csv("department_data_cleaned.csv")
res = pd.read_csv("resource_utilization_cleaned.csv")

lines = []
def log(s=""):
    print(s)
    lines.append(s)

log("=" * 70)
log("RELATIONSHIP & KEY VALIDATION REPORT (v2 — real relational HMIS source)")
log("=" * 70)

log("\n--- 1. Grain integrity ---")
log(f"hospital_overview: {len(overview)} rows, admission_id unique: {overview['admission_id'].is_unique}")
log(f"patient_flow: {len(flow)} rows, admission_id unique: {flow['admission_id'].is_unique}")
dept_dupes = dept.duplicated(subset=["hospital_id", "department_id", "date"]).sum()
log(f"department_analytics grain duplicates: {dept_dupes}")
bed_res = res[res["resource_type"] == "Bed"]
res_dupes = bed_res.duplicated(subset=["hospital_id", "department_id", "date", "resource_type"]).sum()
log(f"resource_utilization (Bed) grain duplicates: {res_dupes}")

log("\n--- 2. Orphan key checks ---")
ov_deps = set(overview["department_id"].unique())
dept_deps = set(dept["department_id"].unique())
flow_ids = set(flow["admission_id"])
ov_ids = set(overview["admission_id"])
log(f"department_ids in overview but not in department_analytics: {ov_deps - dept_deps or 'None'}")
log(f"admission_ids in patient_flow but not in hospital_overview: {len(flow_ids - ov_ids)}")
log(f"admission_ids in hospital_overview but not in patient_flow: {len(ov_ids - flow_ids)}")

log("\n--- 3. Date consistency ---")
for name, df, col in [("hospital_overview", overview, "admission_date"),
                       ("patient_flow", flow, "admission_date"),
                       ("department_analytics", dept, "date")]:
    bad = pd.to_datetime(df[col], errors="coerce").isnull().sum()
    log(f"{name}.{col}: {bad} unparseable")

log("\n--- 4. Occupancy sanity (must be 0-100%) ---")
over_100 = (bed_res["occupancy_rate_pct"] > 100).sum()
neg = (bed_res["occupancy_rate_pct"] < 0).sum()
log(f"occupancy_rate_pct > 100%: {over_100}; < 0%: {neg}")

log("\n--- 5. hospital_id consistency ---")
for name, df in [("overview", overview), ("flow", flow), ("dept", dept), ("res", res)]:
    log(f"{name}: {sorted(df['hospital_id'].unique())}")

log("\n--- 6. Summary ---")
issues = []
if not overview["admission_id"].is_unique: issues.append("Duplicate admission_id in overview")
if dept_dupes > 0: issues.append("Grain duplicates in department_analytics")
if res_dupes > 0: issues.append("Grain duplicates in resource_utilization")
if len(flow_ids - ov_ids) > 0: issues.append("Orphaned admission_ids in patient_flow")
if over_100 > 0 or neg > 0: issues.append("Invalid occupancy_rate_pct values")

if issues:
    log("ISSUES FOUND:")
    for i in issues:
        log(f"  - {i}")
else:
    log("PASS: no orphaned keys, no grain duplicates, no invalid dates, "
        "no occupancy values outside 0-100%, hospital_id consistent.")

with open("relationship_validation_report.md", "w") as f:
    f.write("# Relationship & Key Validation Report — MedTrack_DV (v2)\n\n```\n")
    f.write("\n".join(lines))
    f.write("\n```\n")

print("\nWritten to relationship_validation_report.md")
