"""Basic utility functions for ERP-SCANR."""

##################################################################################
##################################################################################
##################################################################################

def comb_terms(lst, jt):
    """Combine a list of terms to use as search arguments.

    Parameters
    ----------
    lst : list of str
        List of terms to combine together.
    jt : {'or', 'not'}
        Term to use to join together terms.

    Returns
    -------
    out : str
        String
    """

    # Add quotes to list items for exact search
    lst = ['"'+ item + '"' for item in lst]

    # Join together using requested join term
    if jt == 'or':
        out = '(' + 'OR'.join(lst) + ')'
    elif jt == 'not':
        out = 'NOT' + 'NOT'.join(lst)

    return out