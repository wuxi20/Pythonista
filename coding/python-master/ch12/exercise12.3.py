#Use urllib to replicate the previous exercise of (1) retrieving the
#document from a URL, (2) displaying up to 3000 characters, and (3) counting the
#overall number of characters in the document. Dont worry about the headers for
#this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error

webpage = urllib.request.urlopen('http://www.w3schools.com/html')

line = webpage.read(100)

count = 0

for character in line:
    count = count + len(character)
    if count == 100: break
    print(line)
    #print count

print(count)
#print line
