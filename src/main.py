from datetime import datetime
from core import Scheduler, Logger
from google_spreadsheets import google_spreadsheet
from currencies import Currency, currencies


def job():
    for currency in currencies:
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
        try:
            price = currency.fetch_price()
            exchange_rate = Currency.get_exchange_rate()

            if not price:
                raise ValueError(f"Error fetching {currency} price")

            google_spreadsheet.update_worksheet(
                currency.name, current_time, float(price), exchange_rate
            )

        except ValueError as e:
            Logger.error(e)
        except Exception:
            Logger.error(
                f"An error occured while updating the spreadsheet - {current_time}"
            )

        Logger.info(f"Spreadsheet updated successfully! - {current_time}")


Scheduler.schedule_job(job)
