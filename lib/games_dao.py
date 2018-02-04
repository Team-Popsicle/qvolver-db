import boto3
import json
import os

dynamodb = boto3.resource('dynamodb', region_name='us-west-1', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Games')

def get_all_games():
    response = table.scan()
    games = []
    for game in response['Items']:
        games.append(game)

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        for game in response['Items']:
            games.append(game)
    return games

def get_game_by_id(id):
    return 'returns a game dict'

def delete_game_by_id(id):
    return 'true or false depending on success'

def create_game(game):
    response = table.put_item(
        Item={
            'name': game['name'],
            'display_name': game['display_name'],
            'platforms': game['platforms'],
            'image_url': game['image_url'],
            'data_owner': game['data_owner'],
            'events': game['events']
        },
        ReturnValues = 'ALL_NEW'
    )
    return response

def update_game(game):
    response = table.put_item(
        Item={
            'name': game['name'],
            'display_name': game['display_name'],
            'platforms': game['platforms'],
            'image_url': game['image_url'],
            'data_owner': game['data_owner'],
            'events': game['events']
        },
        ReturnValues = 'ALL_NEW'
    )

    return response
