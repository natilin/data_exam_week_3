from model.Fantasy_team import Fantasy_team
from repository.database import get_db_connection


def create_fantasy_team_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fantasy_team (
    team_id SERIAL PRIMARY KEY NOT NULL,
    team_name varchar(50) NOT NULL,
    PG_player VARCHAR(10) NOT NULL,
    SG_player VARCHAR(10) NOT NULL,
    SF_player VARCHAR(10) NOT NULL,
    PF_player VARCHAR(10) NOT NULL,
    C_player VARCHAR(10) NOT NULL 
    )
    """)
    conn.commit()
    cur.close()


def create_fantasy_team(team: Fantasy_team):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fantasy_team (team_name, PG_player, SG_player, SF_player, PF_player, C_player)
                VALUES ( %s, %s, %s, %s, %s, %s)
                RETURNING * 
                """, (team.team_name, team.PG_player, team.SG_player, team.SF_player,
                      team.PF_player, team.C_player))
            res = cursor.fetchone()
            connection.commit()
    return res


def get_fantasy_team_by_id(team_id):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT * FROM player_season_stats 
                where player_id = %s   
                """, (team_id,))
            res = cursor.fetchone()

    return res
