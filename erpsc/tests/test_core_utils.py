"""Tests for the basic utilities functions from erpsc.core."""

from erpsc.core.utils import comb_terms

##########################################################################
##########################################################################
##########################################################################

def test_comb_terms():
    """Test the comb_terms function."""

    out = comb_terms(['one', 'two'], 'or')
    assert out == '("one"OR"two")'

    out = comb_terms(['one', 'two'], 'not')
    assert out == 'NOT"one"NOT"two"'
