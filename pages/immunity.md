# Rolling Immunity

## Methodolody

## Countries

### Israel

```json chart
{
  "width": 750,
  "data": {"url": "../data/locations/ISR/immunity.csv"},
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
  "width": 750,
  "data": {"url": "../data/locations/GBR/immunity.csv"},
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
  "width": 750,
  "data": {"url": "../data/locations/USA/immunity.csv"},
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
  "width": 750,
  "data": {"url": "../data/locations/DEU/immunity.csv"},
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
  "width": 750,
  "data": {"url": "../data/locations/BRA/immunity.csv"},
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

### Summary
