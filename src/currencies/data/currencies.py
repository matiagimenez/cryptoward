from currencies import Currency
from pydantic import ValidationError
from core.logger import Logger

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
        # Currency(
        #     name="Polygon",
        #     code="MATIC",
        #     endpoint="https://coinmarketcap.com/es/currencies/polygon/",
        #     index=2,
        # ),
        # Currency(
        #     name="Solana",
        #     code="SOL",
        #     endpoint="https://coinmarketcap.com/es/currencies/solana/",
        #     index=3,
        # ),
    ]
except ValidationError as e:
    Logger.error(e.errors())
