# coding: utf-8
import clipboard
import urllib.request, urllib.error, urllib.parse
import webbrowser

clipString = clipboard.get()

marky = 'http://heckyesmarkdown.com/go/?u='

queryString = marky + clipString

reqMD = urllib.request.Request(queryString)
openMD = urllib.request.urlopen(reqMD)
content = (openMD.read().decode('utf-8'))
clipboard.set(content)

webbrowser.open(queryString)
