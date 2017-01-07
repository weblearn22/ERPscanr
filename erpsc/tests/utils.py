"""Helper functions for testing ERPSC."""

import pkg_resources as pkg

from erpsc.base import Base
from erpsc.erp_words import ERPWords
from erpsc.core.db import ERPDB

##################################################################################
##################################################################################
##################################################################################

class TestDB(ERPDB):
    """   """

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

def load_erp_words(add_dat=False):
    """Helper function to load ERPWords() object for testing."""

    test_erp = 'test'
    words = ERPWords(test_erp)

    if add_dat:
        words.add_id(1)
        words.add_title('title')
        words.add_journal('science', 'sc')
        words.add_authors(('A', 'B', 'C', 'D'))
        words.add_words(['new', 'words'])
        words.add_kws(['lots', 'of', 'erps'])
        words.add_year(2112)
        words.increment_n_articles()

    return words
