"""Helper functions for testing ERPSC."""

from erpsc.erp_words import ERPWords

##
##
##

def load_erp_words(add_dat=False):
    """   """

    test_erp = 'test'
    words = ERPWords(test_erp)

    if add_dat:
        words.add_id(1)
        words.add_title('title')
        words.add_words(['new', 'words'])
        words.add_year(2112)
        words.increment_n_articles()

    return words