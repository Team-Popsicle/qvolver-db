from context import lib
from lib import games_dao as games_dao

game = {
    'name': 'Test-Game',
    'display_name': 'Test Game',
    'platforms': ['PC'],
    'image_url': 'image.jpg',
    'data_owner': 'test',
    'events': []
}
create_game_result = games_dao.create_game(game)
print(create_game_result)
games = games_dao.get_all_games()
print(games)
games = games_dao.get_game_by_id(game['name'])
print(games)
result = games_dao.delete_game_by_id(game['name'])
print(result)
