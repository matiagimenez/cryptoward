from currencies.currency import Currency
from pydantic import ValidationError

try:
    currencies = [
        Currency(
            name="Bitcoin",
            code="BTC",
            endpoint="https://coinmarketcap.com/es/currencies/bitcoin/",
            index=0,
        ),
        Currency(
            name="Ethereum",
            code="ETH",
            endpoint="https://coinmarketcap.com/es/currencies/ethereum/",
            index=1,
        ),
        Currency(
            name="Polygon",
            code="MATIC",
            endpoint="https://coinmarketcap.com/es/currencies/polygon/",
            index=2,
        ),
    ]
except ValidationError as e:
    print(e.errors())
