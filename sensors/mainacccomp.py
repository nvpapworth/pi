from accelerometerCompass6AxisSensor import *
import time
import json

print("running")
print("Initialising accelerometer and Compass 6 Axis sensor...")
myAC = accelerometerCompass6AxisSensor()

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      acValues = myAC.getValues()
      print "acValues = " + json.dumps(acValues)
      time.sleep(.5)

   except IOError:
        print ("Error")

