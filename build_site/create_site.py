"""Prepare and move the data and figures for the website."""

import os
import json
from pathlib import Path
from shutil import copyfile
from datetime import datetime

from lisc.utils import SCDB, load_object
from lisc.utils.io import parse_json_data

# Import local utility code
from code.db import WebDB
from code.settings import WEBSITE_LOC

###################################################################################################
###################################################################################################

# Set names for database and data objects
DB_NAME = '../data'
F_NAME = 'words_erps'

# Set the file format for plots to use for website
PLT_EXT = '.svg'

COPY_FIGS = ['cognitive_time',
             'cognitive_clustermap',
             'disorders_clustermap',
             'erp_network']

###################################################################################################
###################################################################################################

# Get the current date for creating the posts
DATE = datetime.today().strftime('%Y-%m-%d')

def main():
    """Build the website page from ERPscanr results."""

    # Print out status
    print('\n\n GENERATING WEBSITE DATA \n\n')

    # Get database object for the data, and paths of interest
    db = SCDB(DB_NAME)
    w_sum_path = Path(db.paths['summary'])
    c_sum_path = Path(db.paths['counts']) / 'summary'

    # Get the database object for the website
    wdb = WebDB(WEBSITE_LOC)

    # Load word object, used to get the index of all collect ERPs
    words = load_object(F_NAME, directory=db)

    # Loop through each erp and copy words data
    for label in words.labels:

        # Create website template file
        make_post_md(label, wdb)

        # Load and copy combined summary data
        words_summary = next(parse_json_data(w_sum_path / (label + '.json')))
        counts_summary = next(parse_json_data(c_sum_path / (label + '.json')))
        comb_summary = {**words_summary, **counts_summary}

        # Website data json - save out to website directory
        with open(wdb.data_path / (label + '.json'), 'w') as outfile:
            json.dump(comb_summary, outfile)

        # Check website plots folder
        w_plts_path = wdb.erp_plot_path / label
        if not os.path.exists(w_plts_path):
            os.mkdir(w_plts_path)

        # Wordcloud - copy to website directory
        copyfile(db.get_file_path('figures', 'wc/' + label + PLT_EXT),
                 w_plts_path / ('wc' + PLT_EXT))

        # Publication graph - copy to wesbite directory
        copyfile(db.get_file_path('figures', 'years/' + label + PLT_EXT),
                 w_plts_path / ('hist' + PLT_EXT))

    # Copy over 'group' figures
    for fig in COPY_FIGS:

        # Check for figure file in possible folders, and copy if present
        for folder in ['counts', 'network']:

            fig_path = db.get_file_path('figures', folder + '/' + fig + PLT_EXT)
            if os.path.exists(fig_path):
                copyfile(fig_path, wdb.group_plot_path / (fig + PLT_EXT))
                break

        # Print status if figure not found to copy
        else:
            print('Could not copy {:s} - file not found'.format(fig))

    # Copy over co-occurence summary data for association terms
    for assoc in ['cognitive', 'disorders']:
        copyfile(db.get_folder_path('counts') + '/assocs/' + assoc + '.json',
                 wdb.data_path / (assoc + '.json'))

    # Print out status
    print('\n\n WEBSITE DATA GENERATED \n\n')


def make_post_md(label, wdb):
    """Create the markdown post page for ERP-SCANR website."""

    # Get website database object, if not provided
    if not wdb:
        wdb = WebDB()

    # Create the markdown file with yml front matter
    with open(os.path.join(wdb.post_path, DATE + '-' + label + '.md'), 'w') as post_file:
        post_file.write('---\n')
        post_file.write('title: \"' + label + '\"\n')
        post_file.write('date: ' + DATE.replace('-', '/') + '\n')
        post_file.write('layout: erp\n')
        post_file.write('---')

if __name__ == "__main__":
    main()
