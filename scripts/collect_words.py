"""Script to run words collection for the ERP-SCANR project."""

from lisc import Words
from lisc.utils import save_object

###################################################################################################
###################################################################################################

TEST = True
SAVE_NAME = 'BaseScrape'

###################################################################################################
###################################################################################################

def main():

    words = Words()

    if TEST:
        words.add_terms([['P100'], ['N100']])
        words.add_terms([['protein'], ['protein']], term_type='exclusions')

    else:
        # ToDo: coordinate where to load terms from
        words.set_terms_file('erps.txt', dim='A')
        words.set_terms_file('erps_exclude.txt', term_type='exclusions', dim='A')

    print('\n\nRUNNING WORDS COLLECTION')
    retmax = '5' if TEST else '5000'
    words.run_collection(db='pubmed', retmax=retmax, usehistory=True, verbose=True)
    print('\n\nWORDS COLLECTION FINISHED')

    save_object(words, SAVE_NAME)
    print('WORDS COLLECTION SAVED\n\n')


if __name__ == "__main__":
    main()
