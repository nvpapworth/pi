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
              { "name": "temperature", "value": 0 },
              { "name": "humidity",    "value": 0 }
            ]
          }

class temperatureHumidity:

   def __init__(self, digitalPort):
      print("Initialising temperature and humidity sensor digital port", digitalPort)
      self.port = digitalPort
#      grovepi.pinMode(self.port, "INPUT")

   def __del__(self):
      print("destructor for light sensor port", self.port)
#      grovepi.pinMode(self.port, "OUPUT")

   def getValue(self):
      print("getting light sensor value...")
      # Get sensor value
      sensor_value = grovepi.analogRead(self.port)

      # Calculate resistance of sensor in K
      resistance = (float)(1023 - sensor_value) * 10 / sensor_value

      print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))

      return sensor_value;

   def getValues(self):
      print("getting temperature and humidity values...")
      return_values = []
      # The first parameter is the port, the second parameter is the type of sensor.
      [temp,humidity] = grovepi.dht(self.port,blue)
      if math.isnan(temp) == False and math.isnan(humidity) == False:
          print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))

      return_values = [ temp, humidity ]

      return return_values;

   def getValues2(self):
      print("getting temperature and humidity values...")
      return_values = []
      # The first parameter is the port, the second parameter is the type of sensor.
      [temp,humidity] = grovepi.dht(self.port,blue)
      if math.isnan(temp) == False and math.isnan(humidity) == False:
          print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))

      sensors['sensors'][0]['value'] = int(temp)
      sensors['sensors'][1]['value'] = int(humidity)

      return sensors;

