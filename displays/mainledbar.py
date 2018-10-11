from ledBarStack import *
import time

ledBarPort = 7

print("running")
print("Initialising LED bar port...")
myLcd = ledBarStack(ledBarPort, 1)

myLcd.setLevel(5)

print("sleeping 2...")
time.sleep(2)

myLcd.setLevel(0)
time.sleep(1)
myLcd.setLed(1, 1)
time.sleep(1)
myLcd.setLed(3, 1)
time.sleep(1)
myLcd.setLed(5, 1)


print("sleeping 2...")
time.sleep(2)


myLcd.toggleLed(5)
time.sleep(1)
myLcd.toggleLed(5)
time.sleep(1)
myLcd.toggleLed(5)
time.sleep(1)
myLcd.toggleLed(5)
time.sleep(1)

print("sleeping 2...")
time.sleep(2)


myLcd.setBits(682)
time.sleep(1)
myLcd.setBits(341)
time.sleep(1)
myLcd.setBits(682)
time.sleep(1)
myLcd.setBits(341)
time.sleep(1)

print("sleeping 2...")
time.sleep(2)

myBits = myLcd.getBits()
print "myBits = ", myBits

print("sleeping 2...")
time.sleep(2)


myLcd.setLevel(4)
time.sleep(1)
myLcd.setOrientation(0)
time.sleep(1)
myLcd.setOrientation(1)
time.sleep(1)
myLcd.setOrientation(0)
time.sleep(1)
myLcd.setOrientation(1)
time.sleep(1)
time.sleep(2)
