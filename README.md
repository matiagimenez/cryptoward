# Cryptoward

**Cryptoward** is an end-to-end real-time data pipeline that scrapes cryptocurrency prices from the web, publishes them to Kafka, stores them in PostgreSQL, and exposes the data via a RESTful API using FastAPI.

1. **Web Scraping**: Periodically fetch crypto prices from public websites.
2. **Event Streaming**: Send scraped data as Kafka events for decoupled, real-time processing.
3. **Data Storage**: Persist the events in a PostgreSQL database for further analysis.
4. **REST API**: Serve historical and real-time crypto price data to consumers via FastAPI.

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [Kafka](https://kafka.apache.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

## ⚙️ Features

- 🔄 **Real-time Web Scraping** of selected cryptocurrency sources
- 📬 **Kafka-based Streaming** of price events
- 💾 **Persistent Storage** using PostgreSQL
- 🌐 **RESTful API** for querying current and historical price data
- 🐳 **Dockerized Architecture** for easy setup and local testing
