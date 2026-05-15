import os
import pytest
from db_connection import get_connection
from utils import read_sql_file


@pytest.fixture(scope="module")
def db_connection():
    required_vars = ["DB_SERVER", "DB_NAME", "DB_USER", "DB_PASSWORD"]
    if not all(os.getenv(name) for name in required_vars):
        pytest.skip("Skipping Provider Rad Roster tests because DB credentials are not configured.")
    return get_connection()


def _run_count_query(cursor, sql_path):
    query = read_sql_file(sql_path)
    cursor.execute(query)
    return cursor.fetchone()[0]


def test_person_first_name_not_null(db_connection):
    cursor = db_connection.cursor()
    count = _run_count_query(cursor, "sql/null_check_person_first_name.sql")
    assert count == 0, f"Found {count} rows with NULL or empty person_first_name"


def test_person_last_name_not_null(db_connection):
    cursor = db_connection.cursor()
    count = _run_count_query(cursor, "sql/null_check_person_last_name.sql")
    assert count == 0, f"Found {count} rows with NULL or empty person_last_name"


def test_npi_not_null(db_connection):
    cursor = db_connection.cursor()
    count = _run_count_query(cursor, "sql/null_check_npi.sql")
    assert count == 0, f"Found {count} rows with NULL or empty NPI"


def test_no_duplicate_npi(db_connection):
    cursor = db_connection.cursor()
    count = _run_count_query(cursor, "sql/duplicate_check_npi.sql")
    assert count == 0, f"Found {count} duplicate NPI values"


def test_hire_date_not_greater_than_termination_date(db_connection):
    cursor = db_connection.cursor()
    count = _run_count_query(cursor, "sql/date_range_check_hire_termination.sql")
    assert count == 0, f"Found {count} rows where hire_date is greater than termination_date"


def test_fte_percentage_in_range(db_connection):
    cursor = db_connection.cursor()
    count = _run_count_query(cursor, "sql/fte_percentage_check.sql")
    assert count == 0, f"Found {count} rows with invalid FTE percentage"


def test_local_practice_name_not_null(db_connection):
    cursor = db_connection.cursor()
    count = _run_count_query(cursor, "sql/null_check_local_practice_name.sql")
    assert count == 0, f"Found {count} rows with NULL or empty local_practice_name"
