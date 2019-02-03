#!python2

# https://www.kochi-coders.com/2011/05/30/lets-scrape-the-page-using-python-beautifulsoup/2/

from bs4 import BeautifulSoup
import urllib.request
import console

url="http://www.utexas.edu/world/univ/alpha/"

page=urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
universities=soup.findAll('a',{'class':'institution'})
for eachuniversity in universities:
	print(eachuniversity['href']+","+eachuniversity.string)


