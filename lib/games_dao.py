import boto3
import json
import os

dynamodb = boto3.resource('dynamodb', region_name='us-west-1', endpoint_url=os.environ("DYNAMODB_URL"))
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
    response = table.get_item(
        Key={
            'name': id
        }
    )
    return response['Item']

def delete_game_by_id(id):
    response = table.delete_item(
        Key={
            'name': id
        },
        ReturnValues = 'ALL_OLD'
    )
    return id == response['Attributes']['name']

def create_game(game):
    table.put_item(
        Item={
            'name': game['name'],
            'display_name': game['display_name'],
            'platforms': game['platforms'],
            'image_url': game['image_url'],
            'data_owner': game['data_owner'],
            'events': game['events']
        }
    )
    return game

def update_game(game):
    response = table.update_item(
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
    return response['Attributes']
