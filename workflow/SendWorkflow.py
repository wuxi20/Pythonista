# coding: utf-8

# http://plobo.net/send-workflow-to-another-device-with-pythonista-command-c/

import re
import urllib.request, urllib.error, urllib.parse
import clipboard
import webbrowser

source = clipboard.get()
mystring = urllib.request.urlopen(source).read()

clipboard.set(re.search("workflow://.*\\b",mystring,re.M).group(0))
webbrowser.open('workflow://')
