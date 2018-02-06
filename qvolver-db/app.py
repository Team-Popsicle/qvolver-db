from chalice import Chalice
from chalice import NotFoundError

app = Chalice(app_name='qvolver-db')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/game', methods=['GET', 'POST'])
def game():
    raise NotFoundError('Endpoint Not Implemented. Yet.')

@app.route('/game/{id}', methods=['GET', 'POST', 'DELETE'])
def get_or_update_game(id):
    raise NotFoundError('Endpoint Not Implemented. Yet.')


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
