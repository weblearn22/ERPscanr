"""Script to run counts collection for the ERP-SCANR project."""

from lisc import Counts
from lisc.utils import SCDB, save_object, load_api_key

###################################################################################################
###################################################################################################

# Set whether to run a test run
TEST = False

# Set locations / names for loading files
DB_NAME = '../data'
TERMS_DIR = '../terms/'
API_FILE = 'api_key.txt'

# Set label for secondary terms to run
#   Options: 'cognitive', 'disorders', 'erp'
LABEL = 'cognitive'

# Set collection settings
LOGGING = None
VERBOSE = True

# Update settings for test run
if TEST:
    LABEL = 'test'

###################################################################################################
###################################################################################################

def main():

    db = SCDB(DB_NAME)
    api_key = load_api_key(API_FILE)

    counts = Counts()

    if TEST:

        counts.add_terms([['P600'], ['N170'], ['N400']], dim='A')
        counts.add_terms([['language'], ['visual']], dim='B')

    else:

        counts.add_terms('erps.txt', dim='A', directory=TERMS_DIR)
        counts.add_terms('erps_exclude.txt', term_type='exclusions',
                         dim='A', directory=TERMS_DIR)
        counts.add_labels('erp_labels.txt', dim='A', directory=TERMS_DIR)

        if LABEL != 'erp':
            counts.add_terms(LABEL + '.txt', dim='B', directory=TERMS_DIR)

    print('\n\nRUNNING COUNTS COLLECTION')
    print('RUNNING COLLECTION: ', LABEL, '\n\n')

    counts.run_collection(db='pubmed', api_key=api_key, logging=LOGGING, verbose=VERBOSE)

    save_object(counts, 'counts_' + LABEL, db)

    print('\n\nCOUNTS COLLECTION FINISHED\n\n')


if __name__ == "__main__":
    main()
