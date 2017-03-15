"""Tests for the ERPData() class and related functions from erpsc."""

from py.test import raises

from erpsc.erp_data import *
from erpsc.tests.utils import load_erp_data

######################################################################################
############################## TESTS - ERPSC - ERP_DATA ##############################
######################################################################################

def test_erp_data():
    """Test the ERPData object."""

    # Check that ERPData returns properly.
    erp = 'test'
    assert ERPData(erp)

def test_add_id():
    """   """

    words = load_erp_data()

    words.add_id(1)

    assert words.ids

def test_add_title():
    """   """

    words = load_erp_data()

    words.add_title('title')

    assert words.titles

def test_add_authors():
    """   """

    words = load_erp_data()

    words.add_authors(('Last', 'First', 'IN', 'School'))

    assert words.authors

def test_add_journal():
    """   """

    words = load_erp_data()

    words.add_journal('Journal name', 'J abbrev')

    assert words.journals

def test_add_words():
    """   """

    words = load_erp_data()

    words.add_words(['new', 'words'])

    assert words.words

def test_add_kws():
    """   """

    words = load_erp_data()

    words.add_kws(['list', 'of', 'kws'])

    assert words.kws

def test_add_pub_date():
    """   """

    words = load_erp_data()

    words.add_pub_date((2000, 'Feb'))

    assert words.years
    assert words.months

def test_add_doi():
    """   """

    words = load_erp_data()

    words.add_doi('doi_str')

    assert words.dois

"""
def test_add_year():
    "   ""

    words = load_erp_data()

    words.add_year(2112)

    assert words.years
"""

def test_increment_n_articles():
    """   """

    words = load_erp_data()

    words.increment_n_articles()

    assert words.n_articles

def test_check_results():
    """   """

    words = load_erp_data(add_dat=True)

    words.check_results()

    words.n_articles += 1

    with raises(InconsistentDataError):
        assert words.check_results()
