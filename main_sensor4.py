import sys
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/camera')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/awsS3Helper')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/awsRekognitionHelper')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/awsDynamoDBHelper')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/sensors')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/displays')

from camera import camera
from awsS3Helper import awsS3Helper
from awsRekognitionHelper import awsRekognitionHelper
from awsDynamoDBHelper import awsDynamoDBHelper
from sensors.sensors import sensors
from displays.fourDigitDisplay import fourDigitDisplay

import time
import json
import datetime

imageFileDateFormat = "%Y%m%d%H%M%S.%f"
rootDirectory       = "/home/pi/Neil/project/"
imageDirectory      = rootDirectory + "images/"
videoDirectory      = rootDirectory + "video/"

s3BucketName = "neil2-pi-bucket"
s3BucketPrefix = "images/"
labelConfidence = 40

labelTableName  = "LabelTable"
sensorTableName = "SensorTable"

#
# r = 16 + 32 + 1 = 49
# E = 32 + 16 + 8 + 64 + 1 = 121
# e = 64 + 2 + 1 + 32 + 16 + 8 = 123
# A = 16 + 32 + 1 + 2 + 4 + 64 = 119
# d = 64 + 16 + 8 + 4 + 2 = 94
#

fddDigitalPort = 8

print "Running..."

my4dd = fourDigitDisplay(fddDigitalPort)

my4dd.setOn()
my4dd.setSegment(0, 49)
my4dd.setSegment(1, 121)
my4dd.setSegment(2, 119)
my4dd.setSegment(3, 94)

now = datetime.datetime.now()
print "datetime = ", now
dateTime = now.strftime(imageFileDateFormat)

#print "Initialising AWS S3..."
#myAwsS3 = awsS3Helper.awsS3Helper()

print("Initialising AWS DynamoDB for SensorTable...")
myAwsDDb_sensor = awsDynamoDBHelper.awsDynamoDBHelper(sensorTableName)


print "main - initializing sensors"

mySensors = sensors()
mySensors.initializeSensors()

print("sleeping 2...")
#time.sleep(2)

print "reading sensors"

sensorValues = mySensors.getValues3()
#sensorValues = mySensors.getValues3Old()

print "sensorValues = ", sensorValues
print "str sensorValues = ", str(sensorValues)

ddbKey = dateTime[0:14]
print "ddbKey = ", ddbKey

sensorValues["recorddatetime"] =  ddbKey
dbRecord = sensorValues
print "dbRecord = " + json.dumps(dbRecord)


#myAwsDDb_sensor.putItem(ddbKey, dbRecord);
#myAwsDDb_sensor.putItemNamed(ddbKey, 'sensors', sensorValues);
myAwsDDb_sensor.putItemRaw(ddbKey, sensorValues);

my4dd.setOff()


print("exiting...")

