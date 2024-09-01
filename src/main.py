import requests
from bs4 import BeautifulSoup

endpoints = {
    "btc": "https://coinmarketcap.com/es/currencies/bitcoin/",
    "eth": "https://coinmarketcap.com/es/currencies/ethereum/",
}

for currency, endpoint in endpoints.items():
    response = requests.get(endpoint)

    page = BeautifulSoup(response.text, "html.parser")

    element = page.find(class_="sc-65e7f566-0 clvjgF base-text")
    price = element.get_text().split("$")[1]

    print(f"{currency}: {price}")
