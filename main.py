import RPi.GPIO as GPIO
import signal

LEDPINS = [7, 8, 25, 24, 23, 18, 15, 14]
PIR = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIR, GPIO.IN)
for pin in LEDPINS:
    GPIO.setup(pin, GPIO.OUT)

# region Functions
def get_bit(value, bit_index):
    return value & (1 << bit_index)

def disableLEDs():
    for pin in LEDPINS:
        GPIO.output(pin, GPIO.LOW)

def lightLEDsAsBinaryFromNumber(number):
    disableLEDs()

    for i in range(len(LEDPINS)):
        bitval = get_bit(number, bit_index=i)
        if (bitval): 
            GPIO.output(LEDPINS[i], GPIO.HIGH)
# endregion

count = 0

def pir_triggered(pin):
    global count

    pirval = GPIO.input(PIR)
    if (pirval):
        count += 1
        lightLEDsAsBinaryFromNumber(count)
        print("New movement detected. Amount of movements detected: " + str(count))

GPIO.add_event_detect(PIR, GPIO.BOTH, callback=pir_triggered)

disableLEDs()

signal.pause()

