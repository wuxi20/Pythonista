# I got help from here: http://twolivesleft.com/Codea/Talk/discussion/1652/what-others-do%3A-pythonista/p1
# I got help from here: http://www.macdrifter.com/2012/09/pythonista-trick-url-to-markdown.html

import clipboard
import urllib.request, urllib.error, urllib.parse
import editor
import os

url = clipboard.get()
scriptName = os.path.basename(url)
contents = urllib.request.urlopen(url).read()
editor.make_new_file(scriptName[:-3], contents)


