# coding: utf-8
import clipboard
import urllib.request, urllib.parse, urllib.error

s = clipboard.get()

s = s.encode('utf-8')
s = urllib.parse.quote(s, safe='')

print(s)


