from service.player_dto_service import calculate_ppg_ratio, calculate_atr, get_players_by_pos_and_season_to_dto


def test_calculate_ppg_ratio():
    ppg = calculate_ppg_ratio("lawsoaj01", 2022)
    assert ppg


def test_calculate_atr():
    atr = calculate_atr("lawsoaj01")
    assert atr


def test_get_players_by_pos_and_season_to_dto():
    lst = get_players_by_pos_and_season_to_dto("PG", 2022)
    assert lst
