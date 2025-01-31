# {py:mod}`quantstats_lumi.reports`

```{py:module} quantstats_lumi.reports
```

```{autodoc2-docstring} quantstats_lumi.reports
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_get_trading_periods <quantstats_lumi.reports._get_trading_periods>`
  - ```{autodoc2-docstring} quantstats_lumi.reports._get_trading_periods
    :summary:
    ```
* - {py:obj}`_match_dates <quantstats_lumi.reports._match_dates>`
  - ```{autodoc2-docstring} quantstats_lumi.reports._match_dates
    :summary:
    ```
* - {py:obj}`html <quantstats_lumi.reports.html>`
  - ```{autodoc2-docstring} quantstats_lumi.reports.html
    :summary:
    ```
* - {py:obj}`full <quantstats_lumi.reports.full>`
  - ```{autodoc2-docstring} quantstats_lumi.reports.full
    :summary:
    ```
* - {py:obj}`basic <quantstats_lumi.reports.basic>`
  - ```{autodoc2-docstring} quantstats_lumi.reports.basic
    :summary:
    ```
* - {py:obj}`parameters_section <quantstats_lumi.reports.parameters_section>`
  - ```{autodoc2-docstring} quantstats_lumi.reports.parameters_section
    :summary:
    ```
* - {py:obj}`metrics <quantstats_lumi.reports.metrics>`
  - ```{autodoc2-docstring} quantstats_lumi.reports.metrics
    :summary:
    ```
* - {py:obj}`plots <quantstats_lumi.reports.plots>`
  - ```{autodoc2-docstring} quantstats_lumi.reports.plots
    :summary:
    ```
* - {py:obj}`_calc_dd <quantstats_lumi.reports._calc_dd>`
  - ```{autodoc2-docstring} quantstats_lumi.reports._calc_dd
    :summary:
    ```
* - {py:obj}`_html_table <quantstats_lumi.reports._html_table>`
  - ```{autodoc2-docstring} quantstats_lumi.reports._html_table
    :summary:
    ```
* - {py:obj}`_download_html <quantstats_lumi.reports._download_html>`
  - ```{autodoc2-docstring} quantstats_lumi.reports._download_html
    :summary:
    ```
* - {py:obj}`_open_html <quantstats_lumi.reports._open_html>`
  - ```{autodoc2-docstring} quantstats_lumi.reports._open_html
    :summary:
    ```
* - {py:obj}`_embed_figure <quantstats_lumi.reports._embed_figure>`
  - ```{autodoc2-docstring} quantstats_lumi.reports._embed_figure
    :summary:
    ```
````

### API

````{py:function} _get_trading_periods(periods_per_year=365)
:canonical: quantstats_lumi.reports._get_trading_periods

```{autodoc2-docstring} quantstats_lumi.reports._get_trading_periods
```
````

````{py:function} _match_dates(returns, benchmark)
:canonical: quantstats_lumi.reports._match_dates

```{autodoc2-docstring} quantstats_lumi.reports._match_dates
```
````

````{py:function} html(returns, benchmark: pandas.Series = None, rf: float = 0.0, grayscale: bool = False, title: str = 'Strategy Tearsheet', output: str = None, compounded: bool = True, periods_per_year: int = 365, download_filename: str = 'tearsheet.html', figfmt: str = 'svg', template_path: str = None, match_dates: bool = True, parameters: dict = None, log_scale: bool = False, show_match_volatility: bool = True, **kwargs)
:canonical: quantstats_lumi.reports.html

```{autodoc2-docstring} quantstats_lumi.reports.html
```
````

````{py:function} full(returns, benchmark=None, rf=0.0, grayscale=False, figsize=(8, 5), display=True, compounded=True, periods_per_year=365, match_dates=True, **kwargs)
:canonical: quantstats_lumi.reports.full

```{autodoc2-docstring} quantstats_lumi.reports.full
```
````

````{py:function} basic(returns, benchmark=None, rf=0.0, grayscale=False, figsize=(8, 5), display=True, compounded=True, periods_per_year=365, match_dates=True, **kwargs)
:canonical: quantstats_lumi.reports.basic

```{autodoc2-docstring} quantstats_lumi.reports.basic
```
````

````{py:function} parameters_section(parameters)
:canonical: quantstats_lumi.reports.parameters_section

```{autodoc2-docstring} quantstats_lumi.reports.parameters_section
```
````

````{py:function} metrics(returns, benchmark=None, rf=0.0, display=True, mode='basic', sep=False, compounded=True, periods_per_year=365, prepare_returns=True, match_dates=True, **kwargs)
:canonical: quantstats_lumi.reports.metrics

```{autodoc2-docstring} quantstats_lumi.reports.metrics
```
````

````{py:function} plots(returns, benchmark=None, grayscale=False, figsize=(8, 5), mode='basic', compounded=True, periods_per_year=365, prepare_returns=True, match_dates=True, **kwargs)
:canonical: quantstats_lumi.reports.plots

```{autodoc2-docstring} quantstats_lumi.reports.plots
```
````

````{py:function} _calc_dd(df, display=True, as_pct=False)
:canonical: quantstats_lumi.reports._calc_dd

```{autodoc2-docstring} quantstats_lumi.reports._calc_dd
```
````

````{py:function} _html_table(obj, showindex='default')
:canonical: quantstats_lumi.reports._html_table

```{autodoc2-docstring} quantstats_lumi.reports._html_table
```
````

````{py:function} _download_html(html, filename='quantstats-tearsheet.html')
:canonical: quantstats_lumi.reports._download_html

```{autodoc2-docstring} quantstats_lumi.reports._download_html
```
````

````{py:function} _open_html(html)
:canonical: quantstats_lumi.reports._open_html

```{autodoc2-docstring} quantstats_lumi.reports._open_html
```
````

````{py:function} _embed_figure(figfiles, figfmt)
:canonical: quantstats_lumi.reports._embed_figure

```{autodoc2-docstring} quantstats_lumi.reports._embed_figure
```
````
