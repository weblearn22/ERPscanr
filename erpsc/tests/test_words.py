"""   """

from erpsc.words import Words
from erpsc.words import _ids_to_str, _process_words

#######################################################################################
################################ TESTS - ERPSC - WORDS ################################
#######################################################################################

def test_words():
    """   """

    assert Words()

#######################################################################################
###################### TEST - ERPSC - WORDS - PRIVATE FUNCTIONS  ######################
#######################################################################################

def test_ids_to_str():
    """
    NOTE: unclear how to initialize bs4 tag objects.
    """
    pass

def test_process_words():
    """   """

    words = ['The', 'Last', 'wOrd', 'in', 'they', 'eRp']

    words_out = _process_words(words)
    exp_out = ['last', 'word', 'erp']

    assert words_out == exp_out
