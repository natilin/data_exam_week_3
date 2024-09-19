from model.PlayerSeasonStats import PlayerSeasonStats


def json_to_model(json):
    return PlayerSeasonStats(**json)
