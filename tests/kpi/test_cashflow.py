from src.analytics.cashflow_kpis import *


def test_fcf():
    assert free_cash_flow(100, -40) == 60


def test_cfo_quality_high():
    assert cfo_quality_score(120, 100) == "High Quality"


def test_cfo_quality_moderate():
    assert cfo_quality_score(60, 100) == "Moderate"


def test_cfo_quality_risk():
    assert cfo_quality_score(20, 100) == "Accrual Risk"


def test_capex_light():
    assert capex_intensity(-20, 1000) == "Asset Light"


def test_capex_moderate():
    assert capex_intensity(-50, 1000) == "Moderate"


def test_capex_heavy():
    assert capex_intensity(-150, 1000) == "Capital Intensive"


def test_fcf_conversion():
    assert fcf_conversion(100, 200) == 50.00


def test_pattern():
    assert capital_allocation_pattern(100, -50, -20) == "Reinvestor"  