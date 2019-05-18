"""Utility functions for ERPSCANR plts."""

import matplotlib.pyplot as plt

from erpsc.core.db import check_db

###################################################################################################
###################################################################################################

def _save_fig(save_fig, savename, folder=None, db=None):

    if save_fig:

        db = check_db(db)
        save_file = os.path.join(db.figs_path, folder, savename + '.svg')

        plt.savefig(save_file, transparent=True)


def _disp_fig(disp_fig):

    if not disp_fig:
        plt.close()
