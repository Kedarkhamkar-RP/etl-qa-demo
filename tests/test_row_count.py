
from db_connection import get_connection
from utils import read_sql_file
 
def test_row_count():
 
   conn = get_connection()
   cursor = conn.cursor()
 
   source_query = read_sql_file("sql/source_count.sql")
   target_query = read_sql_file("sql/target_count.sql")
 
   cursor.execute(source_query)
   source_count = cursor.fetchone()[0]
 
   cursor.execute(target_query)
   target_count = cursor.fetchone()[0]
 
   cursor.execute(target_query)
   target_count = cursor.fetchone()[0]
 
   print(f"Source Count: {source_count}")
   print(f"Target Count: {target_count}")
 
   #source_count = 0
   #target_count = 1
 
   assert source_count == target_count