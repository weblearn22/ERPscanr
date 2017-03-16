from erpsc.words import Words

###############################################################################
###############################################################################

TEST = True
S_NAME = 'BaseScrape'

###############################################################################
###############################################################################

def main():
    """Run scrape of words data."""

    words = Words()

    if TEST:
        words.set_erps([['P100'], ['P300'], ['N170'], ['P600'], ['N400']])
        words.set_exclusions([['protein'], ['protein'], ['protein'], ['protein'], ['protein']])
    else:
        words.set_erps_file()
        words.set_exclusions_file()

    words.scrape_data(db='pmc', retmax=500)

    save_pickle_obj(words, S_NAME)

if __name__ == "__main__":
    main()