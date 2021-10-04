# Regions

## Deaths

Here is an interactive map showing amount of total deaths per region:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/regions.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "properties.CONTINENT",
      "from": {
        "data": {
          "url": "../data/reports/regions.csv"
        },
        "key": "location",
        "fields": ["location", "total_deaths_per_million"]
      }
    }
  ],
  "projection": {"type": "mercator"},
  "mark": {
    "type": "geoshape",
    "stroke": "#757575",
    "strokeWidth": 0.5
  },
  "encoding": {
    "color": {
      "field": "total_deaths_per_million",
      "type": "quantitative",
      "scale": {"scheme": "Reds"},
      "legend": {
          "title": "Deaths/1M"
      }
    },
    "tooltip": [
      {
         "field": "properties.CONTINENT",
         "type": "nominal",
         "title": "Region"
      },
      {
         "field": "total_deaths_per_million",
         "type": "quantitative",
         "title": "Deaths/1M"
      }
    ]
  }
}
```

## Total Cases

Here is an interactive map showing amount of total cases per region:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/regions.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "properties.CONTINENT",
      "from": {
        "data": {
          "url": "../data/reports/regions.csv"
        },
        "key": "location",
        "fields": ["location", "total_cases_per_million"]
      }
    }
  ],
  "projection": {"type": "mercator"},
  "mark": {
    "type": "geoshape",
    "stroke": "#757575",
    "strokeWidth": 0.5
  },
  "encoding": {
    "color": {
      "field": "total_cases_per_million",
      "type": "quantitative",
      "scale": {"scheme": "Blues"},
      "legend": {
          "title": "Deaths/1M"
      }
    },
    "tooltip": [
      {
         "field": "properties.CONTINENT",
         "type": "nominal",
         "title": "Region"
      },
      {
         "field": "total_cases_per_million",
         "type": "quantitative",
         "title": "Cases/1M"
      }
    ]
  }
}
```

## Vaccinations

Here is an interactive map showing amount of total shots taken per region:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/regions.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "properties.CONTINENT",
      "from": {
        "data": {
          "url": "../data/reports/regions.csv"
        },
        "key": "location",
        "fields": ["location", "total_vaccinations_per_hundred"]
      }
    }
  ],
  "projection": {"type": "mercator"},
  "mark": {
    "type": "geoshape",
    "stroke": "#757575",
    "strokeWidth": 0.5
  },
  "encoding": {
    "color": {
      "field": "total_vaccinations_per_hundred",
      "type": "quantitative",
      "scale": {"scheme": "Greens"},
      "legend": {
          "title": "Shots/100"
      }
    },
    "tooltip": [
      {
         "field": "properties.CONTINENT",
         "type": "nominal",
         "title": "Region"
      },
      {
         "field": "total_vaccinations_per_hundred",
         "type": "quantitative",
         "title": "Shots/100"
      }
    ]
  }
}
```

## Summary

Here is a summary of the key pandemic data by regions:

```yaml table
data:
  path: data/reports/regions.csv
  layout:
    pickFields:
      - iso_code
      - location
      - total_cases
      - total_deaths
      - total_cases_per_million
      - total_deaths_per_million
      - total_vaccinations
      - total_vaccinations_per_hundred
filters: true
dropdownMenu: true
columnSorting:
  initialConfig:
    column: 1
    sortOrder: desc
width: 940
colWidths: [2, 1, 1, 1, 1, 1, 1]
stretchH: all
colHeaders:
  - Location
  - Deaths
  - Deaths/1M
  - Cases
  - Cases/1M
  - Shots
  - Shots/100
columns:
  - data: 1
  - data: 3
  - data: 5
  - data: 2
  - data: 4
  - data: 6
  - data: 7
```
