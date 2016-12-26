"""

"""
from __future__ import division

import time
import requests

REST_TIME = 1/3

##################################################################################
##################################################################################
##################################################################################

class Requester(object):
    """Object to handle URL requests.

    Attributes
    ----------
    n_requests : int
        Number of requests that have been completed.
    st_time : str
        xx
    en_time : str
        xx
    time_last_req : float
        xx
    """

    def __init__():
        """   """

        self.n_requests = int()

        self.st_time = time.strftime('%H:%M %A %d %B')
        self.en_time = str()

        self.time_last_req = str()


    def get_url(self, url):
        """   """

        self.check_last_req_time()

        out = requests.get(url)

        self.time_last_req = time.time()
        self.n_requests += 1

        return out


    def check_last_req_time(self):
        """   """

        #
        time_since_req = time.time() - self.time_last_req

        #
        if time_since_req < REST_TIME:
            self.wait(time_since_req - REST_TIME)


    def wait(self, wait_time):
        """Wait for specified time.

        Parameters
        ----------
        wait_time : float
            Time, in seconds, to wait.
        """

        time.sleep(wait_time)


    def close(self):
        """   """
        pass
