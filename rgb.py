import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def button_callback(channel):
    print("Button was pushed")
    GREEN.start(100)

button = 23
green = 27
red = 17
blue = 22

GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

try:
    while True:
        RED.start(100)
        GREEN.start(100)
        if not 'event' in locals():
            event = GPIO.add_event_detect(button,GPIO.RISING, callback=button_callback)
        else::
            time.sleep(10)
finally:
    GPIO.cleanup()