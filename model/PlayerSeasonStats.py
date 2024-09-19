from dataclasses import dataclass


@dataclass
class PlayerSeasonStats:
    id: int
    player_name: str
    position: str
    age: int
    games: int
    games_started: int
    minutes_per_game: float
    field_goals: int
    field_attempts: int
    field_percent: float
    three_fg: int
    three_attempts: int
    three_percent: float
    two_fg: int
    two_attempts: int
    two_percent: float
    effective_fg_percent: float
    free_throws: int
    free_throw_attempts: int
    free_throw_percent: float
    offensive_rebounds: int
    defensive_rebounds: int
    total_rebounds: int
    assists: int
    steals: int
    blocks: int
    turnovers: int
    personal_fouls: int
    points: int
    team: str
    season: int
    player_id: str
