"""Script to run words collection for the ERP-SCANR project."""

from lisc import Words
from lisc.utils import SCDB, save_object

###################################################################################################
###################################################################################################

# Set whether to run a test run
TEST = True

# Set label for collection
LABEL = 'erps'

# Set directory to load terms from
TERMS_DIR = '../terms/'

# Set e-utils settings
FIELD = 'TIAB'
RETMAX = 5000

# Set collection settings
SAVE_N_CLEAR = True

###################################################################################################
###################################################################################################

def main():

    db = SCDB('../data')

    words = Words()

    if TEST:

        words.add_terms([['P100'], ['N100']])
        words.add_terms([['protein'], ['protein']], term_type='exclusions')

        RETMAX = 5
        SAVE_N_CLEAR = False
        LABEL = 'test'

    else:

        words.set_terms_file('erps.txt', dim='A', directory=TERMS_DIR)
        words.set_terms_file('erps_exclude.txt', term_type='exclusions',
                             dim='A', directory=TERMS_DIR)

    print('\n\nRUNNING WORDS COLLECTION')

    words.run_collection(db='pubmed', retmax=RETMAX, field=FIELD, usehistory=True,
                         save_and_clear=SAVE_N_CLEAR, directory=db, verbose=True)

    save_object(words, 'words_' + LABEL, db)

    print('\n\nWORDS COLLECTION FINISHED\n\n')


if __name__ == "__main__":
    main()
