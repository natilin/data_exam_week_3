from repository.database import get_db_connection


def create_fantasy_team_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fantasy_team (
    player_id varchar(20) PRIMARY KEY NOT NULL,
    player_name VARCHAR(50) NOT NULL
    )
    """)
    conn.commit()
    cur.close()
