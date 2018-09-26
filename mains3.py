from awsS3Helper import *
from awsRekognitionHelper import *
import time
import datetime

bucketName = "neilpis3bucket"
filename = "temp.txt"

print("running")

print("Initialising AWS S3...")
myAwsS3 = awsS3Helper()

# image_filename = "ScoutsRefuseBags.jpg"
# file_filename = "ScoutsRefuseBags-downloaded.jpg"

image_filename = "image-20171218151248-407109.jpg"
file_filename = "image-20171218151248-407109-downloaded.jpg"

print("getting file ", filename, " from S3 bucket ", bucketName, " into file 111.jpg")
# myAwsS3.getFileFromBucket(bucketName, image_filename, file_filename)
# myAwsS3.getFileFromBucketClient(bucketName, image_filename, file_filename)
myAwsS3.getFileFromBucketClientProgress(bucketName, image_filename, file_filename)

time.sleep(2)
print("exiting...")
