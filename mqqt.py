import paho.mqtt.publish as publish

MQTT_SERVER = "192.168.3.196"
MQTT_PATH = "domoticz/in"

import time
nv = 0
device_id = 15

while True:
    nv = nv + 1
    print(nv)
    publish.single(MQTT_PATH, '{ "idx" : ' + str(device_id) + ', "nvalue" : ' + str(nv) + ', "svalue" : "Detected"}' , hostname=MQTT_SERVER)  # send data continuously every 3 seconds
    time.sleep(3)