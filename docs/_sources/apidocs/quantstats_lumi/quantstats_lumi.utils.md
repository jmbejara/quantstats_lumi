# {py:mod}`quantstats_lumi.utils`

```{py:module} quantstats_lumi.utils
```

```{autodoc2-docstring} quantstats_lumi.utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_mtd <quantstats_lumi.utils._mtd>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._mtd
    :summary:
    ```
* - {py:obj}`_qtd <quantstats_lumi.utils._qtd>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._qtd
    :summary:
    ```
* - {py:obj}`_ytd <quantstats_lumi.utils._ytd>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._ytd
    :summary:
    ```
* - {py:obj}`_pandas_date <quantstats_lumi.utils._pandas_date>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._pandas_date
    :summary:
    ```
* - {py:obj}`_pandas_current_month <quantstats_lumi.utils._pandas_current_month>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._pandas_current_month
    :summary:
    ```
* - {py:obj}`multi_shift <quantstats_lumi.utils.multi_shift>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.multi_shift
    :summary:
    ```
* - {py:obj}`to_returns <quantstats_lumi.utils.to_returns>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.to_returns
    :summary:
    ```
* - {py:obj}`to_prices <quantstats_lumi.utils.to_prices>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.to_prices
    :summary:
    ```
* - {py:obj}`log_returns <quantstats_lumi.utils.log_returns>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.log_returns
    :summary:
    ```
* - {py:obj}`to_log_returns <quantstats_lumi.utils.to_log_returns>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.to_log_returns
    :summary:
    ```
* - {py:obj}`exponential_stdev <quantstats_lumi.utils.exponential_stdev>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.exponential_stdev
    :summary:
    ```
* - {py:obj}`rebase <quantstats_lumi.utils.rebase>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.rebase
    :summary:
    ```
* - {py:obj}`group_returns <quantstats_lumi.utils.group_returns>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.group_returns
    :summary:
    ```
* - {py:obj}`aggregate_returns <quantstats_lumi.utils.aggregate_returns>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.aggregate_returns
    :summary:
    ```
* - {py:obj}`to_excess_returns <quantstats_lumi.utils.to_excess_returns>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.to_excess_returns
    :summary:
    ```
* - {py:obj}`_prepare_prices <quantstats_lumi.utils._prepare_prices>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._prepare_prices
    :summary:
    ```
* - {py:obj}`_prepare_returns <quantstats_lumi.utils._prepare_returns>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._prepare_returns
    :summary:
    ```
* - {py:obj}`download_returns <quantstats_lumi.utils.download_returns>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.download_returns
    :summary:
    ```
* - {py:obj}`_prepare_benchmark <quantstats_lumi.utils._prepare_benchmark>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._prepare_benchmark
    :summary:
    ```
* - {py:obj}`_round_to_closest <quantstats_lumi.utils._round_to_closest>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._round_to_closest
    :summary:
    ```
* - {py:obj}`_file_stream <quantstats_lumi.utils._file_stream>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._file_stream
    :summary:
    ```
* - {py:obj}`_in_notebook <quantstats_lumi.utils._in_notebook>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._in_notebook
    :summary:
    ```
* - {py:obj}`_count_consecutive <quantstats_lumi.utils._count_consecutive>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._count_consecutive
    :summary:
    ```
* - {py:obj}`_score_str <quantstats_lumi.utils._score_str>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._score_str
    :summary:
    ```
* - {py:obj}`make_index <quantstats_lumi.utils.make_index>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.make_index
    :summary:
    ```
* - {py:obj}`make_portfolio <quantstats_lumi.utils.make_portfolio>`
  - ```{autodoc2-docstring} quantstats_lumi.utils.make_portfolio
    :summary:
    ```
* - {py:obj}`_flatten_dataframe <quantstats_lumi.utils._flatten_dataframe>`
  - ```{autodoc2-docstring} quantstats_lumi.utils._flatten_dataframe
    :summary:
    ```
````

### API

````{py:function} _mtd(df)
:canonical: quantstats_lumi.utils._mtd

```{autodoc2-docstring} quantstats_lumi.utils._mtd
```
````

````{py:function} _qtd(df)
:canonical: quantstats_lumi.utils._qtd

```{autodoc2-docstring} quantstats_lumi.utils._qtd
```
````

````{py:function} _ytd(df)
:canonical: quantstats_lumi.utils._ytd

```{autodoc2-docstring} quantstats_lumi.utils._ytd
```
````

````{py:function} _pandas_date(df, dates)
:canonical: quantstats_lumi.utils._pandas_date

```{autodoc2-docstring} quantstats_lumi.utils._pandas_date
```
````

````{py:function} _pandas_current_month(df)
:canonical: quantstats_lumi.utils._pandas_current_month

