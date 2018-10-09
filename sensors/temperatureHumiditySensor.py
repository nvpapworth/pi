import sys
import time
from threading import Timer
import math
import grovepi

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

sensors = { 'sensors':
            [
              { "name": "temperature", "value": 999 },
              { "name": "humidity",    "value": 999 }
            ]
          }

class temperatureHumiditySensor:

   def __init__(self, digitalPort):
      print("Initialising temperature and humidity sensor digital port", digitalPort)
      self.port = digitalPort
#      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print("destructor for light sensor port", self.port)
#      grovepi.pinMode(self.port, "OUPUT")

   def getValues(self):
      print("getting temperature and humidity values...")
      temp = 0.0
      humidity = 0.0
      # The first parameter is the port, the second parameter is the type of sensor.
      [temp,humidity] = grovepi.dht(self.port,blue)
      if math.isnan(temp) == False and math.isnan(humidity) == False:
          print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
          sensors['sensors'][0]['value'] = int(temp)
          sensors['sensors'][1]['value'] = int(humidity)
      else:
          sensors['sensors'][0]['value'] = 999
          sensors['sensors'][1]['value'] = 999

      return sensors

