import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'airQualitySensor':
            [
              { "name": "airQualityValue", "value": 0 },
              { "name": "airQualityStatus", "value": 0 }
            ]
          }

sensors3 = { "airQualitySensor.value": 0,
             "airQualitySensor.status": 0 } 

class airQualitySensor:

   def __init__(self, analoguePort):
      print "Initialising air quality sensor analogue port", analoguePort
      self.port = analoguePort
      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print "destructor for air quality sensor port", self.port
      grovepi.pinMode(self.port, "OUTPUT")

   def getValue(self):
      print "getting air quality sensor value..."

      # Get sensor value
      quality = grovepi.analogRead(self.port)

      print "quality = %.2f" %(quality)

      if quality > 700:
          status = 2
      elif quality > 300:
          status = 1
      else:
          status = 0

      print "status = ", status

      sensors['airQualitySensor'][0]['value'] = int(quality)
      sensors['airQualitySensor'][1]['value'] = status

      return sensors;

   def getValue3(self):
      print "getting air quality sensor value v3..."

      # Get sensor value
      quality = grovepi.analogRead(self.port)

      print "quality = %.2f" %(quality)

      if quality > 700:
          status = 2
      elif quality > 300:
          status = 1
      else:
          status = 0

      print "status = ", status

      sensors3["airQualitySensor.value"] = int(quality)
      sensors3["airQualitySensor.status"] = status

      return sensors3;

