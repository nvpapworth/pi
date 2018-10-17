import sys
import time
from threading import Timer
import math
import grovepi
import atexit

sensors = { 'dustSensor':
            [
              { "name": "newValue", "value": 0 },
              { "name": "dustLevel", "value": 0 }
            ]
          }

sensors3 = { "dustSensor.newValue":  0,
             "dustSensor.dustLevel": 0 }

class dustSensor:

   def __init__(self):
      print "Initialising dust sensor"

      try:
        print "Registering..."
        atexit.register(grovepi.dust_sensor_dis)

        print "Enabling..."
        grovepi.dust_sensor_en()

      except:
        print "FAILED TO INITIALISE"


   def __del__(self):
      print "destructor for dust sensor"

   def getValue(self):
      print "getting dust values..."

#      try:
      [new_val,lowpulseoccupancy] = grovepi.dustSensorRead()

      print "new_val = ", new_val, " lowpulseoccupancy = ", lowpulseoccupancy

      sensors['dustSensor'][0]['value'] = new_val
      sensors['dustSensor'][1]['value'] = lowpulseoccupancy


#        if new_val:
#          print(lowpulseoccupancy)
#        time.sleep(5) 

#      except IOError:
#        print "Error"

      return sensors

   def getValue3(self):
      print "getting dust values v3..."

#      try:
      [new_val,lowpulseoccupancy] = grovepi.dustSensorRead()

      print "new_val = ", new_val, " lowpulseoccupancy = ", lowpulseoccupancy

      sensors3["dustSensor.newValue"] = new_val
      sensors3["dustSensor.dustLevel"] = lowpulseoccupancy


#        if new_val:
#          print(lowpulseoccupancy)
#        time.sleep(5) 

#      except IOError:
#        print ("Error")

      return sensors3

