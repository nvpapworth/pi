from soundSensor import *
import json
import time

# Analogue port
soundPort = 2

print("running")
print("Initialising sound sensor...")
mySound = soundSensor(soundPort)

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      soundValue = mySound.getValue()

      print "soundValue = " + json.dumps(soundValue)

      time.sleep(1)

   except IOError:
        print ("Error")

