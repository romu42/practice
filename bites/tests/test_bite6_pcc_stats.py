# https://codechalleng.es/bites/6/

from bites.bite6_pcc_stats import diehard_pybites, Stats


def test_diehard_pybites():
    res = diehard_pybites()
    assert res == Stats(user='clamytoe', challenge=('01', 7))