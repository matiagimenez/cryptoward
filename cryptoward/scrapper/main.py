import inject

from cryptoward.event_handler import Event, EventHandler
from cryptoward.injections import Environment, configure_injections
from cryptoward.scrapper import Scrapper, Selector


def main() -> None:
    selector = Selector(
        element="span", data_attributes={"data-test": "text-cdp-price-display"}
    )
    event_handler = inject.instance(EventHandler)
    scrapper = Scrapper(selector=selector)
    cryptocurrencies = ["bitcoin", "ethereum", "dogecoin"]
    for currency in cryptocurrencies:
        price = scrapper.fetch_cryptocurrency(currency)
        event = Event(currency=currency, price=price)
        event_handler.send_event(event)


if __name__ == "__main__":
    configure_injections(Environment.PRODUCTION)
    main()
