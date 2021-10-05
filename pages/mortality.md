# Excess Mortality

## Excess Deaths

The numbers are based on the World Mortality Dataset:

```json chart
{% with %}
{% include 'blocks/charts/mortality.json' %}
{% endwith %}
```

## Summary

Here is excess deaths by countries:

```yaml table
{% with %}
{% include 'blocks/tables/mortality.yaml' %}
{% endwith %}
```
