import bs4
import requests
from pydantic import BaseModel, Field

from cryptoward.logging import Level, log
from cryptoward.settings import Settings


class Selector(BaseModel):
    element: str
    data_attributes: dict[str, str] = Field(default_factory=dict)


class Scrapper(BaseModel):
    selector: Selector

    @property
    def element(self) -> str:
        return self.selector.element

    @property
    def data_attributes(self) -> dict[str, str]:
        return self.selector.data_attributes

    @property
    def base_url(self) -> str:
        return Settings.DATASOURCE_URL

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
        price_element = finder.find(self.element, attrs=self.data_attributes)
        if not price_element:
            log(
                f"Price element not found with selector {self.selector.model_dump}",
                Level.WARNING,
            )
            return None
        return price_element.text.strip()  # type: ignore[no-any-return]

    def fetch_cryptocurrency(self, cryptocurrency: str) -> str | None:
        url = f"{self.base_url}/{cryptocurrency}"
        response = self.fetch_page(url)
        if not response:
            return None
        return self.extract_price(response.text)
