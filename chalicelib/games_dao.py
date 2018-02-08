import boto3
import json
import os

dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
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
    if 'Item' in response:
        return response['Item']
    else:
        return None
    
def delete_game_by_id(id):
    response = table.delete_item(
        Key={
            'name': id
        },
        ReturnValues = 'ALL_OLD'
    )
    if 'Attributes' in response and 'name' in response['Attributes']:
        return True
    else:
        return False
    #return id == response['Attributes']['name']

def create_game(game):
    db_item={
            'name': 'None',
            'display_name': 'None',
            'platforms': 'None',
            'image_url': 'None',
            'data_owner': 'None',
            'events': 'None'
        }
    if 'name' in game:
        db_item['name'] = game['name']
        if 'display_name' in game:
            db_item['display_name'] = game['display_name']
        if 'platforms' in game:
            db_item['platforms'] = game['platforms']
        if 'image_url' in game:
            db_item['image_url'] = game['image_url']
        if 'data_owner' in game:
            db_item['data_owner'] = game['data_owner']
        if 'events' in game:
            db_item['events'] = game['events']
    else:
        return None
        
    table.put_item(
        Item=db_item
    )
    return game

def update_game(game):
    db_item={
        'display_name': 'None',
        'platforms': 'None',
        'image_url': 'None',
        'data_owner': 'None',
        'events': 'None'
    }
    if 'name' in game:
        if 'display_name' in game:
            db_item['display_name'] = game['display_name']
        if 'platforms' in game:
            db_item['platforms'] = game['platforms']
        if 'image_url' in game:
            db_item['image_url'] = game['image_url']
        if 'data_owner' in game:
            db_item['data_owner'] = game['data_owner']
        if 'events' in game:
            db_item['events'] = game['events']
    else:
        return None
        
    response = table.update_item(
        Key={
            'name': game['name']
        },
        UpdateExpression="set display_name = :d, platforms = :p, image_url= :i, data_owner= :o, events= :e",
        ExpressionAttributeValues= {
            ':d': db_item['display_name'],
            ':p': db_item['platforms'],
            ':i': db_item['image_url'],
            ':o': db_item['data_owner'],
            ':e': db_item['events'],
        },
    ReturnValues="UPDATED_NEW"
    )
    return response['Attributes']