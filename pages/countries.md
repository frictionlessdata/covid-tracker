# Countries

## Deaths

Here is an interactive map showing amount of total deaths per country:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/countries.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "id",
      "from": {
        "data": {
          "url": "../data/reports/countries.csv"
        },
        "key": "iso_code",
        "fields": ["iso_code", "total_deaths_per_million"]
      }
    },
    {
      "calculate": "'#card=' + datum.iso_code", "as": "url"
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
         "field": "properties.name",
         "type": "nominal",
         "title": "Country"
      },
      {
         "field": "total_deaths_per_million",
         "type": "quantitative",
         "title": "Deaths/1M"
      }
    ],
    "href": {"field": "url", "type": "nominal"}
  }
}
```

## Total Cases

Here is an interactive map showing amount of total cases per country:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/countries.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "id",
      "from": {
        "data": {
          "url": "../data/reports/countries.csv"
        },
        "key": "iso_code",
        "fields": ["iso_code", "total_cases_per_million"]
      }
    },
    {
      "calculate": "'#card=' + datum.iso_code", "as": "url"
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
          "title": "Cases/1M"
      }
    },
    "tooltip": [
      {
         "field": "properties.name",
         "type": "nominal",
         "title": "Country"
      },
      {
         "field": "total_cases_per_million",
         "type": "quantitative",
         "title": "Cases/1M"
      }
    ],
    "href": {"field": "url", "type": "nominal"}
  }
}
```

## Vaccinations

Here is an interactive map showing amount of total shots taken per country:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/countries.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "properties.name",
      "from": {
        "data": {
          "url": "../data/reports/countries.csv"
        },
        "key": "location",
        "fields": ["location", "total_vaccinations_per_hundred"]
      }
    },
    {
      "calculate": "'#card=' + datum.iso_code", "as": "url"
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
         "field": "properties.name",
         "type": "nominal",
         "title": "Country"
      },
      {
         "field": "total_vaccinations_per_hundred",
         "type": "quantitative",
         "title": "Shots/100"
      }
    ],
    "href": {"field": "url", "type": "nominal"}
  }
}
```

## Summary

Here is a summary of the key pandemic data by countries:

```yaml table
data:
  path: data/reports/countries.csv
  layout:
    pickFields:
      - total_cases
      - total_deaths
      - total_cases_per_million
      - total_deaths_per_million
      - total_vaccinations
      - total_vaccinations_per_hundred
      - link
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
  - data: 6
    renderer: html
    readOnly: true
    disableVisualSelection: true
  - data: 1
  - data: 3
  - data: 0
  - data: 2
  - data: 4
  - data: 5
```
