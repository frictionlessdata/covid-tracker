from frictionless import Resource

REGIONS = ["OWID_AFR", "OWID_ASI", "OWID_EUR", "OWID_OCE", "OWID_NAM", "OWID_SAM"]

# General

regions = []
countries = []
with Resource("data/latest.csv") as resource:
    for row in resource:
        row = row.to_dict()
        code = row["iso_code"]
        row["link"] = f"<a href='#card={code}'>{row['location']}</a>"
        path = f"data/locations/{code}/latest.csv"
        Resource([row]).write(path)
        if code in REGIONS:
            regions.append(row)
        elif not code.startswith("OWID"):
            countries.append(row)
Resource(regions).write("data/reports/regions.csv")
Resource(countries).write("data/reports/countries.csv")
