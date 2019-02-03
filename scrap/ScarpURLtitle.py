# coding: utf-8
import urllib.request, urllib.parse, urllib.error
import clipboard
import bs4
import console

link = clipboard.get()

console.show_activity()

soup = bs4.BeautifulSoup(urllib.request.urlopen(link))
pageTitle = soup.title.string +' '+ link

console.hide_activity()

console.clear()

print(pageTitle)

