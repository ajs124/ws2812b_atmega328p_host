import serial
NUM_LEDS = 300
BAUD_RATE = 2000000
SERIAL_DEVICE = '/dev/ttyUSB0'

ser = serial.Serial(SERIAL_DEVICE, BAUD_RATE)
