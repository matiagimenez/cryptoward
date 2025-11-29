from cryptoward.models import Element
from cryptoward.services import CryptoService
from cryptoward.utils import Level, Settings, log


def fetch_cryptocurrency_prices() -> list[str]:
    prices = []
    log("Fetching cryptocurrency prices", Level.INFO)
    element = Element(
        tag="span", data_attributes={"data-test": "text-cdp-price-display"}
    )
    crypto_service = CryptoService(element=element)
    for currency in Settings.CRYPTOCURRENCIES:
        price = crypto_service.fetch_cryptocurrency(currency)
        prices.append(f"{currency}: {price}")
        log(f"{currency}: {price}", Level.INFO)
    return prices
