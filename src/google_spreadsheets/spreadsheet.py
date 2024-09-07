from gspread.client import Client
from gspread.worksheet import Worksheet
from gspread.exceptions import WorksheetNotFound, GSpreadException
from pandas import DataFrame
from typing import Optional
import gspread
from pathlib import Path
from pydantic import BaseModel, Field


class Spreadsheet(BaseModel):
    key: str = Field(min_length=1)
    credentials_path: Path
    worksheets: dict[str, int]

    def auth_google_client(self, credentials_path: Path) -> Client:
        return gspread.auth.service_account(credentials_path)

    def get_currency_worksheet_index(self, currency: str) -> Optional[int]:
        return self.worksheets.get(currency)

    def get_worksheet_values_by_index(self, index: int) -> DataFrame:

        if index not in self.worksheets.values():
            raise ValueError(f"The index {index} has not got any currency associated")

        google_client = self.auth_google_client(self.credentials_path)
        spreadsheet = google_client.open_by_key(self.key)

        worksheet = spreadsheet.get_worksheet(index)

        dataframe = DataFrame(worksheet.get_all_records())
        return dataframe

    def get_worksheet_by_currency(self, currency: str) -> Worksheet:
        index = self.get_currency_worksheet_index(currency)

        if index is None:
            raise ValueError(f"The index {index} has not got any currency associated")

        google_client = self.auth_google_client(self.credentials_path)
        spreadsheet = google_client.open_by_key(self.key)

        try:
            worksheet = spreadsheet.get_worksheet(index)
        except WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title=currency, rows=100, cols=20)
            worksheet.append_row(["Date", "Price(U$D)", "Price(AR$)"])
            worksheet.format(
                "A1:C1",
                {
                    "horizontalAlignment": "CENTER",
                },
            )

        return worksheet

    def format_worksheet(self, worksheet, cells_range) -> None:
        worksheet.format(
            cells_range,
            {
                "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 0.0},
                "horizontalAlignment": "CENTER",
                "textFormat": {
                    "foregroundColor": {"red": 0.0, "green": 0.0, "blue": 0.0},
                    "fontSize": 10,
                },
            },
        )

        split_range = cells_range.split(":")
        start_row = int(split_range[0][1:])
        end_col = split_range[1][0]
        row_above_range = f"{split_range[0][0]}{start_row - 1}:{end_col}{start_row - 1}"

        worksheet.format(
            row_above_range,
            {
                "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                "textFormat": {
                    "foregroundColor": {"red": 0.0, "green": 0.0, "blue": 0.0},
                },
            },
        )

    def update_worksheet(
        self, currency: str, current_time: str, price: float, exchange_rate: float
    ) -> None:
        worksheet = self.get_worksheet_by_currency(currency)

        response = worksheet.append_row([current_time, price, price * exchange_rate])
        cells_updated = response.get("updates")

        if not cells_updated:
            raise GSpreadException(
                f"An error occurred while updating the worksheet: {worksheet.title}"
            )

        cells_range = cells_updated["updatedRange"].split("!")[1]
        self.format_worksheet(worksheet, cells_range)
