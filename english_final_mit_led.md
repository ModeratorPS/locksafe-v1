# 8. Final with LED
Create a new file and paste the code:
```
import board
import keypad
import time
import digitalio
 
# LED setup Red.
led1 = digitalio.DigitalInOut(board.GP17)
led1.direction = digitalio.Direction.OUTPUT
led1.value = True

# LED setup Green.
led2 = digitalio.DigitalInOut(board.GP18)
led2.direction = digitalio.Direction.OUTPUT

#Tupel mit genutzten Pins
rowPins = (board.GP10, board.GP11, board.GP12, board.GP13)
columnPins = (board.GP14, board.GP15, board.GP16)

#keypad Matrix wird erstellt
keypadMatrix = keypad.KeyMatrix(rowPins, columnPins)

#Tastenzuweisung
tastenMap = { 0: "1", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8",
              8: "9", 9: "*", 10: "0", 11: "#" }

#Signalpin der mit dem Relais verbunden ist
relais = digitalio.DigitalInOut(board.GP0)
relais.direction = digitalio.Direction.OUTPUT

#LED auf dem Pico, wird aktiviert um zu sehen, dass das Programm läuft
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#Variablen speichern
seq = []
wrongs = 0

#Dauerschleife
while True:
    led.value = True
    event = keypadMatrix.events.get()
    if event:
        if event.pressed:
            print(tastenMap[event.key_number])
            if(tastenMap[event.key_number] == "#"):
                if(seq == ['your_1_number', 'your_2_number', 'your_3_number', 'your_4_number', 'your_5_number', 'your_6_number']):
                   relais.value = True
                   led1.value = False
                   led2.value = True
                   wrongs = 0
                elif(seq == ['#', 'your_1_number', 'your_2_number', 'your_3_number', 'your_4_number', 'your_5_number', 'your_6_number']):
                   relais.value = True
                   led1.value = False
                   led2.value = True
                   wrongs = 0
                elif(seq == ['#']):
                    time.sleep(0.5)
                else:
                   led1.value = False
                   time.sleep(1)
                   led1.value = True
                   wrongalt = wrongs
                   wrongadd = 1
                   wrongs = wrongalt + wrongadd
                   print("Wrongs: " + str(wrongs))
                   if(wrongs == 3):
                       for x in range(60):
                           led1.value = False
                           time.sleep(0.5)
                           led1.value = True
                           time.sleep(0.5)
                       wrongs = 0
                time.sleep(1)
                seq = []
            elif(tastenMap[event.key_number] == "*"):
                 relais.value = False
                 led1.value = True
                 led2.value = False
                 time.sleep(1)
                 seq = []
            else:
                seq.append(tastenMap[event.key_number])
                time.sleep(0.5)
                print(seq)
```
Add your code to the fields where is your_1-6_number (line 41 and 44 in Thonny)<br>
Now save the Python code with the name **main.py**. (With this name, the code will be executed automatically when plugged in.)<br>
You can now unplug the USB plug from your PC and plug it into the USB plug of the 12v power supply.<br>
Now you can unlock your chest...<br>
... _ _ _ _ _ _ #<br>
... enter your 6-digit code and press "#".<br>
...press "star" to close it again<br>
If you enter the code incorrectly 3 times, the chest will be locked for 60 seconds!<br>
To ask? **moderatorps@gmail.com**<br>
## Have fun!
