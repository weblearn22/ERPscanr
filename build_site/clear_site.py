"""Clear out the website to prepare for a new scrape."""

import os
from shutil import copyfile

from erpsc.core.db import ERPDB
from erpsc.core.db import WebDB as WDB

###################################################################################################
###################################################################################################

def main():
    """Clear the website data for the ERP-SCANR site."""

    # Print out status
    print('\n\n CLEARING WEBSITE DATA \n\n')

    # Get database object for the site
    wdb = WDB()

    # Remove data files
    for file in os.listdir(wdb.post_path):
        os.remove(os.path.join(wdb.post_path, file))

    # Remove post pages
    for file in os.listdir(wdb.dat_path):
        os.remove(os.path.join(wdb.dat_path, file))

    # Remove image folders
    for folder in os.listdir(wdb.plt_path):
        shutil.rmdir(os.path.join(wdb.plt_path, folder))


if __name__ == "__main__":
    main()
