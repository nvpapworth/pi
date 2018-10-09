import sys
import time
from threading import Timer
import math
import grovepi
import json
import bme280

sensors = { 'sensors': 
            [
              { "name": "barometric_pressure", "value": 0 },
              { "name": "barometric_humidity", "value": 0 },
              { "name": "barometric_temperature", "value": 0 }
            ]
          }

ids= { 'ids': 
            [
              { "name": "barometric_sensor_chip_id", "value": 0 },
              { "name": "barometric_sensor_chip_version", "value": 0 }
            ]
          }

class barometricSensor:

   def __init__(self, i2cPort):
      print("Initialising baromentric sensor on I2C bus address 0x%02X" %(i2cPort))
      self.port = i2cPort

   def __del__(self):
      print("destructor for baromentric sensor on I2C bus address 0x%02X" %(self.port))

   def getValue(self):
      print("getting baromentric sensor value on I2C bus address 0x%02X..." %(self.port))

      temperature,pressure,humidity = bme280.readBME280All(self.port)

      print "Temperature : ", temperature, "C"
      print "Pressure : ", pressure, "hPa"
      print "Humidity : ", humidity, "%"

      sensors['sensors'][0]['value'] = int(pressure)
      sensors['sensors'][1]['value'] = int(humidity)
      sensors['sensors'][2]['value'] = int(temperature)

      return sensors;

   def getID(self):
      print("getting baromentric sensor ID on I2C bus address 0x%02X..." %(self.port))


      (chip_id, chip_version) = bme280.readBME280ID(self.port)

      print "Chip ID     :", chip_id
      print "Version     :", chip_version

      ids['ids'][0]['value'] = chip_id
      ids['ids'][1]['value'] = chip_version

      return ids;

