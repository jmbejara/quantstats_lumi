# QuantStats Lumi

Last updated: {sub-ref}`today`

```{toctree}
:maxdepth: 1
CHANGELOG.rst
apidocs/index
myst_markdown_demos.md
```

## Description

```{image} https://img.shields.io/badge/python-3.6+-blue.svg?style=flat
:target: https://pypi.python.org/pypi/quantstats
:alt: Python version
```

```{image} https://img.shields.io/pypi/v/quantstats.svg?maxAge=60
:target: https://pypi.python.org/pypi/quantstats
:alt: PyPi version
```

```{image} https://img.shields.io/pypi/status/quantstats.svg?maxAge=60
:target: https://pypi.python.org/pypi/quantstats
:alt: PyPi status
```

```{image} https://img.shields.io/pypi/dm/quantstats.svg?maxAge=2592000&label=installs&color=%2327B1FF
:target: https://pypi.python.org/pypi/quantstats
:alt: PyPi downloads
```

```{image} https://www.codefactor.io/repository/github/ranaroussi/quantstats/badge
:target: https://www.codefactor.io/repository/github/ranaroussi/quantstats
:alt: CodeFactor
```

```{image} https://img.shields.io/github/stars/ranaroussi/quantstats.svg?style=social&label=Star&maxAge=60
:target: https://github.com/ranaroussi/quantstats
:alt: Star this repo
```

```{image} https://img.shields.io/twitter/follow/aroussi.svg?style=social&label=Follow&maxAge=60
:target: https://twitter.com/aroussi
:alt: Follow me on twitter
```


## Fork of Original QuantStats by Ran Aroussi

This is a forked version of the original QuantStats library by Ran Aroussi. The original library can be found at <https://github.com/ranaroussi/quantstats>

This forked version was created because it seems that the original library is no longer being maintained. The original library has a number of issues and pull requests that have been open for a long time and have not been addressed. This forked version aims to address some of these issues and pull requests.

This forked version is created and maintained by the Lumiwealth team. We are a team of data scientists and software engineers who are passionate about quantitative finance and algorithmic trading. We use QuantStats in our daily work with the Lumibot library and we want to make sure that QuantStats is a reliable and well-maintained library.

If you're interested in learning how to make your own trading algorithms, check out our Lumibot library at <https://github.com/Lumiwealth/lumibot> and check out our courses at <https://lumiwealth.com>

## QuantStats: Portfolio analytics for quants

**QuantStats** Python library that performs portfolio profiling, allowing quants and portfolio managers to understand their performance better by providing them with in-depth analytics and risk metrics.

[Changelog](CHANGELOG)

QuantStats is comprised of 3 main modules:

1. `quantstats.stats` - for calculating various performance metrics, like Sharpe ratio, Win rate, Volatility, etc.
2. `quantstats.plots` - for visualizing performance, drawdowns, rolling statistics, monthly returns, etc.
3. `quantstats.reports` - for generating metrics reports, batch plotting, and creating tear sheets that can be saved as an HTML file.

## Quick Start

Install QuantStats Lumi using pip:

```bash
pip install quantstats-lumi
```

```python
%matplotlib inline
import quantstats_lumi as qs

# extend pandas functionality with metrics, etc.
qs.extend_pandas()

# fetch the daily returns for a stock
stock = qs.utils.download_returns('META')

# show sharpe ratio
qs.stats.sharpe(stock)

# or using extend_pandas() :)
stock.sharpe()
```

**Output:**
```
0.8135304438803402
```

### Visualize stock performance

```python
qs.plots.snapshot(stock, title='Facebook Performance', show=True)
# can also be called via: stock.plot_snapshot(title='Facebook Performance', show=True)
```

```{image} https://github.com/ranaroussi/quantstats/blob/main/docs/snapshot.jpg?raw=true
:alt: Snapshot plot
```

### Creating a report

You can create 5 different report tearsheets:

1. [`qs.reports.metrics`](./apidocs/quantstats_lumi/quantstats_lumi.reports.md#quantstats_lumi.reports.metrics) - shows basic/full metrics
2. [`qs.reports.plots`](./apidocs/quantstats_lumi/quantstats_lumi.reports.md#quantstats_lumi.reports.plots) - shows basic/full plots  
3. [`qs.reports.basic`](./apidocs/quantstats_lumi/quantstats_lumi.reports.md#quantstats_lumi.reports.basic) - shows basic metrics and plots
4. [`qs.reports.full`](./apidocs/quantstats_lumi/quantstats_lumi.reports.md#quantstats_lumi.reports.full) - shows full metrics and plots
5. [`qs.reports.html`](./apidocs/quantstats_lumi/quantstats_lumi.reports.md#quantstats_lumi.reports.html) - generates complete HTML report

```python
# Generate HTML report with benchmark comparison
qs.reports.html(stock, "SPY", title="Facebook vs S&P 500")
```

```{image} https://github.com/ranaroussi/quantstats/blob/main/docs/report.jpg?raw=true
:alt: HTML tearsheet
```

[View original html file](https://rawcdn.githack.com/ranaroussi/quantstats/main/docs/tearsheet.html)

## Installation

```bash
pip install quantstats --upgrade --no-cache-dir
```

```bash
conda install -c ranaroussi quantstats
```

## Requirements

- Python >= 3.5+
- pandas >= 0.24.0
- numpy >= 1.15.0
- scipy >= 1.2.0
- matplotlib >= 3.0.0
- seaborn >= 0.9.0
- tabulate >= 0.8.0
- yfinance >= 0.1.38
- plotly >= 3.4.1 (optional)

## Legal

**QuantStats** is distributed under the **Apache Software License**. See the {download}`LICENSE.txt<../LICENSE.txt>` file for details.

## Module Documentation

- {ref}`