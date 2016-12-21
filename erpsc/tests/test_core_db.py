"""Tests for the database classes and functions from erpsc.core."""

from erpsc.core.db import ERPDB, check_db

##################################################################################
##################################################################################
##################################################################################

def test_erpdb():
    """Test the ERPDB object."""

    # Check that ERPDB returns properly.
    assert ERPDB()

def test_check_db():
    """Test the check_db function."""

    # Check that it returns an ERPDB when given None
    db = check_db(None)
    assert isinstance(db, ERPDB)

    # Check that it returns an ERPDb object when given one
    db = ERPDB()
    db = check_db(db)
    assert isinstance(db, ERPDB)