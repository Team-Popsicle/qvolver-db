import players_dao

def lambda_handler(event, context):
    body_load = ''
    call_status = 400
    player_id = None
    
    operation = event['httpMethod']
    if event['pathParameters'] is not None:
        player_id = event['pathParameters']['id']

    if operation == 'GET':
        if player_id is not None:
            body_load = get_player_by_id(game_id)
        else:
            body_load = get_all_players()
        call_status = 200
        
    elif operation == 'DELETE':
        if player_id is not None:
            delete_status = delete_player_by_id(game_id)
            if delete_status:
                body_load = 'Successful Deletion'
            else:
                body_load = 'Game Delete Failed'
        else:
            body_load = 'Sorry, you can\'t delete everything at once'
        call_status = 200
    elif operation == 'POST':
        if event['body'] is not None:
            body_load = create_player(event['body'])
            call_status = 200
        else:
            call_status = 400
            body_load = 'Are you a floating skull? You need a body fool!'
    elif operation == 'PATCH':
        if event['body'] is not None:
            body_load = update_player(event['body'])
            call_status = 200
        else:
            call_status = 400
            body_load = 'Are you a floating skull? You need a body fool!'
    else:
        call_status = 400
        body_load = 'Sorry, the operation is not supported'
        
    return_object = {
        "statusCode": call_status,
        "body": body_load
    }

    return return_object
