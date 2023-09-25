# 
import duckyscript
import neopixel
import os
import board

# first script execute
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

autorun = open("autorun", "r").read()
if autorun in os.listdir("duckyscripts"):
    with open('duckyscripts/{}'.format(autorun)) as file:
        lines = file.read().splitlines()
        for line in lines:
            duckyscript.process(line, None, pixels)

import time
import adafruit_ssd1306
import digitalio

i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

bPin = digitalio.DigitalInOut(board.BUTTON)
bPin.direction = digitalio.Direction.INPUT
bPin.pull = digitalio.Pull.UP

scripts = os.listdir("duckyscripts")


slIndex = 0

class button:
    def pressed():
        if not bPin.value:
            return True
        else:
            return False
        
    def waitForPress():
        cyclesHeld = 0
        while True:
            if not bPin.value:
                while not bPin.value:
                    cyclesHeld += 1
                    time.sleep(0.05)

                    if cyclesHeld > 25 and cyclesHeld < 45:
                        pixels.fill((128,0,128))
                    elif cyclesHeld > 45:
                        pixels.fill((128,128,128))

                return cyclesHeld
            
            time.sleep(0.05)

# initial draw

#pixels.fill((255, 0, 0))

while True:
    oled.fill(0)

    y = 8

    for x in scripts[slIndex:5+slIndex]:
        if scripts.index(x) == slIndex:
            oled.text(' > '+x, 0, y, 1)
        else:
            oled.text(' | '+x, 0, y, 1)
        y += 10


    oled.show()

    cycles = button.waitForPress()

    print(cycles)

    if cycles > 6 and cycles < 25:
        oled.fill(0)
        oled.show()

        if scripts[slIndex] in os.listdir("duckyscripts"):
            with open('duckyscripts/{}'.format(scripts[slIndex])) as file:
                lines = file.read().splitlines()
                for line in lines:
                    duckyscript.process(line, oled, pixels)
    elif cycles > 25 and cycles < 45:
        pixels.fill((128,0,128))
        with open("autorun", "w") as f:
            f.write(scripts[slIndex])
            f.flush()
        time.sleep(0.25)
        pixels.fill((0,0,0))
    elif cycles > 45:
        pixels.fill((128,128,128))
        with open("autorun", "w") as f:
            f.write("")
            f.flush()
        time.sleep(0.25)
        pixels.fill((0,0,0))
        
    else:
        print("go down one")
        slIndex +=1

    if slIndex > len(scripts)-1:
        slIndex = 0

