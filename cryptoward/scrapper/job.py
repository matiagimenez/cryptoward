from cryptoward.scrapper import Scrapper, Selector
from cryptoward.utils import Level, log


def job() -> None:
    selector = Selector(
        element="span", data_attributes={"data-test": "text-cdp-price-display"}
    )
    scrapper = Scrapper(selector=selector)
    cryptocurrencies = ["bitcoin", "ethereum", "dogecoin"]
    for currency in cryptocurrencies:
        price = scrapper.fetch_cryptocurrency(currency)
        log(f"{currency}: {price}", Level.INFO)
