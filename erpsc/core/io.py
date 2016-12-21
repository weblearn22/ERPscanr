"""Load & save functions for ERP-SCANR. p"""

import os
import pickle

from erpsc.words import Words
from erpsc.count import Count
from erpsc.core.db import check_db

##########################################################################################
##########################################################################################
##########################################################################################

"""
def load_pickle_counts(f_name, db=None):
    "Loads a pickle file of an ERPSCCount object.

    Parameters
    ----------
    f_name : str
        File name of the counts file to load.

    Returns
    -------
    ERPSCCount() object
        Count object loaded from file.
    "

    #
    db = check_db(db)

    # Initialize full file name to load
    file_name = f_name + '_counts.p'

    # Load and return the data
    return pickle.load(open(os.path.join(db.counts_path, file_name), 'rb'))


def load_pickle_words(f_name):
    "Loads a pickle file of an ERPSC_Word object.

    Parameters
    ----------
    f_name : str
        File name of the words file to load.

    Returns
    -------
    ERPSC_Words() object
        Words object loaded from file.
    "

    # Get ERPSC database object to set paths
    db = ERPDB()

    # Initialize full file name to load
    file_name = f_name + '_words.p'

    # Load and return the data
    return pickle.load(open(os.path.join(db.words_path, file_name), 'rb'))
"""

def save_pickle_obj(obj, f_name, db=None):
    """   """

    # Check for database object, initialize if not provided
    db = check_db(db)

    #
    if isinstance(obj, Count):
        save_name = f_name + '_counts.p'
        save_path = db.counts_path

    #
    elif isinstance(obj, Words):
        save_name = f_name + '_words.p'
        save_path = db.words_path

    else:
        print('HUH? WHAT IS IT??')

    # Save pickle file
    save_file = os.path.join(save_path, save_name)
    pickle.dump(obj, open(save_file, 'wb'))


def load_pickle_obj(f_name, db=None):
    """   """

    # Check for database object, initialize if not provided
    db = check_db(db)

    #
    counts_objs = os.listdir(db.counts_path)
    words_objs = os.listdir(db.words_path)

    #
    if f_name + '.p' in counts_objs:
        load_path = os.path.join(db.counts_path, f_name + '.p')
    elif f_name + '.p' in words_objs:
        load_path = os.path.join(db.words_path, f_name + '.p')
    else:
        print('AHHH. FILE NOT FOUND')

    # Load and return the data
    return pickle.load(open(load_path, 'rb'))
