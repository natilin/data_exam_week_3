import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URL


def get_db_connection():
    return psycopg2.connect(SQL_URL, cursor_factory=RealDictCursor)
