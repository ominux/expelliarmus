import expelliarmus
from .utils import utils


def test_dat_cutting():
    utils.test_cut_wrapper(
        expelliarmus.cut_dat, expelliarmus.read_dat, "dat_test_NCARS.dat", "out_dat.dat"
    )
    return


def test_evt2_cutting():
    utils.test_cut_wrapper(
        expelliarmus.cut_evt2,
        expelliarmus.read_evt2,
        "evt2_test_sparklers.raw",
        "out_evt2.raw",
    )
    return


def test_evt3_cutting():
    utils.test_cut_wrapper(
        expelliarmus.cut_evt3,
        expelliarmus.read_evt3,
        "evt3_test_pedestrians.raw",
        "out_evt3.raw",
    )
    return
