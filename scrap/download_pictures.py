from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse, os, requests, urllib.parse

path = os.getcwd() + '/images'
if not os.path.exists(path):
  print('Create new path /images')
  os.mkdir(path)

homepage = urllib.request.urlopen('https://lsjeu9vw.api.lncld.net/1.1/classes/Route?order=listnumber').read()
soup = BeautifulSoup(homepage)

images = soup.find_all('img')
for image in images:
  url = image['src']
  filename = os.path.basename(urllib.parse.urlsplit(url)[2])
  dl = requests.get(url, stream=True)
  with open(path + '/' + filename, 'wb') as f:
    for chunk in dl.iter_content(chunk_size=1024):
      if chunk:
        f.write(chunk)
        f.flush()

print('Pictures downloaded to /images')

