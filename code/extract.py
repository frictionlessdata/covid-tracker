from frictionless import Resource

BASEURL = "https://covid.ourworldindata.org/data"

# Timeline

resource = Resource(f"{BASEURL}/owid-covid-data.csv")
resource.write("data/timeline.csv")

# Latest

resource = Resource(f"{BASEURL}/latest/owid-covid-latest.csv")
resource.write("data/latest.csv")
