from dataclasses import dataclass


@dataclass
class Fantasy_team:
    team_name: str
    PG_player: str
    SG_player: str
    SF_player: str
    PF_player: str
    C_player: str
    team_id: int = None
