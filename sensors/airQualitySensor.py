import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'sensors': 
            [
              { "name": "air_quality_value", "value": 0 },
              { "name": "air_quality_status", "value": "" }
            ]
          }

class airQualitySensor:

   def __init__(self, analoguePort):
      print("Initialising air quality sensor analogue port", analoguePort)
      self.port = analoguePort
      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print("destructor for air quality sensor port", self.port)
      grovepi.pinMode(self.port, "OUTPUT")

   def getValue(self):
      print("getting air quality sensor value...")

      # Get sensor value
      quality = grovepi.analogRead(self.port)

      print("quality = %.2f" %(quality))

      if quality > 700:
          status = "HighPollution"
      elif quality > 300:
          status = "LowPollution"
      else:
          status = "AirFresh"

      print("status = ", status)

      sensors['sensors'][0]['value'] = quality
      sensors['sensors'][1]['value'] = status

      return sensors;

