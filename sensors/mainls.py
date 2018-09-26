from lightSensor import *
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

      lsValues = myLS.getValues()
      print("RETURNED sensor_value = %d resistance = %.2f" %(lsValues[0],  lsValues[1]))
      time.sleep(.5)

   except IOError:
        print ("Error")

