from nose.tools import *
from nose.plugins.skip import SkipTest
from pdxart import PdxArt

def test_pdxart():
    """ Test loading PdxArt class without arguments """
    art = PdxArt()
    assert_is_not_none(art)

def test_header():
    """ Test PdxArt header """
    # raise SkipTest
    art = PdxArt()
    header = art.header()
    expected_header = [ 'record_id', 'artist' ]
    assert_equal(expected_header, header[:2])

def test_locations():
    """ Test that latitude and longitude are valid """
    # raise SkipTest
    art = PdxArt()
    for location in art.locations():
        yield check_location, location

# Generator that doesn't get run because 'test' is not in the function name
def check_location(location):
    for x in list(location):
        assert_true(type(x) is str)
        if x != '':
            x_float = float(x)
            assert_true(type(x_float) is float)
