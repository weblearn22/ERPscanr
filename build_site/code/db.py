"""A database object that defines the layout """

from pathlib import Path

###################################################################################################
###################################################################################################

class WebDB(object):
    """Class to hold database information for ERP-SCANR Website.

    Parameters
    ----------
    base_path : str
        Path to base directory of website.
    post_path : str
        Path to posts directory.
    data_path : str
        Path to data directory.
    plot_path : str
        Path to plots directory.
    """

    def __init__(self, base_path):
        """Initialize WebDB object."""

        # Set base path for the website
        self.base_path = Path(base_path)

        # Set paths to directories for the website
        self.post_path = self.base_path / '_posts'
        self.data_path = self.base_path / '_data'
        self.assets_path = self.base_path / 'assets'
        self.erp_plot_path = self.assets_path / 'ERPs'
        self.group_plot_path = self.assets_path / 'FIGS'
