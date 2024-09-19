from functools import partial, reduce

from api.NBA_api import get_players_season_stats
from model.Player import Player
from repository.playerSeasonStats_repository import create_player_season_stats
from repository.seed_repository import is_table_exist, is_table_filled
from repository import fantasy_team_repository, player_repository, playerSeasonStats_repository
from toolz import pipe

from service import player_season_stats_service, player_service


def initial_db():
    if not is_table_exist("player"):
        player_repository.create_player_table()

    if not is_table_exist("player_season_stats"):
        player_season_stats_service.create_player_season_stats_table()

    if not is_table_exist("fantasy_team"):
        fantasy_team_repository.create_fantasy_team_table()



def season_reduce(lst, year: int):
    return lst + get_players_season_stats(year)


def seed_player_season_stats():
    if not is_table_filled("player_season_stats"):
        players_stats = pipe(
            [2022, 2023, 2024],
            lambda li: reduce(season_reduce, li, []),
            partial(map, lambda x: player_season_stats_service.json_to_model(x)),
            list
        )
        print("finish to convert to models")
        for stats in players_stats:
            create_player_season_stats(stats)
        print("finish to upload database")


def seed_players():
    if not is_table_filled("player"):
        players_list = pipe(
            player_season_stats_service.get_all_stats(),
            partial(map, lambda p: Player(p.player_id, p.player_name)),
            list
        )
        for player in players_list:
            player_repository.create_player(player)


def seed_db():
    initial_db()
    seed_player_season_stats()
    seed_players()


