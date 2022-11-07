from network import LoRa
import socket
import machine
import time
import pycom
from machine import Pin

#initialize 'p6' in gpio mode and make it an output
p_in = Pin('P6', mode=Pin.IN, pull=Pin.PULL_DOWN)

def pin_handler(channel):
    print("Sending...")
    s.setblocking(True)
    pycom.rgbled(0x00ff00)
    time.sleep(3)
    s.send("ON")

    s.setblocking(False)
    return

pycom.heartbeat(False)

# initialise LoRa in LORA mode
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
# more params can also be given, like frequency, tx power and spreading factor
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)

# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

while True:
    pycom.rgbled(0xff0000)
    p_in.callback(Pin.IRQ_RISING, pin_handler)



    # # send some data
    # s.setblocking(True)
    # pycom.rgbled(0x00ff00)
    # s.send('Hello')
    # time.sleep(0.1)
    # # get any data received...
    # s.setblocking(False)
    # pycom.rgbled(0xff0000)
    # data = s.recv(64)
    # print(data)
    #
    # # wait a random amount of time
    # time.sleep(machine.rng() & 0x0F)

# import pycom
# import time
#
#
# for i in range(5):
#     pycom.heartbeat(False)
#     pycom.rgbled(0x00ff00)
#     time.sleep(0.5)
#     pycom.rgbled(0xff0000)
#     time.sleep(0.5)
#     pycom.rgbled(0x0000ff)
#     time.sleep(0.5)
#     pycom.rgbled(0xff00ff)
#     time.sleep(0.5)
#
# pycom.heartbeat(True)

# import time
# import struct
# from network import WLAN
#
# wlan = WLAN(mode=WLAN.STA)
# mac = "%02X-%02X-%02X-%02X-%02X-%02X" % struct.unpack("BBBBBB", wlan.mac())
# print("WLAN Mac-address =",mac)
#
# ssid = 'hbo-ict-lab-2.4GHz'
# key  = 'hboictlab2018'
#
# wlan.scan()
# # WLAN network security: WLAN.WEP, WLAN.WPA, WLAN.WPA2, WLAN.WPA2_ENT
# wlan.connect(ssid, auth=(WLAN.WPA2, key))
# while not wlan.isconnected():
#     time.sleep_ms(50)
# print('WLAN connection succeeded!')
#
# print('retrieving ip address',end='')
# for i in range(20):
#     if wlan.ifconfig()[0] !='0.0.0.0':
#         print('\nWLAN IP Settings: (IP, Subnet, Gateway, DNS) =',wlan.ifconfig())
#         break
#     else:
#         print('.', end='')
#         time.sleep(1)
