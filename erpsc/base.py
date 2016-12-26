"""Base object for ERP-SCANR."""

from __future__ import print_function

import pkg_resources as pkg

from erpsc.core.requester import Requester
from erpsc.core.errors import InconsistentDataError

######################################################################################
############################### ERPSC - GENERAL - BASE ###############################
######################################################################################

class Base(object):
    """Base class for ERPSC analyses.

    Attributes
    ----------
    terms_type : {'cognitive', 'disease'}
        Type of terms used.
    erps : list of str
        ERP words.
    exclusions : list of str
        Exclusion words, used to avoid unwanted articles.
    terms : list of str
        Terms words.
    n_erps : int
        Number of erps.
    n_terms : int
        Number of terms.
    req : Requester() object
        Object to handle URL requests.
    date : str
        Date data was collected.
    """

    def __init__(self):
        """Initialize ERP-SCANR Base() object."""

        # Initialize variable to keep track of term type used
        self.terms_type = str()

        # Initialize list of erps & term terms to use
        self.erps = list()
        self.exclusions = list()
        self.terms = list()

        # Initialize counters for numbers of terms
        self.n_erps = int()
        self.n_terms = int()

        # Requester object for handling URL calls
        self.req = Requester()

        # Initialize for date that data is collected
        self.date = ''

        # Initialize vector of counts of number of papers for each term
        #self.erp_counts = np.zeros(0)
        #self.term_counts = np.zeros(0)


    def set_erps(self, erps):
        """Sets the given list of strings as erp terms to use.

        Parameters
        ----------
        erps : list of str
            List of ERP terms to be used.
        """

        # Unload previous terms if some are already loaded
        self.unload_erps()

        # Set given list as the erps
        for erp in erps:
            self.erps.append([erp])

        # Set the number of erps
        self.n_erps = len(erps)


    def set_erps_file(self):
        """Load ERP terms from a txt file."""

        # Unload previous terms if some are already loaded
        self.unload_erps()

        # Get erps from module data file
        erps = _terms_load_file('erps')

        # Set the number of erps
        self.n_erps = len(erps)

        # Drop number indices for erps, and set as list
        for i in range(self.n_erps):
            self.erps.append(erps[i][3:].split(','))


    def check_erps(self):
        """Print out the current list of erps."""

        # Print out header and all current ERPs
        print('List of ERPs used: \n')
        for i in range(self.n_erps):
            print(", ".join(e for e in self.erps[i]))


    def unload_erps(self):
        """Unload the current set of ERP words."""

        # Check if exclusions are loaded, to empty them if so.
        if self.erps:

            # Print status that ERPs are being unloaded
            print('Unloading previous ERP words.')

            # Reset ERP variables to empty
            self.erps = list()
            self.n_erps = int()


    def set_exclusions(self, exclusions):
        """Sets the given list of strings as exclusion words.

        Parameters
        ----------
        exclusions : list of str
            List of exclusion words to be used.
        """

        # Unload previous terms if some are already loaded
        self.unload_exclusions()

        # Set given list as erp exclusion words
        for exclude in exclusions:
            self.exclusions.append([exclude])

        # Check that the number of exclusions matches n_erps
        if len(exclusions) != self.n_erps:
            raise InconsistentDataError('Mismatch in number of exclusions and erps!')


    def set_exclusions_file(self):
        """Load exclusion words from a txt file."""

        # Unload previous terms if some are already loaded
        self.unload_exclusions()

        # Get exclusion words from module data file
        exclusions = _terms_load_file('erps_exclude')

        # Check that the number of exclusions matches n_erps
        if len(exclusions) != self.n_erps:
            raise InconsistentDataError('Mismatch in number of exclusions and erps!')

        # Drop number indices for exclusions, and set as list
        for i in range(self.n_erps):
            self.exclusions.append(exclusions[i][3:].split(','))


    def check_exclusions(self):
        """Print out the current list of exclusion words."""

        # Print out header and all exclusion words
        print('List of exclusion words used: \n')
        for i in range(self.n_erps):
            print(self.erps[i][0] + "\t : " +
                  ", ".join(e for e in self.exclusions[i]))


    def unload_exclusions(self):
        """Unload the current set of exclusion words."""

        # Check if exclusions are loaded. If so, print status and empty.
        if self.exclusions:

            # Print status that exclusion words are being unloaded
            print('Unloading previous exclusion words.')

            # Reset exclusions variables to empty
            self.exclusions = list()


    def set_terms(self, terms):
        """Sets the given list of strings as term terms to use.

        Parameters
        ----------
        terms : list of str
            List of terms to be used.
        """

        # Unload previous terms if some are already loaded
        self.unload_terms()

        # Set given list as the terms
        for term in terms:
            self.terms.append([term])

        # Set the number of terms
        self.n_terms = len(terms)


    def set_terms_file(self, terms_type):
        """Load terms from a txt file."""

        # Unload previous terms if some are already loaded
        self.unload_terms()

        # Set the type of terms
        self.terms_type = terms_type

        # Get erps from module data file
        self.terms = _terms_load_file(terms_type)

        # Set the number of terms
        self.n_terms = len(self.terms)


    def check_terms(self):
        """Print out the current list of terms."""

        # Print out header and all term words
        print('List of terms used: \n')
        print("\n".join(self.terms))


    def unload_terms(self):
        """Unload the current set of terms."""

        # Check if exclusions are loaded, to empty them if so.
        if self.terms:

            # Print status that term words are being unloaded
            print('Unloading previous terms words.')

            # Reset term variables to empty
            self.terms_type = str()
            self.terms = list()
            self.n_terms = int()

##########################################################################################
##########################################################################################
##########################################################################################

def _terms_load_file(dat_name):
    """Loads a terms data file from within the module

    Parameters
    ----------
    dat_name : str
        Name of the terms data file to load.
    """

    # Open file
    f_name = 'terms/' + dat_name + '.txt'
    f_path = pkg.resource_filename(__name__, f_name)
    terms_file = open(f_path, 'r')

    # Pull out data from file
    dat = terms_file.read().splitlines()

    return dat
