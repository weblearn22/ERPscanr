"""   """

import os

from erpsc.core.db import ERPDB
from erpsc.core.db import WebDB as WDB

def main():
    """   """

    db = ERPDB()

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

        # Wordcloud - copy to website directory

        # Publication graph - copy to wesbite directory

def make_post_md(label):
    """   """

    # Get website database object
    wdb = WDB()

    # Create the markdown file with yml header
    with open(os.path.join(wdb.post_path, label + '.md'), 'w') as post_file:
        post_file.write('---\n')
        post_file.write('title: \"' + label + '\"\n')
        post_file.write('date: 2017/03/15\n')
        post_file.write('layout: erp\n')
        post_file.write('---')

if __name__ == "__main__":
    main()