"""Create data plots for ERP-SCANR project - plots for group analysis."""

import os

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hier

from erpsc.core.db import check_db
from erpsc.plts.utils import _save_fig, _set_lr_spines

###################################################################################################
###################################################################################################

def plot_count_hist(data, plt_log=True, save_fig=False, save_name=None):

    fig, ax = plt.subplots(figsize=(6, 5))
    if plt_log:
        data = np.log10(data)

    plt.hist(data, bins=10, color='#5b7399')

    _set_lr_spines(ax, 2)
    _save_fig(save_fig, save_name)


def plot_time_assocs(dat, save_fig=False, save_name='LatencyAssociations'):
    """Plot top associations for each ERP across time.

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
    _set_lr_spines(ax, 2)
    ax.spines['bottom'].set_position('center')
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add data to plot from
    for d in dat:

        # Text takes: [X-pos, Y-pos, word, rotation]
        #  Where X-pos is latency, y-pos & rotation are defaults given +/-
        ax.text(d[2], offsets[d[1]], d[0], rotation=rotations[d[1]], fontsize=20)

    _save_fig(save_fig, save_name)


def plot_matrix(dat, x_labels, y_labels, square=False, figsize=(10, 12), save_fig=False, save_name='Matrix'):
    """Plot the matrix of percent asscociations between ERPs & terms."""

    f, ax = plt.subplots(figsize=figsize)

    sns.heatmap(dat, square=square, xticklabels=x_labels, yticklabels=y_labels)

    f.tight_layout()

    _save_fig(save_fig, save_name)


def plot_clustermap(dat, cmap='purple', save_fig=False, save_name='Clustermap'):
    """Plot clustermap.

    Parameters
    ----------
    dat : pandas.DataFrame
        Data to create clustermap from.
    """

    # Set up plotting and aesthetics
    sns.set()
    sns.set_context("paper", font_scale=1.5)

    # Set colourmap
    if cmap == 'purple':
        cmap = sns.cubehelix_palette(as_cmap=True)
    elif cmap == 'blue':
        cmap = sns.cubehelix_palette(as_cmap=True, rot=-.3, light=0.9, dark=0.2)

    # Create the clustermap
    cg = sns.clustermap(dat, cmap=cmap, method='complete', metric='cosine', figsize=(12, 10))

    # Fix axes
    cg.cax.set_visible(True)
    _ = plt.setp(cg.ax_heatmap.xaxis.get_majorticklabels(), rotation=60, ha='right')
    _ = plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)

    _save_fig(save_fig, save_name)


def plot_dendrogram(dat, labels, save_fig=False, save_name='Dendrogram'):
    """Plot dendrogram."""

    plt.figure(figsize=(3, 15))

    Y = hier.linkage(dat, method='complete', metric='cosine')

    Z = hier.dendrogram(Y, orientation='left', labels=labels,
                        color_threshold=0.25, leaf_font_size=12)

    _save_fig(save_fig, save_name)
