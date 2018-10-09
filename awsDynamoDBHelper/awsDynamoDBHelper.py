
# Import the SDK
import boto3
import json
import decimal
from botocore.exceptions import ClientError

class awsDynamoDBHelper:

   def __init__(self, tableName):
      print("Initialising AWS DynamoDB helper for table ", tableName)
#      self.dynamoDBClient = boto3.client('dynamodb')
      self.dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')
      self.tableName = tableName
      self.table = self.dynamoDB.Table(self.tableName)

   def __del__(self):
      print("Destructor for AWS DynamoDB helper for table ", self.tableName)


   def putItem(self, recorddatetime, itemList):

      print('Putting item into into table ', self.tableName)

      self.response = ""

      try:
        self.response = self.table.put_item(
          Item={
            'recorddatetime': recorddatetime,
            'itemList': itemList
          }
        )

      except Exception as e:
        print("put_item failed")
        print(e)

      else:
        print("put_item succeeded")

      print(self.response)

      return self.response;

