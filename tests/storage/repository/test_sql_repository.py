from collections.abc import Iterable
from typing import Any

import pytest

from cryptoward.storage import CurrencyPrice, SQLStorageRepository


def test_entity_type(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
) -> None:
    assert currency_price_repository.entity is CurrencyPrice


def test_get_all_with_empty_repository(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
) -> None:
    assert currency_price_repository.get_all() == []


@pytest.mark.usefixtures("_populate_currency_price_repository")
def test_get_all_with_several_results(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    several_currency_prices: Iterable[CurrencyPrice],
) -> None:
    assert currency_price_repository.get_all() == several_currency_prices


@pytest.mark.usefixtures("_populate_currency_price_repository")
def test_get_by_id(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    currency_price: CurrencyPrice,
) -> None:
    assert currency_price_repository.get_by_id(currency_price.id_) == currency_price


def test_get_by_id_with_empty_database(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    currency_price: CurrencyPrice,
) -> None:
    assert currency_price_repository.get_by_id(currency_price.id_) is None


@pytest.mark.usefixtures("_populate_currency_price_repository")
def test_get_by_params(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    currency_price: CurrencyPrice,
    matching_filter_params: dict[str, Any],
) -> None:
    result = currency_price_repository.get_by_params(matching_filter_params)
    assert result == [currency_price]


@pytest.mark.usefixtures("_populate_currency_price_repository")
def test_get_by_params_with_non_matching_params(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    non_matching_filter_params: dict[str, Any],
) -> None:
    assert currency_price_repository.get_all()
    result = currency_price_repository.get_by_params(non_matching_filter_params)
    assert result == []


def test_get_by_params_with_empty_database(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    matching_filter_params: dict[str, Any],
) -> None:
    assert currency_price_repository.get_by_params(matching_filter_params) == []


@pytest.mark.usefixtures("_populate_currency_price_repository")
def test_get_by_params_without_params(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    several_currency_prices: Iterable[CurrencyPrice],
) -> None:
    assert currency_price_repository.get_by_params({}) == several_currency_prices


def test_get_by_params_with_unexisting_param(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    invalid_filter_params: dict[str, Any],
) -> None:
    with pytest.raises(AttributeError):
        currency_price_repository.get_by_params(invalid_filter_params)


def test_add(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
    currency_price: CurrencyPrice,
) -> None:
    assert currency_price_repository.get_all() == []
    currency_price_repository.add(currency_price)
    assert currency_price in currency_price_repository.get_all()


@pytest.mark.usefixtures("_populate_currency_price_repository")
def test_delete_all_with_several_entities(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
) -> None:
    assert currency_price_repository.get_all()
    currency_price_repository.delete_all()
    assert currency_price_repository.get_all() == []


@pytest.mark.usefixtures("_populate_currency_price_repository")
def test_delete_all_with_empty_repository(
    currency_price_repository: SQLStorageRepository[CurrencyPrice],
) -> None:
    assert currency_price_repository.get_all()
    currency_price_repository.delete_all()
    assert currency_price_repository.get_all() == []
