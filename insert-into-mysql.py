import mysql.connector
import json
import os
from os import listdir
from PIL import Image as PImage
import base64

def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    return imagesList


homedir = os.path.expanduser("~")
directory = homedir + '/pyhton-scripts/images/'
imgs = loadImages(directory)


# match by remove .jpg
def find_id(words, word):
    i = 0
    for w in words:
        if word == w[:-4]:
            return i
        i += 1

mydb = mysql.connector.connect(
  host="localhost",
  user="nendoroid_db_admin",
  password="Mikuisthebest@108",
  database="nendoroid_db"
)



mycursor = mydb.cursor()


# Open the JSon file
f = open('nendoroid.json')

data = json.load(f)



for i in data['nendoroid_list']:
    sql = "INSERT INTO nendoroid (name, number, image, description) VALUES (%s, %s,%s, %s)"

    index = find_id(imgs, i.get("Number"))

    with open(directory + imgs[index], "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    val = (i.get("Name"), i.get("Number"), encoded_string, "Nendoroid Description")

    
    
    print(val)
    mycursor.execute(sql, val)
mydb.commit()

print(mydb)


