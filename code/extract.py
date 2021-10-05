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
