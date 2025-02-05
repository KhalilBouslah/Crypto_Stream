# Crypto_Stream
CryptoStream is a real-time data engineering pipeline that ingests Bitcoin price data from the Yahoo Finance API using Kafka, processes it with Apache Spark, stores it in a PostgreSQL database, and visualizes the data using Matplotlib. This project showcases end-to-end data pipeline orchestration with Apache Airflow.

# Architecture Diagram
![Crypto_stream pipeline](https://github.com/KhalilBouslah/Crypto_Stream/blob/main/Screenshots/CryptoStream%20architecure.png)

# ⚙️ Tech Stack

Data Ingestion: Yahoo Finance API (yfinance library)

Streaming: Apache Kafka

Processing: Apache Spark

Storage: PostgreSQL

Visualization: Plotly

Orchestration: Apache Airflow

Programming Language: Python

# 🏗️ Architecture

Data Ingestion: Fetches Bitcoin price data (1-minute intervals) from Yahoo Finance API.

Streaming: Kafka acts as the message broker, streaming data to Spark in real-time.

Processing: Spark cleans and transforms the data.

Storage: Processed data is stored in a PostgreSQL database.

Visualization: Plotly generates interactive visualizations for price trends.

Orchestration: Airflow manages and schedules the entire pipeline.

📦 Features

Real-time data ingestion and processing

Scalable data streaming with Kafka and Spark

Structured data storage using PostgreSQL

Dynamic and interactive visualizations with Plotly

Automated workflows using Apache Airflow

🚀 Getting Started

1️⃣ Prerequisites

Python 3.12

Docker & Docker Compose (for easier setup)

PostgreSQL

Apache Kafka

Apache Spark

Apache Airflow



