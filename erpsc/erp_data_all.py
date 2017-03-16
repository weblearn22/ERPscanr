"""Classes and functions to store aggregated ERP paper data."""
#from __future__ import print_function

import nltk

##########################################################################################
##########################################################################################
##########################################################################################

class ERPDataAll(object):
    """Object to hold ERP data, aggregated across papers.

    Attributes
    ----------
    erp : list of str
        Name(s) of the ERP word data relates to.
    n_articles : int
        Number of articles whos data is included in object.
    all_words : list of str
        All abstract words collected across all articles.
    all_kws : list of str
        All keywords collected across all articles.
    word_freqs : nltk.probability.FreqDist
        Frequency distribution of all words.
    kw_freqs : nltk.probability.FreqDist
        Frequency distribution of all keywords.
    author_counts : list of tuple of (int, (str, str))
        Counter across all authors.
    f_author_counts : list of tuple of (int, (str, str))
        Counter across all first authors.
    journal_counts : list of tuple of (int, str)
        Counter across all journals.
    year_counts : list of tuple of (int, int)
        Counter across all years of publication.
    """

    def __init__(self, erp_data):
        """   """

        self.erp = erp_data.erp
        self.n_articles = erp_data.n_articles

        #
        self.all_words = list()
        self.all_kws = list()

        self.combine_words(erp_data)
        self.combine_kws(erp_data)

        #
        self.word_freqs = None
        self.create_word_freq_dist()
        self.kw_freqs = None
        self.create_kw_freq_dist()

        #
        self.author_counts = _proc_authors(erp_data.authors)
        self.f_author_counts = _proc_fst_authors(erp_data.authors)
        self.journal_counts = _proc_journals(erp_data.journals)
        self.year_counts = _proc_years(erp_data.years)


    def combine_words(self, erp_data):
        """Combine the words from all articles together."""

        #
        for ind in range(erp_data.n_articles):
            if erp_data.words[ind]:
                self.all_words.extend(erp_data.words[ind])


    def combine_kws(self, erp_data):
        """Combine the keywords from all articles together."""

        #
        for ind in range(erp_data.n_articles):
            if erp_data.kws[ind]:
                self.all_kws.extend(erp_data.kws[ind])

    def create_word_freq_dist(self):
        """Create frequency distribution of all abstract words."""

        self.word_freqs = nltk.FreqDist(self.all_words)

        # Remove ERP name(s) - so they aren't trivially most common
        for erp in self.erp:
            try:
                self.word_freqs.pop(erp.lower())
            except KeyError:
                pass


    def create_kw_freq_dist(self):
        """Create frequency distribution of all keywords."""

        self.kw_freqs = nltk.FreqDist(self.all_kws)


    def check_words(self, n_check):
        """Check the most common words for the ERP.

        Parameters
        ----------
        n_check : int, optional (default=20)
            Number of top words to print out.
        """

        # Get the requested number of most common words for the ERP
        top_words = self.word_freqs.most_common()[0:n_check]

        # Join together the top words into a string
        top_words_str = ''
        for i in range(n_check):
            top_words_str += top_words[i][0]
            top_words_str += ' , '

        # Print out the top words for the current ERP
        print(self.erp[0], ': ', top_words_str)


    def check_kws(self, n_check):
        """Check the most common kws for the ERP.

        Parameters
        ----------
        n_check : int, optional (default=20)
            Number of top words to print out.
        """

        # Get the requested number of most common kws for the ERP
        top_words = self.kw_freqs.most_common()[0:n_check]

        # Join together the top words into a string
        top_words_str = ''
        for i in range(n_check):
            top_words_str += top_words[i][0]
            top_words_str += ' , '

        # Print out the top words for the current ERP
        print(self.erp[0], ': ', top_words_str)


    def print_summary(self):
        """Print out a summary of the scraped ERP paper data."""

        print('The number of articles is', str(self.n_articles))
        print('The most common author is', self.author_counts[0][1][1],
              self.author_counts[0][1][0], 'with', self.author_counts[0][0],
              'articles.')
        print('The most common journal is', self.journal_counts[0][1],
              'with', self.journal_counts[0][0], 'articles.')

##########################################################################################
##########################################################################################
##########################################################################################

def _proc_years(year_lst):
    """Process years.

    Parameters
    ----------
    year_lst : list of int
        Year of publication of all papers.

    Returns
    -------
    counts : list of tuple of (int, int)
        Number of publications per year - (year, n).
    """

    counts = [(year, year_lst.count(year)) for year in set(year_lst) - set([None])]
    counts.sort()

    return counts

def _proc_journals(j_lst):
    """Process journals.

    Parameters
    ----------
    j_lst : list of tuple of (str, str)
        List of journals articles come from.
            (Journal Name, ISO abbreviation)

    Returns
    -------
    counts : list of tuple of (int, str)
        Number of publications per journal - (n, Journal Name).
    """

    names = [j[1] for j in j_lst]
    counts = [(names.count(i), i) for i in set(names)]

    counts.sort(reverse=True)

    return counts

def _proc_fst_authors(a_lst):
    """Process first authors only.

    Parameters
    ----------
    a_lst : list of list of tuple of (str, str, str, str)
        Authors of all articles included in object.
            (Last Name, First Name, Initials, Affiliation)

    Returns
    -------
    counts : list of tuple of (int, (str, str))
        Number of publications per author - (n, (Last Name, Initials)).
    """

    names = [(author[0], author[2]) for author in [authors[0] for authors in a_lst]]

    # Sometimes full author name ends up in the last name field
    #  If first name is None, assume this happened
    #   Split up the text in first name, and grab the first name initial
    names = [(name[0].split(' ')[1], name[0].split(' ')[0][0])
             if name[1] is None else name for name in names]

    counts = [(names.count(i), i) for i in set(names)]

    counts.sort(reverse=True)

    return counts

def _proc_authors(a_lst):
    """Process all authors.

    Parameters
    ----------
    a_lst : list of list of tuple of (str, str, str, str)
        Authors of all articles included in object.
            (Last Name, First Name, Initials, Affiliation)

    Returns
    -------
    counts : list of tuple of (int, (str, str))
        Number of publications per author - (n, (Last Name, Initials)).
    """

    names = [(author[0], author[2]) for authors in a_lst for author in authors]

    # Sometimes full author name ends up in the last name field
    #  If first name is None, assume this happened
    #   Split up the text in first name, and grab the first name initial
    names = [(name[0].split(' ')[1], name[0].split(' ')[0][0])
             if name[1] is None else name for name in names]

    counts = [(names.count(i), i) for i in set(names)]

    counts.sort(reverse=True)

    return counts
