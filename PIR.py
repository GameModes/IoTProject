import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)
i = 0
try:
    time.sleep(2) # to stabalize sensor
    while True:
        if GPIO.input(23):
            print("Movement detected" + str(i))
            i = i + 1
            GPIO.output(17, 1)
            time.sleep(1) # to avoid multiple detection
            GPIO.output(17, 0)
        time.sleep(2) # loop delay
    GPIO.cleanup()
finally:
    print("OOps")
    GPIO.cleanup()
print('Cleaning up')
GPIO.cleanup()
