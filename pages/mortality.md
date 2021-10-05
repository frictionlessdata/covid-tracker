# Excess Mortality

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
          "url": "../data/reports/mortality.csv"
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
          "title": "Deaths/100k"
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
         "title": "Deaths/100k"
      }
    ]
  }
}
```

## Summary

Here is excess deaths by countries:

```yaml table
data:
  path: data/reports/mortality.csv
  schema:
    missingValues: ['', 'NaN']
    fields:
      - name: Country
      - name: Excess deaths
      - name: Undercount ratio
      - name: Excess per 100k
  layout:
    pickFields:
      - Country
      - Excess deaths
      - Undercount ratio
      - Excess per 100k
filters: true
dropdownMenu: true
columnSorting:
  initialConfig:
    column: 1
    sortOrder: desc
width: 940
colWidths: [2, 1, 1, 1]
stretchH: all
colHeaders:
  - Location
  - Deaths
  - Deaths/100k
  - Undercount
columns:
  - data: 0
    disableVisualSelection: true
  - data: 1
  - data: 3
  - data: 2
```
