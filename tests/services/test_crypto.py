import pytest
import requests

from cryptoward.services import CryptoService
from cryptoward.utils import Settings


def test_build_from_settings() -> None:
    crypto_service = CryptoService.from_settings()
    assert isinstance(crypto_service, CryptoService)


@pytest.mark.vcr
def test_fetch_page_gets_response(
    crypto_service: CryptoService, valid_url: str
) -> None:
    response = crypto_service.fetch_page(valid_url)

    assert isinstance(response, requests.Response)
    assert response.status_code == 200


@pytest.mark.vcr
def test_fetch_invalid_page_gets_none(
    crypto_service: CryptoService, invalid_url: str
) -> None:
    response = crypto_service.fetch_page(invalid_url)
    assert response is None


def test_extract_price(
    crypto_service: CryptoService, html_page: str, expected_price: str
) -> None:
    price = crypto_service.extract_price(html_page)
    assert price == expected_price


def test_extract_price_from_unexisting_element(
    crypto_service: CryptoService, html_page_without_price: str
) -> None:
    price = crypto_service.extract_price(html_page_without_price)
    assert price == "-"


@pytest.mark.vcr
def test_fetch_cryptocurrency_prices(crypto_service: CryptoService) -> None:
    prices = crypto_service.fetch_cryptocurrency_prices()
    assert len(prices) == len(Settings.CRYPTOCURRENCIES)
