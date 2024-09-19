import os

SQL_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost/nba_teams_exam')
