#!/usr/bin/env python
import boto3

# if we import os we can use os.environ('ENDPOINT_URL') to access dynamoDB
# this endpoint url may need to change based on your dev setup
dynamodb = boto3.resource('dynamodb', region_name='us-west-1', endpoint_url="http://192.168.99.100:8000")


table = dynamodb.create_table(
    TableName='Games',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print("Table status:", table.table_status)