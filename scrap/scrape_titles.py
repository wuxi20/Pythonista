import urllib.request, urllib.error, urllib.parse
import re

#urls = ['http://youtube.com', 'http://google.com', 'http://yahoo.com', 'http://www.inquirer.net']
urls = ['http://amdouni.com']
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

i = 0
while i < len(urls):
    html_file = urllib.request.urlopen(urls[i])
    html_text = html_file.read()
    titles = re.findall(pattern, html_text)
    print(titles)
    i += 1
