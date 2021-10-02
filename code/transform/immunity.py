from frictionless import Resource, Field, transform, steps

FRAME = 180

# Helpers


def add_immunity_field(resource):
    current = resource.to_copy()
    buffer = []

    # Data
    def data():
        with current:
            for row in current.row_stream:
                buffer.append(row)
                immunity = calculate_immunity(buffer)
                row = row.to_dict()
                row["rolling_immunity"] = immunity
                yield row

    # Meta
    resource.data = data
    resource.schema.add_field(Field(name="rolling_immunity", type="number"))


def calculate_immunity(buffer):
    total_units = 0
    for number, row in enumerate(reversed(buffer[-FRAME:]), start=1):
        new_vaccinations = float(row["new_vaccinations"] or 0)
        new_cases = float(row["new_deaths"] or 0) * 100
        #  new_cases = float(row["new_cases"] or 0) * 2
        row_units = (new_cases + new_vaccinations) * ((FRAME - number + 1) / FRAME)
        row_units = row_units / float(row["population"])
        total_units += row_units
    return total_units


# General

for code in ["ISR", "USA", "DEU", "GBR", "BRA"]:
    transform(
        Resource(f"data/locations/{code}/timeline.csv"),
        steps=[
            steps.table_normalize(),
            add_immunity_field,
            steps.table_write(path=f"data/locations/{code}/immunity.csv"),
        ],
    )
