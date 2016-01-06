#!/usr/bin/python
import serial

ser = serial.Serial('/dev/ttyUSB0', 2000000)
print(ser.name)

ser.write(b"\xFF")
ser.close()
