"""Analysis functions for the ERPscanr project."""

import numpy as np

###################################################################################################
###################################################################################################

def get_time_associations(counts):
    """Get time associations from canonically named ERP components."""

    time_associations = []

    for erp_ind, erp in enumerate(counts.terms['A'].labels):

        # List is: [word, P or N, latency]
        temp  = [None, None, None]

        # Get P/N & latency for ERPs with naming convention
        if erp[1:].isdigit():

            # Get P or N
            if erp[0] == 'P':
                temp[1] = 'P'
            elif erp[0] == 'N':
                temp[1] = 'N'

            # Get latency
            temp[2] = int(erp[1:])

            # Get association
            term_ind = np.argmax(counts.score[erp_ind, :])
            temp[0] = counts.terms['B'].terms[term_ind][0]

            # Collect ERP data
            time_associations.append(temp)

    return time_associations


def scale_number(unscaled, to_min, to_max, from_min, from_max):
    """Scale a number to be within a given range.
    From here: http://stackoverflow.com/questions/929103
    """

    return (to_max - to_min) * (unscaled - from_min) / (from_max - from_min) + to_min


def scale_list(lst, to_min, to_max):
    """Scale a list of number to a given range."""

    return [scale_number(ind, to_min, to_max, min(lst), max(lst)) for ind in lst]
