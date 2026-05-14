import os
import pyodbc
from dotenv import load_dotenv
load_dotenv()

def get_connection():
 
   conn = pyodbc.connect(
       f"DRIVER={{ODBC Driver 18 for SQL Server}};"
      f"SERVER={os.getenv('DB_SERVER')};"
      f"DATABASE={os.getenv('DB_NAME')};"
      f"Authentication=ActiveDirectoryInteractive;"
      f"Encrypt=yes;"
      f"TrustServerCertificate=yes;"
   )
 
   return conn
 