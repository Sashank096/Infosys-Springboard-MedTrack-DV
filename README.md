# MedTrack DV

MedTrack is a hospital performance intelligence project for operational and
patient-care analytics. It converts a relational HMIS source into four
analysis-ready tables while preserving the grain and relationships of each
dataset.

## Repository structure

```text
MedTrack-DV/
├── data/
│   ├── raw/                 Source HMIS CSV files
│   └── cleaned/             Four generated analytical tables
├── docs/                    Data model, cleaning, quality, and KPI notes
├── notebooks/               Exploratory analysis and dashboard preparation
├── scripts/
│   ├── build_datasets.py    ETL and analytical table generation
│   └── validate_datasets.py Relationship, grain, and quality checks
└── README.md
```

This layout follows the reference analytics repository: raw data, cleaned
data, and analysis work are separated from reproducible project documentation.

## Reproduce the pipeline

From the repository root:

```bash
pip install pandas numpy
python scripts/build_datasets.py
python scripts/validate_datasets.py
```

Generated CSVs are written to `data/cleaned/`. The validation report is written
to `docs/relationship_validation_report.md`.

## Analytical outputs

- `hospital_operations_cleaned.csv`: one row per admission
- `patient_admissions_cleaned.csv`: one row per admission assignment
- `department_data_cleaned.csv`: one hospital, department, and day
- `resource_utilization_cleaned.csv`: one hospital, department, day, and resource type

See `docs/DATA_MODEL.md` for grains and relationships, and
`docs/KPI_DEFINITIONS.md` for the documented KPI formulas.