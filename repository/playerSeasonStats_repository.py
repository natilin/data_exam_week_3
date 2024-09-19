from model.PlayerSeasonStats import PlayerSeasonStats
from repository.database import get_db_connection


def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS player_season_stats (
        id  int PRIMARY KEY,
        player_name VARCHAR(100),
        player_id varchar(20),
        position VARCHAR(50),
        age INT,
        games INT,
        field_goals INT,
        field_attempts INT,
        field_percent FLOAT,
        three_percent FLOAT,
        two_percent FLOAT,
        assists INT,
        turnovers INT,
        points INT,
        team VARCHAR(10),
        season INT
                )

    """)

    conn.commit()
    cur.close()


def create_player_season_stats(player: PlayerSeasonStats):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO player_season_stats ( id,
                player_name, player_id, position, age, games, field_goals, field_attempts, field_percent, 
                three_percent, two_percent, assists, turnovers, points, team, season
            ) 

                 VALUES (%s,%s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
                RETURNING * 
            """, (
                player.id, player.player_name, player.player_id, player.position, player.age, player.games, player.field_goals,
                player.field_attempts, player.field_percent, player.three_percent, player.two_percent,
                player.assists, player.turnovers, player.points, player.team, player.season))
            res = cursor.fetchone()
            connection.commit()

    return res


def get_all_stats():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM player_season_stats         
                """)
            res = cursor.fetchall()

    return res


def get_players_by_pos_and_season(pos, season):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT DISTINCT ON (player_id) * FROM player_season_stats 
                where season = %s and position LIKE %s      
                """, (season, f"%{pos}%",))
            res = cursor.fetchall()

    return res


def get_players_by_pos(pos):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT DISTINCT ON (player_id) * FROM player_season_stats 
                where position LIKE %s      
                """, (f"%{pos}%",))
            res = cursor.fetchall()

    return res
