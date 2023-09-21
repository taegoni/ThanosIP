import pyodbc
import pandas as pd

dbkeys=open("./etc/teniron.json",'r',encoding='utf-8')

SERVER = dbkeys["server"]
DATABASE= dbkeys["database"]
USERNAME = 'team'
PASSWORD = dbkeys["password"]

connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};trusted_connection="yes"'

conn=pyodbc.connect(connectionString)
cursor = conn.cursor()

query= "SELECT * FROM test_table"

df_existing_tables = pd.read_sql(query,conn)
df_existing_tables