from airQualitySensor import *
import json
import time

# Analogue port
airQualityPort = 1

print("running")
print("Initialising air quality sensor...")
myAirQuality = airQualitySensor(airQualityPort)

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      airQualityValue = myAirQuality.getValue()

      print "airQualityValue = " + json.dumps(airQualityValue)

      time.sleep(1)

   except IOError:
        print ("Error")

