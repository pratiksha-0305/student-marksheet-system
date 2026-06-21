import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Pmali_09",
    database="collage"
)
print("connected successfully")
cursor=conn.cursor()#to execute query
cursor.execute("SELECT * FROM student")
rows= cursor.fetchall()
for row in rows:
    print(row)
conn.close()    