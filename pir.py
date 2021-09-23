import RPi.GPIO as GPIO
import sys
import signal

PIR = 17

def pir_triggered(pin):
    if GPIO.input(pin):
        print('movement detected!')
    else:
        print('no movement detected')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIR, GPIO.IN)

GPIO.add_event_detect(PIR, GPIO.BOTH, callback=pir_triggered)

signal.pause()

# while True:
#     if GPIO.input(PIR):
#         print('movement detected!')

