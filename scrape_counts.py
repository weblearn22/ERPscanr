from erpsc.count import Count
from erpsc.core.io import save_pickle_obj

###############################################################################
###############################################################################

TEST = False
TERMS_TYPE = 'cognitive'
S_NAME = 'CogScrape'

###############################################################################
###############################################################################

def main():
    """Run scrape of counts data."""

    counts = Count()

    if TEST:
        counts.set_erps([['P600'], ['N170']])
        counts.set_terms([['language'], ['visual']])
    else:
        counts.set_erps_file()
        counts.set_exclusions_file()
        counts.set_terms_file(TERMS_TYPE)

    counts.scrape_data(db='pubmed', verbose=True)

    save_pickle_obj(counts, S_NAME)

if __name__ == "__main__":
    main()