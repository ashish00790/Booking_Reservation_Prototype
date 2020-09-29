#!/usr/bin/env python
# coding: utf-8

import os
import json
from time import sleep
from kafka import KafkaProducer
from reservations import create_random_transaction   ## Importing random data generator class 'reservations.py'


#setting the environment variables below

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND



#initiating the main function to send the reservation data into kafka topic 
if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKER_URL,value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    while True:
        transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction)  # DEBUG
        sleep(SLEEP_TIME)

