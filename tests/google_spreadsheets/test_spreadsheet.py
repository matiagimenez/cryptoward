from pathlib import Path
from currencies.currency import Currency
from google_spreadsheets.spreadsheet import Spreadsheet
from core.config import settings
import pytest


@pytest.fixture
def spreadsheet():
    google_spreadsheet_key: str = settings.spreadsheet_key
    credentials_path = Path.joinpath(settings.root_dir, "credentials.json")

    currencies = [
        Currency(
            name="Bitcoin",
            code="BTC",
            endpoint="https://coinmarketcap.com/es/currencies/bitcoin/",
            index=0,
        ),
    ]

    worksheets = {currency.name: currency.index for currency in currencies}

    spreadsheet = Spreadsheet(
        key=google_spreadsheet_key,
        worksheets=worksheets,
        credentials_path=credentials_path,
    )

    return spreadsheet


def test_get_worksheet_index(spreadsheet) -> None:
    assert spreadsheet.get_currency_worksheet_index("Bitcoin") == 0
    assert spreadsheet.get_currency_worksheet_index("Ethereum") is None


def test_get_worksheet_by_currency(spreadsheet) -> None:
    assert spreadsheet.get_worksheet_by_currency("Bitcoin") is not None

    try:
        spreadsheet.get_worksheet_by_currency("Ethereum")
        assert False
    except Exception:
        assert True
