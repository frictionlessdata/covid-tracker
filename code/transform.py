from frictionless import Resource, transform, steps

# Timeline

transform(
    Resource("data/timeline.csv"),
    steps=[
        steps.row_filter(function=lambda row: row["iso_code"] == "OWID_WRL"),
        steps.table_write(path="data/countries/owid_wrl/timeline.csv"),
    ],
)

# Latest

transform(
    Resource("data/latest.csv"),
    steps=[
        steps.row_filter(function=lambda row: row["iso_code"] == "OWID_WRL"),
        steps.table_write(path="data/countries/owid_wrl/latest.csv"),
    ],
)

# Regions

codes = ["OWID_AFR", "OWID_ASI", "OWID_EUR", "OWID_OCE", "OWID_NAM", "OWID_SAM"]
transform(
    Resource("data/latest.csv"),
    steps=[
        steps.table_normalize(),
        steps.row_filter(function=lambda row: row["iso_code"] in codes),
        steps.row_sort(field_names=["total_deaths_per_million"], reverse=True),
        steps.table_write(path="data/regions/latest.csv"),
    ],
)
