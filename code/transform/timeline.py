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
    return total_units


# General


with Resource("data/timeline.csv") as resource:
    code = None
    group = []
    for row in resource:
        row = row.to_dict()
        row["rolling_immunity"] = calculate_rolling_immunity(group)
        path = f"data/locations/{code}/timeline.csv"
        if code != row["iso_code"]:
            if group:
                Resource(group).write(path)
            code = row["iso_code"]
            group = []
        group.append(row)
    if group:
        Resource(group).write(path)
