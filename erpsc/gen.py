"""MODULE DOCSTRING: TO FINISH
This ....

EUtils Quick Start: http://www.ncbi.nlm.nih.gov/books/NBK25500/
EUtils in Depth: https://www.ncbi.nlm.nih.gov/books/NBK25499/

A list of all the valid databases is here:
    https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi

TODO:
  - Figure out 'HTTP POST' for large # of ID fetches
"""

from __future__ import print_function, division
import os
import numpy as np

#######################################################################################
############################## ERPSC - GENERAL - CLASSES ##############################
#######################################################################################

class ERPDB(object):
    """Class to hold database information ERP SCANR project."""

    def __init__(self):

        # Set base path for the project
        self.project_path = ("/Users/thomasdonoghue/Documents/"
                             "Research/1-Projects/ERP-SCANR/")

        # Set the data path
        self.data_path = os.path.join(self.project_path, '2-Data')

        # Set paths to different data types
        self.dict_path = os.path.join(self.data_path, 'dicts')
        self.counts_path = os.path.join(self.data_path, 'counts')
        self.words_path = os.path.join(self.data_path, 'words')


class URLS(object):
    """Class to hold URL information for ERP SCANR project."""

    def __init__(self, db_in):
        """Initialize the ncbi e-utils urls.

        Parameters
        ----------
        db : {'pubmed', 'pmc'}
            Which database to use.
        """

        # Parameters
        db = db_in
        retmax_val = 500
        field_val = ''
        retmode_val = 'xml'

        # Parameter
        db_arg = 'db=' + db
        retmax_arg = 'retmax=' + str(retmax_val)
        field_arg = 'field=' + field_val
        retmode_arg = 'retmode=' + retmode_val

        # Set up the base url for ncbi e-utils
        self.eutils = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

        # Set the search url
        search_base = self.eutils + 'esearch.fcgi?'
        self.search = search_base + db_arg + '&' + field_arg + '&' + 'term='

        # Set the fetch url
        fetch_base = self.eutils + 'efetch.fcgi?'
        self.fetch = fetch_base + db_arg + '&' + retmode_arg + '&' + 'id='

        # OLD:
        # Set the search url
        #self.search = self.base_url + 'esearch.fcgi?db=pmc&field=word&term='
        #self.fetch = self.base_url + ''
        #self.retmax = ''

######################################################################################
############################### ERPSC - GENERAL - BASE ###############################
######################################################################################

class ERPSCBase(object):
    """Base class for ERPSC analyses."""

    def __init__(self):

        # Initialize variable to keep track of term type used
        self.terms_type = str()

        # Initialize list of erps & term terms to use
        self.erps = list()
        self.exclusions = list()
        self.terms = list()

        # Initialize counters for numbers of terms
        self.n_erps = int()
        self.n_terms = int()

        # Initialize vector of counts of number of papers for each term
        self.erp_counts = np.zeros(0)
        self.term_counts = np.zeros(0)

        # Initialize for date that data is collected
        self.date = ''


    def set_erps(self, erps):
        """Sets the given list of strings as erp terms to use.

        Parameters
        ----------
        erps : list of str
            List of ERP terms to be used.
        """

        # Set given list as the erps
        for erp in erps:
            self.erps.append(erp)

        # Set the number of erps
        self.n_erps = len(erps)

        # Initialize count variable to the correct length
        self.erp_counts = np.zeros([self.n_erps])


    def set_erps_file(self, f_name=None):
        """Load ERP terms from a txt file.

        Parameters
        ----------
        f_name : str, optional (default = None)
            Name of the file to be loaded as ERP terms.
                Default None, loads standard terms from module.
        """

        # Open file to read from - either input file or default from module
        if f_name:
            terms_file = open(f_name, 'r')
        else:
            terms_file = open('erpsc/terms/erps.txt', 'r')

        # Read file and input ERP terms
        erps = terms_file.read().splitlines()

        # Set the number of erps
        self.n_erps = len(erps)

        # Drop number indices for erps, and set as list
        for i in range(self.n_erps):
            self.erps.append(erps[i][3:].split(','))

        # Initialize count variable to the correct length
        self.erp_counts = np.zeros([self.n_erps])


    def check_erps(self):
        """Print out the current list of erps."""

        print('List of ERPs used: \n')
        for i in range(self.n_erps):
            print(", ".join(e for e in self.erps[i]))


    def set_exclusions(self, exclusions):
        """Sets the given list of strings as exclusion words.

        Parameters
        ----------
        exclusions : list of str
            List of exclusion words to be used.
        """

        # Set given list as erp exclusion words
        for exclude in exclusions:
            self.exclusions.append(exclude)

        # Check that the number of exclusions matches n_erps
        if len(exclusions) != self.n_erps:
            print('Mismatch in number of exclusions and erps!')


    def set_exclusions_file(self, f_name=None):
        """Load exclusion words from a txt file.

        Parameters
        ----------
        f_name : str, optional (default = None)
            Name of the file to be loaded as exclusion words.
                Default None, loads standard exclusion words from module.
        """

        # Open file to read from - either input file or default from module
        if f_name:
            terms_file = open(f_name, 'r')
        else:
            terms_file = open('erpsc/terms/erps_exclude.txt', 'r')

        # Read file and input exclusion terms
        exclusions = terms_file.read().splitlines()

        # Check that the number of exclusions matches n_erps
        if len(exclusions) != self.n_erps:
            print('Mismatch in number of exclusions and erps!')

        # Drop number indices for exclusions, and set as list
        for i in range(self.n_erps):
            self.exclusions.append(exclusions[i][3:].split(','))


    def check_exclusions(self):
        """Print out the current list of exclusion words."""

        print('List of exclusion words used: \n')
        for i in range(self.n_erps):
            print(self.erps[i][0] + "\t : " +
                  ", ".join(e for e in self.exclusions[i]))


    def set_terms(self, terms):
        """Sets the given list of strings as term terms to use.

        Parameters
        ----------
        terms : list of str
            List of terms to be used.
        """

        # Set given list as the terms
        self.terms = terms

        # Set the number of terms
        self.n_terms = len(terms)

        # Initialize count variable to the correct length
        self.term_counts = np.zeros([self.n_terms])


    def set_terms_file(self, terms_type, f_name=None):
        """Load terms from a txt file.

        Parameters
        ----------
        terms_type : {'cognitive', 'disease'}
            Type of the terms to be loaded.
        f_name : str, optional (default = None)
            Name of the file to be loaded as terms.
        """

        # Set the type of terms
        self.terms_type = terms_type

        # Open file to read from - either input file or default from module
        if f_name:
            terms_file = open(f_name, 'r')
        else:
            terms_file = open('erpsc/terms/' + terms_type + '.txt', 'r')

        # Read file and input ERP terms
        self.terms = terms_file.read().splitlines()

        # Set the number of terms
        self.n_terms = len(self.terms)

        # Initialize count variable to the correct length
        self.term_counts = np.zeros([self.n_terms])


    def check_terms(self):
        """Print out the current list of terms."""

        print('List of terms used: \n')
        print("\n".join(self.terms))
