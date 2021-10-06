# Rolling Immunity

```yaml remark
type: warning
text: It's a data journalism rather than scientific work. Immunity/antibodies analysis is complicated matter. You can read more about it, for example, in this <a href="https://www.nature.com/articles/s41591-021-01377-8">scientific paper</a>.
```

**Rolling immynity** (in terms of this page) is a collective immunity metric based on factual uses cases (counted using deaths) and vaccination shots timeline and the fact that individual immunity decreases over time.  This page is about finding relations with pandemic outbreaks and rolling immunity concept.

## Examples

To showcase the idea we use 5 countries having different vaccination timeframes. The Israel use case **might** be showing that having too fast vaccination campaign leads to following outbreaks due to low levels of rolling immunity. This USA case **mighe** show that vaccination level wasn't enough.

### Israel

```json chart
{% with code="ISR" %}
{% include 'blocks/charts/immunity.json' %}
{% endwith %}
```

### USA

```json chart
{% with code="USA" %}
{% include 'blocks/charts/immunity.json' %}
{% endwith %}
```

### UK

```json chart
{% with code="GBR" %}
{% include 'blocks/charts/immunity.json' %}
{% endwith %}
```

### Germany

```json chart
{% with code="DEU" %}
{% include 'blocks/charts/immunity.json' %}
{% endwith %}
```

### Brasil


```json chart
{% with code="BRA" %}
{% include 'blocks/charts/immunity.json' %}
{% endwith %}
```

## Locations

Explore charts for other countries and [share](forum.html) what you think. Take into account that this methodology is very approximate as the numbers depend on the healthcare and vaccines efficacy in the exact country. This table uses 7 day moving averages for deaths and cases:

```yaml table
{% with %}
{% include 'blocks/tables/immunity.yaml' %}
{% endwith %}
```

## Methodology

We use oversimplified rolling immunity formula for a date. We use deaths instead of use cases to overcome the problem of inaccurate use cases reporting. The exact ratio is configurable; we use 1 death for 100 use cases based on known death rate for now around 50 use cases per a death and estimating unreported use cases as 50 use cases per 1 death:

```
rolling_immunity_for_a_date = (estimated_new_cases + new_vaccinations) / population
estimated_new_cases = new_deaths * 100
```

We count one case to be equal to one vaccination shot. For the model we use the decreasing ration `(180 - days)/180` meaning that you will lose all the immunity you had acquired in 180 days. Again, this parameter is configurable and might be changed in other models.

```
rolling_immunity_for_a_date = 100%
rolling_immunity_for_a_date_in_180_days = 0%
```

Please take a look at the [full algorithm](data.html).
