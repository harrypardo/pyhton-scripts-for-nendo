import json
import urllib.request
import os

# Open the JSon file
f = open('nendoroid.json')

homedir = os.path.expanduser("~")
data = json.load(f)


directory = homedir + '/pyhton-scripts/images'


for i in data['nendoroid_list']:
    urllib.request.urlretrieve(i.get('Image'), os.path.join(directory, i.get('Number') + '.jpg'))
    print("Downloaded  " + i.get('Name'))


