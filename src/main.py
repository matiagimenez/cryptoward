from datetime import datetime
from typing import Optional
from gspread import worksheet
import requests
from typing import Union
from bs4 import BeautifulSoup, Tag, NavigableString
from pathlib import Path
import os
from google_spreadsheets.spreadsheet import Spreadsheet


def fetch_data(url: str) -> str:
    try:
        response = requests.get(url)
        return response.text
    except Exception:
        raise requests.RequestException(f"Error fetching data from {url}")


def extract_element_value(html_content: str, class_value: str) -> Optional[str]:
    try:
        page = BeautifulSoup(html_content, "html.parser")
        element: Union[Tag, None, NavigableString] = page.find(class_=class_value)

        if element is None:
            raise ValueError(
                f'Element not found in the HTML with the class="{class_value}"'
            )

        return element.get_text()
    except Exception as e:
        raise ValueError(e)


endpoints: dict[str, str] = {
    "btc": "https://coinmarketcap.com/es/currencies/bitcoin/",
    "eth": "https://coinmarketcap.com/es/currencies/ethereum/",
}

worksheets: dict[str, int] = {
    "btc": 0,
    "eth": 1,
}

spreadsheet_key: str = os.environ.get("SPREADSHEET_KEY") or ""
credentials_path = Path.joinpath(
    Path(__file__).resolve().parent, "..", "credentials.json"
)
spreadsheet = Spreadsheet(spreadsheet_key, credentials_path, worksheets)


for currency_name, currency_endpoint in endpoints.items():
    try:
        html_content = fetch_data(currency_endpoint)
        price = extract_element_value(html_content, "sc-65e7f566-0 clvjgF base-text")

        if not price:
            continue

        price = price.split("$")[1].replace(",", "")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        spreadsheet.update_worksheet(currency_name, current_time, float(price))

    except Exception as e:
        print(e)
