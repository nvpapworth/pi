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

      lsValue = myLS.getValue()
      time.sleep(.5)

      lsValues = myLS.getValues2()
#      print("RETURNED sensor_value = %d resistance = %.2f" %(lsValues[0],  lsValues[1]))
      print "lsValues = " + json.dumps(lsValues)
      time.sleep(.5)

   except IOError:
        print ("Error")

