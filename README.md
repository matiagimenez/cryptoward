# Cryptoward

**Cryptoward** is a bot designed to periodically scrape the price of selected cryptocurrencies and shares the data in Telegram.

## 🚀 Features

- **Web Scraping**: Fetches real-time cryptocurrency prices from configured sources.
- **Scheduling**: Configurable execution interval for periodic updates.

## 🛠️ Built With

- [Python 3.13](https://www.python.org/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Scheduler](https://pypi.org/project/scheduler/)
- [Pydantic](https://docs.pydantic.dev/)

## ⚙️ Configuration

The application is configured using environment variables (or a `.env` file). Key settings include:

- `DATASOURCE_URL`: The base URL for scraping prices
- `SCHEDULE_TIME_IN_MINUTES`: Interval between scrapes in minutes
