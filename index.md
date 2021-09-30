# COVID-19 Tracker

[![Build](https://img.shields.io/github/workflow/status/frictionlessdata/livemark/general/main)](https://github.com/frictionlessdata/livemark/actions)
[![Codebase](https://img.shields.io/badge/codebase-github-brightgreen)](https://github.com/frictionlessdata/livemark)
[![Support](https://img.shields.io/badge/support-discord-brightgreen)](https://discord.com/channels/695635777199145130/695635777199145133)

{% set last_updated = frictionless.extract('data/countries/owid_wrl/latest.csv')[0].last_updated_date %}

```yaml remark
type: primary
text: "Last data update: <strong>{{ last_updated }}</strong> (this site is being updated on a nightly basis)."
```

**Coronavirus disease 2019 (COVID-19)**, also known as [COVID](https://en.wikipedia.org/wiki/COVID-19) and the coronavirus, is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The data dashboard has been created by the Frictionless Data team and it's open for contributing for anyone who is interested.

## Status

The main three core metrics we track: total deaths, total cases, and all the vaccination shots taken:

```html markup
{% for row in frictionless.extract('data/countries/owid_wrl/latest.csv') %}
<div class="status row">
  <div class="col-sm-4">
    <div role="button" class="btn btn-danger w-100">
      Deaths<br>
      <span class="badge badge-light">
        {{ (row.total_deaths/1000000) | round(1) }}M
      </span>
    </div>
  </div>
  <div class="col-sm-4">
    <div role="button" class="btn btn-primary w-100">
      Cases<br>
      <span class="badge badge-light">
        {{ (row.total_cases/1000000) | round(1) }}M
      </span>
    </div>
  </div>
  <div class="col-sm-4">
    <div role="button" class="btn btn-success w-100">
      Vaccinations<br>
      <span class="badge badge-light">
        {{ (row.total_vaccinations/1000000000) | round(1) }}B
      </span>
    </div>
  </div>
</div>
{% endfor %}
```

## Deaths

Here is a timeline of the worldwide deaths caused by the COVID-19 pandemic:

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

The new cases data is less reliable as cases registration really depends on the testing volume and methodology:

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

The vaccination campaign had been started around January 2021; this chart counds all the shots taken:

```json chart
{
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

## Combined

The conbined chart might help analyze how the vaccination helps to fight the pandemic and case/deaths causalities:

```json chart
{
  "width": 750,
  "data": {"url": "data/countries/owid_wrl/timeline.csv"},
  "resolve": {"scale": {"y": "independent"}},
  "encoding": {
    "x": {"field": "date", "type": "temporal"}
  },
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_deaths", "type": "quantitative"},
        "color": {"value": "red"}
      }
    },
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_cases", "type": "quantitative"},
        "color": {"value": "blue"}
      }
    },
    {
      "mark": "line",
      "encoding": {
        "y": {"field": "new_vaccinations", "type": "quantitative"},
        "color": {"value": "green"}
      }
    }
  ]
}
```

## Sources

> Put here links to files and cards with table exploration

The page has been created using the following dataset. You can [download CSV](data/countries/owid_wrl/timeline.csv) or explore the table:

```yaml table
data: data/countries/owid_wrl/timeline.csv
filters: true
dropdownMenu: true
contextMenu: true
columnSorting:
  initialConfig:
    column: 3
    sortOrder: desc
width: 900
height: 300
```
