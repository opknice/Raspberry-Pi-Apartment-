#----------connect_mysql.py------------

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="mypassword",
  database="iot_device"
)
mycursor = mydb.cursor()

sql = 'INSERT INTO iot(iot_name, iot_value1, iot_value2) VALUES (%s, %s, %s)'
val = ('TEMP', '20', '25')
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")
