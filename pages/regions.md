# Regions

## Deaths

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

## Cases

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
