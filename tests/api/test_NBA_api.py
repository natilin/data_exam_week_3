import pytest

from api.NBA_api import get_player_season_stats


# @pytest.fixture(scope="module")
# def get_list():
#     return [9, 8]



def test_get_player_season_stats():
    players_stats_2024 = get_player_season_stats(2024)
    assert players_stats_2024
