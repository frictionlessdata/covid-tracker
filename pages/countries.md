# Countries

## Deaths

Here is an interactive map showing amount of total deaths per country:

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
      "lookup": "id",
      "from": {
        "data": {
          "url": "../data/reports/countries.csv"
        },
        "key": "iso_code",
        "fields": ["iso_code", "total_deaths_per_million"]
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
      "field": "total_deaths_per_million",
      "type": "quantitative",
      "scale": {"scheme": "Reds"},
      "legend": {
          "title": "Deaths/1M"
      }
    },
    "tooltip": [
      {
         "field": "properties.name",
         "type": "nominal",
         "title": "Country"
      },
      {
         "field": "total_deaths_per_million",
         "type": "quantitative",
         "title": "Deaths/1M"
      }
    ]
  }
}
```

## Cases

Here is an interactive map showing amount of total cases per country:

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
      "lookup": "id",
      "from": {
        "data": {
          "url": "../data/reports/countries.csv"
        },
        "key": "iso_code",
        "fields": ["iso_code", "total_cases_per_million"]
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
      "field": "total_cases_per_million",
      "type": "quantitative",
      "scale": {"scheme": "Blues"},
      "legend": {
          "title": "Cases/1M"
      }
    },
    "tooltip": [
      {
         "field": "properties.name",
         "type": "nominal",
         "title": "Country"
      },
      {
         "field": "total_cases_per_million",
         "type": "quantitative",
         "title": "Cases/1M"
      }
    ]
  }
}
```

## Vaccinations

Here is an interactive map showing amount of total shots taken per country:

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
          "url": "../data/reports/countries.csv"
        },
        "key": "location",
        "fields": ["location", "total_vaccinations_per_hundred"]
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
      "field": "total_vaccinations_per_hundred",
      "type": "quantitative",
      "scale": {"scheme": "Greens"},
      "legend": {
          "title": "Shots/100"
      }
    },
    "tooltip": [
      {
         "field": "properties.name",
         "type": "nominal",
         "title": "Country"
      },
      {
         "field": "total_vaccinations_per_hundred",
         "type": "quantitative",
         "title": "Shots/100"
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
    <th>Deaths/1M</th>
    <th>Cases/1M</th>
    <th>Shots/100</th>
  </tr>
  {% for row in frictionless.extract('data/reports/countries.csv') | selectattr('total_deaths_per_million') | sort(attribute='total_deaths_per_million', reverse=True) %}
  <tr>
    <td><a href="#card={{ row.iso_code }}">{{ row.location }}</a></td>
    <td>{{ row.total_deaths_per_million }}</td>
    <td>{{ row.total_cases_per_million }}</td>
    <td>{{ row.total_vaccinations_per_hundred }}</td>
  </tr>
  {% endfor %}
</table>
```
