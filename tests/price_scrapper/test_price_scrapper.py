import pytest
import requests

from cryptoward.price_scrapper import PriceScrapper


@pytest.mark.vcr
def test_fetch_page_gets_response(scrapper: PriceScrapper, valid_url: str) -> None:
    response = scrapper.fetch_page(valid_url)

    assert isinstance(response, requests.Response)
    assert response.status_code == 200


@pytest.mark.vcr
def test_fetch_invalid_page_gets_none(scrapper: PriceScrapper, invalid_url: str) -> None:
    response = scrapper.fetch_page(invalid_url)
    assert response is None


def test_extract_price(scrapper: PriceScrapper, html_page: str, expected_price: str) -> None:
    price = scrapper.extract_price(html_page)
    assert price == expected_price


@pytest.mark.vcr
def test_fetch_cryptocurrency(scrapper: PriceScrapper, cryptocurrency: str) -> None:
    price = scrapper.fetch_cryptocurrency(cryptocurrency)
    assert price
    assert "$" in price


@pytest.mark.vcr
def test_fetch_unexisting_cryptocurrency(scrapper: PriceScrapper) -> None:
    price = scrapper.fetch_cryptocurrency("test_invalid_cryptocurrency")
    assert not price


@pytest.mark.vcr
def test_fetch_cryptocurrency_with_non_matching_selector(
    scrapper_with_non_matching_selector: PriceScrapper, cryptocurrency: str
) -> None:
    price = scrapper_with_non_matching_selector.fetch_cryptocurrency(cryptocurrency)
    assert not price
