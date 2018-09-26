
# Import the SDK
import boto3
import json
import decimal

class awsDynamoDBHelper:

   def __init__(self):
      print("Initialising AWS DynamoDB helper")
#      self.dynamoDBClient = boto3.client('dynamodb')
      self.dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')
      self.labelTable = self.dynamoDB.Table('LabelTable')

   def __del__(self):
      print("Destructor for AWS DynamoDB helper")


   def putLabelItem(self, datetime, itemList):

      print('Putting item into into LabelTable')

      self.response = self.labelTable.put_item(
        Item={
          'datetime': datetime,
          'itemList': itemList
        }
      )

      return self.response;

