#!/usr/bin/python
from base import *
import sys
from time import sleep

start = int(sys.argv[1])

if start > NUM_LEDS:
    sys.exit(1)

for i in range(start, -1, -1):
    ser.write(b"\x42"*i*3)
    ser.write(b"\x00"*(NUM_LEDS-i)*3)
    ser.write(b"\xFF")
    print(i)
    sleep(0.05)

ser.close()