```{autodoc2-docstring} quantstats_lumi.utils._pandas_current_month
```
````

````{py:function} multi_shift(df, shift=3)
:canonical: quantstats_lumi.utils.multi_shift

```{autodoc2-docstring} quantstats_lumi.utils.multi_shift
```
````

````{py:function} to_returns(prices, rf=0.0)
:canonical: quantstats_lumi.utils.to_returns

```{autodoc2-docstring} quantstats_lumi.utils.to_returns
```
````

````{py:function} to_prices(returns, base=100000.0)
:canonical: quantstats_lumi.utils.to_prices

```{autodoc2-docstring} quantstats_lumi.utils.to_prices
```
````

````{py:function} log_returns(returns, rf=0.0, nperiods=None)
:canonical: quantstats_lumi.utils.log_returns

```{autodoc2-docstring} quantstats_lumi.utils.log_returns
```
````

````{py:function} to_log_returns(returns, rf=0.0, nperiods=None)
:canonical: quantstats_lumi.utils.to_log_returns

```{autodoc2-docstring} quantstats_lumi.utils.to_log_returns
```
````

````{py:function} exponential_stdev(returns, window=30, is_halflife=False)
:canonical: quantstats_lumi.utils.exponential_stdev

```{autodoc2-docstring} quantstats_lumi.utils.exponential_stdev
```
````

````{py:function} rebase(prices, base=100.0)
:canonical: quantstats_lumi.utils.rebase

```{autodoc2-docstring} quantstats_lumi.utils.rebase
```
````

````{py:function} group_returns(returns, groupby, compounded=False)
:canonical: quantstats_lumi.utils.group_returns

```{autodoc2-docstring} quantstats_lumi.utils.group_returns
```
````

````{py:function} aggregate_returns(returns, period=None, compounded=True)
:canonical: quantstats_lumi.utils.aggregate_returns

```{autodoc2-docstring} quantstats_lumi.utils.aggregate_returns
```
````

````{py:function} to_excess_returns(returns, rf, nperiods=None)
:canonical: quantstats_lumi.utils.to_excess_returns

```{autodoc2-docstring} quantstats_lumi.utils.to_excess_returns
```
````

````{py:function} _prepare_prices(data, base=1.0)
:canonical: quantstats_lumi.utils._prepare_prices

```{autodoc2-docstring} quantstats_lumi.utils._prepare_prices
```
````

````{py:function} _prepare_returns(data, rf=0.0, nperiods=None)
:canonical: quantstats_lumi.utils._prepare_returns

```{autodoc2-docstring} quantstats_lumi.utils._prepare_returns
```
````

````{py:function} download_returns(ticker, period='max', interval='1d', **kwargs)
:canonical: quantstats_lumi.utils.download_returns

```{autodoc2-docstring} quantstats_lumi.utils.download_returns
```
````

````{py:function} _prepare_benchmark(benchmark=None, period='max', rf=0.0, prepare_returns=True)
:canonical: quantstats_lumi.utils._prepare_benchmark

```{autodoc2-docstring} quantstats_lumi.utils._prepare_benchmark
```
````

````{py:function} _round_to_closest(val, res, decimals=None)
:canonical: quantstats_lumi.utils._round_to_closest

```{autodoc2-docstring} quantstats_lumi.utils._round_to_closest
```
````

````{py:function} _file_stream()
:canonical: quantstats_lumi.utils._file_stream

```{autodoc2-docstring} quantstats_lumi.utils._file_stream
```
````

````{py:function} _in_notebook(matplotlib_inline=False)
:canonical: quantstats_lumi.utils._in_notebook

```{autodoc2-docstring} quantstats_lumi.utils._in_notebook
```
````

````{py:function} _count_consecutive(data)
:canonical: quantstats_lumi.utils._count_consecutive

```{autodoc2-docstring} quantstats_lumi.utils._count_consecutive
```
````

````{py:function} _score_str(val)
:canonical: quantstats_lumi.utils._score_str

```{autodoc2-docstring} quantstats_lumi.utils._score_str
```
````

````{py:function} make_index(ticker_weights, rebalance='1M', period='max', returns=None, match_dates=False)
:canonical: quantstats_lumi.utils.make_index

```{autodoc2-docstring} quantstats_lumi.utils.make_index
```
````

````{py:function} make_portfolio(returns, start_balance=100000.0, mode='comp', round_to=None)
:canonical: quantstats_lumi.utils.make_portfolio

```{autodoc2-docstring} quantstats_lumi.utils.make_portfolio
```
````

````{py:function} _flatten_dataframe(df, set_index=None)
:canonical: quantstats_lumi.utils._flatten_dataframe

```{autodoc2-docstring} quantstats_lumi.utils._flatten_dataframe
```
````
