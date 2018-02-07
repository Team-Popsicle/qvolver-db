from chalice import Chalice, Response
from chalice import NotFoundError, BadRequestError
from chalicelib import games_dao

app = Chalice(app_name='qvolver-db')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/game', methods=['GET', 'POST'])
def game():
    request = app.current_request
    response = None
    if request.method == 'GET':
        response = games_dao.get_all_games()
        if response == None:
            raise NotFoundError('No games found')
    elif request.method == 'POST':
        new_game = request.json_body
        response = games_dao.create_game(new_game)
        if response == None:
            raise BadRequestError('Bad data submitted')
        else:
            # we use a 201 because this path creates a new item
            return Response(body=response, status_code=201)
    return Response(body=response)

@app.route('/game/{id}', methods=['GET', 'PUT', 'DELETE'])
def get_or_update_game(id):
    request = app.current_request
    response = None
    if request.method == 'GET':
        response = games_dao.get_game_by_id(id)
        if response == None:
            raise NotFoundError(f'Cannot find game for {id}')
    if request.method == 'PUT':
        game_for_edit = request.json_body
        response = games_dao.update_game(game_for_edit)
        if response == None:
            raise BadRequestError(f'Could not edit game {game_for_edit}')
    if request.method == 'DELETE':
        response = games_dao.delete_game_by_id(id)
    return Response(body=response)
