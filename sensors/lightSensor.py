import sys
import time
from threading import Timer
import math
import grovepi
import json

sensors = { 'sensors': 
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
      grovepi.pinMode(self.port, "OUPUT")

   def getValue(self):
      print("getting light sensor value...")
      # Get sensor value
      sensor_value = grovepi.analogRead(self.port)

      # Calculate resistance of sensor in K
      resistance = (float)(1023 - sensor_value) * 10 / sensor_value

      print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))

      return sensor_value;

   def getValues(self):
      print("getting light sensor values...")
      return_values = []
      # Get sensor value
      sensor_value = grovepi.analogRead(self.port)

      # Calculate resistance of sensor in K
      resistance = (float)(1023 - sensor_value) * 10 / sensor_value

      print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))

      return_values = [ sensor_value, resistance ]
#      return_values[0] = sensor_value
#      return_values[1] = resistance

      return return_values;

   def getValues2(self):
      print("getting light sensor values...")
      return_json = {}
      # Get sensor value
      sensor_value = grovepi.analogRead(self.port)

      # Calculate resistance of sensor in K
      resistance = (float)(1023 - sensor_value) * 10 / sensor_value

      print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))

      sensors['sensors'][0]['value'] = sensor_value
      sensors['sensors'][1]['value'] = int(resistance)

      return sensors;

