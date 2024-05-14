from mfrc522 import *
import RPi.GPIO as GPIO
import signal
import sys

continue_reading = True

def end_read(signal, frame):
    global continue_reading
    print("CTRL-C captured, ending reading")
    continue_reading = False
    GPIO.cleanup()
    sys.exit()

def get_reading():
    reader = SimpleMFRC522()
    while True:
        try:
            id, text = reader.read()
            if len(reader.read())>0:
                return id, text
        finally:
            GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)



if __name__ == "__main__":
    print(get_reading())
