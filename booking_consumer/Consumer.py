#!/usr/bin/env python
# coding: utf-8


from kafka import KafkaConsumer, KafkaProducer
import os
import json
from time import sleep
import pandas as pd



#Setting the environment variables
KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
OUTPUT_TOPIC = os.environ.get("OUTPUT_TOPIC")  

#Consuming the kafka topic 'TRANSACTIONS_TOPIC'
consumer = KafkaConsumer (TRANSACTIONS_TOPIC,bootstrap_servers = KAFKA_BROKER_URL ,enable_auto_commit=True, auto_offset_reset='earliest', value_deserializer=lambda m: json.loads(m.decode('utf-8')))

#Producing the output data into kafka topic 'OUTPUT_TOPIC'
producer = KafkaProducer(bootstrap_servers = KAFKA_BROKER_URL,value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#Transforming the input data into desired output data
for message in consumer:
    Reservation_DF = pd.DataFrame.from_dict(message[6])
    currency_map = {'CNY': Reservation_DF['booking_amount']*0.1, 'INR': Reservation_DF['booking_amount']*0.01, 'USD': Reservation_DF['booking_amount']*0.8, 'GBP':Reservation_DF['booking_amount']*1.10}
    Reservation_String = Reservation_DF.to_string()
    List_of_Words = Reservation_String.split()
    Fetched_currency = List_of_Words[-1]
    normalised_amount = currency_map[Fetched_currency]
    Reservation_DF['normalised_booking_amount'] = normalised_amount
    Reservation_DF['normalised_currency'] = 'EUR'
    
    Reservation_json_data = Reservation_DF.to_json(orient ='records')
    producer.send(OUTPUT_TOPIC, value=Reservation_json_data)
    print(Reservation_json_data)

