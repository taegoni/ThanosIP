import pyodbc
import pandas as pd
import json

dbkeys=open("./etc/teniron.json",'r',encoding='utf-8')
db_meta=json.load(dbkeys)
SERVER = db_meta["MariaDB"]["server"]
DATABASE= db_meta["MariaDB"]["database"]
USERNAME = 'team'
PASSWORD = db_meta["MariaDB"]["password"]

connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};trusted_connection="yes"'

conn=pyodbc.connect(connectionString)
cursor = conn.cursor()

query= "SELECT * FROM test_table"

df_existing_tables = pd.read_sql(query,conn)
df_existing_tables