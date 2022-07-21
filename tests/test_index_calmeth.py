from index_calmeth import toone, topsis, rsr, ni_rsr, critic, stddev, ewm, gini
import numpy as np
import pytest

test_array = np.array([[1, 7, 6, 5, 4],
                       [3, 9, 4, 2, 1],
                       [5, 7, 5, 1, 5],
                       [3, 1, 9, 4, 6],
                       [6, 0, 7, 1, 4]])

toone_res = np.array([[-0.52, 0.24444444, -0.04, 0.6, 0.],
                      [-0.12, 0.46666667, -0.44, -0.15, -0.6],
                      [0.28, 0.24444444, -0.24, -0.4, 0.2],
                      [-0.12, -0.42222222, 0.56, 0.35, 0.4],
                      [0.48, -0.53333333, 0.16, -0.4, 0.]])

critic_res = np.array(
    [0.21802097, 0.2822422, 0.15262514, 0.20722381, 0.13988788])

ewm_res = np.array(
    [0.20929503, 0.19983426, 0.20219102, 0.17326676, 0.21541292])

stddev_res = np.array(
    [0.19017149, 0.21814166, 0.18765255, 0.2215239, 0.1825104])

gini_res = np.array(
    [0.17142857, 0.34285714, 0.17142857, 0.15714286, 0.15714286])

gini_topsis_res = np.array(
    [[0.08462044], [0.3925441], [0.79943818], [0.41634438], [0.94094968]])

gini_rsr_res = np.array(
    [[0.36285714], [0.37142857], [0.36857143], [0.46], [0.27142857]])

gini_ni_rsr_res = np.array(
    [[0.66933333], [0.56057143], [0.65104762], [0.64247619], [0.49485714]])


def test_toone():
    assert toone(test_array, mode='1').all() == toone_res.all()  # type:ignore


def test_critic():
    assert critic(test_array).all() == critic_res.all()


def test_ewm():
    assert ewm(test_array).all() == ewm_res.all()


def test_stddev():
    assert stddev(test_array).all() == stddev_res.all()


def test_gini():
    assert gini(test_array).all() == gini_res.all()


@pytest.mark.filterwarnings("ignore::PendingDeprecationWarning")
def test_gini_topsis():
    assert topsis(test_array, gini(test_array)).all() == gini_topsis_res.all()


@pytest.mark.filterwarnings("ignore::PendingDeprecationWarning")
def test_gini_rsr():
    assert rsr(test_array, gini(test_array)).all() == gini_rsr_res.all()


@pytest.mark.filterwarnings("ignore::PendingDeprecationWarning")
def test_gini_ni_rsr():
    assert ni_rsr(test_array, gini(test_array)).all() == gini_ni_rsr_res.all()
