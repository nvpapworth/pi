import sys
import time
from threading import Timer
import math
import grovepi
import json
from accelerometerCompass6AxisSensor import *
from airQualitySensor import *
from barometricSensor import *
from temperatureHumiditySensor import *
from dustSensor import *
from lightSensor import *
from motionSensor import *
from soundSensor import *
from temperatureSensor import *

sensors = { 'sensors': 
            [
              { "name": "dummy", "value": 0 }
            ]
          }

class sensors:

   def __init__(self):
      print("Initializing sensors")

   def __del__(self):
      print("destructor for sensors")

   def initializeSensors(self):
      print("Initializing sensor devices...")

      print("Initializing accelerometer and Compass 6 Axis sensor...")
      self.myAccCompass6Axis = accelerometerCompass6AxisSensor()

      print("Initializing air quality sensor...")
      # Analogue port
      airQualitySensorAnaloguePort = 1
      self.myAirQuality = airQualitySensor(airQualitySensorAnaloguePort)

      print("Initializing barometric sensor...")
      barometer_i2cAddress = 0x77
      self.myBarometer = barometricSensor(barometer_i2cAddress)

      print("Initializing temperature and humidity sensor...")
      # Digital port
      temperatureHumiditySensorDigitalPort = 3
      self.myDHT = temperatureHumiditySensor(temperatureHumiditySensorDigitalPort)

      print("Initializing dust sensor...")
      self.myDust = dustSensor()

      print("Initializing light sensor...")
      # Analogue port
      lightSensorAnaloguePort = 1
      self.myLight = lightSensor(lightSensorAnaloguePort)

      print("Initializing motion sensor...")
      # Analogue port
      motionSensorAnaloguePort = 5
      self.myMotion = motionSensor(motionSensorAnaloguePort)

      print("Initializing sound sensor...")
      # Analogue port
      soundSensorAnaloguePort = 2
      self.mySound = soundSensor(soundSensorAnaloguePort)

#      print("Initializing temperature sensor...")
      # Analogue port
#      temperatureSensorAnaloguePort = 0
#      self.myTemp = temperatureSensor(temperatureSensorAnaloguePort)

      success = 1

      return success;

   def initializeSensors3(self):
      print("Initializing sensor devices v3...")

      print("Initializing barometric sensor...")
      barometer_i2cAddress = 0x77
      self.myBarometer = barometricSensor(barometer_i2cAddress)

      print("Initializing temperature and humidity sensor...")
      # Digital port
      temperatureHumiditySensorDigitalPort = 3
      self.myDHT = temperatureHumiditySensor(temperatureHumiditySensorDigitalPort)

      success = 1

      return success;

   def getValues(self):
      print("Reading sensor values...")

      print("Reading accelerometer and Compass 6 Axis sensor...")
      reading1 = self.myAccCompass6Axis.getValue()

      print "reading1 = " + json.dumps(reading1)

      print("Reading air quality sensor...")
      reading2 = self.myAirQuality.getValue()

      print("Reading barometric sensor...")
      reading3 = self.myBarometer.getValue()

      print("Reading temperature and humidity sensor...")
      reading4 = self.myDHT.getValue()

      print("Reading dust sensor...")
      reading5 = self.myDust.getValue()

      print("Reading light sensor...")
      reading6 = self.myLight.getValue()

      print("Reading motion sensor...")
      reading7 = self.myMotion.getValue()

      print("Reading sound sensor...")
      reading8 = self.mySound.getValue()

#      print("Reading temperature sensor...")
#      reading9 = self.myTemp.getValue()

      print("Reading temperature and humidity sensor v2...")
      reading10 = self.myDHT.getValue2()

#      y = dict ( reading1.items() + reading2.items() + reading3.items() + reading4.items() + reading5.items() +
#                 reading6.items() + reading7.items() + reading8.items() + reading9.items() + reading10.items() )
      y = dict ( reading1.items() + reading2.items() + reading3.items() + reading4.items() + reading5.items() +
                 reading6.items() + reading7.items() + reading8.items() + reading10.items() )

      print "y = " + json.dumps(y)

      return y

   def getValues3Old(self):

      print("Reading sensor values v3...")

      print("Reading barometric sensor...")
      reading3 = self.myBarometer.getValue3()

      print("Reading temperature and humidity sensor...")
      reading4 = self.myDHT.getValue3()

#      y = dict ( reading3.items() + reading4.items() )
      z = reading3 + reading4

#      print "y = " + json.dumps(y)
      print "z = " , z

      return y

   def getValues3(self):
      print("Reading sensor values v3...")

      print("Reading accelerometer and Compass 6 Axis sensor...")
      reading1 = self.myAccCompass6Axis.getValue3()

      print("Reading air quality sensor...")
      reading2 = self.myAirQuality.getValue3()

      print("Reading barometric sensor...")
      reading3 = self.myBarometer.getValue3()

      print("Reading temperature and humidity sensor...")
      reading4 = self.myDHT.getValue3()

      print("Reading dust sensor...")
      reading5 = self.myDust.getValue3()

      print("Reading light sensor...")
      reading6 = self.myLight.getValue3()

      print("Reading motion sensor...")
      reading7 = self.myMotion.getValue3()

      print("Reading sound sensor...")
      reading8 = self.mySound.getValue3()

#      print("Reading temperature sensor...")
#      reading9 = self.myTemp.getValue3()

#      y = reading1 + reading2 + reading3 + reading4 + reading5 + reading6 + reading7 + reading8 + reading10

#      print "y = ", y
#      print "json y = ", json.dumps(y)

      y = dict ( reading1.items() + reading2.items() + reading3.items() + reading4.items() + reading5.items() +
                 reading6.items() + reading7.items() + reading8.items() )

      print "y = ", json.dumps(y)

      return y

