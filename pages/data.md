# Data Collection

## Extract

First of all, we need to extract all the data packages from Github. We're going to look at all the repos having `datapackage.json` in the root directory. Github Search API has quite strict querying limits so we have to use different techniques to avoid rate limit errors:

```bash
$ python code/extract.py
```

```python file
code/extract.py
```

## Transform

As a high-level data collections framework, we will use Frictionless Transform. It will sort the packages by repository's stargazers count and save it to the CSV file:

```bash
$ python code/transform.py
```

```python file
code/transform.py
```

## Load

After we have the `packages.csv` file filled with data packages, we need to load them as Livemark Cards. To achieve this task we will use builtin methods that comes with the Cards plugin:

```bash
$ python code/load.py
```

```python file
code/load.py
```
