import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="cpe54146",
  database="log_asset"
)

mycursor = mydb.cursor()

sql = 'INSERT INTO log_data(ROOM, STATUS, DATE) VALUES (%s, %s, %s)'
val = ('2', 'ON', '2019-07-30')
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")
