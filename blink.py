#!/usr/bin/python
import serial
import sys
from time import sleep

NUM_LEDS = 300

ser = serial.Serial('/dev/ttyUSB0', 1000000)

while True:
    for x in range(0, NUM_LEDS*3):
        ser.write(b"\x00")
    ser.write(b"\xFF")
    sleep(0.014) # 900 bytes / 1 megabit/s * 2
    for x in range(0, NUM_LEDS*3):
        ser.write(b"\xF0")
    ser.write(b"\xFF")
    sleep(0.014)

ser.close()
