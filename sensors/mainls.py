from lightSensor import *
import json
import time

lsPort = 1

print("running")
print("Initialising light sensor...")
myLS = lightSensor(lsPort)

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      lsValues = myLS.getValue()
      print "lsValues = " + json.dumps(lsValues)
      time.sleep(.5)

   except IOError:
        print ("Error")

