"""Run analysis on collected words data."""

import os
import json

import numpy as np

from lisc.utils import SCDB, load_object

###################################################################################################
###################################################################################################

# Set data for counts objects to load
TERM_DIR = '../terms'
DB_NAME = '../data'
COG_F_NAME = 'counts_cognitive'
DIS_F_NAME = 'counts_disorders'

# Set the number of top terms to get
N_TERMS = 3

###################################################################################################
###################################################################################################

def main():

    print('\n\n ANALYZING COUNTS DATA \n\n')

    db = SCDB(DB_NAME)

    # Check for counts summary path, and create if it doesn't exist
    counts_summary_path = os.path.join(db.paths['counts'], 'summary')
    if not os.path.exists(counts_summary_path):
        os.mkdir(counts_summary_path)

    # Load the counts objects, used to grab co-occurence information
    cog_counts = load_object(COG_F_NAME, directory=db)
    dis_counts = load_object(DIS_F_NAME, directory=db)

    # Normalize data in counts objects
    cog_counts.compute_score('normalize', dim='A')
    dis_counts.compute_score('normalize', dim='A')

    # Collect the top associations from cognitive & disorder-related co-occurence analyses
    for l_ind, label in enumerate(cog_counts.terms['A'].labels):

        top_assocs = {'top_cog_assocs' : [], 'top_dis_assocs' : []}

        for t_ind, assoc in zip(range(N_TERMS), np.flip(np.argsort(cog_counts.score[l_ind, :]))):
            top_assocs['top_cog_assocs'].append(cog_counts.terms['B'][assoc].label)

        for t_ind, assoc in zip(range(N_TERMS), np.flip(np.argsort(dis_counts.score[l_ind, :]))):
            top_assocs['top_dis_assocs'].append(dis_counts.terms['B'][assoc].label)

        # Save out summary for each components highest associations
        with open(os.path.join(counts_summary_path, label + '.json'), 'w') as outfile:
            json.dump(top_assocs, outfile)

    print('\n\n FINISHED ANALYZING WORDS DATA \n\n')


if __name__ == "__main__":
    main()
