import bs4
import requests
from pydantic import BaseModel

from cryptoward.models import Element
from cryptoward.utils import Level, Settings, log


class CryptoService(BaseModel):
    element: Element

    @staticmethod
    def fetch_page(url: str) -> requests.Response | None:
        log(f"Fetching data from {url}")
        response = requests.get(url)
        if response.status_code != 200:
            log(f"Failed to fetch data from datasource {url}", Level.WARNING)
            return None
        return response

    def extract_price(self, page: str) -> str | None:
        finder = bs4.BeautifulSoup(page, "html.parser")
        price_element = finder.find(
            self.element.tag,
            attrs=self.element.data_attributes,
        )
        if not price_element:
            log(
                f"Price element not found with element {self.element.model_dump}",
                Level.WARNING,
            )
            return None
        return price_element.text.strip() or "-"

    def fetch_cryptocurrency_prices(self) -> list[str]:
        prices = []
        log("Fetching cryptocurrency prices", Level.INFO)
        for cryptocurrency in Settings.CRYPTOCURRENCIES:
            url = f"{Settings.DATASOURCE_URL}/{cryptocurrency}"
            response = self.fetch_page(url)
            if not response:
                continue
            price = self.extract_price(response.text)
            name = (
                cryptocurrency.capitalize()
                if len(cryptocurrency) > 5
                else cryptocurrency.upper()
            )
            prices.append(f"{name}: {price}")
            log(f"{name}: {price}", Level.INFO)
        return prices
