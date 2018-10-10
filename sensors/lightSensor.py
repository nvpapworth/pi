import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'lightSensor':
            [
              { "name": "lightBrightness", "value": 0 },
              { "name": "lightResistance", "value": 0 }
            ]
          }

class lightSensor:

   def __init__(self, analoguePort):
      print("Initialising light sensor analogue port", analoguePort)
      self.port = analoguePort
      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print("destructor for light sensor port", self.port)
      grovepi.pinMode(self.port, "OUTPUT")

   def getValue(self):
      print("getting light sensor values...")
      return_json = {}
      # Get sensor value
      sensor_value = grovepi.analogRead(self.port)

      # Calculate resistance of sensor in K
      if sensor_value > 0:
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value
      else:
        print "sensor_value = 0, avoid divide by zero error"
        resistance = 0

      print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))

      sensors['lightSensor'][0]['value'] = sensor_value
      sensors['lightSensor'][1]['value'] = int(resistance)

      return sensors;

