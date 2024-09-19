from dataclasses import dataclass


@dataclass
class Player_fantasy_team:
    team_id: int
    PG_player: str
    SG_player: str
    SF_player: str
    PF_player: str
    C_player: str
