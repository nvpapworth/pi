import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'temperatureSensor':
            [
              { "name": "temperature", "value": 0 }
            ]
          }

class temperatureSensor:

   def __init__(self, analoguePort):
      print("Initialising temperature sensor v1.2 analogue port", analoguePort)
      self.port = analoguePort
      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print("destructor for temperature sensor v1.2 port", self.port)
      grovepi.pinMode(self.port, "OUTPUT")

   def getValue(self):
      print("getting temperature sensor v1.2 value...")

      # Get sensor value
      temperature = grovepi.temp(self.port, '1.2')

      print("temperature = %.2f" %(temperature))

      sensors['temperatureSensor'][0]['value'] = int(temperature)

      return sensors;

