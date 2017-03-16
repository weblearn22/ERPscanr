"""Classes and functions for Word analysis (text analysis of abstract texts)."""
from __future__ import print_function, division

import datetime
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

# Import custom code
from erpsc.base import Base
from erpsc.erp_data import ERPData
from erpsc.core.urls import URLS
from erpsc.core.utils import CatchNone, CatchNone2, comb_terms, extract

#################################################################################################
#################################### ERPSC - WORDS - Classes ####################################
#################################################################################################

class Words(Base):
    """Class for searching through words in the abstracts of specified papers.

    Attributes
    ----------
    results : list of ERPData() objects
        Results for each ERP, stored in custom Words object.
    """

    def __init__(self):
        """Initialize ERP-SCANR Words() object."""

        # Inherit from ERPSC Base Class
        Base.__init__(self)

        # Initialize a list to store results for all the erps
        self.results = list()


    def add_results(self, new_result):
        """Add a new Words() results object.

        Parameters
        ----------
        new_result : ERPData() object
            Object with information about current ERP term.
        """

        self.results.append(new_result)


    @staticmethod
    def extract_add_info(cur_erp, new_id, art):
        """Extract information from article web page and add to

        Parameters
        ----------
        cur_erp : ERPData() object
            Object to store information for the current ERP term.
        new_id : int
            Paper ID of the new paper.
        art : bs4.element.Tag() object
            Extracted pubmed article.

        NOTES
        -----
        - Data extraction is all in try/except statements in order to
        deal with missing data, since fields may be missing.

        TODO: Add DOI extraction
        """

        # Add ID of current article
        cur_erp.add_id(new_id)
        cur_erp.add_title(extract(art, 'ArticleTitle', 'str'))
        cur_erp.add_authors(_process_authors(extract(art, 'AuthorList', 'raw')))
        cur_erp.add_journal(extract(art, 'Title', 'str'), extract(art, 'ISOAbbreviation', 'str'))
        cur_erp.add_words(_process_words(extract(art, 'AbstractText', 'str')))
        cur_erp.add_kws(_process_kws(extract(art, 'Keyword', 'all')))
        cur_erp.add_pub_date(_process_pub_date(extract(art, 'PubDate', 'raw')))
        cur_erp.add_doi(_process_ids(extract(art, 'ArticleId', 'all')))

        # Old year extraction - was the wrong field
        #cur_erp.add_year(extract(extract(art, 'DateCreated', 'raw'), 'Year', 'str'))

        # Increment number of articles included in ERPData
        cur_erp.increment_n_articles()

        return cur_erp


    def scrape_data(self, db=None, retmax=None):
        """Search through pubmed for all abstracts referring to a given ERP.

        The scraping does an exact word search for the ERP term given.
        It then loops through all the artciles found about that data.
        For each article, pulls title, year and word data.

        Notes
        -----
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
        urls = URLS(db=db, retmax=retmax, retmode='xml', auto_gen=False)
        urls.build_info(['db'])
        urls.build_search(['db', 'retmax', 'retmode'])
        urls.build_fetch(['db', 'retmax', 'retmode'])

        # Get current information about database being used
        self.get_db_info(urls.info)

        # Loop through all the erps
        for ind, erp in enumerate(self.erps):

            # Initiliaze object to store data for current erp papers
            cur_erp = ERPData(erp)

            # Set up search terms - add exclusions, if there are any
            if self.exclusions[ind][0]:
                #term_arg = '"' + erp[0] + '"' + 'NOT' + '"' + self.exclusions[ind][0] + '"'
                term_arg = comb_terms(erp, 'or') + comb_terms(self.exclusions[ind], 'not')
            else:
                #term_arg = '"' + erp[0] + '"'
                term_arg = comb_terms(erp, 'or')

            # Create the url for the erp search term
            url = urls.search + term_arg

            # Get page and parse
            page = self.req.get_url(url)
            page_soup = BeautifulSoup(page.content, 'lxml')

            # Get all ids
            ids = page_soup.find_all('id')

            # Convert ids to string
            ids_str = _ids_to_str(ids)

            # Get article page
            art_url = urls.fetch + ids_str
            art_page = self.req.get_url(art_url)
            art_page_soup = BeautifulSoup(art_page.content, "xml")

            # Pull out articles
            articles = art_page_soup.findAll('PubmedArticle')

            # Loop through each article, extracting relevant information
            for ind, art in enumerate(articles):

                # Get ID of current article
                new_id = int(ids[ind].text)

                # Extract and add all relevant info from current articles to ERPData object
                cur_erp = self.extract_add_info(cur_erp, new_id, art)

            # Check consistency of extracted results
            cur_erp.check_results()

            # Add the object with current erp data to results list
            self.add_results(cur_erp)

        # Set Requester object as finished being used
        self.req.close()

    """
    def combine_words(self):
        ""Combine the words from each article together.""

        # Loop through each erp, and each article
        for erp in range(self.n_erps):
            for art in range(self.results[erp].n_articles):

                # Combine the words from each article into the 'all_words' collection
                if self.results[erp].words[art]:
                    self.results[erp].all_words.extend(self.results[erp].words[art])


    def freq_dists(self):
        ""Create a frequency distribution from all the extracted words.""

        # Loop through all ERPs
        for erp in range(self.n_erps):

            # Use nltk to create a frequency distribution from all words
            self.results[erp].freqs = nltk.FreqDist(self.results[erp].all_words)

            # Remove the ERPs name from list of words - so ERP isn't trivially most common
            try: self.results[erp].freqs.pop(self.erps[erp][0].lower())
            except KeyError: pass


    def check_words(self, n_check=20):
        ""Check the most common words for each ERP.

        Parameters
        ----------
        n_check : int, optional (default=20)
            Number of top words, for each ERP, to print out.
        ""

        # Loop through each ERP term
        for erp in range(self.n_erps):

            # Get the requested number of most common words for the ERP
            top_words = self.results[erp].freqs.most_common()[0:n_check]

            # Join together the top words into a string
            top_words_str = ''
            for i in range(n_check):
                top_words_str += top_words[i][0]
                top_words_str += ' , '

            # Print out the top words for the current ERP
            print(self.erps[erp][0], ': ', top_words_str)
    """

#######################################################################################################
################################# ERPSC - WORDS - FUNCTIONS (PRIVATE) #################################
#######################################################################################################

def _ids_to_str(ids):
    """Takes a list of pubmed ids, returns a str of the ids separated by commas.

    Parameters
    ----------
    ids : bs4.element.ResultSet
        List of pubmed ids.

    Returns
    -------
    ids_str : str
        A string of all concatenated ids.
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


