import sys
import time
from threading import Timer
import math
import grovepi

class genericDigitalOnOff:

   def __init__(self, deviceName, port):
      print "Initialising genericDigitalOnOff("+deviceName+") digital port", port
      self.digitalPort = port
      self.deviceName = deviceName
      self.actualState = 0
      grovepi.pinMode(self.digitalPort, "OUTPUT")

   def __del__(self):
      print "destructor for genericDigitalOnOff(" + self.deviceName + ") digital port", self.digitalPort
      grovepi.pinMode(self.digitalPort, "INPUT")

   def turnOn(self):
      print "genericDigitalOnOff("+self.deviceName+") ON..."
      self.actualState = 1
      grovepi.digitalWrite(self.digitalPort, 1)
      return;

   def turnOnWait(self, seconds):
      print "genericDigitalOnOff("+self.deviceName+") ON for " + str(seconds) + " seconds..."
      self.actualState = 1
      grovepi.digitalWrite(self.digitalPort, 1)
      time.sleep(seconds)
      print "genericDigitalOnOff("+self.deviceName+") OFF..."
      grovepi.digitalWrite(self.digitalPort, 0)
      self.actualState = 0
      return;

   def turnOffAsync(self):
      print "genericDigitalOnOff(" + self.deviceName + ") OFF for async call..."
      grovepi.digitalWrite(self.digitalPort, 0)
      self.actualState = 0
      return;

   def turnOnAsync(self, seconds):
      print "genericDigitalOnOff(" + self.deviceName + ") ON async for", seconds, "seconds"
      self.actualState = 1
      grovepi.digitalWrite(self.digitalPort, 1)
      Timer(seconds, self.turnOffAsync, ()).start()
      return;

   def turnOff(self):
      print "genericDigitalOnOff(" + self.deviceName + ") OFF..."
      grovepi.digitalWrite(self.digitalPort, 0)
      self.actualState = 0
      return;

   def getState(self):
      print "genericDigitalOnOff(" + self.deviceName + ") state = ", self.actualState
      return self.actualState;

