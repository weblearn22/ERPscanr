"""Plotting functions for the  ERPscanr project."""

import os

import numpy as np
import matplotlib.pyplot as plt

###################################################################################################
###################################################################################################

def plot_count_hist(data, plt_log=True):
    """Plot a count histogram of collected data."""

    fig, ax = plt.subplots(figsize=(6, 5))

    if plt_log:
        data = np.log10(data)

    plt.hist(data, bins=10, color='#5b7399')

    _set_lr_spines(ax, 2)


def plot_time_associations(data):
    """Plot top associations for each ERP across time.

    Parameters
    ----------
    data : list of list of [str, str, int]
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
    _set_lr_spines(ax, 2)
    ax.spines['bottom'].set_position('center')
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add data to plot from
    for datum in data:

        # Text takes: [X-pos, Y-pos, word, rotation]
        #   Where X-pos is latency, y-pos & rotation are defaults given +/-
        ax.text(datum[2], offsets[datum[1]], datum[0],
                rotation=rotations[datum[1]], fontsize=20)

###################################################################################################
###################################################################################################

def _set_lr_spines(ax, lw=None):
    """Set the spines to drop top & right box & set linewidth."""

    # Set the top and right side frame & ticks off
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Set linewidth of remaining spines
    if lw:
        ax.spines['left'].set_linewidth(lw)
        ax.spines['bottom'].set_linewidth(lw)
