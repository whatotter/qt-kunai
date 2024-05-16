# qt-kunai
a badusb with a 0.96 inch OLED screen, supporting multiple payloads and mouse control, using a trinkey QT2040 (~$14 USD)

***
![image](https://github.com/whatotter/qt-kunai/assets/42103041/e85b9420-94cd-4e47-92a1-6723773301ad)
<sub>(i know i misspelled mouse and green, thats the funny part)</sub>
***

## install

### BOM
| item | price |
| ---- | ----- |
| [trinkey QT2040](https://www.adafruit.com/product/5056) | $8 USD |
| [0.96in OLED](https://www.aliexpress.us/item/2251832770994631.html) | $3 USD |
| [4pin JST-SH StemmaQT wire](https://www.aliexpress.us/item/2251832425806254.html) | $3 USD |
| TOTAL: $14 USD |

### setup
1. solder the 4 pin JST-SH connector to the OLED screen - the pinout is [here](https://learn.adafruit.com/adafruit-trinkey-qt2040/pinouts)  
2. connect the now modified OLED to your QT2040
3. flash a circuitpython .uf2 file [from here](https://circuitpython.org/board/adafruit_qt2040_trinkey/)
4. "flash" the repository by `git clone`ing the project to your circuitpython equipped trinkey
5. profit


## usage
everything is controlled by one button (the BOOT button), as the reset button cant be used  

tap once to go down one, hold for 1-2 seconds to run  
hold 3-4 seconds to set a script to autorun on next boot  
hold for 4+ seconds to clear the autorun  

to clear the autorun script w/o running anything, go into programming mode (view section below) and it'll automatically clear entering it - just press the reset button and boom
to not run anything on start, hold the boot button about half a second to 1 second after the orangeish light flashes

## adding scripts/programming
to program your qtkunai after it's been "flashed", you have to hold the BOOT button after it's booted (contradictory)  
an easy way to do this is to hold the boot button while the yellow light flashes  
hold the button until the neopixel turns blue, then let go for it to turn purple, meaning its enabled it's usb storage  

to add a duckyscript script, just put it in the `/duckyscripts` folder - it'll automatically restart the kunai and show up  

## duckyscript syntax
the syntax for this is similar to duckyscript 1.0, supporting REM, STRINGLN, and some other things  
most payloads will be supported by the qt-kunai, and if not, require basic editing  
numbers wrapped in parenthesis must be an integer, never a string  
quick reminder to remove the parenthesis when using  
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


