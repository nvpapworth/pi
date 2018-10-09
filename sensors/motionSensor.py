import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'sensors': 
            [
              { "name": "motion_detected", "value": "" }
            ]
          }

class motionSensor:

   def __init__(self, digitalPort):
      print("Initialising motion sensor digital port", digitalPort)
      self.port = digitalPort
      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print("destructor for motion sensor port", self.port)
      grovepi.pinMode(self.port, "OUTPUT")

   def getValue(self):
      print("getting motion sensor value...")

      # Get sensor value
      motion = grovepi.digitalRead(self.port)

      print("motion = ", motion)

      if motion:
          status = "true"
      else:
          status = "false"

      print("status = ", status)

      sensors['sensors'][0]['value'] = status

      return sensors;

