import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="newpassword",
  database="mydatabase"

)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE movie (name VARCHAR(255), actor VARCHAR(255) , actress VARCHAR(255), release_year VARCHAR(255) , director VARCHAR(255))")