from model.Player import Player
from repository.database import get_db_connection


def create_player_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS player (
    playerId varchar(20) PRIMARY KEY NOT NULL,
    playerName VARCHAR(50) NOT NULL
    )
    """)
    conn.commit()
    cur.close()


def create_player(player: Player):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO player (playerId, playerName)
                VALUES ( %(playerId)s, %(playerName)s)
                ON CONFLICT (playerId) DO NOTHING
                RETURNING * 
                """, {'playerName': player.playerName,
                      'playerId': player.playerId})
            cursor.fetchone()
            connection.commit()
