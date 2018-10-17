import sys
import time
from threading import Timer
import math
import grovepi
import lsm303d

sensors = { 'accelerometerCompass6AxisSensor':
            [
              { "name": "accelerometerX", "value": 999 },
              { "name": "accelerometerY", "value": 999 },
              { "name": "accelerometerZ", "value": 999 },
              { "name": "compassHeading", "value": 999 }
            ]
          }

sensors3 = { "accelerometerCompass6AxisSensor.accelerometerX": 999,
             "accelerometerCompass6AxisSensor.accelerometerY": 999,
             "accelerometerCompass6AxisSensor.accelerometerZ": 999,
             "accelerometerCompass6AxisSensor.compassHeading": 999 } 

class accelerometerCompass6AxisSensor:

   def __init__(self):
      print "Initialising 6 axis accelerometer and compass sensor"

      try:
        print "Initialising LSM303D..."
        self.acc_mag = lsm303d.lsm303d()
        self.initOK = 1

      except:
        print "FAILED TO INITIALISE"
        self.initOK = 0


   def __del__(self):
      print "destructor for 6 axis accelerometer and compass sensor"

   def getValue(self):
      print "getting 6 axis accelerometer and compass values..."

      if self.initOK == 0:
        print "Sensor failed to inialise, returning..."
        return sensors
      
#      try:

      # Get accelerometer values
      acc = self.acc_mag.getRealAccel()

      # Check for compass being ready
      if self.acc_mag.isMagReady():

        print "Compass is ready"

        # Read the heading
        heading = self.acc_mag.getHeading()

      else:

        print "Compass is NOT ready"

        heading = 360;


      print "Acceleration of X,Y,Z is %.3fg, %.3fg, %.3fg" %(acc[0], acc[1], acc[2])
      print "Heading %.3f degrees\n" %(heading)

      sensors['accelerometerCompass6AxisSensor'][0]['value'] = int(1000 * acc[0])
      sensors['accelerometerCompass6AxisSensor'][1]['value'] = int(1000 * acc[1])
      sensors['accelerometerCompass6AxisSensor'][2]['value'] = int(1000 * acc[2])
      sensors['accelerometerCompass6AxisSensor'][3]['value'] = int(heading)

#      except IOError:
#        print "Error"

      return sensors

   def getValue3(self):
      print "getting 6 axis accelerometer and compass values v3..."

      if self.initOK == 0:
        print "Sensor failed to inialise, returning..."
        return sensors3
      
#      try:

      # Get accelerometer values
      acc = self.acc_mag.getRealAccel()

      # Check for compass being ready
      if self.acc_mag.isMagReady():

        print "Compass is ready"

        # Read the heading
        heading = self.acc_mag.getHeading()

      else:

        print "Compass is NOT ready"

        heading = 360;


      print "Acceleration of X,Y,Z is %.3fg, %.3fg, %.3fg" %(acc[0], acc[1], acc[2])
      print "Heading %.3f degrees\n" %(heading)

      sensors3["accelerometerCompass6AxisSensor.accelerometerX"] = int(1000 * acc[0])
      sensors3["accelerometerCompass6AxisSensor.accelerometerY"] = int(1000 * acc[1])
      sensors3["accelerometerCompass6AxisSensor.accelerometerZ"] = int(1000 * acc[2])
      sensors3["accelerometerCompass6AxisSensor.compassHeading"] = int(heading)

#      except IOError:
#        print ("Error")

      return sensors3

