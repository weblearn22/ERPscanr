"""Tests for the Base Class from erpsc.

NOTES
-----
- Load from file method '_file' are only tested for default (from module) loads.
"""

from py.test import raises

from erpsc.base import Base
from erpsc.tests.utils import load_base
from erpsc.core.errors import InconsistentDataError

########################################################################################
############################ TESTS - ERPSC - GENERAL - BASE ############################
########################################################################################

def test_base():
    """Test the Base() object returns properly."""

    assert Base()

def test_set_erps():
    """Test the set_erps method of Base()."""

    base = load_base()
    base.set_erps(['N100', 'P100'])

    assert base.erps

def test_set_erps_file():
    """Test the set_erps_file method of Base()."""

    base = load_base()
    base.set_erps_file()

    assert base.erps

def tests_check_erps():
    """Test the check_erps method of Base()."""

    base = load_base(set_erps=True)

    base.check_erps()

    assert True

def test_unload_erps():
    """Test unloading of ERP words."""

    base = load_base(set_erps=True)

    base.unload_erps()

    assert not base.erps
    assert not base.n_erps

def test_set_exclusions():
    """Test the set_exclusions method of Base."""

    base = Base()
    base.set_erps(['N100', 'P100'])
    base.set_exclusions(['not', 'this'])

    assert base.exclusions

    # Check error with improper # of exclusion words
    base = Base()
    base.set_erps(['N100', 'P100'])

    with raises(InconsistentDataError):
        base.set_exclusions(['bad'])

def test_set_exclusions_file():
    """Test the set_exclusions_file method of Base()."""

    base = load_base(set_erps=True)
    base.set_exclusions_file()

    assert base.exclusions

def test_check_exclusions():
    """Test the check_exclusions method of Base()."""

    base = load_base(set_erps=True, set_excl=True)

    base.check_exclusions()

    assert True

def test_unload_exclusions():
    """Test unload_exclusions of Base()."""

    base = load_base(set_erps=True, set_excl=True)

    base.unload_exclusions()

    assert not base.exclusions

def test_set_terms():
    """Test the set_terms method of Base."""

    base = load_base()
    base.set_terms(['think', 'do'])

    assert base.terms

def test_set_terms_file_cog():
    """Test the set_terms_file method of Base(), for cognitive files."""

    base = load_base()
    base.set_terms_file('cognitive')

    assert base.terms

def test_set_terms_file_dis():
    """Test the set_terms_file method of Base(), for disease files."""

    base = load_base()
    base.set_terms_file('disease')

    assert base.terms

def test_check_terms():
    """Test the check_terms method of Base()."""

    base = load_base(set_terms='cognitive')

    base.check_terms()

    assert True

def test_unload_terms():
    """Test the unload_terms method of Base()."""

    base = load_base(set_terms='disease')

    base.unload_terms()

    assert not base.terms_type
    assert not base.terms
    assert not base.n_terms
