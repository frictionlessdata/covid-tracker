# Regions

## Deaths

Here is an interactive map showing amount of total deaths per region:

```json chart
{% with field='total_deaths_per_million', title='Deaths/1M', scheme='reds' %}
{% include 'blocks/charts/regions.json' %}
{% endwith %}
```

## Total Cases

Here is an interactive map showing amount of total cases per region:

```json chart
{% with field='total_cases_per_million', title='Cases/1M', scheme='blues' %}
{% include 'blocks/charts/regions.json' %}
{% endwith %}
```

## Vaccinations

Here is an interactive map showing amount of total shots taken per region:

```json chart
{% with field='total_vaccinations_per_hundred', title='Shots/100', scheme='greens' %}
{% include 'blocks/charts/regions.json' %}
{% endwith %}
```

## Summary

Here is a summary of the key pandemic data by regions:

```yaml table
{% with type='regions' %}
{% include 'blocks/tables/locations.json' %}
{% endwith %}
```
