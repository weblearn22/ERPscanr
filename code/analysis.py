"""Analysis functions for the ERPscanr project."""

from copy import deepcopy

import numpy as np

###################################################################################################
###################################################################################################

def get_time_associations(counts, latencies, collect='highest'):
    """Get highest associations for each ERP component, based on co-occurence data."""

    time_associations = []
    latency_dict = {'name' : None, 'polarity' : None,
                    'latency' : None, 'association' : None}

    for erp_ind, erp in enumerate(counts.terms['A'].labels):

        # Initialize store & get latency information
        temp = deepcopy(latency_dict)
        latency = latencies[erp]

        # Parse information into latency dictionary
        temp['name'] = erp
        temp['polarity'] = latency[0]
        temp['latency'] = int(latency[1])

        # Get association
        if collect == 'highest':
            term_ind = np.argmax(counts.score[erp_ind, :])
            temp['association'] = counts.terms['B'].terms[term_ind][0]
        elif collect == 'all':
            temp['association'] = counts.score[erp_ind, :]

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
