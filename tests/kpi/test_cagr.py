from src.analytics.cagr import *


def test_revenue_cagr():
    assert revenue_cagr(100, 200, 5) == 14.87


def test_pat_cagr():
    assert pat_cagr(50, 100, 5) == 14.87


def test_eps_cagr():
    assert eps_cagr(10, 20, 5) == 14.87


def test_zero_start():
    assert revenue_cagr(0, 100, 5) is None


def test_negative_start():
    assert revenue_cagr(-100, 200, 5) is None


def test_negative_end():
    assert revenue_cagr(100, -200, 5) is None


def test_zero_years():
    assert revenue_cagr(100, 200, 0) is None