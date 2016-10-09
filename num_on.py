#!/usr/bin/python
import sys
from base import *

ser.write(b"\x42"*int(sys.argv[1])*3)
ser.write(b"\x00"*(NUM_LEDS*3-int(sys.argv[1])*3))
ser.write(b"\xFF")

ser.close()
