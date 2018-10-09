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
from sensors import barometricSensor

import time
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


print "Running..."

now = datetime.datetime.now()
print "datetime = ", now

print "Initialising camera..."
myCamera = camera.camera()

print "Initialising AWS S3..."
myAwsS3 = awsS3Helper.awsS3Helper()

print("Initialising AWS Rekognition...")
myAwsRek = awsRekognitionHelper.awsRekognitionHelper()

print("Initialising AWS DynamoDB for LabelTable...")
myAwsDDb_label = awsDynamoDBHelper.awsDynamoDBHelper(labelTableName)

print("Initialising AWS DynamoDB for SensorTable...")
myAwsDDb_sensor = awsDynamoDBHelper.awsDynamoDBHelper(sensorTableName)

/*
print "Sleeping 2..."
#time.sleep(2)

print "Taking picture with current date/time..."
now = datetime.datetime.now()
dateTime = now.strftime(imageFileDateFormat)
pictureFilename = "image-" + dateTime + ".jpg"
pictureLocation = imageDirectory + pictureFilename
objectKey2 = s3BucketPrefix + pictureFilename
objectKey = s3BucketPrefix + dateTime[0:4] + "/" + dateTime[4:6] + "/" + dateTime[6:8] + "/" + dateTime[8:10] + "/" + pictureFilename

print "pictureFilename = ", pictureFilename
print "pictureLocation = ", pictureLocation
print "objectKey       = ", objectKey
print "objectKey2      = ", objectKey2

#filename = ""
#filename = myCamera.takePictureFileCurrentDateTime()



myCamera.takePictureFile(pictureLocation)

print "Uploading file ", pictureFilename, " to S3 bucket ", s3BucketName, " from location ", pictureLocation, " objectKey = ", objectKey
#myAwsS3.uploadFileToBucket(s3BucketName, filename)
myAwsS3.uploadFileToBucket2(s3BucketName, pictureLocation, objectKey)
print "S3 Upload complete..."

#objectKey = "images/test3.jpg"

print "Getting Rekognition labels for file/object ", objectKey, " in S3 bucket ", s3BucketName
response = myAwsRek.detectLabels(s3BucketName, objectKey, labelConfidence)
print "Rotation :", response['OrientationCorrection']
print "Got the following labels :"
for label in response['Labels']:
  print (label['Name'] + ' : ' + str(label['Confidence']))

for label in response['Labels']:
  label['Confidence'] = int(label['Confidence'])

ddbKey = dateTime[0:14]
print "ddbKey = ", ddbKey

myAwsDDb_label.putItem(ddbKey, response['Labels']);





#print "Getting Rekognition text for file/object ", objectKey, " in S3 bucket ", s3BucketName
#response = myAwsRek.detectText(s3BucketName, objectKey)
#for label in response['TextDetections']:
#  print (label['DetectedText'] + ' : ' + str(label['Confidence']))

#print "Getting Rekognition faces for file/object ", objectKey, " in S3 bucket ", s3BucketName
#response = myAwsRek.detectFaces(s3BucketName, objectKey)
#print('Detected faces for ' + objectKey)
#for label in response['FaceDetails']:
#  print (label['Gender']['Value'], "Range",label['AgeRange']['Low'],"-",label['AgeRange']['High'], "Smile:", label['Smile']['Value'], label['Smile']['Confidence'])

#print "Getting Rekognition celebrity recognition for file/object ", objectKey, " in S3 bucket ", s3BucketName
#response = myAwsRek.recognizeCelebrities(s3BucketName, objectKey)
#print('Detected celebrities ' + objectKey)
#for label in response['CelebrityFaces']:
#  print (label['Name'])

*/

print "reading sensors"

print("Initialising barometric sensor...")
i2cPort = 0x77
myBarometer = barometricSensor(i2cPort)

time.sleep(2)

barometricValue = myBarometer.getValue()

print "barometricValue = " + json.dumps(barometricValue)




print("exiting...")

