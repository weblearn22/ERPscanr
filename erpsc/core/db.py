"""   """

import os

##
##
##

class ERPDB(object):
    """Class to hold database information ERP SCANR project.

    Attributes
    ----------
    project_path : str
        Base path to the ERPSC project.
    data_path : str
        Path to the data folder of the ERPSC project.
    counts_path : str
        Path to the data folder for counts data.
    words_path : str
        Path to the data folder for words data.
    """

    def __init__(self):

        # Set base path for the project
        self.project_path = ("/Users/thomasdonoghue/Documents/"
                             "Research/1-Projects/ERP-SCANR/")

        # Set the data path
        self.data_path = os.path.join(self.project_path, '2-Data')

        # Set paths to different data types
        self.counts_path = os.path.join(self.data_path, 'counts')
        self.words_path = os.path.join(self.data_path, 'words')