#!/usr/bin/python
import serial
import numpy
import os
import pyaudio
from time import sleep

SAMPLING_RATE = 44100 
CHANNELS = 1
CHUNK = 2048

NUM_LEDS = 300

os.nice(-20)
ser = serial.Serial('/dev/ttyUSB0', 2000000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=SAMPLING_RATE,
                input=True,
                frames_per_buffer=CHUNK)

m = 128
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

while True:
    a = numpy.absolute(numpy.fft.fft(list(stream.read(CHUNK*2)))) # *2, because it works
    out = bytearray(b'\x00'*900)
    for x in range(0, NUM_LEDS):
       # print(a[x])
        for i in range(0, min(NUM_LEDS, int(a[x]/m))):
            out[i*3] = colors[899-x*3]
            out[i*3+1] = colors[898-x*3]
            out[i*3+2] = colors[897-x*3]

    out[38*3] = 0  
    out[38*3+1] = 0
    out[38*3+2] = 0
    ser.write(out)
    ser.write(b"\xFF")

ser.close()

stream.stop_stream()
stream.close()

p.terminate()
