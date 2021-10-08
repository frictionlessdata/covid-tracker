# Regions
This page displays the total count of deaths, case numbers, and vaccinations for regions of the world.

## Deaths

Here is an interactive map showing the count of total deaths per region:

```json chart
{% with field='total_deaths_per_million', title='Deaths/1M', scheme='reds' %}
{% include 'blocks/charts/regions.json' %}
{% endwith %}
```
*[source code for chart](https://github.com/frictionlessdata/covid-tracker/blob/main/pages/regions.md#deaths)*

## Total Cases

Here is an interactive map showing the count of total cases per region:

```json chart
{% with field='total_cases_per_million', title='Cases/1M', scheme='blues' %}
{% include 'blocks/charts/regions.json' %}
{% endwith %}
```
*[source code for chart](https://github.com/frictionlessdata/covid-tracker/blob/main/pages/regions.md#total-cases)*

## Vaccinations

Here is an interactive map showing the amount of total shots taken per region:

```json chart
{% with field='total_vaccinations_per_hundred', title='Shots/100', scheme='greens' %}
{% include 'blocks/charts/regions.json' %}
{% endwith %}
```
*[source code for chart](https://github.com/frictionlessdata/covid-tracker/blob/main/pages/regions.md#vaccinations)*

## Locations

Here is a summary of the key pandemic data by region:

```yaml table
{% with type='regions' %}
{% include 'blocks/tables/locations.yaml' %}
{% endwith %}
```
*[source code for table](https://github.com/frictionlessdata/covid-tracker/blob/main/pages/regions.md#locations)*