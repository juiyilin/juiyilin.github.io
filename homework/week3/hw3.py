import urllib.request
import json


url='https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json'
with urllib.request.urlopen(url) as response:
    data=json.load(response)


#type(data) :dict
spots=data['result']['results']

spotdata=''
for i,spot in enumerate(spots):
    #處理圖檔網址
    first_img='http'+spot['file'].split('http')[1]
    spotdata+=','.join([spot['stitle'],spot['longitude'],spot['latitude'],first_img])
    if i!=len(spots)-1:
        spotdata+='\n'

    with open('data.txt','w',encoding='utf8') as file:
        file.write(spotdata)