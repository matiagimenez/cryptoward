# CryptoWard

CryptoWard is a comprehensive cryptocurrency monitoring tool designed to keep you informed about Bitcoin and Ethereum. The app provides real-time price updates, historical data analysis, and automated reporting, helping you stay on top of market trends and make informed investment decisions.

## **Instructions**

1. Install dependencies

```sh
pipenv install
```

2. Activate the virtual environment

```sh
pipenv shell
```

3. Run the application

```sh
python src/main.py
```

## **Features**

1. **Regular Price Scraping:**

    Constant monitoring of cryptocurrencies with up-to-date records, retrieving current prices of Bitcoin and Ethereum at regular intervals and storing them in a Google Sheets document.

2. **Price History:**

    Store a price history in Google Sheets to analyze trends over time.

3. **Threshold Notifications:**

    To enable users to make informed and quick decisions based on significant market changes, configure alerts to notify the user when the price of Bitcoin or Ethereum exceeds or drops below a certain threshold.

4. **Price Charts:**

    To clearly and accessibly visualize price trends, automatically generate charts in Google Sheets that show the evolution of prices over time.

5. **Scheduled Notifications:**

    To keep users informed of recent changes without the need for manual queries, schedule the bot to send daily, weekly, and monthly price summaries, reflecting variations compared to the previous summary, whether daily, monthly, or annually.

    Use the OpenAI to generate automatic reports that include a summary of cryptocurrency performance, trend analysis, and possible market movements.
