# {{ data.location }}

{% set total_deaths = data.total_deaths or 0 %}
{% set total_cases = data.total_cases or 0 %}
{% set total_vaccinations = data.total_vaccinations or 0 %}

## Status

The main three core metrics we track: total deaths, total cases, and all the vaccination shots taken:

```html markup
<div class="status row">
  <div class="col-sm-4">
    <div role="button" class="btn btn-danger w-100">
      Deaths<br>
      <span class="badge badge-light">
        {% if total_deaths > 1000000 %}
        {{ (total_deaths/1000000) | round(1) }}M
        {% elif total_deaths > 1000 %}
        {{ (total_deaths/1000) | round(1) }}K
        {% else %}
        {{ total_deaths | round(0) }}
        {% endif %}
      </span>
    </div>
  </div>
  <div class="col-sm-4">
    <div role="button" class="btn btn-primary w-100">
      Cases<br>
      <span class="badge badge-light">
        {% if total_cases > 1000000 %}
        {{ (total_cases/1000000) | round(1) }}M
        {% elif total_cases > 1000 %}
        {{ (total_cases/1000) | round(1) }}K
        {% else %}
        {{ total_cases | round(0) }}
        {% endif %}
      </span>
    </div>
  </div>
  <div class="col-sm-4">
    <div role="button" class="btn btn-success w-100">
      Vaccinations<br>
      <span class="badge badge-light">
        {% if total_vaccinations > 1000000 %}
        {{ (total_vaccinations/1000000) | round(1) }}M
        {% elif total_vaccinations > 1000 %}
        {{ (total_vaccinations/1000) | round(1) }}K
        {% else %}
        {{ total_vaccinations | round(0) }}
        {% endif %}
      </span>
    </div>
  </div>
</div>
```

## Deaths

Here is a timeline of the worldwide deaths caused by the COVID-19 pandemic:

```json chart card
{
  "width": 800,
  "data": {"url": "../data/locations/{{ code }}/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_deaths", "type": "quantitative", "scale": {"domainMin": 0}}
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

The new cases data is less reliable as cases registration really depends on the testing volume and methodology:

```json chart card
{
  "width": 800,
  "data": {"url": "../data/locations/{{ code }}/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_cases", "type": "quantitative", "scale": {"domainMin": 0}}
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

The vaccination campaign had been started around January 2021; this chart counds all the shots taken:

```json chart card
{
  "width": 800,
  "data": {"url": "../data/locations/{{ code }}/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_vaccinations", "type": "quantitative", "scale": {"domainMin": 0}}
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

## Rolling Immunity

```json chart card
{
  "width": 800,
  "data": {"url": "../data/locations/{{ code }}/timeline.csv"},
  "resolve": {"scale": {"y": "independent"}},
  "encoding": {
    "x": {"field": "date", "type": "temporal"}
  },
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_deaths_per_million", "type": "quantitative", "scale": {"domainMin": 0}},
        "color": {"value": "red"}
      }
    },
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "rolling_immunity", "type": "quantitative", "scale": {"domain": [0, 1]}},
        "color": {"value": "green"}
      }
    }
  ]
}
```

## Summary

TBD
