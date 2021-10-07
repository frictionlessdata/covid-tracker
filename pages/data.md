# Data Collection

All data on this site was generated (cleaned, analysed) using the [Frictionless Python Framework](https://framework.frictionlessdata.io/) on openly availabe data. The data is from [Our World in Data](https://ourworldindata.org/coronavirus) and [Excess Mortality](https://github.com/dkobak/excess-mortality). Read on to see the Frictionless code that was used to analyse the data.

## Extract

First of all, we need to extract all the data from [Our World in Data](https://ourworldindata.org/coronavirus) and [Excess Mortality](https://github.com/dkobak/excess-mortality) repositories:

```bash
$ python code/extract.py
```

```python file
code/extract.py
```

## Transform

We will split the data by location and calculate rolling immunity:

```bash
$ python code/transform/timeline.py
```

```python file
code/transform/timeline.py
```

```bash
$ python code/transform/latest.py
```

```python file
code/transform/latest.py
```

## Load

To show different locations as cards we render them:

```bash
$ python code/load.py
```

```python file
code/load.py
```
