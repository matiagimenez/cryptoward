import pytest

from cryptoward.price_scrapper import PriceScrapper, Selector
from cryptoward.settings import Settings


@pytest.fixture
def data_attributes() -> dict[str, str]:
    return {"data-test": "text-cdp-price-display"}


@pytest.fixture
def element() -> str:
    return "span"


@pytest.fixture
def cryptocurrency() -> str:
    return "bitcoin"


@pytest.fixture
def selector(element: str, data_attributes: dict[str, str]) -> Selector:
    return Selector(element=element, data_attributes=data_attributes)


@pytest.fixture
def non_matching_selector() -> Selector:
    return Selector(element="test_element")


@pytest.fixture
def scrapper(selector: Selector) -> PriceScrapper:
    return PriceScrapper(selector=selector)


@pytest.fixture
def scrapper_with_non_matching_selector(non_matching_selector: Selector) -> PriceScrapper:
    return PriceScrapper(selector=non_matching_selector)


@pytest.fixture
def valid_url() -> str:
    return f"{Settings.DATASOURCE_URL}/bitcoin"


@pytest.fixture
def invalid_url() -> str:
    return f"{Settings.DATASOURCE_URL}/test_invalid_url"


@pytest.fixture
def expected_price() -> str:
    return "$1000"


@pytest.fixture
def html_page(
    expected_price: str, element: str, data_attributes: dict[str, str]
) -> str:
    attributes = " ".join(f'{k}="{v}"' for k, v in data_attributes.items())
    return f"<{element} {attributes}>{expected_price}</{element}>"
