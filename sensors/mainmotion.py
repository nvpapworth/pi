from motionSensor import *
import json
import time

# Analogue port
motionPort = 5

print("running")
print("Initialising motion sensor...")
myMotion = motionSensor(motionPort)

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      motionValue = myMotion.getValue()

      print "motionValue = " + json.dumps(motionValue)

      time.sleep(1)

   except IOError:
        print ("Error")

