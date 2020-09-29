#!/usr/bin/env python
# coding: utf-8


from random import choice, randint, uniform


city_list = ['Delhi', 'New York', 'Mumbai', 'Agra', 'Amsterdam', 'Washington DC', 'England']

currency_list = ['GBP', 'USD', 'INR', 'CNY']

def randon_reservation_id() -> int:
    return randint(100, 999)
 
def random_hotel_id() -> int:
    return randint(1000, 9999)

def random_city() -> str:
    return choice(city_list)

def random_Nights_booked() -> int:
    return randint(1, 20)

def random_booking_amount() -> float:
    return uniform(10000, 100000)

def random_currency() -> str:
    return choice(currency_list)


def create_random_transaction() -> dict:
    return {
        'reservation_id': [randon_reservation_id()],
        'hotel_id': [random_hotel_id()],
        'city': [random_city()],
        # Keep it simple: it's all euros
        'nights_booked': [random_Nights_booked()],
        'booking_amount': [round(random_booking_amount(),2)],
        'currency': [random_currency()]    
    }

