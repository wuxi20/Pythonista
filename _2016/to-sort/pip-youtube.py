import bs4, urllib.request, urllib.error, urllib.parse, webbrowser
starturl = input('url: ')
#handle redirects, in case of shortened url
url = urllib.request.urlopen(urllib.request.Request(starturl)).geturl()
#keepvid page url
url = 'http://www.keepvid.com/?url='+url.split('&feature')[0]
#beautifulsoup object of keepvid page
soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read())
#find valid links
links = []
for l in soup.select('a'):
    if l.get('href'):
        if 'googlevideo.com' in l.get('href'):
            links.append(l)
#Open the link
webbrowser.open('safari-'+links[0].get('href'))

