import sys
import time
from threading import Timer
import math
import grovepi

# 4 Digit Display methods
# grovepi.fourDigit_init(pin)
# grovepi.fourDigit_number(pin,value,leading_zero)
# grovepi.fourDigit_brightness(pin,brightness)
# grovepi.fourDigit_digit(pin,segment,value)
# grovepi.fourDigit_segment(pin,segment,leds)
# grovepi.fourDigit_score(pin,left,right)
# grovepi.fourDigit_monitor(pin,analog,duration)
# grovepi.fourDigit_on(pin)
# grovepi.fourDigit_off(pin)

class fourDigitDisplay:

   def __init__(self, digitalPort):
      print("Initialising four digit display digital port", digitalPort)
      self.port = digitalPort
      grovepi.pinMode(self.port, "OUTPUT")
      grovepi.fourDigit_init(self.port)

   def __del__(self):
      print("destructor for four digit display port", self.port)
      grovepi.fourDigit_off(self.port)

   def setBrightness(self, brightness):
      print("set brightness to", brightness)
      grovepi.fourDigit_brightness(self.port, brightness)
      return;

   def setValue(self, value, leadingZero):
      print("set value to", value, " with leadingZero = ", leadingZero)
      grovepi.fourDigit_number(self.port, value, leadingZero)
      return;

   def setDigit(self, digit, value):
      print("set digit ", digit, " value to", value)
      grovepi.fourDigit_digit(self.port, digit, value)
      return;

   def setSegment(self, digit, value):
      print("set digit ", digit, " segment value to", value)
      grovepi.fourDigit_segment(self.port, digit, value)
      return;

   def setScore(self, left, right):
      print("set score ", left, ":", right)
      grovepi.fourDigit_score(self.port, left, right)
      return;

   def setOn(self):
      print("set four digit display on")
      grovepi.fourDigit_on(self.port)
      return;

   def setOff(self):
      print("set four digit display off")
      grovepi.fourDigit_off(self.port)
      return;

   def monitorAnalogue(self, analoguePort, duration):
      print("monitor analogue port", analoguePort, "for ", duration, "seconds")
      grovepi.fourDigit_monitor(self.port, analoguePort, duration)
      return;



