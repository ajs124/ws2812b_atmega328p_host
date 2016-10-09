#!/usr/bin/python
from base import *
from time import sleep
import sys

brightness = int(sys.argv[1])
data = bytearray(b'\x00'*900)
# "wärmeres" bzw. röteres licht
# pixel sind GRB
for i in range(0, 900):
	if i%3 == 1:
		data[i] = int(brightness*1.4)
	elif i%3 == 2:
		data[i] = int(brightness*0.9)
	else:
		data[i] = brightness

ser.write(data)
while True:
	ser.write(b"\xFF")
	sleep(1)

ser.close()
