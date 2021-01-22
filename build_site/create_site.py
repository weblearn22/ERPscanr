"""Prepare and move the data and figures for the website."""

import os
from shutil import copyfile
from datetime import datetime

# TODO:
#from erpsc.core.db import ERPDB

# Import local utility code
from code.db import WebDB
from code.settings import WEBSITE_LOC

###################################################################################################
###################################################################################################

# Get the current date for creating the posts
DATE = datetime.today().strftime('%Y-%m-%d')

def main():
    """Build the website page from ERP-SCANR results."""

    # Print out status
    print('\n\n GENERATING WEBSITE DATA \n\n')

    # Get database object for the data
    db = ERPDB()

    # Get the database object for the website
    wdb = WebDB(WEBSITE_LOC)

    # Load list of labels
    with open(os.path.join(db.words_path, 'labels.txt')) as infile:
        labels = infile.read().split('\n')
    # Remove trailing empty line
    _ = labels.pop()

    # Loop through each erp
    for label in labels:

        # Create website template file
        make_post_md(label)

        # Website data json - copy to website directory
        copyfile(os.path.join(db.words_path, 'summary', label + '.json'),
                 os.path.join(wdb.data_path, label + '.json'))

        # Check website plots folder
        w_plts_path = os.path.join(wdb.plot_path, label)
        if not os.path.exists(w_plts_path):
            os.mkdir(w_plts_path)

        # Wordcloud - copy to website directory
        copyfile(os.path.join(db.figs_path, 'wc', label + '.svg'),
                 os.path.join(w_plts_path, 'wc.svg'))

        # Publication graph - copy to wesbite directory
        copyfile(os.path.join(db.figs_path, 'year', label + '.svg'),
                 os.path.join(w_plts_path, 'hist.svg'))

    # Print out status
    print('\n\n WEBSITE DATA GENERATED \n\n')


def make_post_md(label):
    """Create the markdown post page for ERP-SCANR website."""

    # Get website database object
    wdb = WDB()

    # Create the markdown file with yml front matter
    with open(os.path.join(wdb.post_path, DATE + '-' + label + '.md'), 'w') as post_file:
        post_file.write('---\n')
        post_file.write('title: \"' + label + '\"\n')
        post_file.write('date: ' + DATE.replace('-', '/') + '\n')
        post_file.write('layout: erp\n')
        post_file.write('---')

if __name__ == "__main__":
    main()
