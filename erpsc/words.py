"""MODULE DOCSTRING: TO FILL IN.

"""

from __future__ import print_function, division

import pickle
import datetime
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

# Import custom code
from erpsc.gen import *

#################################################################################
############################ ERPSC - WORDS - Classes ############################
#################################################################################

class Words(object):
    """An object to hold the word results for a given ERP or term.

    Attributes
    ----------
    erp : str
        Name of the ERP word data relates to.
    ids : list of int
        Pubmed article ids for all articles included in object.
    n_articles : int
        Number of articles included in object.
    years : list of int
        Publication year of each article included in object.
    titles : list of unicode
        Titles of all articles included in object.
    words : list of list of unicode
        Words extracted from each article.
    all_words : list of unicode
        All words from all articles.
    freqs : nltk FreqDist
        Frequency distribution of all words.
    """

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
        self.titles = list()
        self.words = list()
        self.years = list()

        # Initialize a list to store all words (across all papers)
        self.all_words = list()

        # Initialize to store FreqDists (across all words)
        self.freqs = list()

    def add_id(self, new_id):
        """Add a new id to Words object."""

        self.ids.append(new_id)

    def add_title(self, new_title):
        """Add a new title to Words object."""

        self.titles.append(new_title)

    def add_words(self, new_words):
        """Add new words to Words object."""

        self.words.append(new_words)

    def add_year(self, new_year):
        """Add a new year to Words object."""

        self.years.append(new_year)

    def check_results(self):
        """Check for consistencty in extracted results.

        If everything worked, each data field (ids, titles, words, years)
        should have the same length, equal to the number of articles.
        Some entries may be blank (missing data), but if the lengths are not
        the same then the data does not line up and cannot be trusted.
        """

        # Check that all data fields have length n_articles
        if not (self.n_articles == len(self.ids) == len(self.titles)
                == len(self.words) == len(self.years)):

            # If not, print out error
            print('DATA ERROR')


class ERPSCWords(ERPSCBase):
    """This is a class for searching through words in the abstracts of specified papers.

    XX...

    Attributes
    ----------
    results : list of Words() objects
        Results for each ERP, stored in custom Words object.
    """

    def __init__(self):

        # Inherit from ERPSC Base Class
        ERPSCBase.__init__(self)

        # Initialize a list to store results for all the erps
        self.results = list()

        # Set url and setting for e-search. Retmax is maximum number of ids to return
        #self.eutils_search = self.eutils_url + 'esearch.fcgi?db=pubmed&field=word&term='
        #self.search_retmax = '&retmax=500'

        # Set the url and settings for the e-fetch utility
        #self.eutils_fetch = self.eutils_url + 'efetch.fcgi?db=pubmed&retmode=xml&id='


    def add_results(self, new_result):
        """   """

        self.results.append(new_result)


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
        for ind, erp in enumerate(self.erps):

            # Initiliaze object to store data for current erp papers
            cur_erp = Words(erp)

            # Set up search terms - add exclusions, if there are any
            if self.exclusions[ind][0]:
                term_arg = '"' + erp[0] + '"' + 'NOT' + '"' + self.exclusions[ind][0] + '"'
            else:
                term_arg = '"' + erp[0] + '"'

            # Create the url for the erp search term
            url = urls.search + term_arg
            #url = urls.search + '"' + erp[0] + '"'
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
                new_id = int(ids[art].text)
                cur_erp.add_id(new_id)

                # Get Title of the paper, if available, and add to current results
                try:
                    cur_title = articles[art].find('ArticleTitle').text
                except AttributeError:
                    cur_title = []
                cur_erp.add_title(cur_title)

                # Get Words from the Abstract, if available, and add to current results
                try:
                    cur_words = articles[art].find('AbstractText').text.split()
                    cur_words = _process_words(cur_words)
                except AttributeError:
                    cur_words = []
                cur_erp.add_words(cur_words)

                # Get the Year of the paper, if available, and add to current results
                try:
                    cur_year = int(articles[art].find('DateCreated').find('Year').text)
                except AttributeError:
                    cur_year = []
                cur_erp.add_year(cur_year)

            # Check consistency of extracted results
            cur_erp.check_results()

            # Add the object with current erp data to results list
            self.add_results(cur_erp)


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

            # Remove the ERPs name from list of words
            #  Do this so that the erp itself isn't trivially the most common word
            try:
                self.results[erp].freqs.pop(self.erps[erp][0].lower())
            except KeyError:
                pass


    def check_words(self, n_check=20):
        """Check the most common words for each ERP.

        Parameters
        ----------
        n_check : int, optional (default=20)
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
            print(self.erps[erp][0], ': ', top_words_str)


    def save_pickle(self, f_name):
        """Saves out a pickle file of the ERPSC_Word object.

        Parameters
        ----------
        f_name : str
            String to append to beginning of file to save out.
        """

        # Get ERPSC database object to set paths
        db = ERPDB()

        # Initialize full file name
        save_name = f_name + '_words.p'

        # Save pickle file
        save_file = os.path.join(db.words_path, save_name)
        pickle.dump(self, open(save_file, 'wb'))


#################################################################################
####################### ERPSC - WORDS - FUNCTIONS (PUBLIC) ######################
#################################################################################

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


#######################################################################################
######################### ERPSC - WORDS - FUNCTIONS (PRIVATE) #########################
#######################################################################################

def _ids_to_str(ids):
    """Takes a list of pubmed ids, returns a str of the ids separated by commas.

    Parameters
    ----------
    ids : list of int
        List of pubmed ids.
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
    words : list of str
        List of words.
    """

    # Remove stop words, and anything that is only one character (punctuation). Return the result.
    return [word.lower() for word in words if ((not word.lower() in stopwords.words('english'))
                                               & (len(word) > 1))]
