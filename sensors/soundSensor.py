import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'sensors': 
            [
              { "name": "sound_v1.6", "value": 0 }
            ]
          }

class soundSensor:

   def __init__(self, analoguePort):
      print("Initialising sound sensor v1.6 analogue port", analoguePort)
      self.port = analoguePort
      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print("destructor for sound sensor v1.6 port", self.port)
      grovepi.pinMode(self.port, "OUTPUT")

   def getValue(self):
      print("getting sound sensor v1.6 value...")

      # Get sensor value
      sound = grovepi.analogRead(self.port)

      print("sound = %.2f" %(sound))

      sensors['sensors'][0]['value'] = sound

      return sensors;

