from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
 
#local file
#soup = BeautifulSoup(open("index.html"))
 
#homepage
homepage = urllib.request.urlopen('http://imdb.com').read()
soup = BeautifulSoup(homepage)
 
images = soup.find_all('img')
for image in images:
    print(image['src'])
    print()

