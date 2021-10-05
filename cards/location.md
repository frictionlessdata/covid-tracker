# {{ data.location }}

## Status

The main three core metrics we track: total deaths, total cases, and all the vaccination shots taken:

```html markup
{% with data=data %}
{% include 'blocks/status.html' %}
{% endwith %}
```

## Deaths

Here is a timeline of the worldwide deaths caused by the COVID-19 pandemic:

```json chart card
{% with code=code, field='new_deaths', title='Deaths', color='red', card=True %}
{% include 'blocks/charts/timeline.json' %}
{% endwith %}
```

## New Cases

The new cases data is less reliable as cases registration really depends on the testing volume and methodology:

```json chart card
{% with code=code, field='new_cases', title='Cases', color='blue', card=True %}
{% include 'blocks/charts/timeline.json' %}
{% endwith %}
```

## Vaccinations

The vaccination campaign had been started around January 2021; this chart counds all the shots taken:

```json chart card
{% with code=code, field='new_vaccinations', title='Shots', color='green', card=True %}
{% include 'blocks/charts/timeline.json' %}
{% endwith %}
```

## Rolling Immunity

```json chart card
{% with code=code %}
{% include 'blocks/charts/immunity.json' %}
{% endwith %}
```

## Summary

Here is a summary of the key pandemic data by countries:

```html markup
{% with code=code %}
{% include 'blocks/tables/timeline.html' %}
{% endwith %}
```
