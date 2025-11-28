from cryptoward.scrapper import Scrapper, Selector
from cryptoward.utils import Level, Settings, log


def fetch_cryptocurrency_prices() -> list[str]:
    prices = []
    log("Fetching cryptocurrency prices", Level.INFO)
    selector = Selector(
        element="span", data_attributes={"data-test": "text-cdp-price-display"}
    )
    scrapper = Scrapper(selector=selector)
    for currency in Settings.CRYPTOCURRENCIES:
        price = scrapper.fetch_cryptocurrency(currency)
        prices.append(price)
        log(f"{currency}: {price}", Level.INFO)
    return prices
