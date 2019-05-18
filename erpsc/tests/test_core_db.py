"""Tests for the database classes and functions from erpsc.core."""

import os

from erpsc.core.db import ERPDB, WebDB, check_db

###################################################################################################
###################################################################################################

def test_erpdb():

    assert ERPDB(auto_gen=False)

def test_erpdb_gen_paths():

    db = ERPDB(auto_gen=False)
    db.gen_paths()

    assert db

def test_erpdb_paths():

    db = ERPDB()

    # Tests that all defined ERPDB paths exist.
    #  Skips vars without '_path' marker, and empty variables
    for key, val in vars(db).items():
        if '_path' in key and val:
            assert os.path.exists(val)

def test_webdb():

    # Check that WebDB returns properly
    assert WebDB()

def test_webdb_paths():

    db = WebDB()

    # Tests that all defined WEBDB paths exist.
    #  Skips vars without '_path' marker, and empty variables
    for key, val in vars(db).items():
        if '_path' in key and val:
            assert os.path.exists(val)

def test_check_db():

    # Check that it returns an ERPDB when given None
    db = check_db(None)
    assert isinstance(db, ERPDB)

    # Check that it returns an ERPDb object when given one
    db = ERPDB()
    db = check_db(db)
    assert isinstance(db, ERPDB)
