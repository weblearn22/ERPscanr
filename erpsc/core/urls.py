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
    lit_db : ?
        xx
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

        # TODO: Save settings in a dictionary?
        self.settings = dict()

        # Save settings to object
        self.lit_db = lit_db
        self.retmax_val = retmax_val
        self.field_val = field_val
        self.retmode_val = retmode_val

        if auto_gen:
            self.build_param_settings
            self.build_search_url
            self.build_fetch_url

        # OLD:
        # Set the search url
        #self.search = self.base_url + 'esearch.fcgi?db=pmc&field=word&term='
        #self.fetch = self.base_url + ''
        #self.retmax = ''

    def build_param_settings(self):
        """   """

        # Parameter
        self.db_arg = 'db=' + self.lit_db
        self.retmax_arg = 'retmax=' + str(self.retmax_val)
        self.field_arg = 'field=' + self.field_val
        self.retmode_arg = 'retmode=' + self.retmode_val

    def build_search_url(self):
        """   """

        # Set the search url
        search_base = self.eutils + 'esearch.fcgi?'
        self.search = search_base + db_arg + '&' + field_arg + '&' + 'term='

    def build_fetch_url(self):
        """   """

        # Set the fetch url
        fetch_base = self.eutils + 'efetch.fcgi?'
        self.fetch = fetch_base + db_arg + '&' + retmode_arg + '&' + 'id='
