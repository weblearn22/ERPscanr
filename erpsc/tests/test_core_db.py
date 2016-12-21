"""   """

from erpsc.core.db import ERPDB, check_db

##################################################################################
##################################################################################
##################################################################################

def test_erpdb():
    """Test the ERPDB object."""

    # Check that ERPDB returns properly.
    assert ERPDB()

def test_check_db():
    """   """

    db = check_db(None)
    assert isinstance(db, ERPDB)

    db = ERPDB()
    db = check_db(db)
    assert isinstance(db, ERPDB)