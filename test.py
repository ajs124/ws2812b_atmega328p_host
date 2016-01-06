#!/usr/bin/python
import serial
import sys
from time import sleep

NUM_LEDS = 300

ser = serial.Serial('/dev/ttyUSB0', 1000000)

for x in range(0, NUM_LEDS):
    for i in range(0, x):
        if x%3 == 0:
            ser.write((100).to_bytes(3, byteorder='little'))
        elif x%3 == 1:
            ser.write((100).to_bytes(3, byteorder='big'))
        else:
            ser.write((100).to_bytes(2, byteorder='big'))
            ser.write(b"\x00")
    for i in range(x, NUM_LEDS):
        ser.write((0).to_bytes(3, byteorder='big'))
    ser.write(b"\xFF")
    sleep(0.014) # 900 bytes / 1 megabit/s * 2

ser.close()
