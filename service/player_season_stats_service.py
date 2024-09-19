from model.PlayerSeasonStats import PlayerSeasonStats
from repository import playerSeasonStats_repository


def json_to_model(json):
    return PlayerSeasonStats(
        id=json["id"],
        player_id=json["playerId"],
        player_name=json["playerName"],
        position=json["position"],
        age=json["age"],
        games=json["games"],
        field_goals=json["fieldGoals"],
        field_attempts=json["fieldAttempts"],
        field_percent=json["fieldPercent"],
        three_percent=json["threePercent"],
        two_percent=json["twoPercent"],
        assists=json["assists"],
        turnovers=json["turnovers"],
        points=json["points"],
        team=json["team"],
        season=json["season"]
    )




def create_player_season_stats_table():
    playerSeasonStats_repository.create_table()


def create_player_season_stats():
    player = playerSeasonStats_repository.create_player_season_stats()
    return PlayerSeasonStats(**player)


def get_all_stats():
    stats_list = playerSeasonStats_repository.get_all_stats()
    return [PlayerSeasonStats(**stats) for stats in stats_list]


