import pytest

from cryptoward.helpers import fetch_cryptocurrency_prices
from cryptoward.utils import Settings


@pytest.mark.vcr
def test_fetch_cryptocurrency_prices() -> None:
    prices = fetch_cryptocurrency_prices()
    assert len(prices) == len(Settings.CRYPTOCURRENCIES)
