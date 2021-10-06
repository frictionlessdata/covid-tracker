# Contribute

To start working on the project clone the repository and enter its directory:

```bash
$ git clone git@github.com:frictionlessdata/covid-tracker.git
$ cd covid-tracker
```

## Install

Run the following script to initiate a virtual environment and install the dependencies:

```bash
$ make install
```

## Data

To collect the data use the data collection script (run only if you want to update the data):

```bash
$ make data
```

## Build

To build the project use one of these Livemark commands:

```bash
$ livemark start # to build and start a live-reload server
$ livemark build # to build in non-interactive mode
```

## Deploy

The project is deployed automatically to Github Pages on every push to "main". It means that if one propose a change in a PR it will be deployed automatically after merging.
