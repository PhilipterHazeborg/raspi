import RPi.GPIO as GPIO
import dht11
import time
import sqlite3
import datetime

import charts

charts.init()


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


try:
    while True:
        connection = sqlite3.connect("temperatur.db")
        cursor = connection.cursor()
        time_now = datetime.datetime.now()
        instance = dht11.DHT11(pin = 4)
        result = instance.read()
        while not result.is_valid():  # read until valid values
            result = instance.read()
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        cursor.execute("INSERT INTO daten (date, temp, hum) VALUES (?,?,?)",(time_now, "%3.1f" % result.temperature, "%3.1f" % result.humidity)) 
        connection.commit()
        connection.close()
        time.sleep(5)
except KeyboardInterrupt:
    exit(-1)
