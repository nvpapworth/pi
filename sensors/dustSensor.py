import sys
import time
from threading import Timer
import math
import grovepi
import atexit

sensors = { 'sensors':
            [
              { "name": "newval", "value": 0 },
              { "name": "dust", "value": 0 }
            ]
          }

class dustSensor:

   def __init__(self):
      print("Initialising dust sensor")

      try:
        print("Registering...")
        atexit.register(grovepi.dust_sensor_dis)

        print("Enabling...")
        grovepi.dust_sensor_en()

      except:
        print("FAILED TO INITIALISE")


   def __del__(self):
      print("destructor for dust sensor")

   def getValues(self):
      print("getting dust values...")

#      try:
      [new_val,lowpulseoccupancy] = grovepi.dustSensorRead()

      print("new_val = ", new_val, " lowpulseoccupancy = ", lowpulseoccupancy)

      sensors['sensors'][0]['value'] = new_val
      sensors['sensors'][1]['value'] = lowpulseoccupancy


#        if new_val:
#          print(lowpulseoccupancy)
#        time.sleep(5) 

#      except IOError:
#        print ("Error")

      return sensors

