import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

page = requests.get("https://republika.co.id/")

object = BeautifulSoup(page.text, 'html.parser')
today = datetime.today()

data=[]

dt_string = today.strftime("%H:%M:%S")

for headline in object.find_all('div',class_='teaser_conten1_center'):
    print(headline.find('h1').text)
    print(headline.find('h2').text)
    print(object.find('div',class_='date').text)
    print (dt_string) 

f=open('D:\Scrapping\headline.json','w')
for headline in object.find_all('div',class_='teaser_conten1_center'):
    data.append({"kategori":headline.find('h1').text,
    "judul":headline.find('h2').text,
    "waktupublish":object.find('div',class_='date').text,
    "waktuScraping":dt_string})    

jdumps=json.dumps(data)
f.writelines(jdumps)
f.close()