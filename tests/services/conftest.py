import pytest

from cryptoward.models import Element
from cryptoward.services import CryptoService
from cryptoward.utils import Settings


@pytest.fixture
def data_attributes() -> dict[str, str]:
    return {"data-test": "text-cdp-price-display"}


@pytest.fixture
def tag() -> str:
    return "span"


@pytest.fixture
def cryptocurrency() -> str:
    return "bitcoin"


@pytest.fixture
def element(tag: str, data_attributes: dict[str, str]) -> Element:
    return Element(tag=tag, data_attributes=data_attributes)


@pytest.fixture
def non_matching_element() -> Element:
    return Element(tag="test_element")


@pytest.fixture
def crypto_service(element: Element) -> CryptoService:
    return CryptoService(element=element)


@pytest.fixture
def crypto_service_with_non_matching_element(
    non_matching_element: Element,
) -> CryptoService:
    return CryptoService(element=non_matching_element)


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
