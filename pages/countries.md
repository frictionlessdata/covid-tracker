# Countries

## Deaths

Here is an interactive map showing amount of total deaths per country:

```json chart
{% with field='total_deaths_per_million', title='Deaths/1M', scheme='reds' %}
{% include 'blocks/charts/countries.json' %}
{% endwith %}
```

## Total Cases

Here is an interactive map showing amount of total cases per country:

```json chart
{% with field='total_cases_per_million', title='Cases/1M', scheme='blues' %}
{% include 'blocks/charts/countries.json' %}
{% endwith %}
```

## Vaccinations

Here is an interactive map showing amount of total shots taken per country:

```json chart
{% with field='total_vaccinations_per_hundred', title='Shots/100', scheme='greens' %}
{% include 'blocks/charts/countries.json' %}
{% endwith %}
```

## Summary

Here is a summary of the key pandemic data by countries:

```yaml table
{% with type='countries' %}
{% include 'blocks/tables/locations.yaml' %}
{% endwith %}
```
