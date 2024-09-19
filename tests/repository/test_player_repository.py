from repository.player_repository import get_all_players


def test_get_all_players():
    players_list = get_all_players()
    assert players_list


