from cryptoward.injections import Environment, configure_injections

from .price_collector import PriceCollector


def price_collector() -> None:
    PriceCollector.start()


if __name__ == "__main__":
    configure_injections(Environment.PRODUCTION)
    price_collector()
