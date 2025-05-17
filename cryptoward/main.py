from cryptoward.logging import log
from cryptoward.scrapper import Scrapper, Selector


def main() -> None:
    selector = Selector(
        element="span", data_attributes={"data-test": "text-cdp-price-display"}
    )
    crypto_scrapper = Scrapper(selector=selector)

    cryptocurrencies = ["bitcoin", "ethereum", "dogecoin"]
    for currency in cryptocurrencies:
        price = crypto_scrapper.fetch_cryptocurrency(currency)
        log(f"The price of {currency} is {price}")


main()
