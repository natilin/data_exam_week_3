from model.Fantasy_team import Fantasy_team
from repository import fantasy_team_repository
from toolz import pipe


def from_json_to_fantasy_team(json):
    return Fantasy_team(
        team_name=json["team_name"],
        PF_player=json["PF_player"],
        PG_player=json["PG_player"],
        SG_player=json["SG_player"],
        C_player=json["C_player"],
        SF_player=json["SF_player"]
    )


def create_fantasy_team(json):
    return pipe(
        json,
        from_json_to_fantasy_team,
        fantasy_team_repository.create_fantasy_team
    )
