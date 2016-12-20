"""Load & save functions for ERP-SCANR. p"""

import pickle

##########################################################################################
##########################################################################################
##########################################################################################

def load_pickle_counts(f_name):
    """Loads a pickle file of an ERPSCCount object.

    Parameters
    ----------
    f_name : str
        File name of the counts file to load.

    Returns
    -------
    ERPSCCount() object
        Count object loaded from file.
    """

    # Get ERPSC database object to set paths
    db = ERPDB()

    # Initialize full file name to load
    file_name = f_name + '_counts.p'

    # Load and return the data
    return pickle.load(open(os.path.join(db.counts_path, file_name), 'rb'))


def load_pickle_words(f_name):
    """Loads a pickle file of an ERPSC_Word object.

    Parameters
    ----------
    f_name : str
        File name of the words file to load.

    Returns
    -------
    ERPSC_Words() object
        Words object loaded from file.
    """

    # Get ERPSC database object to set paths
    db = ERPDB()

    # Initialize full file name to load
    file_name = f_name + '_words.p'

    # Load and return the data
    return pickle.load(open(os.path.join(db.words_path, file_name), 'rb'))
