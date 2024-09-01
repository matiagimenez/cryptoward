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
    ]
except ValidationError as e:
    print(e.errors())
    """
    [
        {
            'type': 'int_parsing',
            'loc': ('id',),
            'msg': 'Input should be a valid integer, unable to parse string as an integer',
            'input': 'not an int',
            'url': 'https://errors.pydantic.dev/2/v/int_parsing',
        },
        {
            'type': 'missing',
            'loc': ('signup_ts',),
            'msg': 'Field required',
            'input': {'id': 'not an int', 'tastes': {}},
            'url': 'https://errors.pydantic.dev/2/v/missing',
        },
    ]
    """
