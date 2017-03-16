from erpsc.words import Words

###############################################################################
###############################################################################

TEST = True

###############################################################################
###############################################################################

def main():
    """   """

    words = Words()

    if TEST:
        counts.set_erps([['P600'], ['N170']])
        counts.set_exclusions([['protein'], ['histone']])
    else:
        counts.set_erps_file()
        counts.set_exclusions_file()

    words.scrape_data(db='pmc')


if __name__ == "__main__":
    main()