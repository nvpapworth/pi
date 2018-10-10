from temperatureHumiditySensor import *
import time
import json

dhtPort = 3

print("running")
print("Initialising temperature and humidity sensor...")
myDHT = temperatureHumiditySensor(dhtPort)

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      dhtValues = myDHT.getValue2()
      print "dhtValues = " + json.dumps(dhtValues)
      time.sleep(.5)

   except IOError:
        print ("Error")

