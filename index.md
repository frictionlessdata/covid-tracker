# COVID-19 Tracker

[![Build](https://img.shields.io/github/workflow/status/frictionlessdata/livemark/general/main)](https://github.com/frictionlessdata/livemark/actions)
[![Codebase](https://img.shields.io/badge/codebase-github-brightgreen)](https://github.com/frictionlessdata/livemark)
[![Support](https://img.shields.io/badge/support-discord-brightgreen)](https://discord.com/channels/695635777199145130/695635777199145133)

{% set data = frictionless.extract('data/locations/OWID_WRL/latest.csv')[0] %}

```yaml remark
type: primary
text: "Last data update: <strong>{{ data.last_updated_date }}</strong> (this site is being updated on a nightly basis)."
```

**Coronavirus disease 2019 (COVID-19)**, also known as [COVID](https://en.wikipedia.org/wiki/COVID-19) and the coronavirus, is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The data dashboard has been created by the Frictionless Data team and it's open for contributing for anyone who is interested.

## Status

The main three core metrics we track: total deaths, total cases, and all the vaccination shots taken:

```html markup
{% with data=data %}
{% include 'blocks/status.html' %}
{% endwith %}
```

## Deaths

Here is a timeline of the worldwide deaths caused by the COVID-19 pandemic:

```json chart
{% with code='OWID_WRL', field='new_deaths', title='Deaths', color='red' %}
{% include 'blocks/charts/timeline.json' %}
{% endwith %}
```

## New Cases

The new cases data is less reliable as cases registration really depends on the testing volume and methodology:

```json chart
{% with code='OWID_WRL', field='new_cases', title='Cases', color='blue' %}
{% include 'blocks/charts/timeline.json' %}
{% endwith %}
```

## Vaccinations

The vaccination campaign had been started around January 2021; this chart shows all the shots taken:

```json chart
{% with code='OWID_WRL', field='new_vaccinations', title='Shots', color='green' %}
{% include 'blocks/charts/timeline.json' %}
{% endwith %}
```

## Locations

Here is a summary of the key pandemic data:

```yaml table
{% with type='world' %}
{% include 'blocks/tables/locations.yaml' %}
{% endwith %}
```
