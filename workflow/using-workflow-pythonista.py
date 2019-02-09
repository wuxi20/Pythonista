# coding: utf-8

# Workflow & Pythonista

import urllib.request, urllib.parse, urllib.error
import webbrowser

webbrowser.open('workflow://x-callback-url/run-workflow?name=PythonistaTest&input='+urllib.parse.quote('Hi!'))

# pythonista://[[script name]]?action=run&argv=[[some argument to pass, can be a variable]]

