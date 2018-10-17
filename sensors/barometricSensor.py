import sys
import time
from threading import Timer
import math
import grovepi
import json
import bme280

sensors = { 'barometricSensor':
            [
              { "name": "barometricPressure", "value": 0 },
              { "name": "barometricHumidity", "value": 0 },
              { "name": "barometricTemperature", "value": 0 }
            ]
          }

ids = { 'barometricSensor':
        [
          { "name": "barometricSensorChipId", "value": 0 },
          { "name": "barometricSensorChipVersion", "value": 0 }
        ]
      }

sensors3 = { "barometricSensor.pressure":    0,
             "barometricSensor.humidity":    0,
             "barometricSensor.temperature": 0 }

ids3 = { "barometricSensor.chipId": 0,
         "barometricSensor.chipVersion": 0 }

class barometricSensor:

   def __init__(self, i2cPort):
      print "Initialising baromentric sensor on I2C bus address 0x%02X" %(i2cPort)
      self.port = i2cPort

   def __del__(self):
      print "destructor for baromentric sensor on I2C bus address 0x%02X" %(self.port)

   def getValue(self):
      print "getting baromentric sensor value on I2C bus address 0x%02X..." %(self.port)

      temperature,pressure,humidity = bme280.readBME280All(self.port)

      print "Temperature : ", temperature, "C"
      print "Pressure : ", pressure, "hPa"
      print "Humidity : ", humidity, "%"

      sensors['barometricSensor'][0]['value'] = int(pressure)
      sensors['barometricSensor'][1]['value'] = int(humidity)
      sensors['barometricSensor'][2]['value'] = int(temperature)

      return sensors;

   def getValue3(self):
      print "getting baromentric sensor value v3 on I2C bus address 0x%02X..." %(self.port)

      temperature,pressure,humidity = bme280.readBME280All(self.port)

      print "Temperature : ", temperature, "C"
      print "Pressure : ", pressure, "hPa"
      print "Humidity : ", humidity, "%"

      sensors3['barometricSensor.pressure']    = int(pressure)
      sensors3['barometricSensor.humidity']    = int(humidity)
      sensors3['barometricSensor.temperature'] = int(temperature)

      print sensors3

      return sensors3;

   def getID(self):
      print "getting baromentric sensor ID on I2C bus address 0x%02X..." %(self.port)


      (chip_id, chip_version) = bme280.readBME280ID(self.port)

      print "Chip ID     :", chip_id
      print "Version     :", chip_version

      ids['barometricSensor'][0]['value'] = chip_id
      ids['barometricSensor'][1]['value'] = chip_version

      return ids;

   def getID3(self):
      print "getting baromentric sensor ID v3 on I2C bus address 0x%02X..." %(self.port)


      (chip_id, chip_version) = bme280.readBME280ID(self.port)

      print "Chip ID     :", chip_id
      print "Version     :", chip_version

      ids3["barometricSensor.chipId"] = chip_id
      ids3["barometricSensor.chipVersion"] = chip_version

      return ids3;

