# {py:mod}`quantstats_lumi._plotting.wrappers`

```{py:module} quantstats_lumi._plotting.wrappers
```

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`to_plotly <quantstats_lumi._plotting.wrappers.to_plotly>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.to_plotly
    :summary:
    ```
* - {py:obj}`snapshot <quantstats_lumi._plotting.wrappers.snapshot>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.snapshot
    :summary:
    ```
* - {py:obj}`earnings <quantstats_lumi._plotting.wrappers.earnings>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.earnings
    :summary:
    ```
* - {py:obj}`returns <quantstats_lumi._plotting.wrappers.returns>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.returns
    :summary:
    ```
* - {py:obj}`log_returns <quantstats_lumi._plotting.wrappers.log_returns>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.log_returns
    :summary:
    ```
* - {py:obj}`daily_returns <quantstats_lumi._plotting.wrappers.daily_returns>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.daily_returns
    :summary:
    ```
* - {py:obj}`yearly_returns <quantstats_lumi._plotting.wrappers.yearly_returns>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.yearly_returns
    :summary:
    ```
* - {py:obj}`distribution <quantstats_lumi._plotting.wrappers.distribution>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.distribution
    :summary:
    ```
* - {py:obj}`histogram <quantstats_lumi._plotting.wrappers.histogram>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.histogram
    :summary:
    ```
* - {py:obj}`drawdown <quantstats_lumi._plotting.wrappers.drawdown>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.drawdown
    :summary:
    ```
* - {py:obj}`drawdowns_periods <quantstats_lumi._plotting.wrappers.drawdowns_periods>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.drawdowns_periods
    :summary:
    ```
* - {py:obj}`rolling_beta <quantstats_lumi._plotting.wrappers.rolling_beta>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.rolling_beta
    :summary:
    ```
* - {py:obj}`rolling_volatility <quantstats_lumi._plotting.wrappers.rolling_volatility>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.rolling_volatility
    :summary:
    ```
* - {py:obj}`rolling_sharpe <quantstats_lumi._plotting.wrappers.rolling_sharpe>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.rolling_sharpe
    :summary:
    ```
* - {py:obj}`rolling_sortino <quantstats_lumi._plotting.wrappers.rolling_sortino>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.rolling_sortino
    :summary:
    ```
* - {py:obj}`monthly_heatmap <quantstats_lumi._plotting.wrappers.monthly_heatmap>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.monthly_heatmap
    :summary:
    ```
* - {py:obj}`monthly_returns <quantstats_lumi._plotting.wrappers.monthly_returns>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.monthly_returns
    :summary:
    ```
* - {py:obj}`monthly_returns_detailedview <quantstats_lumi._plotting.wrappers.monthly_returns_detailedview>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.monthly_returns_detailedview
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_FLATUI_COLORS <quantstats_lumi._plotting.wrappers._FLATUI_COLORS>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers._FLATUI_COLORS
    :summary:
    ```
* - {py:obj}`_GRAYSCALE_COLORS <quantstats_lumi._plotting.wrappers._GRAYSCALE_COLORS>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers._GRAYSCALE_COLORS
    :summary:
    ```
* - {py:obj}`_HAS_PLOTLY <quantstats_lumi._plotting.wrappers._HAS_PLOTLY>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.wrappers._HAS_PLOTLY
    :summary:
    ```
````

### API

````{py:data} _FLATUI_COLORS
:canonical: quantstats_lumi._plotting.wrappers._FLATUI_COLORS
:value: >
   ['#fedd78', '#348dc1', '#af4b64', '#4fa487', '#9b59b6', '#808080']

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers._FLATUI_COLORS
```

````

````{py:data} _GRAYSCALE_COLORS
:canonical: quantstats_lumi._plotting.wrappers._GRAYSCALE_COLORS
:value: >
   None

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers._GRAYSCALE_COLORS
```

````

````{py:data} _HAS_PLOTLY
:canonical: quantstats_lumi._plotting.wrappers._HAS_PLOTLY
:value: >
   False

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers._HAS_PLOTLY
```

````

````{py:function} to_plotly(fig)
:canonical: quantstats_lumi._plotting.wrappers.to_plotly

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.to_plotly
```
````

````{py:function} snapshot(returns, grayscale=False, figsize=(10, 8), title='Portfolio Summary', fontname='Arial', lw=1.5, mode='comp', subtitle=True, savefig=None, show=True, log_scale=False, **kwargs)
:canonical: quantstats_lumi._plotting.wrappers.snapshot

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.snapshot
```
````

````{py:function} earnings(returns, start_balance=100000.0, mode='comp', grayscale=False, figsize=(10, 6), title='Portfolio Earnings', fontname='Arial', lw=1.5, subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.wrappers.earnings

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.earnings
```
````

