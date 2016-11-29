"""DOCSTRING

EUtils Quick Start: http://www.ncbi.nlm.nih.gov/books/NBK25500/
EUtils in Depth: https://www.ncbi.nlm.nih.gov/books/NBK25499/

A list of all the valid databases is here:
    https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi

TODO:
  - Figure out 'HTTP POST' for large # of ID fetches
"""

##
##
##

class URLS(object):
    """Class to hold URL information for ERP SCANR project.

    Attributes
    ----------
    db : ERPDB() object
        Object that stores all paths for the ERPSC project.
    eutils : str
        Base URL for the e-utils tools.
    search : str
        URL for searching with e-utils.
    fetch  : str
        URL for fetching with e-utils.
    """

    def __init__(self, db_in):
        """Initialize the ncbi e-utils urls.

        Parameters
        ----------
        db_in : {'pubmed', 'pmc'}
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
