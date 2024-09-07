from datetime import datetime
from google_spreadsheets import google_spreadsheet
from currencies import Currency, currencies


# TODO: Create a cronjob for updating worksheet everyday
for currency in currencies:
    try:
        price = currency.fetch_price()
        current_time = datetime.now().strftime("%d-%m-%Y")
        exchange_rate = Currency.get_exchange_rate()

        if not price:
            raise ValueError(f"Error fetching {currency} price")

        google_spreadsheet.update_worksheet(
            currency.name, current_time, float(price), exchange_rate
        )

    except Exception as e:
        print(e)
