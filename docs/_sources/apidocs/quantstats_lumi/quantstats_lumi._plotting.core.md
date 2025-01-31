# {py:mod}`quantstats_lumi._plotting.core`

```{py:module} quantstats_lumi._plotting.core
```

```{autodoc2-docstring} quantstats_lumi._plotting.core
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_get_colors <quantstats_lumi._plotting.core._get_colors>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core._get_colors
    :summary:
    ```
* - {py:obj}`plot_returns_bars <quantstats_lumi._plotting.core.plot_returns_bars>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_returns_bars
    :summary:
    ```
* - {py:obj}`plot_timeseries <quantstats_lumi._plotting.core.plot_timeseries>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_timeseries
    :summary:
    ```
* - {py:obj}`plot_histogram <quantstats_lumi._plotting.core.plot_histogram>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_histogram
    :summary:
    ```
* - {py:obj}`plot_rolling_stats <quantstats_lumi._plotting.core.plot_rolling_stats>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_rolling_stats
    :summary:
    ```
* - {py:obj}`plot_rolling_beta <quantstats_lumi._plotting.core.plot_rolling_beta>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_rolling_beta
    :summary:
    ```
* - {py:obj}`plot_longest_drawdowns <quantstats_lumi._plotting.core.plot_longest_drawdowns>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_longest_drawdowns
    :summary:
    ```
* - {py:obj}`plot_distribution <quantstats_lumi._plotting.core.plot_distribution>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_distribution
    :summary:
    ```
* - {py:obj}`plot_table <quantstats_lumi._plotting.core.plot_table>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_table
    :summary:
    ```
* - {py:obj}`monthly_heatmap_detailedview <quantstats_lumi._plotting.core.monthly_heatmap_detailedview>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.monthly_heatmap_detailedview
    :summary:
    ```
* - {py:obj}`calculate_monthly_drawdowns <quantstats_lumi._plotting.core.calculate_monthly_drawdowns>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.calculate_monthly_drawdowns
    :summary:
    ```
* - {py:obj}`format_cur_axis <quantstats_lumi._plotting.core.format_cur_axis>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.format_cur_axis
    :summary:
    ```
* - {py:obj}`format_pct_axis <quantstats_lumi._plotting.core.format_pct_axis>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core.format_pct_axis
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_FLATUI_COLORS <quantstats_lumi._plotting.core._FLATUI_COLORS>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core._FLATUI_COLORS
    :summary:
    ```
* - {py:obj}`_GRAYSCALE_COLORS <quantstats_lumi._plotting.core._GRAYSCALE_COLORS>`
  - ```{autodoc2-docstring} quantstats_lumi._plotting.core._GRAYSCALE_COLORS
    :summary:
    ```
````

### API

````{py:data} _FLATUI_COLORS
:canonical: quantstats_lumi._plotting.core._FLATUI_COLORS
:value: >
   ['#FEDD78', '#348DC1', '#BA516B', '#4FA487', '#9B59B6', '#613F66', '#84B082', '#DC136C', '#559CAD', ...

```{autodoc2-docstring} quantstats_lumi._plotting.core._FLATUI_COLORS
```

````

````{py:data} _GRAYSCALE_COLORS
:canonical: quantstats_lumi._plotting.core._GRAYSCALE_COLORS
:value: >
   ['#000000', '#222222', '#555555', '#888888', '#AAAAAA', '#CCCCCC', '#EEEEEE', '#333333', '#666666', ...

```{autodoc2-docstring} quantstats_lumi._plotting.core._GRAYSCALE_COLORS
```

````

````{py:function} _get_colors(grayscale)
:canonical: quantstats_lumi._plotting.core._get_colors

```{autodoc2-docstring} quantstats_lumi._plotting.core._get_colors
```
````

````{py:function} plot_returns_bars(returns, benchmark=None, returns_label='Strategy', hline=None, hlw=None, hlcolor='red', hllabel='', resample='YE', title='Returns', match_volatility=False, log_scale=False, figsize=(10, 6), grayscale=False, fontname='Arial', ylabel=True, subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.core.plot_returns_bars

```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_returns_bars
```
````

````{py:function} plot_timeseries(returns, benchmark=None, title='Returns', compound=False, cumulative=True, fill=False, returns_label='Strategy', hline=None, hlw=None, hlcolor='red', hllabel='', percent=True, match_volatility=False, log_scale=False, resample=None, lw=1.5, figsize=(10, 6), ylabel='', grayscale=False, fontname='Arial', subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.core.plot_timeseries

```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_timeseries
```
````

````{py:function} plot_histogram(returns, benchmark, resample='ME', bins=20, fontname='Arial', grayscale=False, title='Returns', kde=True, figsize=(10, 6), ylabel=True, subtitle=True, compounded=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.core.plot_histogram

```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_histogram
```
````

````{py:function} plot_rolling_stats(returns, benchmark=None, title='', returns_label='Strategy', hline=None, hlw=None, hlcolor='red', hllabel='', lw=1.5, figsize=(10, 6), ylabel='', grayscale=False, fontname='Arial', subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.core.plot_rolling_stats

```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_rolling_stats
```
````

````{py:function} plot_rolling_beta(returns, benchmark, window1=126, window1_label='', window2=None, window2_label='', title='', hlcolor='red', figsize=(10, 6), grayscale=False, fontname='Arial', lw=1.5, ylabel=True, subtitle=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.core.plot_rolling_beta

```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_rolling_beta
```
````

````{py:function} plot_longest_drawdowns(returns, periods=5, lw=1.5, fontname='Arial', grayscale=False, title=None, log_scale=False, figsize=(10, 6), ylabel=True, subtitle=True, compounded=True, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.core.plot_longest_drawdowns

```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_longest_drawdowns
```
````

````{py:function} plot_distribution(returns, figsize=(10, 6), fontname='Arial', grayscale=False, ylabel=True, subtitle=True, compounded=True, title=None, savefig=None, show=True, log_scale=False)
:canonical: quantstats_lumi._plotting.core.plot_distribution

```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_distribution
```
````

````{py:function} plot_table(tbl, columns=None, title='', title_loc='left', header=True, colWidths=None, rowLoc='right', colLoc='right', colLabels=None, edges='horizontal', orient='horizontal', figsize=(5.5, 6), savefig=None, show=False)
:canonical: quantstats_lumi._plotting.core.plot_table

```{autodoc2-docstring} quantstats_lumi._plotting.core.plot_table
```
````

````{py:function} monthly_heatmap_detailedview(returns, grayscale=False, figsize=(14, 6), annot_size=11, returns_label='Strategy', fontname='Arial', monthly_dd_font_rate=0.8, annual_dd_font_rate=0.8, return_font_rate=1.0, savefig=None, show=True)
:canonical: quantstats_lumi._plotting.core.monthly_heatmap_detailedview

```{autodoc2-docstring} quantstats_lumi._plotting.core.monthly_heatmap_detailedview
```
````

````{py:function} calculate_monthly_drawdowns(returns)
:canonical: quantstats_lumi._plotting.core.calculate_monthly_drawdowns

```{autodoc2-docstring} quantstats_lumi._plotting.core.calculate_monthly_drawdowns
```
````

````{py:function} format_cur_axis(x, _)
:canonical: quantstats_lumi._plotting.core.format_cur_axis

```{autodoc2-docstring} quantstats_lumi._plotting.core.format_cur_axis
```
````

````{py:function} format_pct_axis(x, _)
:canonical: quantstats_lumi._plotting.core.format_pct_axis

```{autodoc2-docstring} quantstats_lumi._plotting.core.format_pct_axis
```
````
