#!/usr/bin/python
import serial
import sys

NUM_LEDS = 300

ser = serial.Serial('/dev/ttyUSB0', 1000000)

for i in range(0,int(sys.argv[1])*3):
   ser.write(b"\x42")
for i in range(int(sys.argv[1])*3,NUM_LEDS*3):
   ser.write(b"\x00")

ser.write(b"\xFF")

ser.close()
