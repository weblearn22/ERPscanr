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
        self.all_words = _combine(erp_data.words)
        self.all_kws = _combine(erp_data.kws)

        #
        self.word_freqs = _freq_dist(self.all_words, self.erp)
        self.kw_freqs = _freq_dist(self.all_kws, self.erp)

        #
        self.author_counts = _proc_authors(erp_data.authors)
        self.f_author_counts, self.l_author_counts = \
            _proc_end_authors(erp_data.authors)
        self.journal_counts = _proc_journals(erp_data.journals)
        self.year_counts = _proc_years(erp_data.years)


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

def _combine(in_lst):
    """Combine list of lists into one large list.

    Parameters
    ----------
    in_lst : list of list of str
        Embedded lists to combine.

    Returns
    -------
    out : list of str
        Combined list.
    """

    out = []

    for ind in range(len(in_lst)):
        if in_lst[ind]:
            out.extend(in_lst[ind])

    return out

def _freq_dist(in_lst, exclude):
    """Create frequency distribution.

    Parameters
    ----------
    in_lst : list of str
        Word items to create frequecy distribution of.
    exclude : list of str
        Words to exclude from list.

    Returns
    -------
    freqs : nltk.FreqDist
        Frequency distribution of the input list.
    """

    freqs = nltk.FreqDist(in_lst)

    for it in exclude:
        try:
            freqs.pop(it.lower())
        except KeyError:
            pass

    return freqs

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

    Notes
    -----
    The non-obvious list comprehension is more obviously written as:
    names = []
    for authors in a_lst:
        for author in authors:
            all_authors.append(author)
    """

    # Drop author lists that are None
    a_lst = [a for a in a_lst if a is not None]

    # Reduce author fields to pair of tuples (L_name, Initials)
    names = [(author[0], author[2]) for authors in a_lst for author in authors]

    # Count how often each author published
    return _count(_fix_names(names))

def _proc_end_authors(a_lst):
    """Process first and last authors only.

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

    # Drop author lists that are None
    a_lst = [a for a in a_lst if a is not None]

    # Pull out the full name for the first & last author of each paper
    #  Last author is only considered if there is more than 1 author
    firsts = [authors[0] for authors in a_lst]
    f_names = [(author[0], author[2]) for author in firsts]
    lasts = [authors[-1] for authors in a_lst if len(authors) > 1]
    l_names = [(author[0], author[2]) for author in lasts]

    f_counts = _count(_fix_names(f_names))
    l_counts = _count(_fix_names(l_names))

    return f_counts, l_counts

def _fix_names(names):
    """Fix author names.

    Parameters
    ----------
    names : list of tuple of (L_Name, Initials)
        Author names.

    Returns
    -------
    names : list of tuple of (L_Name, Initials)
        Author names.

    Notes
    -----
    Sometimes full author name ends up in the last name field.
    If first name is None, assume this happened:
        Split up the text in first name, and grab the first name initial.
    """

    # Drop names whos data is all None
    names = [n for n in names if n != (None, None)]

    # Fix names if full name ended up in last name field
    names = [(name[0].split(' ')[1], name[0].split(' ')[0][0])
             if name[1] is None else name for name in names]

    return names

def _count(d_lst):
    """Count occurences of each item in a list.

    Parameters
    ----------
    d_lst : list of str
        List of items to count occurences of.

    Returns
    -------
    counts : list of tuple of (item_label, count)
        Counts for how often each item occurs in the input list.
    """

    counts = [(d_lst.count(i), i) for i in set(d_lst)]
    counts.sort(reverse=True)

    return counts
