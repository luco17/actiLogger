'''
Connect to Dynamo and create the table object for export
'''

import os
import boto3

TABLE=os.environ.get('TABLE')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)

print(table.key_schema)
