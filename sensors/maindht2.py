from temperatureHumidity import *
import time

dhtPort = 3

print("running")
print("Initialising temperature and humidity sensor...")
myDHT = temperatureHumidity(dhtPort)

print("sleeping 2...")
time.sleep(2)

while True:
   try:

      dhtValues = myDHT.getValues()
      print dhtValues
      time.sleep(.1)

   except IOError:
        print ("Error")

