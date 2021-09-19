import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="newpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM movie")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print("*********")
sql = "SELECT * FROM movie WHERE release_year =2021"
mycursor.execute(sql)
myresult1 = mycursor.fetchall()
for x in myresult1:
  print(x)

