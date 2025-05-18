# Cryptoward

Build an end-to-end ETL pipeline that scrapes crypto prices and stores them for real-time or batch analysis.

## Build with

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Spark](https://spark.apache.org/docs/latest/api/python/index.html)
- [Airflow](https://airflow.apache.org/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [Kafka](https://kafka.apache.org/)
- [InfluxDB](https://www.influxdata.com/)
- [Grafana](https://grafana.com/)

## **Features**

1. **Data Source Scrapping**
2. **Streaming with Kafka**
3. **ETL Processing with Spark Streaming**
4. **Storage of timeseries data using InfluxDB**
5. **Visualization in Grafana**

## **Instructions**

1. Install dependencies

```sh
pipenv install --dev
```

2. Activate the virtual environment

```sh
pipenv shell
```

3. Run the application

```sh
pipenv run start
```
