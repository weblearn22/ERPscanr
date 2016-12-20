"""   """

from erpsc.core.urls import URLS

##################################################################################
##################################################################################
##################################################################################

def test_urls():
    """Test the URLS object."""

    # Check that URLS returns properly, with database inputs
    assert URLS('pubmed')
    assert URLS('pmc')

    # NOTE: ADD ERROR CHECK - AFTER ADD ERROR CHECKING