````{py:function} returns(returns, benchmark=None, grayscale=False, figsize=(10, 6), fontname='Arial', lw=1.5, match_volatility=False, compound=True, cumulative=True, resample=None, ylabel='Cumulative Returns', subtitle=True, savefig=None, show=True, prepare_returns=True)
:canonical: quantstats_lumi._plotting.wrappers.returns

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.returns
```
````

````{py:function} log_returns(returns, benchmark=None, grayscale=False, figsize=(10, 5), fontname='Arial', lw=1.5, match_volatility=False, compound=True, cumulative=True, resample=None, ylabel='Cumulative Returns', subtitle=True, savefig=None, show=True, prepare_returns=True)
:canonical: quantstats_lumi._plotting.wrappers.log_returns

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.log_returns
```
````

````{py:function} daily_returns(returns, benchmark, grayscale=False, figsize=(10, 4), fontname='Arial', lw=0.5, log_scale=False, ylabel='Returns', subtitle=True, savefig=None, show=True, prepare_returns=True, active=False)
:canonical: quantstats_lumi._plotting.wrappers.daily_returns

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.daily_returns
```
````

````{py:function} yearly_returns(returns, benchmark=None, fontname='Arial', grayscale=False, hlw=1.5, hlcolor='red', hllabel='', match_volatility=False, log_scale=False, figsize=(10, 5), ylabel=True, subtitle=True, compounded=True, savefig=None, show=True, prepare_returns=True)
:canonical: quantstats_lumi._plotting.wrappers.yearly_returns

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.yearly_returns
```
````

````{py:function} distribution(returns, fontname='Arial', grayscale=False, ylabel=True, figsize=(10, 6), subtitle=True, compounded=True, savefig=None, show=True, title=None, prepare_returns=True, log_scale=True)
:canonical: quantstats_lumi._plotting.wrappers.distribution

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.distribution
```
````

````{py:function} histogram(returns, benchmark=None, resample='ME', fontname='Arial', grayscale=False, figsize=(10, 5), ylabel=True, subtitle=True, compounded=True, savefig=None, show=True, prepare_returns=True)
:canonical: quantstats_lumi._plotting.wrappers.histogram

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.histogram
```
````

````{py:function} drawdown(returns, grayscale=False, figsize=(10, 5), fontname='Arial', lw=1, log_scale=False, match_volatility=False, compound=False, ylabel='Drawdown', resample=None, subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.wrappers.drawdown

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.drawdown
```
````

````{py:function} drawdowns_periods(returns, periods=5, lw=1.5, log_scale=False, fontname='Arial', grayscale=False, title=None, figsize=(10, 5), ylabel=True, subtitle=True, compounded=True, savefig=None, show=True, prepare_returns=True)
:canonical: quantstats_lumi._plotting.wrappers.drawdowns_periods

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.drawdowns_periods
```
````

````{py:function} rolling_beta(returns, benchmark, window1=126, window1_label='6-Months', window2=365, window2_label='12-Months', lw=1.5, fontname='Arial', grayscale=False, figsize=(10, 3), ylabel=True, subtitle=True, savefig=None, show=True, prepare_returns=True)
:canonical: quantstats_lumi._plotting.wrappers.rolling_beta

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.rolling_beta
```
````

````{py:function} rolling_volatility(returns, benchmark=None, period=126, period_label='6-Months', periods_per_year=365, lw=1.5, fontname='Arial', grayscale=False, figsize=(10, 3), ylabel='Volatility', subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.wrappers.rolling_volatility

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.rolling_volatility
```
````

````{py:function} rolling_sharpe(returns, benchmark=None, rf=0.0, period=126, period_label='6-Months', periods_per_year=365, lw=1.25, fontname='Arial', grayscale=False, figsize=(10, 3), ylabel='Sharpe', subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.wrappers.rolling_sharpe

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.rolling_sharpe
```
````

````{py:function} rolling_sortino(returns, benchmark=None, rf=0.0, period=126, period_label='6-Months', periods_per_year=365, lw=1.25, fontname='Arial', grayscale=False, figsize=(10, 3), ylabel='Sortino', subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.wrappers.rolling_sortino

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.rolling_sortino
```
````

````{py:function} monthly_heatmap(returns, benchmark=None, annot_size=10, figsize=(10, 5), cbar=True, square=False, returns_label='Strategy', compounded=True, eoy=False, grayscale=False, fontname='Arial', ylabel=True, savefig=None, show=True, active=False)
:canonical: quantstats_lumi._plotting.wrappers.monthly_heatmap

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.monthly_heatmap
```
````

````{py:function} monthly_returns(returns, annot_size=10, figsize=(10, 5), cbar=True, square=False, compounded=True, eoy=False, grayscale=False, fontname='Arial', ylabel=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.wrappers.monthly_returns

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.monthly_returns
```
````

````{py:function} monthly_returns_detailedview(returns, grayscale=False, figsize=(14, 6), annot_size=11, returns_label='Strategy', fontname='Arial', return_font_rate=1.0, monthly_dd_font_rate=0.8, annual_dd_font_rate=0.8, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.wrappers.monthly_returns_detailedview

```{autodoc2-docstring} quantstats_lumi._plotting.wrappers.monthly_returns_detailedview
```
````
