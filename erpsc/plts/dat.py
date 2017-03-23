"""Create data plots for ERP-SCANR project."""

import os
import matplotlib.pyplot as plt

from erpsc.core.db import check_db

#####################################################################################
#####################################################################################
#####################################################################################

def plot_years(year_counts, label, disp_fig=True, save_fig=False, db=None):
    """Plot publications across years histogram."""

    f, ax = plt.subplots(figsize=(12, 4))

    yrs = set(range(1985, 2016))

    # Extract x & y data to plot
    x_dat = [y[0] for y in year_counts]
    y_dat = [y[1] for y in year_counts]

    # Add line and points to plot
    plt.plot(x_dat, y_dat)
    plt.plot(x_dat, y_dat, '.', markersize=14)

    # Set plot limits
    plt.xlim([min(yrs), max(yrs)])
    plt.ylim([0, max(y_dat)+5])

    # Add title & labels
    plt.title('Publication History')
    plt.xlabel('Year')
    plt.ylabel('# Pubs')

    if save_fig:

        db = check_db(db)
        s_file = os.path.join(db.figs_path, 'year', label + '.png')

        plt.savefig(s_file, transparent=True)
        if not disp_fig:
            plt.close()
