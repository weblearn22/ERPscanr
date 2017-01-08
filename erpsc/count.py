"""Classes and functions for Count analysis (key word co-occurences in papers)."""
from __future__ import print_function, division

import datetime
import numpy as np
from bs4 import BeautifulSoup

# Import custom code
from erpsc.base import Base
from erpsc.core.utils import comb_terms
from erpsc.core.urls import URLS

#########################################################################################
################################ ERPSC - COUNT - CLASSES ################################
#########################################################################################

class Count(Base):
    """This is a class for counting co-occurence of pre-specified ERPs & terms.

    Attributes
    ----------
    erp_counts : 1d array
        Counts of how many articles found for each ERP word.
    term_counts : 1d array
        Counts of how many articles found for each term word.
    dat_numbers : 2d array
        How many papers found for each ERP / term combination.
    dat_percent : 2d array
        Percent of papers that with co-occuring ERP and term words.
    """

    def __init__(self):
        """Initialize ERP-SCANR Count() object."""

        # Inherit from the ERPSC base class
        Base.__init__(self)

        # Initialize vector of counts of number of papers for each term
        self.erp_counts = np.zeros(0)
        self.term_counts = np.zeros(0)

        # Initialize data output variables
        self.dat_numbers = np.zeros(0)
        self.dat_percent = np.zeros(0)

        # Set the esearch url for pubmed
        #self.eutils_search = self.eutils_url + 'esearch.fcgi?db=pubmed&field=word&term='
        #self.eutils_search = self.eutils_url + 'esearch.fcgi?db=pmc&field=word&term='


    def scrape_data(self, db=None):
        """Search through pubmed for all abstracts with co-occurence of ERP & terms.

        The scraping does an exact word search for two terms (one ERP and one term)
        The HTML page returned by the pubmed search includes a 'count' field.
        This field contains the number of papers with both terms. This is extracted.
        """

        # Set date of when data was scraped
        self.date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        # Get e-utils URLS object
        urls = URLS(db=db, retmode='xml')
        urls.build_search(['db', 'retmode'])
        urls.build_fetch(['db', 'retmode'])

        # Initialize count variables to the correct length
        self.term_counts = np.zeros([self.n_terms])
        self.erp_counts = np.zeros([self.n_erps])

        # Initialize right size matrices to store data
        self.dat_numbers = np.zeros([self.n_erps, self.n_terms])
        self.dat_percent = np.zeros([self.n_erps, self.n_terms])

        # Loop through each ERP term
        for erp in self.erps:

            # For each ERP, loop through each term term
            for term in self.terms:

                # Get the indices of the current erp & term terms
                erp_ind = self.erps.index(erp)
                term_ind = self.terms.index(term)

                # Make URL - Exact Term Version
                #url = urls.search + '"' + erp[0] + '"AND"' + term[0] + '"'
                url = urls.search + comb_terms(erp, 'or') + 'AND' + comb_terms(term, 'or')

                # Make URL - Non-exact term version
                #url = self.eutils_search + erp + ' erp ' + term

                # Pull the page, and parse with Beautiful Soup
                page = self.req.get_url(url)
                page_soup = BeautifulSoup(page.content, 'lxml')

                # Get all 'count' tags
                counts = page_soup.find_all('count')

                # Initialize empty temp vector to hold counts
                vec = []

                # Loop through counts, extracting into vec
                for i in range(len(counts)):
                    count = counts[i]
                    ext = count.text
                    vec.append(int(ext))

                # Add the total number of papers for erp & term
                self.erp_counts[erp_ind] = vec[1]
                self.term_counts[term_ind] = vec[2]

                # Add the number & percent of overlapping papers
                self.dat_numbers[erp_ind, term_ind] = vec[0]
                self.dat_percent[erp_ind, term_ind] = vec[0]/vec[1]

        # Set Requester object as finished being used
        self.req.close()


    def check_cooc_erps(self):
        """"Prints out the terms most associatied with each ERP."""

        # Loop through each erp term, find maximally associated term term and print out
        for erp in self.erps:

            # Find the index of the most common term for current erp
            erp_ind = self.erps.index(erp)
            term_ind = np.argmax(self.dat_percent[erp_ind, :])

            # Print out the results
            print("For the  {:5} the most common association is \t {:10} with \t %{:05.2f}"
                  .format(erp[0], self.terms[term_ind], \
                  self.dat_percent[erp_ind, term_ind]*100))


    def check_cooc_terms(self):
        """Prints out the ERP terms most associated with each term."""

        # Loop through each cig term, find maximally associated erp term and print out
        for term in self.terms:

            # Find the index of the most common erp for current term
            term_ind = self.terms.index(term)
            erp_ind = np.argmax(self.dat_percent[:, term_ind])

            # Print out the results
            print("For  {:20} the strongest associated ERP is \t {:5} with \t %{:05.2f}"
                  .format(term, self.erps[erp_ind][0], \
                  self.dat_percent[erp_ind, term_ind]*100))


    def check_top(self):
        """Check the terms with the most papers."""

        # Find and print the erp term for which the most papers were found
        print("The most studied ERP is  {:6}  with {:8.0f} papers"
              .format(self.erps[np.argmax(self.erp_counts)], \
              self.erp_counts[np.argmax(self.erp_counts)]))

        # Find and print the term term for which the most papers were found
        print("The most studied term is  {:6}  with {:8.0f}  papers"
              .format(self.terms[np.argmax(self.term_counts)], \
              self.term_counts[np.argmax(self.term_counts)]))


    def check_counts(self, dat):
        """Check how many papers found for each term.

        Parameters
        ----------
        dat : {'erp', 'term'}
            Which data type to print out.
        """

        # Check counts for all ERP terms
        if dat is 'erp':
            for erp in self.erps:
                erp_ind = self.erps.index(erp)
                print('{:5} - {:8.0f}'.format(erp[0], self.erp_counts[erp_ind]))

        # Check counts for all term terms
        elif dat is 'term':
            for term in self.terms:
                term_ind = self.terms.index(term)
                print('{:18} - {:10.0f}'.format(term, self.term_counts[term_ind]))
