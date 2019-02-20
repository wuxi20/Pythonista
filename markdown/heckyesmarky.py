# http://www.macdrifter.com/2012/09/pythonista-trick-url-to-markdown.html
# http://heckyesmarkdown.com

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

