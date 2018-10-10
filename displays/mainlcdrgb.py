from lcdRgbBacklightDisplay import *
import time

print("running")
print("Initialising LCD RGB Backlightdisplay...")
myLcd = lcdRgbBacklightDisplay()

#print("sleeping 2...")
#time.sleep(2)

#myLcd.setRGB(255,0,0)
#time.sleep(2)

#myLcd.setRGB(0,255,0)
#time.sleep(2)

#myLcd.setRGB(0,0,255)
#time.sleep(2)

myLcd.setRGB(128,128,128)
time.sleep(2)

myLcd.setText("Hello\nWorld...")
time.sleep(2)

myLcd.clearScreen()
myLcd.setText_norefresh("X\nX")
time.sleep(2)

