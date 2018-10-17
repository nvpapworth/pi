import sys
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/camera')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/awsS3Helper')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/awsRekognitionHelper')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/awsDynamoDBHelper')
sys.path.insert(0, sys.path[0]+'/home/pi/Neil/project/sensors')

from camera import camera
from awsS3Helper import awsS3Helper
from awsRekognitionHelper import awsRekognitionHelper
from awsDynamoDBHelper import awsDynamoDBHelper
from sensors.sensors import sensors

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
sensorTableName = "SensorTable2"


print "Running..."

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


print("exiting...")

