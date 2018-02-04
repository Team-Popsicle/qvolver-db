import games_dao

def lambda_handler(event, context):
    body_load = ''
    call_status = 400
    game_id = None
    
    operation = event['httpMethod']
    if event['pathParameters'] is not None:
        game_id = event['pathParameters']['id']

    if operation == 'GET':
        if game_id is not None:
            body_load = games_dao.get_game_by_id(game_id)
        else:
            body_load = games_dao.get_all_games()
        call_status = 200
        
    elif operation == 'DELETE':
        if game_id is not None:
            delete_status = games_dao.delete_game_by_id(game_id)
            if delete_status:
                body_load = 'Successful Deletion'
            else:
                body_load = 'Game Delete Failed'
        else:
            body_load = 'Sorry, you can\'t delete everything at once'
        call_status = 200
    elif operation == 'POST':
        if event['body'] is not None:
            body_load = games_dao.create_game(event['body'])
            call_status = 200
        else:
            call_status = 400
            body_load = 'Are you a floating skull? You need a body fool!'
    elif operation == 'PATCH':
        if event['body'] is not None:
            body_load = games_dao.update_game(event['body'])
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


