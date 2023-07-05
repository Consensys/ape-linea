# Quick Start

Ecosystem Plugin for linea support in Ape.

## Dependencies

- [python3](https://www.python.org/downloads) version 3.8 or greater, python3-dev

## Installation

### via `setuptools`

> Note: will not work (check TODO section)

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-linea.git
cd ape-linea
python3 setup.py install
```

## Configuration

You need to configure a node provider for Linea in your `ape-config.yaml`.
See `ape-config.yaml.example`

## Quick Usage

Installing this plugin adds support for the Linea ecosystem:

```bash
ape console --network linea:goerli
ape console --network linea:mainnet
```

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.

## Work in progress

- \[ \] Publish the repo on ApeWorX github
- \[ \] Publish the package on pypi

### via `ape`

> Note: will not work (check TODO section)

You can install this plugin using `ape`:

```bash
ape plugins install linea
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: linea
```

### via `pip`

> Note: will not work (check TODO section)

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-linea
```
