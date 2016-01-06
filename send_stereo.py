#!/usr/bin/python
import serial
import numpy
from wavefile import WaveReader,Format
from time import sleep

SAMPLING_RATE = 44100
CHANNELS = 2
FIFO = "/tmp/mpd_stereo.fifo"

NUM_LEDS = 300

ser = serial.Serial('/dev/ttyUSB0', 1000000)

w = WaveReader(FIFO, SAMPLING_RATE, CHANNELS, Format.PCM_16 | Format.RAW | Format.ENDIAN_LITTLE)
m = 16
colors = bytearray(b'\x00'*900)
i = 0
for a in reversed(range(33, 254, 40)):
    for b in reversed(range(33, 254, 40)):
        if a != b:
            for c in reversed(range(33, 254, 40)):
                if i < 900 and b != c:
                    colors[i] = a; i+=1
                    colors[i] = b; i+=1
                    colors[i] = c; i+=1    

for data in w.read_iter(size=1024):
    a = numpy.absolute(numpy.fft.fft(data))
    out = bytearray(b'\x00'*900)
    for x in range(0, NUM_LEDS):
        for i in range(0, min(NUM_LEDS, int(a[0][x]/m*NUM_LEDS))):
            out[i*3] = colors[899-x*3]
            out[i*3+1] = colors[898-x*3]
            out[i*3+2] = colors[897-x*3]

#        out[min(899,int(a[0][x]/m*NUM_LEDS)+(x%3))] = min(out[min(899,int(a[0][x]/m*NUM_LEDS)+(x%3))]+10, 253)

#    print(out)
    ser.write(out)
    ser.write(b"\xFF")
    sleep(0.014) # not needed, blocks while reading samples

ser.close()
