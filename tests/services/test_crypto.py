import pytest
import requests

from cryptoward.services import CryptoService


@pytest.mark.vcr
def test_fetch_page_gets_response(scrapper: CryptoService, valid_url: str) -> None:
    response = scrapper.fetch_page(valid_url)

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


@pytest.mark.vcr
def test_fetch_cryptocurrency(
    crypto_service: CryptoService, cryptocurrency: str
) -> None:
    price = crypto_service.fetch_cryptocurrency(cryptocurrency)
    assert price
    assert "$" in price


@pytest.mark.vcr
def test_fetch_unexisting_cryptocurrency(crypto_service: CryptoService) -> None:
    price = crypto_service.fetch_cryptocurrency("test_invalid_cryptocurrency")
    assert not price


@pytest.mark.vcr
def test_fetch_cryptocurrency_with_non_matching_selector(
    crypto_service_with_non_matching_selector: CryptoService, cryptocurrency: str
) -> None:
    price = crypto_service_with_non_matching_selector.fetch_cryptocurrency(
        cryptocurrency
    )
    assert not price
