import boto3
import json
import os

dynamodb = boto3.resource('dynamodb', region_name='us-west-1', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Games')

def lambda_handler(event, context):
    return 'Hello World'

# TODO finish implementation
def get_all_games():
    response = table.scan()
    games = []
    for game in response['Items']:
        games.append(game)

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        for game in response['Items']:
            games.append(game)