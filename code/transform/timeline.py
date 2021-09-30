from frictionless import Resource

# General

with Resource("data/timeline.csv") as resource:
    code = None
    group = []
    for row in resource:
        path = f"data/locations/{code}/timeline.csv"
        if code != row["iso_code"]:
            if group:
                Resource(group).write(path)
            code = row["iso_code"]
            group = []
        group.append(row)
    if group:
        Resource(group).write(path)
