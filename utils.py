def read_sql_file(file_path):
   with open(file_path, 'r') as file:
       query = file.read()
   return query