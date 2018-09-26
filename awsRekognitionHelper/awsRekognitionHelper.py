
# Import the SDK
import boto3
import uuid

class awsRekognitionHelper:

   def __init__(self):
      print("Initialising AWS Rekognition helper")
      self.rekognitionClient = boto3.client('rekognition')

   def __del__(self):
      print("Destructor for AWS Rekognition helper")


   def detectLabels(self, bucketName, objectKey, labelConfidence):

      print('Getting labels for {} with key: {} with confidence {}%'.format(bucketName, objectKey, labelConfidence))
      self.response = self.rekognitionClient.detect_labels(Image={'S3Object':{'Bucket':bucketName,'Name':objectKey}},MinConfidence=labelConfidence)

#      print('Detected labels for ' + objectKey)
#      for label in self.response['Labels']:
#          print (label['Name'] + ' : ' + str(label['Confidence']))

      return self.response;

   def detectText(self, bucketName, objectKey):

      print('Getting text for {} with key: {}'.format(bucketName, objectKey))
      self.response = self.rekognitionClient.detect_text(Image={'S3Object':{'Bucket':bucketName,'Name':objectKey}})

#      print('Detected text for ' + objectKey)
#      for label in self.response['TextDetections']:
#          print (label['DetectedText'] + ' : ' + str(label['Confidence']))

      return self.response;

   def detectFaces(self, bucketName, objectKey):

      print('Getting faces for {} with key: {}'.format(bucketName, objectKey))
      self.response = self.rekognitionClient.detect_faces(Image={'S3Object':{'Bucket':bucketName,'Name':objectKey}},Attributes=['ALL'])

#      print('Detected faces for ' + objectKey)
#      for label in self.response['FaceDetails']:
#          print (label['Gender']['Value'], "Range",label['AgeRange']['Low'],"-",label['AgeRange']['High'], "Smile:", label['Smile']['Value'], label['Smile']['Confidence'])
#          print (label['Gender'] + label['AgeRange'])
#         print (label)
#         for label2 in label:
#            print (label2)

#          print (label['Gender'])

      return self.response;

   def recognizeCelebrities(self, bucketName, objectKey):

      print('Getting celebrities for {} with key: {}'.format(bucketName, objectKey))
      self.response = self.rekognitionClient.recognize_celebrities(Image={'S3Object':{'Bucket':bucketName,'Name':objectKey}})

#      print('Detected celebrities for ' + objectKey)
#      for label in self.response['CelebrityFaces']:
#          print (label['Name'])

      return self.response;

