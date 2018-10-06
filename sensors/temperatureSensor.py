import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'sensors': 
            [
              { "name": "temperature_v1.2", "value": 0 }
            ]
          }

class temperatureSensor:

   def __init__(self, analoguePort):
      print("Initialising temperature sensor v1.2 analogue port", analoguePort)
      self.port = analoguePort
      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print("destructor for temperature sensor v1.2 port", self.port)
      grovepi.pinMode(self.port, "OUPUT")

   def getValue(self):
      print("getting yemperature sensor v1.2 value...")

      # Get sensor value
      temperature = grovepi.temp(self.port, '1.2')

      print("temperature = %.2f" %(temperature))

      sensors['sensors'][0]['value'] = temperature

      return sensors;

