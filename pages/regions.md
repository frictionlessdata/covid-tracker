# Regions

## Deaths

Here is an interactive map showing amount of total deaths per region:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/regions.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "properties.CONTINENT",
      "from": {
        "data": {
          "url": "../data/latest.csv"
        },
        "key": "location",
        "fields": ["location", "total_deaths_per_million"]
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
         "field": "properties.CONTINENT",
         "type": "nominal",
         "title": "Region"
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

## Total Cases

Here is an interactive map showing amount of total cases per region:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/regions.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "properties.CONTINENT",
      "from": {
        "data": {
          "url": "../data/latest.csv"
        },
        "key": "location",
        "fields": ["location", "total_cases_per_million"]
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
          "title": "Deaths/1M"
      }
    },
    "tooltip": [
      {
         "field": "properties.CONTINENT",
         "type": "nominal",
         "title": "Region"
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

Here is an interactive map showing amount of total shots taken per region:

```json chart
{
  "width": 800,
  "height": 400,
  "data": {
    "url": "../data/spatial/regions.json",
    "format": {"property": "features"}
  },
  "transform": [
    {
      "lookup": "properties.CONTINENT",
      "from": {
        "data": {
          "url": "../data/latest.csv"
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
         "field": "properties.CONTINENT",
         "type": "nominal",
         "title": "Region"
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

## Details

```html markup
<table class="regions table table-bordered table-striped">
  <tr>
    <th>Region</th>
    <th>Deaths/1M</th>
    <th>Cases/1M</th>
    <th>Shots/100</th>
  </tr>
  {% for row in frictionless.extract('data/regions/latest.csv') %}
  <tr>
    <td><a href="#card={{ row.iso_code }}">{{ row.location }}</a></td>
    <td>{{ row.total_deaths_per_million }}</td>
    <td>{{ row.total_cases_per_million }}</td>
    <td>{{ row.total_vaccinations_per_hundred }}</td>
  </tr>
  {% endfor %}
</table>
```
