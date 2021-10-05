from frictionless import Resource

FRAME = 180

# Helpers


def calculate_rolling_immunity(group):
    total_units = 0
    for number, row in enumerate(reversed(group[-FRAME:]), start=1):
        if not row["population"]:
            return 0
        new_vaccinations = float(row["new_vaccinations"] or 0)
        new_cases = float(row["new_deaths"] or 0) * 100
        #  new_cases = float(row["new_cases"] or 0) * 2
        row_units = (new_cases + new_vaccinations) * ((FRAME - number + 1) / FRAME)
        row_units = row_units / float(row["population"])
        total_units += row_units
    return round(total_units, 2)


def write_group(group):
    if group:
        row = group[-1].copy()
        path = f"data/locations/{row['iso_code']}/timeline.csv"
        Resource(group).write(path)
        if (row["population"] or 0) > 1000000:
            row["link"] = f"<a href='#card={row['iso_code']}'>{row['location']}</a>"
            immunity.append(row)
        print(f"Transformed timeline: {row['location']}")


# General


immunity = []
with Resource("data/timeline.csv") as resource:
    code = None
    group = []
    for row in resource:
        if code != row["iso_code"]:
            write_group(group)
            code = row["iso_code"]
            group = []
        row = row.to_dict()
        row["rolling_immunity"] = calculate_rolling_immunity(group)
        group.append(row)
    write_group(group)
Resource(immunity).write("data/reports/immunity.csv")
