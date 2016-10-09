#!/usr/bin/python
import sys
from base import *
from time import sleep

NUM_LEDS = 300

sleeptime = 1/int(sys.argv[1])

while True:
    ser.write(b"\x00"*900)
    ser.write(b"\xFF")
    sleep(sleeptime) #-(NUM_LEDS*3*8/800000)+0.000005) # 900 bytes / 800khz + 50µs reset code
    ser.write(b"\x80"*900)
    ser.write(b"\xFF")
    sleep(sleeptime) #-(NUM_LEDS*3*8/800000)+0.000005)

ser.close()
