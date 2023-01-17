# Data Collection

All data on this site was generated (cleaned, analysed) using the [Frictionless Python Framework](https://framework.frictionlessdata.io/) on openly availabe data. The data is from [Our World in Data](https://ourworldindata.org/coronavirus) and [Excess Mortality](https://github.com/dkobak/excess-mortality). Read on to see the Frictionless code that was used to analyse the data.

## Extract

First of all, we need to extract all the data from [Our World in Data](https://ourworldindata.org/coronavirus) and [Excess Mortality](https://github.com/dkobak/excess-mortality) repositories:

```python task id=data-extract
from frictionless import Resource

OWID = "https://covid.ourworldindata.org/data"
GITHUB = "https://raw.githubusercontent.com"

# Timeline

resource = Resource(f"{OWID}/owid-covid-data.csv")
resource.write("data/timeline.csv")
print(f"Extracted: timeline")

# Latest

resource = Resource(f"{OWID}/latest/owid-covid-latest.csv")
resource.write("data/latest.csv")
print(f"Extracted: latest")

# Mortality

resource = Resource(f"{GITHUB}/dkobak/excess-mortality/main/excess-mortality.csv")
resource.write("data/reports/mortality.csv")
print(f"Extracted: reports/mortality")
```

## Transform

We will split the data by location and calculate rolling immunity:

```python task id=data-transform-timeline
from pprint import pprint
from frictionless import Resource, Detector

FRAME = 180
detector = Detector(sample_size=10000)

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
        Resource(group, detector=detector).write(path)
        if (row["population"] or 0) > 1000000:
            row["link"] = f"<a href='#card={row['iso_code']}'>{row['location']}</a>"
            immunity.append(row)
        print(f"Transformed timeline: {row['location']}")

# General

immunity = []
with Resource("data/timeline.csv", detector=detector) as resource:
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
```

Also, we need to transform `data/latest.csv`:

```python task id=data-transform-latest
from frictionless import Resource

WORLD = ["OWID_WRL"]
REGIONS = ["OWID_AFR", "OWID_ASI", "OWID_EUR", "OWID_OCE", "OWID_NAM", "OWID_SAM"]

# General

world = []
regions = []
countries = []
with Resource("data/latest.csv") as resource:
    for row in resource.row_stream:
        row = row.to_dict()
        code = row["iso_code"]
        row["link"] = f"<a href='#card={code}'>{row['location']}</a>"
        path = f"data/locations/{code}/latest.csv"
        Resource([row]).write(path)
        if code in WORLD:
            world.append(row)
        elif code in REGIONS:
            regions.append(row)
        elif not code.startswith("OWID"):
            countries.append(row)
Resource(world).write("data/reports/world.csv")
Resource(regions).write("data/reports/regions.csv")
Resource(countries).write("data/reports/countries.csv")
print("Transformed latest")
```

## Load

To show different locations as cards we render them:

```python task id=data-load
from frictionless import Resource
from livemark.plugins.cards import CardsPlugin

# General

CardsPlugin.delete_cards()
with Resource("data/latest.csv") as resource:
    for row in resource.row_stream:
        code = row["iso_code"]
        CardsPlugin.create_card("cards/location.md", code=code, data=row)
        print(f"Loaded: {row['location']}")
```
