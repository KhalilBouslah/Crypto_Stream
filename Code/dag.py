from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from kafka import KafkaProducer
import requests
from Get_api import  get_crypto_data, stream_data
import sys
import time
import json
import logging
import uuid
import random
from datetime import datetime,timedelta




start_date = datetime.today() - timedelta(days=1)
# Define the DAG
default_args = {
    'owner': 'khalil',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime(2024,12,6,10,00)
}

dag = DAG(
    'etl_dags',
    default_args=default_args,
    schedule_interval='15 10 * * *',
    catchup=False,      
    description='streaming pipeline'
) 

kafka_stream_task = PythonOperator(
 task_id="kafka_data_stream",
 python_callable=stream_data,
 dag=dag
 )

spark_stream_task = DockerOperator(
 task_id="pyspark_consumer",
 image="stream_project",
 api_version="auto",
 auto_remove='success',
 command="./bin/spark-submit --master local[*] --packages org.postgresql:postgresql:42.5.4,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 ./spark_streaming.py",
 docker_url='unix://var/run/docker.sock',
 environment={'SPARK_LOCAL_HOSTNAME': 'localhost'},
 network_mode="host",
 dag=dag
 )


kafka_stream_task >> spark_stream_task
