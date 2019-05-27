"""Utility functions for ERPSCANR plts."""

import os

import matplotlib.pyplot as plt

from erpsc.core.db import check_db

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


def _save_fig(save_fig, savename, folder=None, db=None):

    if save_fig:

        db = check_db(db)
        save_file = os.path.join(db.figs_path, folder, savename + '.svg')

        plt.savefig(save_file, transparent=True)


def _disp_fig(disp_fig):

    if not disp_fig:
        plt.close()
