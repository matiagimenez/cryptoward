from datetime import time
from gspread.worksheet import Worksheet
from pandas import DataFrame
from typing import Optional
import gspread
from pathlib import Path
from pydantic import BaseModel, Field


class Spreadsheet(BaseModel):
    key: str = Field(min_length=1)
    credentials_path: Path
    worksheets: dict[str, int]

    def auth_google_client(self, credentials_path: Path):
        return gspread.auth.service_account(credentials_path)

    def get_currency_worksheet_index(self, currency: str) -> Optional[int]:
        return self.worksheets.get(currency)

    def get_worksheet_values_by_index(self, index: int) -> Optional[DataFrame]:

        if index not in self.worksheets.values():
            return None

        google_client = self.auth_google_client(self.credentials_path)
        spreadsheet = google_client.open_by_key(self.key)
        worksheet = spreadsheet.get_worksheet(index)
        dataframe = DataFrame(worksheet.get_all_records())
        return dataframe

    def get_worksheet_index(self, currency: str) -> Optional[int]:
        index = self.worksheets.get(currency)

        return index

    def get_worksheet_by_currency(self, currency: str) -> Optional[Worksheet]:
        index = self.get_worksheet_index(currency)
        if index is None:
            return None

        google_client = self.auth_google_client(self.credentials_path)
        spreadsheet = google_client.open_by_key(self.key)
        worksheet = spreadsheet.get_worksheet(index)

        return worksheet

    def format_worksheet(self, worksheet, cells_range):
        worksheet.format(
            cells_range,
            {
                "backgroundColor": {"red": 0.0, "green": 0.0, "blue": 0.0},
                "horizontalAlignment": "CENTER",
                "textFormat": {
                    "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                    "fontSize": 12,
                    "bold": True,
                },
            },
        )

    def update_worksheet(
        self, currency: str, current_time: str, price: float, exchange_rate: float
    ) -> None:
        worksheet = self.get_worksheet_by_currency(currency)
        index = self.get_worksheet_index(currency)

        if index is None or worksheet is None:
            return None

        dataframe = self.get_worksheet_values_by_index(index)

        if dataframe is None:
            return None

        response = worksheet.append_row([current_time, price, price * exchange_rate])
        # TODO: Format the updated cells
        # self.format_cells(worksheet, cells_range)

        print(response)
