from dustSensor import *
import time
import json

print("running")
print("Initialising dust sensor...")
myDust = dustSensor()

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      dustValues = myDust.getValue()
      print "dustValues = " + json.dumps(dustValues)
      time.sleep(.5)

   except IOError:
        print ("Error")

