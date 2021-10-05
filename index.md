# COVID-19 Tracker

[![Build](https://img.shields.io/github/workflow/status/frictionlessdata/livemark/general/main)](https://github.com/frictionlessdata/livemark/actions)
[![Codebase](https://img.shields.io/badge/codebase-github-brightgreen)](https://github.com/frictionlessdata/livemark)
[![Support](https://img.shields.io/badge/support-discord-brightgreen)](https://discord.com/channels/695635777199145130/695635777199145133)

{% set last_updated = frictionless.extract('data/locations/OWID_WRL/latest.csv')[0].last_updated_date %}

```yaml remark
type: primary
text: "Last data update: <strong>{{ last_updated }}</strong> (this site is being updated on a nightly basis)."
```

**Coronavirus disease 2019 (COVID-19)**, also known as [COVID](https://en.wikipedia.org/wiki/COVID-19) and the coronavirus, is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The data dashboard has been created by the Frictionless Data team and it's open for contributing for anyone who is interested.

## Status

The main three core metrics we track: total deaths, total cases, and all the vaccination shots taken:

```html markup
{% for row in frictionless.extract('data/locations/OWID_WRL/latest.csv') %}
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
  "data": {"url": "data/locations/OWID_WRL/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_deaths", "type": "quantitative", "scale": {"domainMin": 0}},
    "tooltip": [
      {
         "field": "date",
         "type": "temporal",
         "title": "Date"
      },
      {
         "field": "new_deaths",
         "type": "quantitative",
         "title": "Deaths"
      }
    ]
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
  "data": {"url": "data/locations/OWID_WRL/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_cases", "type": "quantitative", "scale": {"domainMin": 0}},
    "tooltip": [
      {
         "field": "date",
         "type": "temporal",
         "title": "Date"
      },
      {
         "field": "new_cases",
         "type": "quantitative",
         "title": "Cases"
      }
    ]
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
  "data": {"url": "data/locations/OWID_WRL/timeline.csv"},
  "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "new_vaccinations", "type": "quantitative", "scale": {"domainMin": 0}},
    "tooltip": [
      {
         "field": "date",
         "type": "temporal",
         "title": "Date"
      },
      {
         "field": "new_vaccinations",
         "type": "quantitative",
         "title": "Shots"
      }
    ]
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

## Summary

Here is a summary of the key pandemic data by countries:

```yaml table
data:
  path: data/reports/world.csv
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
