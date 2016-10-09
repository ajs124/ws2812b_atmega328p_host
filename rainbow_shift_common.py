#!/usr/bin/python
from base import *
from time import sleep
import colorsys
import collections
import math
import sys

def rainbow_shift(offset, num):
	data = bytearray(b'\x00'*900)

	N = math.ceil(300/num)
	i = 0
	factor = 100

	HSV_tuples = [(x*1.0/N, 0.9, 0.7) for x in range(N)]
	for x in range(0, math.ceil(300/N)):
		for a in map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples):
			if i < 300:
				r, g, b = a[0], a[1], a[2]
				data[3*i] = int(round(g*factor))
				data[3*i+1] = int(round(r*factor))
				data[3*i+2] = int(round(b*factor))
				i = i+1
	a = collections.deque(data)

	while True:
		try:
			a.rotate(int(offset))
			ser.write(bytearray(a))
			ser.write(b"\xFF")
			sleep(0.025)
		except KeyboardInterrupt:
			ser.close()
			exit(0)
