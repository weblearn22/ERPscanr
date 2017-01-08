"""Tests for the Words() class and related functions from erpsc."""

import requests
from bs4 import BeautifulSoup

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

def test_extract_add_info():
    """  """

    words = Words()

    # Check page with all fields defined - check data extraction
    erp_word = ERPWords('test')
    page = requests.get(("http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
                         "efetch.fcgi?&db=pubmed&retmode=xml&id=28000963"))
    page_soup = BeautifulSoup(page.content, "xml")
    art = page_soup.findAll('PubmedArticle')[0]
    words.extract_add_info(erp_word, 111111, art)

    assert erp_word.ids[0] == 111111
    assert erp_word.titles[0] == ("A Neurocomputational Model of the N400"
                                  " and the P600 in Language Processing.")
    assert erp_word.words[0][0] == "ten"
    assert erp_word.kws[0][0] == "Computational modeling"
    assert erp_word.years[0] == '2016'

    # Check page with all fields missing - check error handling
    page = requests.get('http://www.google.com')
    erp_word = words.extract_add_info(erp_word, 999999, page)

    assert erp_word.ids[1] == 999999
    assert erp_word.titles[1] == None
    assert erp_word.words[1] == None
    assert erp_word.kws[1] == None
    assert erp_word.years[1] == None

def test_scrape():

    words = Words()

    # Add ERPs and terms
    words.set_erps(['N400', 'P600'])
    words.set_terms(['language', 'memory'])
    words.set_exclusions(['cell', ''])

    words.scrape_data(db='pubmed', retmax='5')

    assert True

    comb_words(words)
    freq_dists(words)
    check_words(words)

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

    words = 'The Last wOrd, in they eRp!'

    words_out = _process_words(words)
    exp_out = ['last', 'word', 'erp']

    assert words_out == exp_out
