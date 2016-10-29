from erpsc.gen import *

#######################################################################
################## TESTS - ERPSC - GENERAL - CLASSES ##################
#######################################################################

def test_erpdb():
    """   """

    # Check that ERPDB returns properly.
    assert ERPDB()


def test_urls():
    """   """

    # Check that URLS returns properly, with database inputs
    assert URLS('pubmed')
    assert URLS('pmc')

    # NOTE: ADD ERROR CHECK - AFTER ADD ERROR CHECKING


#####################################################################
################## TESTS - ERPSC - GENERAL - BASES ##################
#####################################################################

## NOTES:
##  - 'check' functions are not tested.
##  - Load from file function '_file' are only tested for default (from module) loads.

def test_erpsc_base():
    """   """

    assert ERPSCBase()

def test_set_erps():
    """   """
    pass

def test_set_erps_file():
    """   """
    pass

def test_set_exclusions():
    """   """
    pass

def test_set_exclusions_file():
    """   """
    pass

def test_set_terms():
    """   """
    pass

def test_set_terms_file():
    """   """
    pass
