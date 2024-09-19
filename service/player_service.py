from model.Player import Player


def json_to_model(json):
    return Player(**json)

