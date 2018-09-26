
# Import the SDK
import boto3
import uuid
#from ProgressPercentage import ProgressPercentage
import ProgressPercentage

# For more details on what you can do with boto3 and Amazon S3, see the API
# reference page:
# https://boto3.readthedocs.org/en/latest/reference/services/s3.html

# USING CLIENT API FIRST

class awsS3Helper:

   def __init__(self):
      print("Initialising S3 helper")
#      session = boto3.Session(profile_name='default')
#      self.s3client = session.client('s3')
#      boto3.set_stream_logger('botocore', level='DEBUG')
      self.s3client = boto3.client('s3')
      self.s3Resource = boto3.resource('s3')

   def __del__(self):
      print("destructor for S3 helper")

   def createBucket(self, bucketName):
      print("creating S3 bucket name = ", bucketName)
      self.s3client.create_bucket(Bucket=bucketName)
      list_buckets_resp = self.s3client.list_buckets()
      for self.bucket in list_buckets_resp['Buckets']:
          if self.bucket['Name'] == bucketName:
              print('(Just created) --> {} - there since {}'.format(
                  self.bucket['Name'], self.bucket['CreationDate']))
      return;

   def createBucketR(self, bucketName):
      print("creating S3 bucket name = ", bucketName)
      self.s3client.create_bucket(Bucket=bucketName)
      list_buckets_resp = self.s3client.list_buckets()
      for self.bucket in list_buckets_resp['Buckets']:
          if self.bucket['Name'] == bucketName:
              print('(Just created) --> {} - there since {}'.format(
                  self.bucket['Name'], self.bucket['CreationDate']))
      return;


   def uploadFileToBucket(self, bucketName, filename):

      objectKey = "images/" + filename
#      object_key = filename

      print('Uploading some data to {} with key: {}'.format(bucketName, objectKey))
      self.s3Resource.meta.client.upload_file(filename, bucketName, objectKey)

#      url = self.s3client.generate_presigned_url(
#          'get_object', {'Bucket': bucketName, 'Key': objectKey})
#      print('\nTry this URL in your browser to download the object:')
#      print(url)
#      return url;
      return;

   def uploadFileToBucket2(self, bucketName, filename, objectKey):

      print('Uploading some data to {} with key: {}'.format(bucketName, objectKey))
      self.s3Resource.meta.client.upload_file(filename, bucketName, objectKey)

#      url = self.s3client.generate_presigned_url(
#          'get_object', {'Bucket': bucketName, 'Key': objectKey})
#      print('\nTry this URL in your browser to download the object:')
#      print(url)
#      return url;
      return;

   def getFileFromBucket(self, bucketName, imageFilename, fileFilename):

      objectKey = "images/" + imageFilename

      print('Getting some data from {} with key: {} to file {}'.format(bucketName, objectKey, fileFilename))
      self.s3Resource.Bucket(bucketName).download_file(objectKey, fileFilename)

      return;

   def getFileFromBucketClient(self, bucketName, imageFilename, fileFilename):

      objectKey = "images/" + imageFilename

      print('Getting some data from {} with key: {} to file {}'.format(bucketName, objectKey, fileFilename))
      self.s3client.download_file(bucketName, objectKey, fileFilename)

      return;

   def getFileFromBucketClientProgress(self, bucketName, imageFilename, fileFilename):

      objectKey = "images/" + imageFilename

      print('Getting some data from {} with key: {} to file {}'.format(bucketName, objectKey, fileFilename))
      self.s3client.download_file(bucketName, objectKey, fileFilename, Callback=ProgressPercentage.ProgressPercentage(fileFilename))

      return;

   def getObjectPublicUrl(self, bucketName, filename):

      objectKey = "images/" + filename

      print('getting URL for {} with key: {}'.format(bucketName, objectKey))

      self.s3Resource.meta.client.upload_file(filename, bucketName, objectKey)

      url = self.s3client.generate_presigned_url(
          'get_object', {'Bucket': bucketName, 'Key': objectKey})
      print('\nTry this URL in your browser to download the object:')
      print(url)
      return url;

   def uploadFileToBucketDummy(self, bucketName, filename):

      object_key = filename
      print('DUMMY Uploading some data to {} with key: {}'.format(
          bucketName, filename))
      self.s3client.put_object(Bucket=bucketName, Key=filename, Body=b'Hello World!')

      url = self.s3client.generate_presigned_url(
          'get_object', {'Bucket': bucketName, 'Key': object_key})
      print('\nTry this URL in your browser to download the object:')
      print(url)
      return url;
