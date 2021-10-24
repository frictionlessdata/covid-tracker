# Contribute

Welcome! We're happy you'd like to contribute! This is an open project, and we value contributions from everyone.

We use Github as a code and issues hosting platform. To report a bug or propose a new feature, please open an [issue](https://github.com/frictionlessdata/covid-tracker/issues). For pull requests, we would ask you initially create an issue and then create a pull requests linked to this issue.

## Setup

To start working on the project clone the repository and enter its directory:

```bash
$ git clone git@github.com:frictionlessdata/covid-tracker.git
$ cd covid-tracker
```

Create a virtual environment (optional):

```bash
$ python3 -m venv .python
$ source .python/bin/activate
```

And install livemark:

```
$ pip install livemark
```

## Install

Run the following command to install dependencies:

```bash task id=install
pip install -r requirements.txt
```

## Data

To collect the data use the data collection script (run only if you want to update the data):

```bash
$ livemark run data
```

See in-detail on the [Data Collection](data.html) page.

## Build

> See the Livemark documentation for full details: https://livemark.frictionlessdata.io/

You can then use the command-line interface to build the output HTML file:

```bash
$ livemark build
```

Or start a livereload server to automatically reload the output page as you modify the input Markdown document:

```bash
$ livemark start
```

## Deploy

The project is deployed automatically to Github Pages on every push to "main". That means that the page will automatically be deployed every time there is a change approved from a Pull Request.

If you'd like to update Github Issue/PR templates run this command:

```bash task id=github
sed -i -E "s/@(\w*)/@$(head -n 1 LEAD.md)/" .github/issue_template.md
sed -i -E "s/@(\w*)/@$(head -n 1 LEAD.md)/" .github/pull_request_template.md
```
