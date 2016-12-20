"""URLs for the ERP-SCANR project.

EUtils Quick Start: http://www.ncbi.nlm.nih.gov/books/NBK25500/
EUtils in Depth: https://www.ncbi.nlm.nih.gov/books/NBK25499/

A list of all the valid databases is here:
    https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi

TODO:
  - Figure out 'HTTP POST' for large # of ID fetches
"""

##################################################################################
##########################################################################################
##########################################################################################

class URLS(object):
    """Class to hold URL information for ERP SCANR project.

    Attributes
    ----------
    lit_db : str
        The literature database to use.
    eutils : str
        Base URL for the e-utils tools.
    search : str
        URL for searching with e-utils.
    fetch  : str
        URL for fetching with e-utils.
    """

    def __init__(self, lit_db, auto_gen=True, retmax_val=500, field_val='', retmode_val='xml'):
        """Initialize the ncbi e-utils urls.

        Parameters
        ----------
        lit_db : {'pubmed', 'pmc'}
            Which literature database to use.
        retmax_val : int, optional (default: 500)
            xx
        field_val : str, optional (default: '')
            xx
        retmode_val : {'lxml', 'xml', ?}, optional
            xx
        """

        # Set up the base url for ncbi e-utils
        self.eutils = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

        # Initialize variables to store search and fetch URLs
        self.search = str()
        self.fetch = str()

        # Initialize dictionary to save settings, and add settings to it
        self.settings = dict()
        self.save_settings(lit_db, str(retmax_val), field_val, retmode_val)

        # Initialize dictionary to save url arguments, and populate it from settings
        self.args = dict()
        self.save_args()

        if auto_gen:
            self.build_search_url(['db', 'retmode'])
            self.build_fetch_url(['db', 'retmode'])

        # OLD:
        # Set the search url
        #self.search = self.base_url + 'esearch.fcgi?db=pmc&field=word&term='
        #self.fetch = self.base_url + ''
        #self.retmax = ''


    def save_settings(self, db=None, retmax=None, field=None, retmode=None):
        """

        Parameters
        ----------

        Notes
        -----
        - All possible settings are set as possible arguments to this function. For each of
            these possible settings, all of which are given a value are saved out into the dictionary.
        - The 'locals()' function returns a dictionary of variables in scope (in this function).
        - Using 'locals()' saves separately defining a list of possible variables, that
            would need to be maintained to make sure it matched the method arguments.

        Equivalent and more explicit:

        # Initialize list of possible settings, and remove the self argument
        possible_settings = locals().keys()
        possible_settings.remove('self')

        # Loop through all possible settings
        for ps in possible_settings:

            # If defined (not None) set the value of the setting
            #   into a dictionary, with key of the name of the setting
            if eval(ps):
                self.settings[ps] = eval(ps)
        """

        # Save all defined settings to a dictionary
        self.settings = {k: v for k, v in locals().items() if k is not 'self' and v is not None}


    def save_args(self):
        """   """

        # For each parameter in settings, create the url argument
        for param in self.settings.keys():
            self.args[param] = param + '=' + self.settings[param]


    def build_search_url(self, args_to_use):
        """

        Parameters
        ----------
        args_to_use : ?
            xx
        """

        # Set the search url
        search_base = self.eutils + 'esearch.fcgi?'
        #self.search = search_base + self.db_arg + '&' + self.field_arg + '&' + 'term='
        self.search = search_base + '&'.join([self.args[arg] for arg in args_to_use]) + '&term='


    def build_fetch_url(self, args_to_use):
        """

        Parameters
        ----------
        args_to_use : ?
            xx
        """

        # Set the fetch url
        fetch_base = self.eutils + 'efetch.fcgi?'
        #self.fetch = fetch_base + self.db_arg + '&' + self.retmode_arg + '&' + 'id='
        self.fetch = fetch_base + '&'.join([self.args[arg] for arg in args_to_use]) + '&id='
