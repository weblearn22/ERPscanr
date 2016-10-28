from __future__ import print_function, division

import datetime
import pickle
import numpy as np
import requests
from bs4 import BeautifulSoup

# Import custom code
from gen import *

"""

"""

#######################################################################
######################## ERPSC_Count - Classes ########################
#######################################################################


class ERPSCCount(ERPSCBase):
    """This is a class for counting co-occurence of pre-specified ERPs & terms."""

    def __init__(self):

        # Inherit from the ERPSC base class
        ERPSCBase.__init__(self)

        # Set the esearch url for pubmed
        #self.eutils_search = self.eutils_url + 'esearch.fcgi?db=pubmed&field=word&term='
        #self.eutils_search = self.eutils_url + 'esearch.fcgi?db=pmc&field=word&term='

        # Initialize data output variables
        self.dat_numbers = np.zeros(0)
        self.dat_percent = np.zeros(0)


    def scrape_data(self):
        """Search through pubmed for all abstracts with co-occurence of ERP & terms.

        The scraping does an exact word search for two terms (one ERP and one term)
        The HTML page returned by the pubmed search includes a 'count' field.
        This field contains the number of papers with both terms. This is extracted.
        """

        # Set date of when data was scraped
        self.date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        # Get e-utils URLS object
        urls = URLS('pubmed')

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
                url = urls.search + '"' + erp[0] + '"AND"' + term + '"'

                # Make URL - Non-exact term version
                #url = self.eutils_search + erp + ' erp ' + term

                # Pull the page, and parse with Beatiful Soup
                page = requests.get(url)
                page_soup = BeautifulSoup(page.content)

                # Get all 'count' tags
                counts = page_soup.find_all('count')

                # Initialize empty temp vector to hold counts
                vec = []

                # Loop through counts, extracting into vec
                for i in range(0, len(counts)):
                    count = counts[i]
                    ext = count.text
                    vec.append(int(ext))

                # Add the total number of papers for erp & term
                self.erp_counts[erp_ind] = vec[1]
                self.term_counts[term_ind] = vec[2]

                # Add the number & percent of overlapping papers
                self.dat_numbers[erp_ind, term_ind] = vec[0]
                self.dat_percent[erp_ind, term_ind] = vec[0]/vec[1]


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
        dat : str
            Which data type to print out.
                Options: {'erp', 'term'}
        """

        # Check counts for all ERP terms
        if dat is 'erp':
            for erp in self.erps:
                erp_ind = self.erps.index(erp)
                print('{:5} - {:8.0f}'.format(erp, self.erp_counts[erp_ind]))

        # Check counts for all term terms
        elif dat is 'term':
            for term in self.terms:
                term_ind = self.terms.index(term)
                print('{:18} - {:10.0f}'.format(term, self.term_counts[term_ind]))


    def save_pickle(self, f_name):
        """Saves out a pickle file of the ERPSCCount object.

        Parameters
        ----------
        f_name : str
            String to add to the beginning of the saved out file.
        """

        # Get ERPSC database object to set paths
        db = ERPDB()

        # Initialize full file name
        save_name = f_name + '_counts.p'

        # Save pickle file
        save_file = os.path.join(db.counts_path, save_name)
        pickle.dump(self, open(save_file, 'wb'))


############################################################################
###################### ERPSC_Words - Public Functions ######################
############################################################################

def load_pickle_counts(f_name):
    """Loads a pickle file of an ERPSCCount object.

    Parameters
    ----------
    f_name : str
        File name of the counts file to load.

    Returns
    -------
    results : ?
        xx
    """

    # Get ERPSC database object to set paths
    db = ERPDB()

    # Initialize full file name to load
    file_name = f_name + '_counts.p'

    # Load and return the data
    return pickle.load(open(os.path.join(db.counts_path, file_name), 'rb'))

