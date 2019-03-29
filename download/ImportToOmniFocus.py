#Summary: Takes copied text and creates new task in OmniFocus
#By: Jason Verly
#Rev: 2013-02-04
#Rev Note: Added Page Title & URL to clipped txt

import webbrowser
import clipboard
import urllib.request, urllib.parse, urllib.error
import console
import sys

title = sys.argv[1]
url = sys.argv[2]

task = console.input_alert('Task', 'Enter task description')
task = urllib.parse.quote(task)

note = clipboard.get()

full_note = ''.join([title,'\n\n', url, '\n\n', note])
full_note = urllib.parse.quote(full_note.encode('utf-8'))

webbrowser.open('omnifocus:///add?name=' + task + '&note=' + full_note)

