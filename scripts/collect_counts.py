"""Script to run counts collection for the ERP-SCANR project."""

from lisc import Counts
from lisc.utils import save_object

###################################################################################################
###################################################################################################

TEST = True
TERMS_TYPE = 'disease'
SAVE_NAME = 'DisScrape'

###################################################################################################
###################################################################################################

def main():

    counts = Counts()

    if TEST:
        counts.add_terms([['P600'], ['N170']], dim='A')
        counts.add_terms([['language'], ['visual']], dim='B')

    else:
        # ToDo: coordinate where to load terms from
        counts.set_terms_file('erps.txt', dim='A')
        counts.set_terms_file('erps_exclude.txt', term_type='exclusions', dim='A')
        counts.set_terms_files('disease.txt', dim='B')

    print('\n\nRUNNING COUNTS COLLECTION')
    print('RUNNING TERMS TYPE: ', TERMS_TYPE, '\n\n')
    counts.run_collection(db='pubmed', verbose=True)
    print('\n\nCOUNTS COLLECTION FINISHED')

    save_object(counts, SAVE_NAME)
    print('COUNTS COLLECTION SAVED\n\n')


if __name__ == "__main__":
    main()
