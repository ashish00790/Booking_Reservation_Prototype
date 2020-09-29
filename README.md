# Booking_Reservation_Prototype  (Ashish)

This Application is a containerised application consist of confluent kafka and python logic for Booking Reservation.

This Application consists of producer and consumer 

Used Technology:
->Kafka : Confluent docker imag
->Zookeeper : Confluent docker image
->Python: Python 3.6

Used Library:
->kafka-python
->Pandas

Data format: json

1- Producer: Producer is inheriting the reservation.py python file(generating random data) ,and storing a topic called "queueing.transactions".
 Input data is as follows:
 {
 "reservation_id": "long",
 "hotel_id": "long",
 "city": "string",
 "nights_booked": "int",
 "booking_amount": "double",
 "currency": "string"
}

2- Consumer: Consumer is taking the data from "queueing.transactions" and applying the conversion logic given below on booking_amount data as above.
  Conversion Logic: 
  GBP:EUR (1:1.1)
  USD:EUR (1:0.8)
  INR:EUR (1: 0.01)
  CNY:EUR (1:0.1)
  
  After the conversion logic data is stored into ""streaming.output" topic.  Output is as follows:
  {
 "reservation_id": 12222,
 "hotel_id": 2333,
 "city": "New York",
 "nights_booked": 2,
 "booking_amount": 120.99,
 "currency": "USD",
 "normalised_booking_amount": 102.5,
 "normalised_currency": "EUR"
}

------------------------------------------------------------------------------------------------------------
To make this application as a containerised application. I did the following things as below.
-Project Directory Structure:
./Booking_Reservation_Prototype
  /booking_consmer
    /Dockerfile
    /requirements
    /Consumer.py
  /booking_producer
    /Dockerfile
    /requirements
    /Consumer.py
    /reservations.py
 /docker-compose.yml


docker-compose.yml
This file pulls the image of confluent kafka broker, confluent zookeeper, consumer class, producer class  
  
Note: To run this project smoothly, I have given 1 min time for zookeeper and kafka to start first

How to run:
Prerequisites: Docker, Docker-compose (both should be installed)
1- Pull this application in your dev environment. 
2- go to  the directory "Booking_Reservation_Prototype"
3- run the command : docker-compose up
it  will first create the  images and then will start zookeeper then kafka, then producer and finally consumer.
output will store in the topic "streaming.output" and also print on the screen.
