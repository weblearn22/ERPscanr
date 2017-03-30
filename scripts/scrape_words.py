from erpsc.words import Words
from erpsc.core.io import save_pickle_obj

###############################################################################
###############################################################################

TEST = False
S_NAME = 'BaseScrape'

###############################################################################
###############################################################################

def main():
    """Run scrape of words data."""

    words = Words()

    if TEST:
        #words.set_erps([['P100']])
        #words.set_exclusions([['protein']])
        words.set_erps([['P100'], ['P300'], ['N170'], ['P600'], ['N400'], ['MMN']])
        words.set_exclusions([['protein'], ['protein'], ['protein'], ['protein'], ['protein'], ['protein']])
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
