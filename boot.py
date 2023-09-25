import usb_cdc
import storage
import neopixel
import digitalio
import board

bPin = digitalio.DigitalInOut(board.BUTTON)
bPin.direction = digitalio.Direction.INPUT
bPin.pull = digitalio.Pull.UP

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

if bPin.value: # depressed
    storage.disable_usb_drive()
    usb_cdc.disable()
    storage.remount("/", False)
else:
    pixels.fill((20,20,255))
    while not bPin.value:
        pass
    pixels.fill((20,255,255))
    pass