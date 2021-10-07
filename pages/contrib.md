# Contribute

Welcome! We're happy you'd like to contribute! This is an open project, and we value contributions from everyone.

We use Github as a code and issues hosting platform. To report a bug or propose a new feature, please open an [issue](https://github.com/frictionlessdata/covid-tracker/issues). For pull requests, we would ask you initially create an issue and then create a pull requests linked to this issue.

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

The project is deployed automatically to Github Pages on every push to "main". That means that the page will automatically be deployed every time there is a change approved from a Pull Request.
