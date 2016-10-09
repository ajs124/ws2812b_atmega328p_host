#!/usr/bin/python
from base import *
from time import sleep
import colorsys
import collections
import math
import sys

def F(n):
	return int(((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5)))

data = bytearray(b'\x00'*377*3)

N = 14
offset = 3
factor = 100

HSV_tuples = [(x*1.0/N, 0.9, 0.7) for x in range(N)]
for x in range(0, N):
	print(F(x))

	for i in range(F(x), F(x+1)):
		a = colorsys.hsv_to_rgb(*HSV_tuples[x])
		r, g, b = a[0], a[1], a[2]
		data[3*i] = int(round(g*factor))
		data[3*i+1] = int(round(r*factor))
		data[3*i+2] = int(round(b*factor))

a = collections.deque(data)

while True:
	try:
		a.rotate(int(offset))
		ser.write(bytearray(a)[0:900])
		ser.write(b"\xFF")
		sleep(0.025)
	except KeyboardInterrupt:
		ser.close()
		exit(0)
