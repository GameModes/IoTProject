# Code from https://www.hackster.io/hardikrathod/pir-motion-sensor-with-raspberry-pi-415c04/

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabalize sensor
    while True:
        if GPIO.input(23):
            print("Hello")
            time.sleep(5) # to avoid multiple detection
        time.sleep(0.1) # loop delay

except:
    GPIO.cleanup()
