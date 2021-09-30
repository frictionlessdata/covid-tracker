# Excess Mortality

## Excess Deaths

The numbers are based on the World Mortality Dataset:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/countries.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "properties.name",
      "from": {
        "data": {
          "url": "../data/mortality.csv"
        },
        "key": "Country",
        "fields": ["Country", "Excess per 100k"]
      }
    }
  ],
  "projection": {"type": "mercator"},
  "mark": {
    "type": "geoshape",
    "stroke": "#757575",
    "strokeWidth": 0.5
  },
  "encoding": {
    "color": {
      "field": "Excess per 100k",
      "type": "quantitative",
      "scale": {"scheme": "Reds"},
      "legend": {
          "title": "Excess/100k"
      }
    },
    "tooltip": [
      {
         "field": "properties.name",
         "type": "nominal",
         "title": "Country"
      },
      {
         "field": "Excess per 100k",
         "type": "quantitative",
         "title": "Excess/100k"
      }
    ]
  }
}
```

## Summary

```html markup
<table class="big table table-bordered table-striped">
  <tr>
    <th>Country</th>
    <th>Excess Deaths</th>
    <th>Excess Deaths/100k</th>
  </tr>
  {% for row in frictionless.extract('data/mortality.csv') | selectattr('Excess deaths') | sort(attribute='Excess deaths', reverse=True) %}
  <tr>
    <td>{{ row['Country'] }}</td>
    <td>{{ row['Excess deaths'] }}</td>
    <td>{{ row['Excess per 100k'] }}</td>
  </tr>
  {% endfor %}
</table>
```
