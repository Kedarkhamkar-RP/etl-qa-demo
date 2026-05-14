
from db_connection import get_connection
from utils import read_sql_file
 
def test_null_check():
   conn = get_connection()
   cursor = conn.cursor()
 
   query = read_sql_file("sql/null_check.sql")
   cursor.execute(query)
   null_count = cursor.fetchone()[0]
   print(f"NULL Count: {null_count}")
   #null_count=0
   assert null_count == 0