@CatchNone
def _process_words(text):
    """Processes abstract text - sets to lower case, and removes stopwords and punctuation.

    Parameters
    ----------
    text : str
        Text as one long string.

    Returns
    -------
    words_cleaned : list of str
        List of words, after processing.
    """

    # Tokenize input text
    words = nltk.word_tokenize(text)

    # Remove stop words, and non-alphabetical tokens (punctuation). Return the result.
    return [word.lower() for word in words if ((not word.lower() in stopwords.words('english'))
                                               & word.isalnum())]


@CatchNone
def _process_kws(keywords):
    """Processes keywords - extract the keywords from tags and converts to strings.

    Parameters
    ----------
    kws : bs4.element.ResultSet
        List of all the keyword tags.

    Returns
    -------
    list of str
        List of all the keywords.
    """

    # NOTE: UPDATE WITH MOVE TO PY35
    return [kw.text for kw in keywords]
    #return [kw.text.encode('ascii', 'ignore') for kw in keywords]


@CatchNone
def _process_authors(author_list):
    """

    Parameters
    ----------
    author_list : bs4.element.Tag
        AuthorList tag, which contains tags related to author data.

    Returns
    -------
    out : list of tuple of (str, str, str, str)
        List of authors, each as (LastName, FirstName, Initials, Affiliation).
    """

    # Pull out all author tags from the input
    authors = extract(author_list, 'Author', 'all')

    # Initialize list to return
    out = []

    # Extract data for each author
    for author in authors:
        out.append((extract(author, 'LastName', 'str'), extract(author, 'ForeName', 'str'),
                    extract(author, 'Initials', 'str'), extract(author, 'Affiliation', 'str')))

    return out


@CatchNone2
def _process_pub_date(pub_date):
    """

    Parameters
    ----------
    pub_date : bs4.element.Tag
        PubDate tag, which contains tags with publication date information.

    Returns
    -------
    year : int
        xx
    month : str
        xx
    """

    # Extract year, convert to int if not None
    year = extract(pub_date, 'Year', 'str')
    if year: year = int(year)

    # Extract month
    month = extract(pub_date, 'Month', 'str')

    return year, month


@CatchNone
def _process_ids(ids):
    """

    Parameters
    ----------
    ids : bs4.element.ResultSet
        All the ArticleId tags, with all IDs for the article.

    Returns
    -------
    str or None
        The DOI if available, otherwise None.
    """

    lst = [str(i.contents[0]) for i in ids if i.attrs == {'IdType' : 'doi'}]

    if lst == []: return None
    else: return lst[0]
