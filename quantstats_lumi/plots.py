"""
Visualization Module for Financial Performance

Provides plotting functions to visualize:
- Cumulative returns
- Drawdown curves
- Rolling metrics (Sharpe, Volatility)
- Return distributions
- Monthly returns heatmaps
- Snapshot tear sheets

All plots are built on matplotlib and can be rendered interactively or saved to file.
"""
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# QuantStats: Portfolio analytics for quants
# https://github.com/ranaroussi/quantstats
#
# Copyright 2019-2023 Ran Aroussi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from pandas.plotting import register_matplotlib_converters as _rmc

    _rmc()
except ImportError:
    pass

from quantstats_lumi._plotting.wrappers import *
from quantstats_lumi._plotting.wrappers import snapshot as _snapshot

def snapshot(
    returns,
    grayscale=False,
    figsize=(10, 8),
    title="Portfolio Summary",
    fontname="Arial",
    lw=1.5,
    mode="comp",
    subtitle=True,
    savefig=None,
    show=True,
    log_scale=False,
    **kwargs,
):
    """Generate comprehensive portfolio performance visualization
    
    ## Parameters
    
    - `returns` (pd.Series/DataFrame): Strategy returns series
    - `grayscale` (bool, default=False): Use grayscale theme
    - `figsize` (tuple, default=(10,8)): Figure dimensions
    - `title` (str, default="Portfolio Summary"): Chart title
    - `fontname` (str, default="Arial"): Base font family
    - `lw` (float, default=1.5): Line width for equity curve
    - `mode` (str, default="comp"): Return calculation mode
    - `subtitle` (bool, default=True): Show date range subtitle
    - `savefig` (str/dict, optional): Save path/config
    - `show` (bool, default=True): Immediately display plot
    - `log_scale` (bool, default=False): Use logarithmic Y-axis
    - `**kwargs`: Passed to matplotlib
    
    ## Returns
    
    matplotlib.figure.Figure: Generated figure object
    
    ## Implementation
    
    Wrapper for [_plotting.wrappers.snapshot] that handles:
    - Multi-column DataFrame inputs
    - Automatic portfolio construction
    - Plot styling configuration
    
    For full implementation details see:
    [wrappers.snapshot](#quantstats_lumi._plotting.wrappers.snapshot)
    """
    return _snapshot(returns, **kwargs)
