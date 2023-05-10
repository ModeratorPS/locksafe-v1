import board
import keypad
import time
import digitalio

relais = digitalio.DigitalInOut(board.GP0)
relais.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    relais.value = True
    time.sleep(2)
    relais.value = False
    time.sleep(2)