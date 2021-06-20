"""Clear out the website to prepare for a new scrape."""

import os
import shutil

# Import local utility code
from code.db import WebDB
from code.settings import WEBSITE_LOC

###################################################################################################
###################################################################################################

def main():
    """Clear the website data for the ERP-SCANR site."""

    # Print out status
    print('\n\n CLEARING WEBSITE DATA \n')

    # Get database object for the site
    wdb = WebDB(WEBSITE_LOC)

    # Remove data files
    for file in os.listdir(wdb.post_path):
        os.remove(wdb.post_path / file)

    # Remove post pages
    for file in os.listdir(wdb.data_path):
        os.remove(wdb.data_path / file)

    # Remove image folders
    for folder in os.listdir(wdb.erp_plot_path):
        if folder[0] == '.':
            continue
        shutil.rmtree(wdb.erp_plot_path / folder)

    # Remove group plots
    for file in os.listdir(wdb.group_plot_path):

        # Ignore png files (like the overview figure)
        if file.split('.')[-1] == 'png': continue

        # Remove other figure files
        os.remove(wdb.group_plot_path / file)

    # Print out status
    print('\n WEBSITE DATA CLEARED \n\n')


if __name__ == "__main__":
    main()
