import pytest

from core import flow


@pytest.fixture
def test_data():
    return {"tickers": ["SBER"], "iteration": 100}


def test_proper_data(test_data):
    """Should return data"""
    assert flow.get_flow_info(
        tickers=test_data["tickers"], iteration=test_data["iteration"]
    )


def test_incorrect_data(test_data):
    """Should raise exception"""
    with pytest.raises(ValueError):
        flow.get_flow_info(tickers="", iteration=test_data["iteration"])
