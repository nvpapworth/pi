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

      dhtValues = myDHT.getValues()
#      print("RETURNED temperature = %.02f C humidity = %.02f" %(dhtValues[0],  dhtValues[1]))
      print "dhtValues = " + json.dumps(dhtValues)
      time.sleep(.5)

   except IOError:
        print ("Error")

