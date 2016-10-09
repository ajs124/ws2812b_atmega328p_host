#!/usr/bin/python
import pyaudio
import wave

CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "/tmp/test.fifo"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)

while True:
    data = stream.read(CHUNK)
    try:
        wf.writeframes(data)
    except:
        pass
    
wf.close()
stream.stop_stream()
stream.close()
p.terminate()
