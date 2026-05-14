
import os
import pytest
from db_connection import get_connection
from utils import read_sql_file
 

@pytest.fixture(scope="module")
def db_connection():
    if not os.getenv("DB_SERVER") or not os.getenv("DB_NAME"):
        pytest.skip("Skipping row count test because database credentials are not configured.")
    return get_connection()
 

def test_row_count(db_connection):
    cursor = db_connection.cursor()
 
    source_query = read_sql_file("sql/source_count.sql")
    target_query = read_sql_file("sql/target_count.sql")
 
    cursor.execute(source_query)
    source_count = cursor.fetchone()[0]
 
    cursor.execute(target_query)
    target_count = cursor.fetchone()[0]
 
    print(f"Source Count: {source_count}")
    print(f"Target Count: {target_count}")
 
    assert source_count == target_count
