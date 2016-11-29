"""   """

from py.test import raises

from erpsc.erp_words import *
from erpsc.tests.utils import load_erp_words

###################################################################
###################### TESTS - ERPSC - WORDS ######################
###################################################################

def test_erp_words():
    """Test the Words object."""

    # Check that ERPSCWords returns properly.
    erp = 'test'
    assert ERPWords(erp)

def test_add_ids():
    """   """

    words = load_erp_words()

    words.add_id(1)

    assert words.ids

def test_add_title():
    """   """

    words = load_erp_words()

    words.add_title('title')

    assert words.titles

def test_add_words():
    """   """

    words = load_erp_words()

    words.add_words(['new', 'words'])

    assert words.words

def test_add_year():
    """   """

    words = load_erp_words()

    words.add_year(2112)

    assert words.years

def test_increment_n_articles():
    """   """

    words = load_erp_words()

    words.increment_n_articles()

    assert words.n_articles

def test_check_results():
    """   """

    words = load_erp_words(add_dat=True)

    words.check_results()

    words.n_articles += 1

    with raises(InconsistentDataError):
        assert words.check_results()
