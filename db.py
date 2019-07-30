#----------connect_mysql.py------------

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="cpe54146",
  database="log_data"
)
mycursor = mydb.cursor()

sql = 'INSERT INTO log_data(ROOM, STATUS, DATE) VALUES ('5', 'OFF', '2019-07-30')'
mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record inserted.")