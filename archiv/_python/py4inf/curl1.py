import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://www.py4inf.com/cover.jpg').read()
fhand = open('cover.jpg', 'w')
fhand.write(img)
fhand.close()

