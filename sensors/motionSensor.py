import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'motionSensor':
            [
              { "name": "motionDetected", "value": "" }
            ]
          }

sensors3 = { "motionSensor.motionDetected": 0 }

class motionSensor:

   def __init__(self, digitalPort):
      print "Initialising motion sensor digital port", digitalPort
      self.port = digitalPort
      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print "destructor for motion sensor port", self.port
      grovepi.pinMode(self.port, "OUTPUT")

   def getValue(self):
      print "getting motion sensor value..."

      # Get sensor value
      motion = grovepi.digitalRead(self.port)

      print "motion = ", motion

      sensors['motionSensor'][0]['value'] = motion

      return sensors;

   def getValue3(self):
      print "getting motion sensor value v3..."

      # Get sensor value
      motion = grovepi.digitalRead(self.port)

      print "motion = ", motion

      sensors3["motionSensor.motionDetected"] = motion

      return sensors3

