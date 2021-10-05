# Rolling Immunity

## Methodolody

## Countries

### Israel

```json chart
{
  "width": 800,
  "data": {"url": "../data/locations/ISR/timeline.csv"},
  "resolve": {"scale": {"y": "independent"}},
  "encoding": {
    "x": {"field": "date", "type": "temporal"}
  },
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_deaths_per_million", "type": "quantitative"},
        "color": {"value": "red"}
      }
    },
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "rolling_immunity", "type": "quantitative"},
        "color": {"value": "green"}
      }
    }
  ]
}
```

### USA

```json chart
{
  "width": 800,
  "data": {"url": "../data/locations/USA/timeline.csv"},
  "resolve": {"scale": {"y": "independent"}},
  "encoding": {
    "x": {"field": "date", "type": "temporal"}
  },
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_deaths_per_million", "type": "quantitative"},
        "color": {"value": "red"}
      }
    },
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "rolling_immunity", "type": "quantitative"},
        "color": {"value": "green"}
      }
    }
  ]
}
```

### UK


```json chart
{
  "width": 800,
  "data": {"url": "../data/locations/GBR/timeline.csv"},
  "resolve": {"scale": {"y": "independent"}},
  "encoding": {
    "x": {"field": "date", "type": "temporal"}
  },
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_deaths_per_million", "type": "quantitative"},
        "color": {"value": "red"}
      }
    },
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "rolling_immunity", "type": "quantitative"},
        "color": {"value": "green"}
      }
    }
  ]
}
```

### Germany

```json chart
{
  "width": 800,
  "data": {"url": "../data/locations/DEU/timeline.csv"},
  "resolve": {"scale": {"y": "independent"}},
  "encoding": {
    "x": {"field": "date", "type": "temporal"}
  },
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_deaths_per_million", "type": "quantitative"},
        "color": {"value": "red"}
      }
    },
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "rolling_immunity", "type": "quantitative"},
        "color": {"value": "green"}
      }
    }
  ]
}
```

### Brasil

```json chart
{
  "width": 800,
  "data": {"url": "../data/locations/BRA/timeline.csv"},
  "resolve": {"scale": {"y": "independent"}},
  "encoding": {
    "x": {"field": "date", "type": "temporal"}
  },
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_deaths_per_million", "type": "quantitative"},
        "color": {"value": "red"}
      }
    },
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "rolling_immunity", "type": "quantitative"},
        "color": {"value": "green"}
      }
    }
  ]
}
```

## Summary

Here is a summary of the key pandemic data by countries:

```yaml table
data:
  path: data/reports/immunity.csv
  layout:
    pickFields:
      - new_cases_smoothed_per_million
      - new_deaths_smoothed_per_million
      - rolling_immunity
      - link
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
  - Immunity
  - Deaths/1M
  - Cases/1M
columns:
  - data: 3
    renderer: html
    readOnly: true
    disableVisualSelection: true
  - data: 2
  - data: 1
  - data: 0
```
