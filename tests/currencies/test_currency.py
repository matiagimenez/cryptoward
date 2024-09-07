from src.currencies.currency import Currency


def test_get_exchage_rate() -> None:
    exchage_rate = Currency.get_exchange_rate()
    assert exchage_rate is not None
    assert isinstance(exchage_rate, float)
    assert exchage_rate >= 0
