from dataclasses import dataclass
from typing import List


@dataclass
class Player_DTO:
    playerName: str
    team: str
    position: str
    season: int
    point: int
    games: int
    twoPercen: float
    threePercent: float
    ATR: float
    PPGRatio: float
