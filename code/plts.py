"""Plotting functions for the ERPscanr project."""

import os

import numpy as np
import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt

from lisc.plts.words import plot_years
from lisc.plts.utils import check_ax, savefig

from analysis import scale_number, scale_list

###################################################################################################
###################################################################################################

@savefig
def plot_count_hist(data, log=True, bins=10, xlabel=None, ylabel=None, **plt_kwargs):
    """Plot a count histogram of collected data."""

    if log:

        # Drop zeros, that mess up logging
        data = np.array(data)
        data = data[~(data == 0)]

        # Use non-equal bin sizes, such that they look equal on log scale
        hist, bins = np.histogram(data, bins=bins)
        bins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))

    ax = check_ax(plt_kwargs.pop('ax', None), plt_kwargs.pop('figsize', (6, 5)))
    ax.hist(data, bins=bins, color=plt_kwargs.pop('color', '#5b7399'), **plt_kwargs)

    if log:
        ax.set_xscale('log')
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

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
def plot_time_associations(data, exclude=[], **plt_kwargs):
    """Plot top associations for each ERP across time.

    Parameters
    ----------
    data : list of list of [str, str, int, str]
        ERP latency data, as [ERP, P or N, latency, association].
    """

    # plot params
    offsets = {'P' : 25, 'N': -25}
    rotations = {'P' : 45, 'N': -45}
    alignments = {'P' : 'bottom', 'N' : 'top'}

    # create axis
    ax = check_ax(plt_kwargs.pop('ax', None), plt_kwargs.pop('figsize', (10, 4)))

    # set plot limits
    ax.set_xlim(plt_kwargs.pop('xlim', [50, 700]))
    ax.set_ylim(plt_kwargs.pop('ylim', [-100, 100]))

    # set ticks and plot lines
    sns.despine(ax=ax)
    plt.setp(ax.spines.values(), linewidth=3)
    ax.spines['bottom'].set_position('center')
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # add x-ticks
    plt.xticks([250, 500], ['250 ms', '500 ms'], fontsize=18)
    ax.set_yticks([])

    # add data to plot
    for datum in data:

        if datum['name'] in exclude: continue

        # text takes: [X-pos, Y-pos, word, rotation]
        #   Where X-pos is latency, y-pos & rotation are defaults given +/-
        ax.text(datum['latency'], offsets[datum['polarity']], datum['association'],
                verticalalignment=alignments[datum['polarity']],
                rotation=rotations[datum['polarity']], fontsize=18)


@savefig
def plot_attrs_by_year(journals, authors, **plt_kwargs):
    """Plot counts of unique attributes by years.

    journals, authors : dict
    """

    fig, ax1 = plt.subplots(figsize=plt_kwargs.pop('figsize', (6, 5)))

    plot_years(journals, color='r', label='Journals',
               alpha=plt_kwargs.pop('alpha', 0.85), ax=ax1)

    ax2 = ax1.twinx()
    plot_years(authors, color='g', label='Authors',
               alpha=plt_kwargs.pop('alpha', 0.85), ax=ax2)

    fig.legend(loc='upper left', bbox_to_anchor=(0, 1), bbox_transform=ax1.transAxes)

    ax1.set_ylabel('Unique Journals')
    ax2.set_ylabel('Unique Authors')


@savefig
def plot_network(network, labels, edge_weights=(0.1, 2), layout_seed=None, figsize=(10, 6)):
    """Plot network.

    Notes: uses the spring_layout approach for setting the layout.
    """

    plt.figure(figsize=figsize)

    # Compute the edges weights to visualize in the plot
    weights = [network[ii][jj]['weight'] for ii, jj in network.edges()]
    widths = scale_list(weights, *edge_weights)

    # Get the location information for plotting the graph
    pos = nx.spring_layout(network, seed=layout_seed)

    # Update the label positions to offset them from on top of nodes
    label_pos = {ind : array + [0, 0.04] for ind, array in pos.items()}

    nx.draw(network, pos=pos, node_size=75, alpha=0.75, width=widths)
    nx.draw_networkx_labels(network, label_pos, labels=labels, font_size=16);


@savefig
def plot_latencies(polarities, latencies, **plt_kwargs):
    """Plot ERP latencies."""

    offsets = {'P' : 25, 'N': -25, 'X' : 0}

    ax = check_ax(plt_kwargs.pop('ax', None), plt_kwargs.pop('figsize', (10, 4)))

    for pol, lat in zip(polarities, latencies):
        ax.plot(lat, offsets[pol], 'b.',
                markersize=plt_kwargs.pop('markersize', 20),
                alpha=plt_kwargs.pop('alpha', 0.25))

    ax.set_ylim([-50, 50])
    ax.set_yticks([-25, 25])
    ax.set_yticklabels(['N', 'P'])

    ax.set_xlabel('Latency')


@savefig
def plot_latency_values(latencies, avgs, **plt_kwargs):
    """Plot average association values across latencies."""

    ax = check_ax(plt_kwargs.pop('ax', None), plt_kwargs.pop('figsize', (6, 4)))

    xlabel = plt_kwargs.pop('xlabel', 'Latency')
    ylabel = plt_kwargs.pop('ylabel', 'Association')

    ax.plot(latencies, avgs, '.', **plt_kwargs)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
