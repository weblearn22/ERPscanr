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
N_DROP = 100

###################################################################################################
###################################################################################################

def main():

    print('\n\n ANALYZING COUNTS DATA \n\n')

    db = SCDB(DB_NAME)

    # Check for counts paths, and create then if they don't exist
    counts_summary_path = os.path.join(db.paths['counts'], 'summary')
    counts_assocs_path = os.path.join(db.paths['counts'], 'assocs')
    for path in [counts_summary_path, counts_assocs_path]:
        if not os.path.exists(path):
            os.mkdir(path)

    # Load the counts objects, used to grab co-occurence information
    cog_counts = load_object(COG_F_NAME, directory=db)
    dis_counts = load_object(DIS_F_NAME, directory=db)

    # Drop rate components and normalize data in counts objects
    cog_counts.drop_data(N_DROP)
    cog_counts.compute_score('normalize', dim='A')
    dis_counts.drop_data(N_DROP)
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

    # Collect & save top components associatied with cognition-related terms
    cog_assocs = {}
    for l_ind, label in enumerate(cog_counts.terms['B'].labels):
        cog_assocs[label] = []
        for t_ind, assoc in zip(range(N_TERMS), np.flip(np.argsort(cog_counts.score[:, l_ind]))):
            cog_assocs[label].append(cog_counts.terms['A'][assoc].label)

    with open(os.path.join(counts_assocs_path, 'cognitive.json'), 'w') as outfile:
        json.dump(cog_assocs, outfile)

    # Collect & save top components associatied with disorder-related terms
    dis_assocs = {}
    for l_ind, label in enumerate(dis_counts.terms['B'].labels):
        dis_assocs[label] = []
        for t_ind, assoc in zip(range(N_TERMS), np.flip(np.argsort(dis_counts.score[:, l_ind]))):
            dis_assocs[label].append(dis_counts.terms['A'][assoc].label)

    with open(os.path.join(counts_assocs_path, 'disorders.json'), 'w') as outfile:
        json.dump(dis_assocs, outfile)


    print('\n\n FINISHED ANALYZING WORDS DATA \n\n')


if __name__ == "__main__":
    main()
