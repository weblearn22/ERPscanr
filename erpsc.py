from __future__ import print_function, division
import numpy as np
import datetime
import requests
#import pickle
from bs4 import BeautifulSoup


class ERPSC_Count:
    """This is a class for counting co-occurence of pre-specified ERP & Cognitive terms. """

    def __init__(self):

        # 
        self.url_front = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&field=word&term='

        # Initliaze list of erp & cog terms to use
        self.erps = list()
        self.cogs = list()

        # Initialize counters for numbers of terms
        self.nERPs = int()
        self.nCOGs = int()

        # Initialize vector of counts of number of papers for each term
        self.ERP_counts = np.zeros(0)
        self.COG_counts = np.zeros(0)

        # Initialize for 
        self.dat_numbers = np.zeros(0)
        self.dat_percent = np.zeros(0)

        # Initialize for date that data is collected
        self.date = ''


    def set_erps(self, erps):
        """Sets the given list of strings as erp terms to use. """

        self.erps = erps
        self.nERPs = len(erps)
        self.ERP_counts = np.zeros([self.nERPs])


    def set_cogs(self, cogs):
        """Sets the given list of strings as cog terms to use. """

        self.cogs = cogs
        self.nCOGs = len(cogs)
        self.COG_counts = np.zeros([self.nCOGs])


    def scrape_data(self):
        """Search through pubmed for all abstracts with co-occurence of ERP & COG terms. """

        # Set date of when data was collected
        self.date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        # Initialize right size matrices to store data
        self.dat_numbers = np.zeros([self.nERPs, self.nCOGs])
        self.dat_percent = np.zeros([self.nERPs, self.nCOGs])

        #
        for erp in self.erps:
            for cog in self.cogs:

                #
                erp_ind = self.erps.index(erp)
                cog_ind = self.cogs.index(cog)

                # Make URL - Exact Term Version
                url = self.url_front + '"' + erp + '"AND"' + cog + '"'

                # Make URL - Non-exact term version
                #url = self.url_front + erp + ' erp ' + cog

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

                # Add the total number of papers for erp & cog
                self.ERP_counts[erp_ind] = vec[1]
                self.COG_counts[cog_ind] = vec[2]

                # Add the number & percent of overlapping papers
                self.dat_numbers[erp_ind, cog_ind] = vec[0]
                self.dat_percent[erp_ind, cog_ind] = vec[0]/vec[1]


    def check_erps(self):
        """"Prints out the COG terms most associatied with each ERP. """

        for erp in self.erps:

            erp_ind = self.erps.index(erp)
            cog_ind = np.argmax(self.dat_percent[erp_ind, :])

            print('For the  {:5} the most common association is  {:10} with %{:05.2f}'.format(erp, self.cogs[cog_ind], self.dat_percent[erp_ind, cog_ind]*100))


    def check_cogs(self):
        """Prints out the ERP terms most associated with each COG. """
        
        for cog in self.cogs:

            cog_ind = self.cogs.index(cog)
            erp_ind = np.argmax(self.dat_percent[:, cog_ind])

            print('For  {:20} the strongest associated ERP is   {:5} with   %{:05.2f}'.format(cog, self.erps[erp_ind], self.dat_percent[erp_ind, cog_ind]*100))


    def check_top(self):
        """Check the terms with the most papers. """
        
        print('The most studied ERP is  {:6}  with  {:8.0f}  papers'.format(self.erps[np.argmax(self.ERP_counts)], \
                                                                    self.ERP_counts[np.argmax(self.ERP_counts)]))
        print('The most studied COG is  {:6}  with  {:8.0f}  papers'.format(self.cogs[np.argmax(self.COG_counts)], \
                                                                    self.COG_counts[np.argmax(self.COG_counts)]))

    def check_counts(self, dat):
        """Check how many papers found for each term. """

        if dat is 'erp':
            for erp in self.erps:
                erp_ind = self.erps.index(erp)
                print('{:5} - {:8.0f}'.format(erp, self.ERP_counts[erp_ind]))

        elif dat is 'cog':
            for cog in self.cogs:
                cog_ind = self.cogs.index(cog)
                print('{:18} - {:10.0f}'.format(cog, self.COG_counts[cog_ind]))


    def save_pickle():
        """NOTE: NOT YET IMPLEMETED"""
        pass

