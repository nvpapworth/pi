import sys
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/awsDynamoDBHelper')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/displays')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/gps')

from camera import camera
from awsS3Helper import awsS3Helper
from awsRekognitionHelper import awsRekognitionHelper
from awsDynamoDBHelper import awsDynamoDBHelper
from sensors.sensors import sensors
from displays.fourDigitDisplay import fourDigitDisplay
from gps.usbGps import usbGps

import time
import json
import datetime

import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


imageFileDateFormat = "%Y%m%d%H%M%S.%f"
rootDirectory       = "/home/pi/Neil/project/"

gpsTableName  = "GpsTable"

print "Running..."

#my4dd = fourDigitDisplay(fddDigitalPort)

#my4dd.setOn()
#my4dd.setSegment(0, 49)
#my4dd.setSegment(1, 121)
#my4dd.setSegment(2, 119)
#my4dd.setSegment(3, 94)

now = datetime.datetime.now()
print "datetime = ", now
dateTime = now.strftime(imageFileDateFormat)

print("Initialising AWS DynamoDB for GpsTable...")
myAwsDDb_gps = awsDynamoDBHelper.awsDynamoDBHelper(gpsTableName)

print "main - initializing USB GPS"

usbPort = "/dev/ttyUSB0"
baud = 4800
timeout = 0

myGps = usbGps(usbPort, baud, timeout)

print("sleeping 1...")
time.sleep(1)

print "reading GPS"

gps_data = myGps.read()

if gps_data != []:

#  print (json.dumps(gps_data))
  print (gps_data)

  ddbKey = dateTime[0:14]
  print "ddbKey = ", ddbKey

  gps_data["recorddatetime"] = ddbKey

  dbRecord = gps_data
#  print "dbRecord = " + json.dumps(dbRecord)
  print "dbRecord = ", dbRecord

  response = myAwsDDb_gps.putItemRaw(ddbKey, gps_data);

#  print response

#  print(json.dumps(response, indent=4, cls=DecimalEncoder))

#my4dd.setOff()

print("exiting...")
