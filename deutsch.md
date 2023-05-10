# Ein Locksafe bauen
## 1. Vorshow
Diese Anleitung erklärt dir, wie du eine eigene Truhe baust, die mit Code gesichtert ist. Zusätzlich lernst du die Programmiersprache Python kennen.<br>
> Du wirst lernen...
- ...Daten eines Keypads abzurufen.
- ...einen kleinen Computer einzurichten.
- ...Stromkreise mit einem Relais zu Schalten.
- ...eine LED anzusteuern.
- ...und viele weitere Dinge.
> Was für Funktionen hat die LockSafe Truhe?
- Du kannst dir einen eigenen 6 stelligen Code überlegen.
- Beim zu oft falsch eingeben, die Truhe für 60 Sekunden sperren.
- Deine Geheimnisse in der Truhe verschließen
- und viele weitere Funktionen...
## 2. Material
Nun kommen wir zum Material. Ich habe dir hier unter eine Liste mit Produkten erstellt, die wir benötigen.
> **Note**<br>
> Es kann sein, dass du ein Produkt schon besitzt. Deswegen, kaufe nur dass, was du benötigst.
- [Raspberry Pico](https://www.reichelt.de/raspberry-pi-pico-rp2040-cortex-m0-microusb-header-rasp-pi-pico-h-p305824.html?&trstct=vrt_pdn&nbc=1) => WICHTIG: Mit Stiftleisten bestellen
- [12v Stecker mit USB und DC-Stecker](https://www.amazon.de/Zolt-Universal-USB-Anschluss-DC-Stecker-Haushaltselektronik/dp/B0932YBT9X/ref=asc_df_B0932YBT9X/?tag=googshopde-21&linkCode=df0&hvadid=546566796845&hvpos=&hvnetw=g&hvrand=10075993509748832043&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9042442&hvtargid=pla-1428434119420&psc=1&th=1&psc=1)
- [MicroUSB JBL Ladekabel](https://www.amazon.de/MicroUSB-Ladekabel-Kompatibel-Bluetooth-Lautsprecher-SOUNDGEAR-Lautsprecher/dp/B08XYX2RRX/ref=asc_df_B08XYX2RRX/?tag=googshopde-21&linkCode=df0&hvadid=546482272521&hvpos=&hvnetw=g&hvrand=2394098469561120703&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9042442&hvtargid=pla-1573446825248&psc=1&th=1&psc=1)
- [Keypad 3x4](https://www.reichelt.de/entwicklerboards-folientastatur-4-x-3-ziffern-debo-tast-4x3-p224223.html?&trstct=vrt_pdn&nbc=1)
- [Verbindungskabel](https://www.amazon.de/Female-Female-Male-Female-Male-Male-Steckbrücken-Drahtbrücken-bunt/dp/B01EV70C78/ref=asc_df_B01EV70C78/?tag=googshopde-21&linkCode=df0&hvadid=310491639325&hvpos=&hvnetw=g&hvrand=11461513820173354466&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9042442&hvtargid=pla-362913641420&psc=1&th=1&psc=1&tag=&ref=&adgrpid=59900935617&hvpone=&hvptwo=&hvadid=310491639325&hvpos=&hvnetw=g&hvrand=11461513820173354466&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9042442&hvtargid=pla-362913641420)
- [Steckplatte](https://www.kaufland.de/product/429289378/?kwd&source=pla&sid=41790452&gclid=Cj0KCQiAnNacBhDvARIsABnDa6-gY4RCjDM2pLt6dpFGdofF5kMT8Iouvvrn-3orQxaCjP3QdQzAJzkaAtBCEALw_wcB)
- Holz-Kiste mit flachem Deckel
- [Relais](https://www.reichelt.de/entwicklerboards-relais-modul-5-v-srd-05vdc-sl-c-debo-relay-5v-p239148.html?CCOUNTRY=445&LANGUAGE=de&&r=1)
- [Schloss](https://www.amazon.de/gp/product/B01N650528/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)
> **Note**<br>
> Folgende Produkte, musst du nur kaufen, wenn du eine LED verwenden möchtest:
- [220 Ohm Wiederstand](https://www.amazon.de/Metallfilm-Fest-Durchgangsloch-widerstände-Strombegrenzung-Rohs-zertifiziert/dp/B08QRXLKZQ/ref=sr_1_3_sspa?keywords=220+Ohm+Widerstand&qid=1670753216&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- [LED](https://www.reichelt.de/led-5-mm-bedrahtet-gruen-110-mcd-22--led-5mm-gn-p10232.html?PROVID=2788&gclid=Cj0KCQiAnNacBhDvARIsABnDa691HgcaGFhhWA0Ui6jMinj2Y0J1jq9og1Tg4IVw1qHuxhXOjJP_KiIaAjaOEALw_wcB)
## 3. Pico und Thonny einrichten
### 3.1 Pico mit dem PC verbinden
Als erstes musst du die Software auf den Raspberry Pico installieren. Da Python zu groß ist, verwenden wir Circuitpython. Halte die Taste Bootsel (welche sich auf dem Board vom Pico befindet) gedrückt und stecke nun den Pico mit dem MicroUSB Ladekabel an deinen PC. **Taste nicht loslassen, bis der Pico an deinem PC angezeigt wird**. (wie ein USB-Stick)
> **Warning**<br>
> Öffne keine der Dateien, die sich auf dem Pico befinden.
### 3.2 Pico Software laden
Besuche nun [diese](https://circuitpython.org/board/raspberry_pi_pico/) Website und lade dir die Datei herunter. Wenn der Download abgeschlossen ist, lege die Datei auf den Raspberry Pico. Der Raspberry Pico wirft sich dann automatisch aus und wird nicht mehr angezeigt. Stecke den Pico aus und wieder rein. Dann sollte er den namen Circuitpython besitzen.<br>
### 3.3 Thonny
Besuche jetzt [diese](https://thonny.org) Seite und lade das Programm herunter. Führe die Datei aus und öffne es.<br>
Sollte unten in der Konsole nicht stehen, dass das Gerät gefunden wurde, klicke im Manü auf Ausführen -> Den Interpreter konfigurieren -> Art: CircuitPython (generic) aus.
> Sollte trotzdem noch ein Fehler auftauchen, kontaktiere mich unter **moderatorps@gmail.com**.
## 4. Pico in Kiste einbauen
Stecke als erstes den Pico in das Breadboard:<br>
![alt text](picobild.png)
<br>Klebe das Breadboard (grün markiert) mit dem JBL Stecker (rot markiert) nach unter in die Kiste:<br>
![alt text](4_KisteBild.png)
Schneide ebenfalls ein Loch für das Kabel. (blau markiert)
## 5. Keypad
Stelle als erstes beim Netzteil 12v auf der Rückkseite ein.<br>
Klebe das Keypad vorne auf die Kiste und schneide wieder ein loch für diese Kabel hinter dem Keypad. Bild: <br>
![alt text](5_keypadaufbox.png)<br>
Stecke nun das Keypad an:<br>
![alt text](keypad-anstecken.png)<br>
Erstelle in Thonny nun eine neue Datei. (Falls noch keine angezeigt wird) <br>
Füge diesen Code ein:
```
import board
import keypad
import time
import digitalio

#Keypad genutzten Pins (GP Art)
rowPins = (board.GP10, board.GP11, board.GP12, board.GP13)
columnPins = (board.GP14, board.GP15, board.GP16)

#keypad Matrix erstellen
keypadMatrix = keypad.KeyMatrix(rowPins, columnPins)

#Tastenzuweisung
tastenMap = { 0: "1", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8",
              8: "9", 9: "*", 10: "0", 11: "#" }

#LED auf dem Pico, wird aktiviert um zu sehen, dass das Programm läuft
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#Info
print("Drücke eine Taste!")

#Dauerschleife
while True:
    led.value = True
    event = keypadMatrix.events.get()
    if event:
        if event.pressed:
            print(tastenMap[event.key_number])
            time.sleep(0.5)
```
Speicher nun den Python Code mit dem namen **keypad_test.py**.
Führe nun den Code mit dem Pfeil aus!
## 6. Relais und Motor
**Einbauen:**<br>
1.Loch vorne in die Kiste wo der Motor reinklackt<br>
2.Motor an die Decke in Richtung vorne ranschrauben<br>
3.Relais mit Tesa neben Pico kleben<br><br>
**Verbinden:**<br>
> **Warning**<br>
> Lass das Keypad angesteckt! Ich habe es bei der Abbildung ausgeblendet, da ihr es schon eingebaut habt.<br>
> ![alt text](6_anstecken.png)
##### Code:
```
import board
import keypad
import time
import digitalio

#Signalpin der mit dem Relais verbunden ist
relais = digitalio.DigitalInOut(board.GP0)
relais.direction = digitalio.Direction.OUTPUT

#LED auf dem Pico, wird aktiviert um zu sehen, dass das Programm läuft
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#Dauerschleife
while True:
    led.value = True
    relais.value = True
    time.sleep(2)
    relais.value = False
    time.sleep(2)
```
Speicher nun den Python Code mit dem namen **relais_test.py**.
Führe nun den Code mit dem Pfeil aus!
## 7. LED (dieser Schritt kann übersprungen werden, wenn du keine LED einbauen möchtest)
**Einbauen:**<br>
Das einzige, was du machen musst ist, ...<br>
...zwei löcher neben dem Keypad schneiden.<br>
...die LEDs durchstecken (Rot + Grün).<br>
**Anstecken:**<br>
> **Warning**<br>
> Lass das Keypad, Relais und den Motor und so weiter angesteckt! Ich habe es bei der Abbildung ausgeblendet, da ihr es schon eingebaut habt.<br>
> ![alt text](led_anstecken.png)
##### Code:
```
import board
import keypad
import time
import digitalio
 
# LED setup.
led1 = digitalio.DigitalInOut(board.GP17)
led1.direction = digitalio.Direction.OUTPUT

#LED auf dem Pico, wird aktiviert um zu sehen, dass das Programm läuft
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#Dauerschleife
while True:
    led.value = True
    led1.value = True
    time.sleep(2)
    led1.value = False
    time.sleep(2)
```
Speicher nun den Python Code mit dem namen **led_test.py**.
Führe nun den Code mit dem Pfeil aus!
## 8. Alles zusammenfassen
> **Note**<br>
> Wähle aus, um den Finalen code zu erhalten:
> - [Mit LED](deutsch_final_mit_led.md)
> - [Ohne LED](deutsch_final_ohne_led.md)
