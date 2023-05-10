import board
import keypad
import time
import digitalio

led1 = digitalio.DigitalInOut(board.GP17)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP18)
led2.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#Dauerschleife
while True:
    led.value = True
    led1.value = True
    led2.value = False
    time.sleep(1)
    led1.value = False
    led2.value = True
    time.sleep(1)