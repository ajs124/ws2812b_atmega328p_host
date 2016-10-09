#!/usr/bin/python
from base import *

ser.write(b"\x00"*900)
ser.write(b"\xFF")
ser.close()
