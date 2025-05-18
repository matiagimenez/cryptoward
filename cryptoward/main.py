from cryptoward.event_handler import Event, KafkaEventHandler
from cryptoward.scrapper import Scrapper, Selector


def main() -> None:
    selector = Selector(
        element="span", data_attributes={"data-test": "text-cdp-price-display"}
    )
    event_handler = KafkaEventHandler()
    crypto_scrapper = Scrapper(selector=selector)
    cryptocurrencies = ["bitcoin", "ethereum", "dogecoin"]
    for currency in cryptocurrencies:
        price = crypto_scrapper.fetch_cryptocurrency(currency)
        event = Event(currency=currency, price=price)
        event_handler.send_event(event)


main()
