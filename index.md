# Data Packages

## Introduction

**Data Package** is a simple container format for describing a coherent collection of data in a single package. We have [collected](data.html) and sorted by the stars count all the data packages available as repositories on Github. Read more about [Data Packages](https://specs.frictionlessdata.io/guides/data-package) and [Frictionless Data](https://frictionlessdata.io). If you are interested in contributing to this livemark please follow this [guide](contrib.html).

```yaml remark
type: warning
text: Currently, some datasets might be missing. See this <a href="https://github.com/frictionlessdata/data-packages/issues/1">issue</a> for more information.
```

## Datasets

```html markup
{% for row in frictionless.extract('data/packages.csv') %}
<div class="item">
  <div class="item-content">
    <h3>
      <a href="#card={{ row.code }}" style="color: black">
        {{ row.title or row.code }}
      </a>
    </h3>
    <p>{{ row.description or 'Description is not provided'}}</p>
    <p>
      <a class="item-content-link" href="https://github.com/{{ row.user}}/{{row.repo }}" target="_blank">
        Github <span class="fa fa-external-link-alt"></span>
      </a>
    </p>
  </div>
  <div class="item-stars">
    <span class="fa-stack fa-2x">
      <i class="fas fa-stack-2x fa-star fa-inverse item-stars-icon"></i>
      <i class="fas fa-stack-1x item-stars-count">{{ row.stars }}</i>
    </span>
  </div>
</div>
{% endfor %}
```
