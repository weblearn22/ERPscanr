"""   """

from erpsc.base import Base

########################################################################
#################### TESTS - ERPSC - GENERAL - BASE ####################
########################################################################

## NOTES:
##  - 'check' functions are not tested.
##  - Load from file function '_file' are only tested for default (from module) loads.

def test_erpsc_base():
    """Test the ERPSCBase object."""

    assert Base()

def test_set_erps():
    """Test the set_erps method of Base."""

    base = Base()
    base.set_erps(['N100', 'P100'])

    assert base.erps

def test_set_erps_file():
    """Test the set_erps_file method of Base."""

    base = Base()
    base.set_erps_file()

    assert base.erps

def tests_check_erps():
    """   """

    base = Base()
    base.set_erps_file()

    base.check_erps()

    assert True

def test_unload_erps():
    """Test unloading of ERP words."""

    base = Base()
    base.set_erps_file()

    base.unload_erps()

    assert not base.erps
    assert not base.n_erps

def test_set_exclusions():
    """Test the set_exclusions method of Base."""

    base = Base()
    base.set_erps(['N100', 'P100'])
    base.set_exclusions(['not', 'this'])

    assert base.exclusions

def test_set_exclusions_file():
    """Test the set_exclusions_file method of Base."""

    base = Base()
    base.set_erps_file()
    base.set_exclusions_file()

    assert base.exclusions

def test_check_exclusions():
    """   """

    base = Base()
    base.set_erps_file()
    base.set_exclusions_file()

    base.check_exclusions()

    assert True

def test_unload_exclusions():
    """Test unloading of exclusion words."""

    base = Base()
    base.set_erps_file()
    base.set_exclusions_file()

    base.unload_exclusions()

    assert not base.exclusions

def test_set_terms():
    """Test the set_terms method of Base."""

    base = Base()
    base.set_terms(['think', 'do'])

    assert base.terms

def test_set_terms_file_cog():
    """Test the set_terms_file method of Base, for cognitive files."""

    base = Base()
    base.set_terms_file('cognitive')

    assert base.terms

def test_set_terms_file_dis():
    """Test the set_terms_file method of Base, for disease files."""

    base = Base()
    base.set_terms_file('disease')

    assert base.terms

def test_check_terms():
    """   """

    base = Base()

    base.set_terms_file('cognitive')

    base.check_terms()

    assert True

def test_unload_terms():
    """Test unloading of term words."""

    base = Base()
    base.set_terms_file('disease')

    base.unload_terms()

    assert not base.terms_type
    assert not base.terms
    assert not base.n_terms
