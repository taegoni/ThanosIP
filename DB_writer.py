# import mariadb
# import json
# import sys
# dbkeys=open("./etc/teniron.json",'r',encoding='utf-8')
# db_meta=json.load(dbkeys)

# SERVER,PORT = db_meta["MariaDB"]["server"].split("/")
# DATABASE= db_meta["MariaDB"]["database"]
# USERNAME = 'team'
# PASSWORD = db_meta["MariaDB"]["password"]

# try:
#     conn = mariadb.connect(user=USERNAME,password=PASSWORD,host=SERVER,port=PORT,database=DATABASE)
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)

# cur = conn.cursor()

# query="SELECT * FROM test_table"

# cur.execute(query)

# rows = cur.fetchall()
# print(rows,'\n')

# conn.commit()

# cur.close()
# conn.close()

import dbModule

table_name="test_table"
insert_data='"123.123.123.123",1,NULL,"KR","never.comx",33'
db_class = dbModule.Database()
sql = f"INSERT INTO {table_name} VALUES({insert_data})"
db_class.execute(sql)
db_class.commit()



