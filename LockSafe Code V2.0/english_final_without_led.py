import board
import keypad
import time
import digitalio

#tuple with used pins
rowPins = (board.GP10, board.GP11, board.GP12, board.GP13)
columnPins = (board.GP14, board.GP15, board.GP16)

#keypad matrix is created
keypadMatrix = keypad.KeyMatrix(rowPins, columnPins)

#key assignment
keyMap = { 0: "1", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8" ,
               8: "9", 9: "*", 10: "0", 11: "#" }

#Signal pin connected to the relay
relay = digitalio.DigitalInOut(board.GP0)
relais.direction = digitalio.Direction.OUTPUT

#LED on the pico will be activated to see that the program is running
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#Save variables
seq = []

#continuous loop
while True:
     led.value = True
     event = keypadMatrix.events.get()
     if event:
         if event.pressed:
             print(keyMap[event.key_number])
             if(keyMap[event.key_number] == "#"):
                 if(seq == ['your_1_number', 'your_2_number', 'your_3_number', 'your_4_number', 'your_5_number', 'your_6_number']):
                    relay.value = True
                 elif(seq == ['#', 'your_1_number', 'your_2_number', 'your_3_number', 'your_4_number', 'your_5_number', 'your_6_number']):
                    relay.value = True
                 else:
                    time.sleep(0.5)
                 time.sleep(1)
                 seq = []
             elif(keyMap[event.key_number] == "*"):
                  relay.value = False
                  time.sleep(1)
                  seq = []
             else:
                 seq.append(keyMap[event.key_number])
                 time.sleep(0.5)
                 print(seq)