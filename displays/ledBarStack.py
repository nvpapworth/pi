import time
import grovepi

class ledBarStack:

   def __init__(self, digitalPort, orientation):
      print "Initialising LED bar stack digital port", digitalPort
      self.port = digitalPort
      grovepi.pinMode(self.port, "OUTPUT")
      grovepi.ledBar_init(self.port, orientation)

   def __del__(self):
      print "destructor for LED bar stack port", self.port
      grovepi.ledBar_setBits(self.port, 0)

   def setLevel(self, levelValue):
      print "set level ", levelValue
      grovepi.ledBar_setLevel(self.port, levelValue)
      return;

   def setLed(self, ledValue, onOff):
      print "set LED ", ledValue, " to ", onOff
      grovepi.ledBar_setLed(self.port, ledValue, onOff)
      return;

   def toggleLed(self, ledValue):
      print "toggle LED ", ledValue
      grovepi.ledBar_toggleLed(self.port, ledValue)
      return;

   def setBits(self, bitValue):
      print "set bits {0:b}".format(bitValue)
      grovepi.ledBar_setBits(self.port, bitValue)
      return;

   def getBits(self):
      print "get bits"
      bits = grovepi.ledBar_getBits(self.port)
      print "bits = ", bits
      return bits;

   def setOrientation(self, orientationValue):
      print "set orientation ", orientationValue
      grovepi.ledBar_orientation(self.port, orientationValue)
      return;

