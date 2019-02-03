# @viticci
# Copy a URL's page title and return title + link format. Example: Tweetbot for Mac Review http://www.macstories.net/news/tweetbot-for-mac-review/

import urllib.request, urllib.parse, urllib.error
import clipboard
import bs4
import webbrowser
import console

link = clipboard.get()

soup = bs4.BeautifulSoup(urllib.request.urlopen(link))
clipboard.set(soup.title.string +' '+ link)
text = clipboard.get()
console.clear()
print(text)
