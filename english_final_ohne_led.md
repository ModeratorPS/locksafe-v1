#8. Final without LED
Create a new file and paste the code:
```
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
```
Add your code to the fields where is your_1-6_number (line 36 and 38 in Thonny)<br>
Now save the Python code with the name **main.py**. (With this name, the code will be executed automatically when plugged in.)<br>
You can now unplug the USB plug from your PC and plug it into the USB plug of the 12v power supply.<br>
Now you can unlock your chest...<br>
... _ _ _ _ _ _ #<br>
... enter your 6-digit code and press "#".<br>
...press "star" to close it again<br>
To ask? **moderatorps@gmail.com**<br>
## Have fun!
