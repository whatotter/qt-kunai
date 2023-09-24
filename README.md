# qt-kunai
a badusb with a 0.98 inch OLED screen, supporting multiple payloads and mouse control, using a trinkey QT2040 (~$14 USD)

***

## usage
everything is controlled by one button (the BOOT button), as the reset button cant be used  

tap once to go down one, hold for 1-2 seconds to run  
hold 3-4 seconds to set a script to autorun on next boot  
hold for 4+ seconds to clear the autorun

## adding scripts/programming
to program your qtkunai after it's been "flashed", you have to hold the BOOT button after it's booted (contradictory)  
an easy way to do this is to hold the boot button while the yellow light flashes  
hold the button until the neopixel turns blue, then let go for it to turn purple, meaning its enabled it's usb storage  

to add a duckyscript script, just put it in the `/duckyscripts` folder - it'll automatically restart the kunai and show up  

## duckyscript syntax
the syntax for this is similar to duckyscript 1.0, supporting REM, STRINGLN, and some other things  
most payloads will be supported by the qt-kunai, and if not, require basic editing  
numbers wrapped in parenthesis must be an integer, never a string  

| script command  | description | usage |
| --- | --- | --- |
| REM | remarks/comments | `REM i am a comment` |
| STRINGDELAY | write a string, with a delay between each space set in miliseconds | `STRINGDELAY (1000) hello world` |
| DELAY | sleep for X miliseconds | `DELAY (1000)` |
| DEFAULTDELAY | delay inbetween each command, set as miliseconds | `DEFAULTDELAY (1000)` |
| STRING | write a string, not ending in a newline/enter | `STRING hello world` |
| STRINGLN | same as above, but ends in a newline/enter | `STRINGLN hello world` |
| REPEAT | repeats the previously executed line X amount of times | `REPEAT (25)` |
| COLOR | sets the color of the neopixel as RGB, no brightness | `COLOR (255) (255) (255)` |
| PRINT | prints to the display text at X and Y coordinates (no wordwrap) | `PRINT (4) (8) hello world` |
| SCNCLR | clears the OLED display | `SCNCLR` |
| LEFTCLICK | left click at current mouse position | `LEFTCLICK` |
| RIGHTCLICK | right click at current mouse position (how obvious) | `RIGHTCLICK` |
| WHEEL | scroll the mouse wheel - positive integer is up, negative is down | `WHEEL (100)` |
| MOUSEMOVE | move the mouse - [view X,Y syntax here](https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.mouse.Mouse.move) | `MOUSEMOVE (100) (100)` |
| GUI | press a key with the GUI key | `GUI r` |
| ALT | press a key with the ALT key | `ALT F4` |
| CTRL | i think you know what this one does | `CTRL d` |

### to be added
- `DEFINE`
- `WAIT_FOR_BUTTON_PRESS`
- `ATTACKMODE`
- `RESTART_TO` (restarts to X line in Y script)
- `AUTORUN` (sets X script to autorun)


