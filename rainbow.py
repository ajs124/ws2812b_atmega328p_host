#!/usr/bin/python
from base import *
from time import sleep
import colorsys
import sys

data = bytearray(b'\x00'*900)

N = 150
factor = 64

HSV_tuples = [(x*1.0/N, 0.9, 0.8) for x in range(N)]

while True:
	try:
		for a in map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples):
			r, g, b = a[0], a[1], a[2]
			for i in range(0, 300):
				data[3*i] = int(round(g*factor))
				data[3*i+1] = int(round(r*factor))
				data[3*i+2] = int(round(b*factor))
			ser.write(data)
			ser.write(b"\xFF")
			sleep(0.025)
	except KeyboardInterrupt:
		ser.close()
		exit(0)
