import sys
import time
from threading import Timer
import math
import grovepi
import lsm303d

sensors = { 'sensors':
            [
              { "name": "accelerometerX", "value": 0 },
              { "name": "accelerometerY", "value": 0 },
              { "name": "accelerometerZ", "value": 0 },
              { "name": "compassHeading", "value": 0 }
            ]
          }

class accelerometerCompass6AxisSensor:

   def __init__(self):
      print("Initialising 6 axis accelerometer and compass sensor")

      try:
        print("Initialising LSM303D...")
        self.acc_mag = lsm303d.lsm303d()
        self.initOK = 1

      except:
        print("FAILED TO INITIALISE")
        self.initOK = 0


   def __del__(self):
      print("destructor for 6 axis accelerometer and compass sensor")

   def getValues(self):
      print("getting 6 axis accelerometer and compass values...")

      if self.initOK == 0:
        print("Sensor failed to inialise, returning...")
        return
      
#      try:

      # Get accelerometer values
      acc = self.acc_mag.getRealAccel()

      # Check for compass being ready
      if acc_mag.isMagReady():

        print("Compass is ready");

        # Read the heading
        heading = acc_mag.getHeading()

      else:

        print("Compass is NOT ready");

        heading = 360;


      print("Acceleration of X,Y,Z is %.3fg, %.3fg, %.3fg" %(acc[0], acc[1], acc[2]))
      print("Heading %.3f degrees\n" %(heading))

      sensors['sensors'][0]['value'] = int(1000 * acc[0])
      sensors['sensors'][1]['value'] = int(1000 * acc[1])
      sensors['sensors'][2]['value'] = int(1000 * acc[2])
      sensors['sensors'][3]['value'] = int(heading)

#      except IOError:
#        print ("Error")

      return sensors

