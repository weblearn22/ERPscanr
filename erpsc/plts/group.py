"""Create data plots for ERP-SCANR project - plots for group analysis."""

import os
import matplotlib.pyplot as plt

from erpsc.core.db import check_db

#########################################################################################
#########################################################################################
#########################################################################################

def plot_time_assocs(dat, save_fig=False):
    """

    Parameters
    ----------
    dat : list of list of [str, str, int]
        ERP data - [association, P or N, latency]
    """

    # Plot params
    offsets = {'P': 50, 'N': -50}
    rotations = {'P': 45, 'N': -45}

    # Initialize Plot
    fig = plt.figure(figsize=(12, 5))
    fig.suptitle('ERP Correlates Across Time', fontsize=24, fontweight='bold')
    ax = fig.add_subplot(111)

    # Set plot limits
    ax.set_xlim([50, 600])
    ax.set_ylim([-100, 100])

    # Add x-ticks
    plt.xticks([250, 500], ['250 ms', '500 ms'])
    ax.set_yticks([])

    # Set ticks and plot lines
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)

    # Add data to plot from
    for d in dat:

        # Text takes: [X-pos, Y-pos, word, rotation]
        #  Where X-pos is latency, y-pos & rotation are defaults given +/-
        ax.text(d[2], offsets[d[1]], d[0], rotation=rotations[d[1]], fontsize=20)

    # Save out - if requested
    if save_fig:

        db = check_db(db)
        s_file = os.path.join(db.figs_path, 'LatencyAssociations' + '.svg')

        plt.savefig(s_file, transparent=True)
