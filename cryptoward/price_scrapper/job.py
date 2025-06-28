import inject

from cryptoward.event_handler import Event, EventHandler
from cryptoward.price_scrapper import PriceScrapper, Selector


def job() -> None:
    selector = Selector(
        element="span", data_attributes={"data-test": "text-cdp-price-display"}
    )
    event_handler = inject.instance(EventHandler)
    scrapper = PriceScrapper(selector=selector)
    cryptocurrencies = ["bitcoin", "ethereum", "dogecoin"]
    for currency in cryptocurrencies:
        price = scrapper.fetch_cryptocurrency(currency)
        event = Event(currency=currency, price=price)
        event_handler.send_event(event)
