"""Create data plots for ERP-SCANR project - plots for single ERPs (for ERP profiles)."""

import os

import matplotlib.pyplot as plt

from erpsc.core.db import check_db
from erpsc.plts.utils import _disp_fig, _save_fig

###################################################################################################
###################################################################################################

def plot_years(year_counts, label, disp_fig=True, save_fig=False, db=None):
    """Plot publications across years histogram."""

    f, ax = plt.subplots(figsize=(10, 5))

    yrs = set(range(1985, 2016))

    # Extract x & y data to plot
    x_dat = [y[0] for y in year_counts]
    y_dat = [y[1] for y in year_counts]

    # Add line and points to plot
    plt.plot(x_dat, y_dat)
    plt.plot(x_dat, y_dat, '.', markersize=16)

    # Set plot limits
    plt.xlim([min(yrs), max(yrs)])
    plt.ylim([0, max(y_dat)+5])

    # Add title & labels
    plt.title('Publication History', fontsize=24, fontweight='bold')
    plt.xlabel('Year', fontsize=18)
    plt.ylabel('# Pubs', fontsize=18)

    _save_fig(save_fig, label, folder='year', db=db)
    _disp_fig(disp_fig)
