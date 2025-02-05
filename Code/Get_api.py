import pandas as pd
import numpy as np 
import yfinance as yf
import time
from kafka import KafkaProducer
import json

id_counter = 1
def get_crypto_data(crypto_symbol):
    global id_counter  
#Fetch live cryptocurrency data from Yahoo Finance.
    
    
    try:
        # Download live data for the specified cryptocurrency
        ticker = yf.Ticker(crypto_symbol)
        data = ticker.history(period="1d", interval="1m")
        
        if data.empty:
            print(f"No data found for {crypto_symbol}.")
            return None
        
        # Extract the latest row of data
        latest_data = data.iloc[-1]
        # Capture the timestamp
        timestamp = latest_data.name
        result = {
            "id": id_counter,
            "Timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            "Symbol": crypto_symbol, 
            "Open": latest_data["Open"],
            "High": latest_data["High"],
            "Low": latest_data["Low"],
            "Close": latest_data["Close"],
            "Volume": latest_data["Volume"]
        }
        id_counter += 1
        return result
    
    except Exception as e:
        print(f"Error fetching data for {crypto_symbol}: {e}")
        return None



# List of cryptocurrencies to track
BTC ="BTC-USD"

def stream_data():
    producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],value_serializer=lambda v:json.dumps(v).encode('utf-8'))
    loop_count=0
    loop_limit=30
    while loop_count<loop_limit:
        loop_count += 1
        data = get_crypto_data(BTC)
        topic = 'crypto'
        if data:
            producer.send(topic, data)
            print(f"Data sent to Kafka topic '{topic}': {data}")
        
        # Fetch new data every 60 seconds
        time.sleep(30)
