from pathlib import Path
import os
from google_spreadsheets.spreadsheet import Spreadsheet
from data.currencies import currencies

google_spreadsheet_key: str = os.environ.get("SPREADSHEET_KEY") or ""
credentials_path = Path.joinpath(
    Path(__file__).resolve().parent, "..", "..", "credentials.json"
)

worksheets = {currency.code: currency.index for currency in currencies}
google_spreadsheet = Spreadsheet(google_spreadsheet_key, credentials_path, worksheets)
