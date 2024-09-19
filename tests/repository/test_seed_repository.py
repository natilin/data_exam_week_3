import pytest

from repository.database import get_db_connection
from repository.seed_repository import is_table_exist


@pytest.fixture(scope="module")
def setup_database():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tests (
                    test varchar(20)
                    )
                    """)
    yield
    # tear down - happens after test finished
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("DROP TABLE tests")


def test_is_table_exist(setup_database):
    assert is_table_exist("tests")
