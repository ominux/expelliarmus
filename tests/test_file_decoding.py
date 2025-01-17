import expelliarmus
from .utils import utils

def test_dat_decoding():
    utils.test_read_wrapper(expelliarmus.read_dat, "dat_test_NCARS.dat", 4407)
    return


def test_evt2_decoding():
    utils.test_read_wrapper(expelliarmus.read_evt2, "evt2_test_sparklers.raw", 521252)
    return

def test_evt3_decoding():
    utils.test_read_wrapper(expelliarmus.read_evt3, "evt3_test_pedestrians.raw", 5000)
    return
