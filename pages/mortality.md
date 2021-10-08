# Excess Mortality

**Excess mortality** is a [term](https://odihpn.org/resources/interpreting-and-using-mortality-data-in-humanitarian-emergencies/) used in epidemiology and public health that refers to the number of deaths from all causes during a crisis above and beyond what we would have expected to see under ‘normal’ conditions.

## Deaths

Here is a representation of excess mortality per country on the world map:

```json chart
{% with %}
{% include 'blocks/charts/mortality.json' %}
{% endwith %}
```

## Locations

Here is a list of excess deaths by countries:

```yaml table
{% with %}
{% include 'blocks/tables/mortality.yaml' %}
{% endwith %}
```

## Methodology

This page is based on researh by [Karlinsky & Kobak](https://github.com/dkobak/excess-mortality). The numbers are based on the World Mortality Dataset and the idea the comparing expected mortality trends with real mortality during pandemic we can calculate the real deaths amount as some countries might provide innacurate data.

