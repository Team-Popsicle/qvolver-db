#!/usr/bin/env python
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-1', endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='Games',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'platform',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'platform',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)