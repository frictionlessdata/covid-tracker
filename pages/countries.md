# Countries

## Deaths

Here is an interactive map showing amount of total deaths per country:

```json chart
{% with field='total_deaths_per_million', title='Deaths/100', scheme='reds' %}
{% include 'blocks/charts/countries.json' %}
{% endwith %}
```

## Total Cases

Here is an interactive map showing amount of total cases per country:

```json chart
{% with field='total_cases_per_million', title='Cases/100', scheme='blues' %}
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
data:
  path: data/reports/countries.csv
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
