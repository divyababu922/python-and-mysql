import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="newpassword",
  database="mydatabase"

)
mycursor = mydb.cursor()



sql = "INSERT INTO movie (name, actor,actress,release_year,director) VALUES (%s, %s,%s, %s,%s)"
val = [
  ('Vedalam', 'Ajithkumar','Shruthi Hasan',2015,'Siva'),
  ('Master', 'Vijay','Malavika Mohanam',2021,'Lokesh Kanakaraj'),
  ('Sultan', 'Karthi','Rashmika Mandanna',2021,'Bakkiyaraj Kannan'),
  ('Karnan', 'Dhanush','Rajisha Vijayan',2021,'Mari Selvaraj'),
  ('Dear Comrade', 'Vijay Devarakonda','Shruthi Ramachandiran',2019,'Bharat Kamma'),

]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")