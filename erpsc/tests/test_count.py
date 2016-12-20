"""   """

from erpsc.count import *

#######################################################################################
################################ TESTS - ERPSC - COUNT ################################
#######################################################################################

def test_erpsc_count():
    """Test the ERPSCCount object."""

    # Check that ERPSCCount returns properly
    assert Count()

def test_scrape_data():
    """   """

    counts = Count()

    # Add ERPs and terms
    counts.set_erps(['N400', 'P600'])
    counts.set_terms(['language', 'memory'])

def test_check_cooc_erps():
    """   """
    pass

def test_check_cooc_terms():
    """   """
    pass

def test_check_top():
    """   """
    pass

def test_check_counts():
    """   """
    pass

def test_save_pickle():
    """   """
    pass
