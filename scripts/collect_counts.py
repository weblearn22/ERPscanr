"""Script to run counts collection for the ERP-SCANR project."""

from lisc import Counts
from lisc.utils import SCDB, save_object, load_api_key

###################################################################################################
###################################################################################################

# Set whether to run a test run
TEST = True

# Set locations / names for loading files
TERMS_DIR = '../terms/'
API_FILE = 'api_key.txt'

# Set label for secondary terms to run
#   Options: 'cognitive', 'disease', 'erp' (run ERPs against each other)
LABEL = 'disease'

# Set collection settings
LOGGING = None

###################################################################################################
###################################################################################################

def main():

    db = SCDB('../data')
    api_key = load_api_key(API_FILE)

    counts = Counts()

    if TEST:

        counts.add_terms([['P600'], ['N170'], ['N400']], dim='A')
        counts.add_terms([['language'], ['visual']], dim='B')

        LABEL = 'test'

    else:

        counts.set_terms_file('erps.txt', dim='A', directory=TERMS_DIR)
        counts.set_terms_file('erps_exclude.txt', term_type='exclusions',
                              dim='A', directory=TERMS_DIR)

        if LABEL != 'erp':
            counts.set_terms_files(LABEL + '.txt', dim='B', directory=TERMS_DIR)

    print('\n\nRUNNING COUNTS COLLECTION')
    print('RUNNING COLLECTION: ', LABEL, '\n\n')

    counts.run_collection(db='pubmed', api_key=api_key, logging=LOGGING, verbose=True)

    save_object(counts, 'counts_' + LABEL, db)

    print('\n\nCOUNTS COLLECTION FINISHED\n\n')


if __name__ == "__main__":
    main()
