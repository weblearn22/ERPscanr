"""   """

from erpsc.erp_words import ERPWords
from erpsc.words import Words
from erpsc.words import _ids_to_str, _process_words

#######################################################################################
################################ TESTS - ERPSC - WORDS ################################
#######################################################################################

def test_words():
    """   """

    assert Words()

def test_add_results():
    """   """

    words = Words()
    new_word = ERPWords('test')

    words.add_results(new_word)

    assert words.results

def test_scrape():

    words = Words()

    # Add ERPs and terms
    words.set_erps(['N400', 'P600'])
    words.set_terms(['language', 'memory'])
    words.set_exclusions(['cell', ''])

    words.scrape_data()

    assert True

    comb_words(words)
    freq_dists(words)
    check_words(words)
    save_pickle(words)

def comb_words(words):

    words.combine_words()

    assert True

def freq_dists(words):

    words.freq_dists()

    assert True

def check_words(words):

    words.check_words()

    assert True

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
