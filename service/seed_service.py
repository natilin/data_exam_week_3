from functools import partial, reduce

from api.NBA_api import get_players_season_stats
from repository.seed_repository import is_table_exist, is_table_filled
from repository import fantasy_team_repository, player_repository, playerSeasonStats_repository
from toolz import pipe

from service import player_season_stats_service


def initial_db():
    if not is_table_exist("player")  :
        player_repository.create_player_table()


    if not is_table_exist("player_season_stats"):
        playerSeasonStats_repository.create_player_season_stats_table()

    if not is_table_exist("fantasy_team"):
        fantasy_team_repository.create_fantasy_team_table()


def seed_player_season_stats():
    if not is_table_filled("player_season_stats"):
        players_stats = pipe(
            [2022, 2023, 2024],
            partial(reduce, lambda lst, year: lst + get_players_season_stats(year), []),
            partial(map, lambda x: player_season_stats_service.json_to_model(x)),
            list
        )
        for stats in players_stats:



