# World

```html markup
{% for row in frictionless.extract('data/countries/owid_wrl/latest.csv') %}
<div class="row">
  <div class="col-4">{{ row.total_deaths }}</div>
  <div class="col-4">{{ row.total_cases }}</div>
  <div class="col-4">{{ row.total_vaccinations }}</div>
</div>
{% endfor %}
```

## Deaths

```json chart
{
  "width": 800,
  "data": {"url": "data/countries/owid_wrl/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_deaths", "type": "quantitative"}
  },
  "mark": {
    "type": "area",
    "line": {"color": "red"},
    "color": {
      "x1": 1, "y1": 1, "x2": 1, "y2": 0, "gradient": "linear",
      "stops": [{"offset": 0, "color": "white"}, {"offset": 1, "color": "red"}]
    }
  }
}
```

## New Cases

```json chart
{
  "width": 800,
  "data": {"url": "data/countries/owid_wrl/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_cases", "type": "quantitative"}
  },
  "mark": {
    "type": "area",
    "line": {"color": "blue"},
    "color": {
      "x1": 1, "y1": 1, "x2": 1, "y2": 0, "gradient": "linear",
      "stops": [{"offset": 0, "color": "white"}, {"offset": 1, "color": "blue"}]
    }
  }
}
```

## Vaccinations

```json chart
{
  "mark": "bar",
  "width": 800,
  "data": {"url": "data/countries/owid_wrl/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_vaccinations", "type": "quantitative"}
  },
  "mark": {
    "type": "area",
    "line": {"color": "green"},
    "color": {
      "x1": 1, "y1": 1, "x2": 1, "y2": 0, "gradient": "linear",
      "stops": [{"offset": 0, "color": "white"}, {"offset": 1, "color": "green"}]
    }
  }
}
```
