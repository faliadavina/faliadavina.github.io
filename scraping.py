#Import Package
import requests
from bs4 import BeautifulSoup

#Req ke website
page = requests.get("https://republika.co.id/")

#Extract konten
object = BeautifulSoup(page.text, 'html.parser')

print ('Menampilkan objek html')
print ('=======================')
print (object)

print ('\n\nMenampilkan title browser dengan tag')
print ('=======================================')
print (object.title)

print ('\n\nMenampilkan title browser tanpa tag')
print ('=======================================')
print (object.title.text)

print ('\n\nMenampilkan semua tag h2')
print ('=======================================')
print (object.find_all('h2'))

print ('\n\nMenampilkan semua teks h2')
print ('=======================================')
for headline in object.find_all('h2'):
    print (headline.text)

print ('\n\nMenampilkan berita terkini berdasarkan div class')
print ('===============================================')
print (object.find_all('div',class_='conten1'))

print ('\n\nMenampilkan semua teks berita terkini')
print ('=======================================')
for headline in object.find_all('div',class_='conten1'):
    print(headline.find('h2').text)

print ('\n\nMenyimpan berita terkini pada file text')
print ('=======================================')
f=open('D:\Scrapping\headline.txt','w')
for headline in object.find_all('div',class_='conten1'):
    f.write(headline.find('h2').text)
    f.write('\n')
f.close()

