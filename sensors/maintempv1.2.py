from temperatureSensor import *
import json
import time

# Analogue port
temperaturePort = 0

print("running")
print("Initialising temperature sensor...")
myTemp = temperatureSensor(temperaturePort)

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      tempValue = myTemp.getValue()

      print "tempValue = " + json.dumps(tempValue)

      time.sleep(1)

   except IOError:
        print ("Error")

