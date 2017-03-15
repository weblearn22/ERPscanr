"""Helper functions for testing ERPSC."""

import pkg_resources as pkg

from erpsc.base import Base
from erpsc.erp_data import ERPData
from erpsc.core.db import ERPDB

##################################################################################
##################################################################################
##################################################################################

class TestDB(ERPDB):
    """Overloads the ERPDB object as database object for test data."""

    def __init__(self):

        # Initialize from OMDB object
        ERPDB.__init__(self, auto_gen=False)

        # Set up the base path to tests data
        self.project_path = pkg.resource_filename(__name__, 'data')
        self.gen_paths()

##################################################################################
##################################################################################
##################################################################################

def load_base(set_erps=False, set_excl=False, set_terms=None):
    """Helper function to load Base() object for testing."""

    base = Base()

    if set_erps:
        base.set_erps_file()

    if set_excl:
        base.set_exclusions_file()

    if set_terms:
        base.set_terms_file(set_terms)

    return base

def load_erp_data(add_dat=False, n=1):
    """Helper function to load ERPData() object for testing."""

    words = ERPData('test')

    if add_dat:
        for i in range(n):
            words.add_id(1)
            words.add_title('title')
            words.add_journal('science', 'sc')
            words.add_authors([('A', 'B', 'C', 'D')])
            words.add_words(['new', 'words'])
            words.add_kws(['lots', 'of', 'erps'])
            words.add_pub_date((2112, 'Jan'))
            words.add_doi('doi_str')
            words.increment_n_articles()

    return words
