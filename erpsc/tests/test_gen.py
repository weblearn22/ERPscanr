from erpsc.gen import *

###########################################################################
#################### TESTS - ERPSC - GENERAL - CLASSES ####################
###########################################################################

def test_erpdb():
    """Test the ERPDB object."""

    # Check that ERPDB returns properly.
    assert ERPDB()

def test_urls():
    """Test the URLS object."""

    # Check that URLS returns properly, with database inputs
    assert URLS('pubmed')
    assert URLS('pmc')

    # NOTE: ADD ERROR CHECK - AFTER ADD ERROR CHECKING

########################################################################
#################### TESTS - ERPSC - GENERAL - BASE ####################
########################################################################

## NOTES:
##  - 'check' functions are not tested.
##  - Load from file function '_file' are only tested for default (from module) loads.

def test_erpsc_base():
    """Test the ERPSCBase object."""

    assert ERPSCBase()

def test_set_erps():
    """Test the set_erps method of ERPSCBase."""

    base = ERPSCBase()
    base.set_erps(['N100', 'P100'])

    assert base.erps

def test_set_erps_file():
    """Test the set_erps_file method of ERPSCBase."""

    base = ERPSCBase()
    base.set_erps_file()

    assert base.erps

def test_unload_erps():
    """Test unloading of ERP words."""

    base = ERPSCBase()
    base.set_erps_file()

    base.unload_erps()

    assert not base.erps
    assert not base.n_erps

def test_set_exclusions():
    """Test the set_exclusions method of ERPSCBase."""

    base = ERPSCBase()
    base.set_erps(['N100', 'P100'])
    base.set_exclusions(['not', 'this'])

    assert base.exclusions

def test_set_exclusions_file():
    """Test the set_exclusions_file method of ERPSCBase."""

    base = ERPSCBase()
    base.set_erps_file()
    base.set_exclusions_file()

    assert base.exclusions

def test_unload_exclusions():
    """Test unloading of exclusion words."""

    base = ERPSCBase()
    base.set_erps_file()
    base.set_exclusions_file()

    base.unload_exclusions()

    assert not base.exclusions

def test_set_terms():
    """Test the set_terms method of ERPSCBase."""

    base = ERPSCBase()
    base.set_terms(['think', 'do'])

    assert base.terms

def test_set_terms_file_cog():
    """Test the set_terms_file method of ERPSCBase, for cognitive files."""

    base = ERPSCBase()
    base.set_terms_file('cognitive')

    assert base.terms

def test_set_terms_file_dis():
    """Test the set_terms_file method of ERPSCBase, for disease files."""

    base = ERPSCBase()
    base.set_terms_file('disease')

    assert base.terms

def test_unload_terms():
    """Test unloading of term words."""

    base = ERPSCBase()
    base.set_terms_file('disease')

    base.unload_terms()

    assert not base.terms_type
    assert not base.terms
    assert not base.n_terms
