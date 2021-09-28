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
