from __future__ import print_function, division

import pickle
import datetime
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

# Import custom code
from erpsc.gen import *

"""

This ...

"""

###############################################################
#################### ERPSC_Words - Classes ####################
###############################################################

class Words(object):
    """An object to hold the word results for a given term."""

    def __init__(self, erp):

        """Initialize

        Parameters
        ----------
        erp  : str
            Name of the ERP.
        """

        # Set the given string as the erp label
        self.erp = erp

        # Initialize list to store pubmed article ids
        self.ids = list()

        # Initialize to store article count
        self.n_articles = int()

        # Initiliaze to store data pulled from articles
        self.years = list()
        self.titles = list()
        self.words = list()

        # Initialize a list to store all words (across all papers)
        self.all_words = list()

        # Initialize to store FreqDists (across all words)
        self.freqs = list()


class ERPSCWords(ERPSCBase):
    """This is a class for searching through words in the abstracts of specified papers."""

    def __init__(self):

        # Inherit from ERPSC Base Class
        ERPSCBase.__init__(self)

        # Set url and setting for e-search. Retmax is maximum number of ids to return
        #self.eutils_search = self.eutils_url + 'esearch.fcgi?db=pubmed&field=word&term='
        #self.search_retmax = '&retmax=500'

        # Set the url and settings for the e-fetch utility
        #self.eutils_fetch = self.eutils_url + 'efetch.fcgi?db=pubmed&retmode=xml&id='

        # Initialize a list to store results for all the erps
        self.results = list()


    def scrape_data(self):
        """Search through pubmed for all abstracts referring to a given ERP.

        The scraping does an exact word search for the ERP term given.
        It then loops through all the artciles found about that data.
        For each article, pulls title, year and word data.

        Notes:
        - Pulls data using the hierarchical tag structure that organize the articles.
        - Initially, the procedure was to pull all tags of a certain type.
            For example: extract all 'DateCreated' tags.
            This procedure fails (or badly organizes data) when an articles is
                missing a particular tag.
            Now: take advantage of the hierarchy, loop through each article tag.
                From here, pull out the data, if available.
                This way, can deal with cases of missing data.
        """

        # Set date of when data was collected
        self.date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        # Get e-utils URLS object
        urls = URLS('pubmed')

        # Loop through all the erps
        for erp in self.erps:

            # Initiliaze object to store data for current erp papers
            cur_erp = Words(erp)

            # Create the url for the erp search term
            url = urls.search + '"' + erp[0] + '"'
            #url = urls.search + '"' + erp + '"' + self.search_retmax
            #url = self.eutils_search + '"' + erp + '"NOT"' + '"cell"' + self.search_retmax

            # Get page and parse
            page = requests.get(url)
            page_soup = BeautifulSoup(page.content)

            # Get all ids
            ids = page_soup.find_all('id')

            # Convert ids to string
            ids_str = _ids_to_str(ids)

            # Get article page
            #art_url = self.eutils_fetch + ids_str
            art_url = urls.fetch + ids_str
            art_page = requests.get(art_url)
            art_page_soup = BeautifulSoup(art_page.content, "xml")

            # Pull out articles
            articles = art_page_soup.findAll('PubmedArticle')

            # Check how many articles there are
            cur_erp.n_articles = len(articles)

            # Loop through each article, pulling out desired info
            for art in range(0, cur_erp.n_articles):

                # NOTE: Pubmed article pages could be missing info.
                # For example, can have an id that's missing abstract text
                # This is why data collections are all in try statements.

                # Add id of current article to object data
                cur_erp.ids.append(int(ids[art].text))

                # Get Title, if there is one
                try:
                    cur_erp.titles.append(articles[art].find('ArticleTitle').text)
                except AttributeError:
                    cur_erp.titles.append([])

                # Get Words from the Abstract, if available
                try:
                    cur_erp.words.append(_process_words(
                        articles[art].find('AbstractText').text.split()))
                except AttributeError:
                    cur_erp.words.append([])

                # Get the Year of the paper, if available
                try:
                    cur_erp.years.append(int(articles[art].find('DateCreated').find('Year').text))
                except AttributeError:
                    cur_erp.years.append([])

            # Add the object with current erp data to results list
            self.results.append(cur_erp)


    def combine_words(self):
        """Combine the words from each article together."""

        # Loop through each erp, and each article
        for erp in range(0, self.n_erps):
            for art in range(0, self.results[erp].n_articles):

                # Combine the words from each article into the 'all_words' collection
                self.results[erp].all_words.extend(self.results[erp].words[art])


    def freq_dists(self):
        """FILL IN DOCSTRING."""

        # Loop through all ERPs
        for erp in range(0, self.n_erps):

            #
            self.results[erp].freqs = nltk.FreqDist(self.results[erp].all_words)

            # Remove ... ?
            #try:
            #    self.results[erp].freqs.pop(self.erps[erp].lower())
            #except KeyError:
            #    pass


    def check_words(self, n_check):
        """Check the most common words for each ERP.

        Parameters
        ----------
        n_check : int
            Number of top words, for each ERP, to print out.
        """

        # Loop through each ERP term
        for erp in range(0, self.n_erps):

            # Get the requested number of most common words for the ERP
            top_words = self.results[erp].freqs.most_common()[0:n_check]

            # Join together the top words into a string
            top_words_str = ''
            for i in range(0, n_check):
                top_words_str += top_words[i][0]
                top_words_str += ' , '

            # Print out the top words for the current ERP
            print(self.erps[erp], ': ', top_words_str)


    def save_pickle(self, f_name):
        """Saves out a pickle file of the ERPSC_Word object.

        Parameters
        ----------
        f_name : ?
            xx
        """

        # Get ERPSC database object to set paths
        db = ERPDB()

        # Initialize full file name
        save_name = f_name + '_words.p'

        # Save pickle file
        save_file = os.path.join(db.words_path, save_name)
        pickle.dump(self, open(save_file, 'wb'))


#########################################################################
##################### ERPSC_Words - Public Functions ####################
#########################################################################

def load_pickle_words(f_name):
    """Loads a pickle file of an ERPSC_Word object.

    Parameters
    ----------
    f_name : str
        File name of the words file to load.

    Returns
    -------
    results : ?
        xx
    """

    # Get ERPSC database object to set paths
    db = ERPDB()

    # Initialize full file name to load
    file_name = f_name + '_words.p'

    # Load and return the data
    return pickle.load(open(os.path.join(db.words_path, file_name), 'rb'))


###################################################################################
######################### ERPSC_Words - Private Functions #########################
###################################################################################

def _ids_to_str(ids):
    """Takes a list of pubmed ids, returns a str of the ids separated by commas.

    Parameters
    ----------
    ids : list(ints)
        List of pubmed ids
    """

    # Check how many ids in list
    n_ids = len(ids)

    # Initialize string with first id
    ids_str = str(ids[0].text)

    # Loop through rest of the id's, appending to end of id_str
    for i in range(1, n_ids):
        ids_str = ids_str + ',' + str(ids[i].text)

    # Return string of ids
    return ids_str


def _process_words(words):
    """Takes a list of words, sets to lower case, and removes all stopwords.

    Parameters
    ----------
    words : list(str)
        List of words
    """

    # Remove stop words, and anything that is only one character (punctuation). Return the result.
    return [word.lower() for word in words if ((not word.lower() in stopwords.words('english'))
                                               & (len(word) > 1))]
