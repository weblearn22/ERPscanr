"""URLs for the ERP-SCANR project.

EUtils Quick Start: http://www.ncbi.nlm.nih.gov/books/NBK25500/
EUtils in Depth: https://www.ncbi.nlm.nih.gov/books/NBK25499/

A list of all the valid databases is here:
    https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi

Most relevant database are: 'pubmed' & 'pmc'
- pubmed: is a database of over 25 million references
- pmc: an archive of freely available full text papers, of around 3 million papers
More info here: https://www.nlm.nih.gov/pubs/factsheets/dif_med_pub.html
FAQ on PMC: https://www.ncbi.nlm.nih.gov/pmc/about/faq/#q1

TODO:
  - Figure out 'HTTP POST' for large # of ID fetches
"""

from erpsc.core.errors import InconsistentDataError

##################################################################################
##########################################################################################
##########################################################################################

class URLS(object):
    """Class to hold URL information for ERP SCANR project.

    Attributes
    ----------
    eutils : str
        Base URL for the e-utils tools.
    query : str
        URL for querying with e-utils.
    search : str
        URL for searching with e-utils.
    fetch  : str
        URL for fetching with e-utils.
    settings : dict()
        Dictionary of all defined settings and their values.
    args : dict()
        Dictionary of all arguments (settings & values) that can be used in e-utirls URL.
    """

    def __init__(self, db=None, retmax=None, field=None, retmode=None, auto_gen=False):
        """Initialize the ncbi e-utils urls.

        NOTE:
        defaults: retmax: 500, field: '', retmode:'xml'

        Parameters
        ----------
        db : {'pubmed', 'pmc'}, optional
            Which literature database to use.
        retmax : str, optional
            The maximum number of papers to return.
        field : str, optional
            ?
        retmode : {'lxml', 'xml', ?}, optional
            The return format for the results.
        auto_gen : boolean, optional
            xx
        """

        # Set up the base url for ncbi e-utils
        self.eutils = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

        # Initialize variables to store search and fetch URLs
        self.search = str()
        self.fetch = str()

        # Initialize dictionary to save settings, and add settings to it
        self.settings = dict()
        self.save_settings(db=db, retmax=retmax, field=field, retmode=retmode)

        # Initialize dictionary to save url arguments, and populate it from settings
        self.args = dict()
        self.save_args()

        if auto_gen:
            self.build_search([])
            self.build_fetch([])

        # OLD:
        # Set the search url
        #self.search = self.base_url + 'esearch.fcgi?db=pmc&field=word&term='
        #self.fetch = self.base_url + ''
        #self.retmax = ''


    def save_settings(self, db=None, retmax=None, field=None, retmode=None):
        """Save provided setting values into a dictionary object.

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
        """Create the arguments that can be added to the e-utils urls."""

        # For each parameter in settings, create the url argument
        for param in self.settings.keys():
            self.args[param] = param + '=' + self.settings[param]


    def check_args(self, args_to_use):
        """Checks whether the requested arguments are defined, so that they can be used.

        Parameters
        ----------
        args_to_use : list of str
            Requested arguments to check that they are defined.
        """

        # Check that all requested arguments are available. Catch and raise custom error if not
        try:
            [self.args[arg] for arg in args_to_use]
        except KeyError:
            raise InconsistentDataError('Not all requested settings provided - can not proceed.')


    def build_query(self, args_to_use):
        """Create the e-utils EGQuery URL, with specified arguments.

        Parameters
        ----------
        args_to_use : list of str
            Arguments to use to build the search URL.
        """

        # Check requested args are defined in settings
        self.check_args(args_to_use)

        # Set the eg query search url
        query_base = self.eutils + 'egquery.fcgi?'
        self.query = query_base + '&'.join([self.args[arg] for arg in args_to_use]) + '&term='


    def build_search(self, args_to_use):
        """Create the e-utils search URL, with specified arguments.

        Parameters
        ----------
        args_to_use : list of str
            Arguments to use to build the search URL.

        Notes
        old: self.search = search_base + self.db_arg + '&' + self.field_arg + '&' + 'term='
        """

        # Check requested args are defined in settings
        self.check_args(args_to_use)

        # Set the search url
        search_base = self.eutils + 'esearch.fcgi?'
        self.search = search_base + '&'.join([self.args[arg] for arg in args_to_use]) + '&term='


    def build_fetch(self, args_to_use):
        """Create the e-utils fetch URL, with specified arguments.

        Parameters
        ----------
        args_to_use : list of str
            Arguments to use to build the fetch URL.

        Notes
        old: self.fetch = fetch_base + self.db_arg + '&' + self.retmode_arg + '&' + 'id='
        """

        # Check requested args are defined in settings
        self.check_args(args_to_use)

        # Set the fetch url
        fetch_base = self.eutils + 'efetch.fcgi?'
        self.fetch = fetch_base + '&'.join([self.args[arg] for arg in args_to_use]) + '&id='
