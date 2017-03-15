"""Tests for the ERPDataAll() class and related functions from erpsc."""

from erpsc.erp_data_all import *
from erpsc.tests.utils import load_erp_data

##
##
##

def test_erp_data_all():
    """   """

    erp_dat = load_erp_data(add_dat=True, n=2)

    erp_dat_all = ERPDataAll(erp_dat)

    assert erp_dat_all