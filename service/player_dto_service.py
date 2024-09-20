from functools import partial

from model.PlayerSeasonStats import PlayerSeasonStats
from model.Player_DTO import Player_DTO
from repository import playerSeasonStats_repository
from service.player_season_stats_service import get_player_stats_by_id, get_players_by_pos_and_season, \
    get_players_by_pos
import statistics
from toolz import pipe


def calculate_ppg_ratio(player_id, season):
    player_stats = get_player_stats_by_id(player_id)
    player_average = player_stats.points / player_stats.games

    all_players_average = pipe(
        get_players_by_pos_and_season(player_stats.position, season),
        partial(map, lambda p: p.points / p.games),
        statistics.mean
    )
    return player_average / all_players_average


def calculate_atr(player_id):
    assist = playerSeasonStats_repository.get_sum_player_assist(player_id)
    turnovers = playerSeasonStats_repository.get_sum_player_turnovers(player_id)
    return assist / turnovers if turnovers > 0 else assist


def from_playerSeasonStats_to_dto(player: PlayerSeasonStats):
    return Player_DTO(
        playerName=player.player_name,
        team=player.team,
        position=player.position,
        season=player.season,
        point=player.points,
        games=player.games,
        twoPercen=player.two_percent,
        threePercent=player.three_percent,
        ATR=calculate_atr(player.player_id),
        PPGRatio=calculate_ppg_ratio(player.player_id, player.season)
    )

def get_players_by_pos_and_season_to_dto(pos, season):
    return pipe(
        get_players_by_pos_and_season(pos, season),
        partial(map, lambda x: from_playerSeasonStats_to_dto(x)),
        list
    )

def get_players_by_pos_ato_dto(pos):
    return pipe(
        get_players_by_pos(pos),
        partial(map, lambda x: from_playerSeasonStats_to_dto(x)),
        list
    )
