from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture

from cryptoward.storage.models import CurrencyPrice


@register_fixture(name="currency_price_factory")
class CurrencyPriceFactory(ModelFactory[CurrencyPrice]): ...
