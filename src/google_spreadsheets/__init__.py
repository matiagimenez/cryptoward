from pathlib import Path
from google_spreadsheets.spreadsheet import Spreadsheet
from currencies.data.currencies import currencies
from core import settings


google_spreadsheet_key: str = settings.spreadsheet_key
credentials_path = Path.joinpath(settings.root_dir, "credentials.json")

worksheets = {currency.name: currency.index for currency in currencies}
google_spreadsheet = Spreadsheet(
    key=google_spreadsheet_key, worksheets=worksheets, credentials_path=credentials_path
)
