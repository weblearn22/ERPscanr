"""   """

from erpsc.core.utils import comb_terms

##
##
##

def test_comb_terms():
    """   """

    out = comb_terms(['one', 'two'], 'or')
    assert out == '("one"OR"two")'

    out = comb_terms(['one', 'two'], 'not')
    assert out == 'NOT"one"NOT"two"'
