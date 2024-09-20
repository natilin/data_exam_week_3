from repository.playerSeasonStats_repository import get_players_by_pos_and_season, get_players_by_pos, \
    get_sum_player_assist, get_sum_player_turnovers
from service.player_season_stats_service import get_all_stats


def test_get_all_stats():
    stats_list = get_all_stats()
    assert stats_list


def test_get_players_by_pos_and_season():
    stats_list = get_players_by_pos_and_season("PG", 2023)
    assert stats_list


def test_get_players_by_pos():
    stats_list = get_players_by_pos("PG")
    assert stats_list


def test_get_sum_player_assist():
    sum_player = get_sum_player_assist("robinor01")
    assert sum_player


def test_get_sum_player_turnovers():
    sum_player = get_sum_player_turnovers("robinor01")
    assert sum_player
