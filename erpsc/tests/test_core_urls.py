"""Tests for URL functions and classes from erpsc.core."""

from py.test import raises

from erpsc.core.urls import URLS
from erpsc.core.errors import InconsistentDataError

###################################################################################################
###################################################################################################

def test_urls():

    assert URLS(auto_gen=False)
    assert URLS(auto_gen=True)

def test_urls_settings_args():
    """Tests URLS() returns properly with settings provided, and args defined.
    This triggers save_settings() and save_args() methods with inputs from __init__.
    """

    assert URLS(db='pubmed', retmax='500', field='id', retmode='xml')

def test_check_args():

    urls = URLS(db='pubmed', field='id')

    urls.check_args(['db', 'field'])

    with raises(InconsistentDataError):
        urls.check_args(['db', 'retmax', 'field'])

def test_build_info():

    urls = URLS()

    urls.build_info([])

    assert urls.info

def test_build_query():

    urls = URLS(db='pubmed')

    urls.build_query(['db'])

    assert urls.query

def test_build_search():

    urls = URLS(db='pubmed', retmax='500', field='id', retmode='xml')

    urls.build_search(['db', 'retmode'])

    assert urls.search

def test_build_fetch():

    urls = URLS(db='pubmed', retmax='500', field='id', retmode='xml')

    urls.build_fetch(['db', 'retmode'])

    assert urls.fetch
