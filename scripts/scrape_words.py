"""ERPSCANR: script to run words scrape."""

from erpsc.words import Words
from erpsc.core.io import save_pickle_obj

###################################################################################################
###################################################################################################

TEST = False
S_NAME = 'BaseScrape'

###################################################################################################
###################################################################################################

def main():

    words = Words()

    if TEST:
        words.set_erps([['P100'], ['N100']])
        words.set_exclusions([['protein'], ['protein']])
    else:
        words.set_erps_file()
        words.set_exclusions_file()

    print('\n\nSTARTING WORDS SCRAPE')

    words.scrape_data(db='pubmed', retmax='5000', use_hist=True, verbose=True)

    print('\n\nWORDS SCRAPE FINISHED\n\n')

    save_pickle_obj(words, S_NAME)

    print('\n\nWORDS SCRAPE SAVED\n\n')


if __name__ == "__main__":
    main()
