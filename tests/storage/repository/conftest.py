from collections.abc import Generator, Iterable
from datetime import datetime
from typing import Any

import pytest
from polyfactory.factories.pydantic_factory import ModelFactory

from cryptoward.storage import (
    ConnectionFactory,
    CurrencyPrice,
    SQLiteConnectionFactory,
    SQLStorageRepository,
)


@pytest.fixture
def timestamp() -> float:
    return datetime.now().timestamp()


@pytest.fixture
def several_currency_prices(
    currency_price_factory: ModelFactory[CurrencyPrice],
    timestamp: float,
) -> Iterable[CurrencyPrice]:
    return [currency_price_factory.build(timestamp=timestamp) for _ in range(5)]


@pytest.fixture
def currency_price(several_currency_prices: list[CurrencyPrice]) -> CurrencyPrice:  # noqa: FURB118
    return several_currency_prices[0]


@pytest.fixture
def connection_factory() -> ConnectionFactory:
    # TODO(matias): Replace with injections once they're configured
    return SQLiteConnectionFactory()


@pytest.fixture
def currency_price_repository(
    connection_factory: ConnectionFactory,
) -> SQLStorageRepository[CurrencyPrice]:
    return SQLStorageRepository[CurrencyPrice](connection_factory)


@pytest.fixture
def matching_filter_params(
    currency_price: CurrencyPrice,
) -> dict[str, Any]:
    return {"currency": currency_price.currency, "price": currency_price.price}


@pytest.fixture
def non_matching_filter_params(
    currency_price_factory: ModelFactory[CurrencyPrice], timestamp: float
) -> dict[str, Any]:
    currency_price = currency_price_factory.build(timestamp=timestamp)
    return {"currency": currency_price.currency, "price": currency_price.price}


@pytest.fixture
def invalid_filter_params() -> dict[str, Any]:
    return {"non_existing_field": "test"}


@pytest.fixture
def _populate_currency_price_repository(
    several_currency_prices: Iterable[CurrencyPrice],
    currency_price: CurrencyPrice,
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
) -> Generator[None, None, None]:
    currency_price_repository.add(currency_price)
    for price in several_currency_prices:
        currency_price_repository.add(price)
    yield
    currency_price_repository.delete_all()
