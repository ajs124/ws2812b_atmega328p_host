#!/usr/bin/python
import numpy
import pyfftw
import os
from base import *
from wavefile import WaveReader,Format
from time import sleep

SAMPLING_RATE = 44100
CHANNELS = 1
FIFO = "/tmp/mpd.fifo"

os.nice(-20)

sleep(1) # wait for mpd to come up

w = WaveReader(FIFO, SAMPLING_RATE, CHANNELS, Format.PCM_16 | Format.RAW | Format.ENDIAN_LITTLE)
m = 8
colors = bytearray(b'\x00'*900)
i = 0
for a in reversed(range(33, 154, 20)):
    for b in reversed(range(33, 154, 20)):
        if a != b:
            for c in reversed(range(33, 154, 20)):
                if i < 900 and b != c:
                    colors[i] = a; i+=1
                    colors[i] = b; i+=1
                    colors[i] = c; i+=1    

pyfftw.interfaces.cache.enable()
a = pyfftw.empty_aligned(1024)
for data in w.read_iter(size=1024):
    a = numpy.absolute(pyfftw.interfaces.numpy_fft.fft(data))
#   print(a)
    out = bytearray(b'\x00'*900)
    for x in range(0, NUM_LEDS):
        for i in range(0, min(NUM_LEDS, int(a[0][x]/m*NUM_LEDS))):
            out[i*3] = colors[899-x*3]
            out[i*3+1] = colors[898-x*3]
            out[i*3+2] = colors[897-x*3]

    # shitty workaround… vermutlich nur ne kalte lötstelle oder sowas, aber das hilft anscheinend.
    for o in range(38*3, 39*3):
        out[o] = 0

    ser.write(out)
    ser.write(b"\xFF")

ser.close()
