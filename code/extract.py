from frictionless import Resource

OWID = "https://covid.ourworldindata.org/data"
GITHUB = "https://raw.githubusercontent.com"

# Timeline

resource = Resource(f"{OWID}/owid-covid-data.csv")
resource.write("data/timeline.csv")

# Latest

resource = Resource(f"{OWID}/latest/owid-covid-latest.csv")
resource.write("data/latest.csv")

# Mortality

resource = Resource(f"{GITHUB}/dkobak/excess-mortality/main/excess-mortality.csv")
resource.write("data/mortality.csv")
