from repository.database import get_db_connection


def create_player_season_stats_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS player_season_stats (
        id INTEGER PRIMARY KEY, 
        player_name VARCHAR(50) NOT NULL,
        position VARCHAR(10),
        age INTEGER,
        games INTEGER,
        games_started INTEGER,
        minutes_per_game FLOAT,
        field_goals INTEGER,
        field_attempts INTEGER,
        field_percent FLOAT,
        three_fg INTEGER,
        three_attempts INTEGER,
        three_percent FLOAT,
        two_fg INTEGER,
        two_attempts INTEGER,
        two_percent FLOAT,
        effective_fg_percent FLOAT,
        free_throws INTEGER,
        free_throw_attempts INTEGER,
        free_throw_percent FLOAT,
        offensive_rebounds INTEGER,
        defensive_rebounds INTEGER,
        total_rebounds INTEGER,
        assists INTEGER,
        steals INTEGER,
        blocks INTEGER,
        turnovers INTEGER,
        personal_fouls INTEGER,
        points INTEGER,
        team VARCHAR(10),
        season INTEGER NOT NULL,
        player_id VARCHAR(20) NOT NULL
    )
    """)

    conn.commit()
    cur.close()
