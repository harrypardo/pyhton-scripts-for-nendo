import mysql.connector
import json


mydb = mysql.connector.connect(
  host="localhost",
  user="nendoroid_db_admin",
  password="",
  database="nendoroid_db"
)



mycursor = mydb.cursor()


# Open the JSon file
f = open('nendoroid.json')

data = json.load(f)



for i in data['nendoroid_list']:
    sql = "INSERT INTO nendoroid (name, number, url, image_url, year) VALUES (%s, %s,%s, %s,%s)"

    val = (i.get("name"), i.get("number"), i.get("url"), i.get("image"), i.get("year"))

    
    
    print(val)
    mycursor.execute(sql, val)
mydb.commit()

print(mydb)


