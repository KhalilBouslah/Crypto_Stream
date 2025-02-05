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


Project Setup
1. Initial Setup

    Create a new project folder and navigate to it:

       mkdir stream_project && cd stream_project

Create and activate a Python virtual environment:

    python -m venv myenv
    source myenv/bin/activate

2. Start Docker Containers

    Use the docker-compose.yml file to pull and run necessary containers:

       sudo docker-compose up -d

Running the Pipeline
1. Producer Script

Run the script to fetch weather data and send it to Kafka:

    python Get_api.py

# Create Database: 
     sudo docker exec -it PostgresCont bash 
     psql -h localhost -U postgres  
     CREATE DATABASE crypto;
     |c crypto;

# Create table:
     python create_table.py
     
2. Install Required Spark Packages

Download necessary jar files for  Kafka and Postgres to connect with Spark (You will find necessary jar names in spark_stream.py):

# Run spark_stream.py:
     spark-submit --packages org.postgresql:postgresql:42.5.4,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4,org.apache.spark:spark-streaming-kafka-0-10_2.12:3.5.4 spark_stream.py
# Dockerize spark_stream.py to execute it with airflow:
     docker build -f Docker -t stream_project --build-arg POSTGRES_PASSWORD=$POSTGRES_PASSWORD  .

# Run job from airflow:

![airflow_dags](https://github.com/KhalilBouslah/Crypto_Stream/blob/main/Screenshots/airflow_crypto.png)
![logs](https://github.com/KhalilBouslah/Crypto_Stream/blob/main/Screenshots/logs.png)

# See insights from data !
![Table](https://github.com/KhalilBouslah/Crypto_Stream/blob/main/Screenshots/Table.png)
![Crypto_stream pipeline](https://github.com/KhalilBouslah/Crypto_Stream/blob/main/Screenshots/vis_crypto.png)

You are encouraged to enhance the visualizations and improve both the quantity and quality of the data.
