from barometricSensor import *
import json
import time

# Analogue port
i2cPort = 0x77

print("running")
print("Initialising barometric sensor...")
myBarometer = barometricSensor(i2cPort)

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      barometricID = myBarometer.getID()

      print "barometricID = " + json.dumps(barometricID)

      barometricValue = myBarometer.getValue()

      print "barometricValue = " + json.dumps(barometricValue)

      time.sleep(1)

   except IOError:
        print ("Error")

