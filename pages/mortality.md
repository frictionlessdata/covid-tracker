# Excess Mortality

## Summary

Here is excess deaths by countries:

```yaml table
data:
  path: data/mortality.csv
  layout:
    pickFields:
      - Country
      - Excess Deaths
      - Excess per 100k
      - Undercount Ratio
filters: true
dropdownMenu: true
columnSorting:
  initialConfig:
    column: 1
    sortOrder: desc
width: 940
height: 300
colWidths: [300, 120, 120, 120]
stretchH: all
colHeaders:
  - Location
  - Deaths
  - Deaths/100k
  - Undercount
columns:
  - data: 0
  - data: 1
  - data: 2
  - data: 3
```

## Excess Deaths

The numbers are based on the World Mortality Dataset:

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
          "url": "../data/mortality.csv"
        },
        "key": "Country",
        "fields": ["Country", "Excess per 100k"]
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
      "field": "Excess per 100k",
      "type": "quantitative",
      "scale": {"scheme": "Reds"},
      "legend": {
          "title": "Excess/100k"
      }
    },
    "tooltip": [
      {
         "field": "properties.name",
         "type": "nominal",
         "title": "Country"
      },
      {
         "field": "Excess per 100k",
         "type": "quantitative",
         "title": "Excess/100k"
      }
    ]
  }
}
```
