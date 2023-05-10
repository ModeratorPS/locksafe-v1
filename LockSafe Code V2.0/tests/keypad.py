import board
import keypad
import time
import digitalio

rowPins = (board.GP10, board.GP11, board.GP12, board.GP13)
columnPins = (board.GP14, board.GP15, board.GP16)

keypadMatrix = keypad.KeyMatrix(rowPins, columnPins)

tastenMap = { 0: "1", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8", 8: "9", 9: "*", 10: "0", 11: "#" }

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

print("Press a button!")

while True:
    led.value = True
    event = keypadMatrix.events.get()
    if event:
        if event.pressed:
            print(tastenMap[event.key_number])
            time.sleep(0.5)