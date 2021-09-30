# {{ data.location }}

## Status

The main three core metrics we track: total deaths, total cases, and all the vaccination shots taken:

```html markup
<div class="status row">
  <div class="col-sm-4">
    <div role="button" class="btn btn-danger w-100">
      Deaths<br>
      <span class="badge badge-light">
        {{ ((data.total_deaths or 0)/1000000) | round(1) }}M
      </span>
    </div>
  </div>
  <div class="col-sm-4">
    <div role="button" class="btn btn-primary w-100">
      Cases<br>
      <span class="badge badge-light">
        {{ ((data.total_cases or 0)/1000000) | round(1) }}M
      </span>
    </div>
  </div>
  <div class="col-sm-4">
    <div role="button" class="btn btn-success w-100">
      Vaccinations<br>
      <span class="badge badge-light">
        {{ ((data.total_vaccinations or 0)/1000000) | round(1) }}M
      </span>
    </div>
  </div>
</div>
```

## Deaths

Here is a timeline of the worldwide deaths caused by the COVID-19 pandemic:

```json chart
{
  "width": 800,
  "data": {"url": "data/locations/{{ code }}/timeline.csv"},
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
