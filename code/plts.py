"""Plotting functions for the ERPscanr project."""

import os

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from lisc.plts.words import plot_years
from lisc.plts.utils import check_ax, savefig

###################################################################################################
###################################################################################################

@savefig
def plot_count_hist(data, log=True, bins=10, **plt_kwargs):
    """Plot a count histogram of collected data."""

    if log:

        hist, bins, _ = plt.hist(data, bins=bins)
        plt.close()

        # Use non-equal bin sizes, such that they look equal on log scale
        bins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))

    ax = check_ax(plt_kwargs.pop('ax', None), plt_kwargs.pop('figsize', (6, 5)))
    ax.hist(data, bins=bins, color=plt_kwargs.pop('color', '#5b7399'), **plt_kwargs)

    if log:
        ax.set_xscale('log')

    sns.despine(ax=ax)
    plt.setp(ax.spines.values(), linewidth=2)


@savefig
def plot_year_comparison(years, counts, labels, **plt_kwargs):
    """Plot a comparison of number of values across years for multiple elements."""

    ax = check_ax(plt_kwargs.pop('ax', None), plt_kwargs.pop('figsize', (6, 4)))

    for count, label, color in zip(counts, labels, sns.color_palette('muted')):
        ax.plot(years, count, label=label, lw=2.5, color=color, alpha=0.9)

    plt.legend()

    ax.set_xlabel('Decade of Publication', fontsize=14)
    ax.set_ylabel('Number of Articles', fontsize=14)


@savefig
def plot_time_associations(data, **plt_kwargs):
    """Plot top associations for each ERP across time.

    Parameters
    ----------
    data : list of list of [str, str, int]
        ERP data - [association, P or N, latency]
    """

    # Plot params
    offsets = {'P' : 30, 'N': -30}
    rotations = {'P' : 45, 'N': -45}
    alignments = {'P' : 'bottom', 'N' : 'top'}

    # Initialize Plot
    ax = check_ax(plt_kwargs.pop('ax', None), plt_kwargs.pop('figsize', (12, 5)))

    # Set plot limits
    ax.set_xlim([50, 750])
    ax.set_ylim([-100, 100])

    # Set ticks and plot lines
    sns.despine(ax=ax)
    plt.setp(ax.spines.values(), linewidth=3)
    ax.spines['bottom'].set_position('center')
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add x-ticks
    plt.xticks([250, 500], ['250 ms', '500 ms'], fontsize=14)
    ax.set_yticks([])

    # Add data to plot from
    for datum in data:

        # Text takes: [X-pos, Y-pos, word, rotation]
        #   Where X-pos is latency, y-pos & rotation are defaults given +/-
        ax.text(datum[2], offsets[datum[1]], datum[0],
                verticalalignment=alignments[datum[1]],
                rotation=rotations[datum[1]], fontsize=18)


def plot_attrs_by_year(journals, authors):
    """Plot counts of unique attributes by years.

    journals, authors : dict
    """

    fig, ax1 = plt.subplots(figsize=(5, 4))

    plot_years(journals, color='r', label='Journals', alpha=0.85, ax=ax1)

    ax2 = ax1.twinx()
    plot_years(authors, color='g', label='Authors', alpha=0.85, ax=ax2)

    fig.legend(loc='upper left', bbox_to_anchor=(0, 1), bbox_transform=ax1.transAxes)
    ax1.set_ylabel('Unique Journals')
    ax2.set_ylabel('Unique Authors')
