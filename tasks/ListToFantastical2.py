# coding: utf-8

# https://github.com/coomlata1/pythonista-scripts

'''
ListToFantastical2.py
Parses BOTH reminders and events from comma
seperated text passed from URL's in LCP, 1Writer,
or Drafts and posts them in Fantastical.
Thanks to Fantastical's natural language parsing,
your 'tasks' can be reminders or events.  The
reminders must start with a 'Task', 'Todo',
'Reminder', or 'Remind me' pre-text followed by the
todo itself.  Events don't need the pre-text. For
more on this see:
   http://www.geekswithjuniors.com/note/5-awesome-things-from-fantastical-2-that-can-improve-your-wo.html
and:
   http://plobo.net/recursive-actions-with-launchcenterpro-and-pythonista
for well documented intros to the proper syntax.
Example caller URL's:
  1Writer:
    pythonista://ListToFantastical2?action=run&argv=[text]&argv=onewriter
  Drafts:
    pythonista://ListToFantastical2?action=run&argv=[[draft]]&argv=drafts4
  LCP:
    pythonista://{{ListToFantastical2}}?action=run&argv=[prompt-list:Enter Todos, Reminders, Events:]&argv=launch
Credit Due:
list2Fantastical.py
https://gist.github.com/pslobo/25af95742e1480210e2e
Thanks to @pslobo for his contribution to GitHub
Thanks to @cclauss for code tightening and cleanup
'''

import sys
import urllib.request, urllib.error, urllib.parse
import webbrowser

# Fast fail if Fantastical2 is not installed
if not webbrowser.can_open('fantastical2://'):
  sys.exit('Error: Fantastical is not installed')

'''
The first arg is a comma seperated list of items
received from user input prompt in LCP or comma
separated text in 1Writer, or Drafts. The second
arg is the caller app.
'''
try:
  _, tasks, caller = sys.argv[:3]
except ValueError:
  sys.exit('Error: Command line args are missing.')

# Initialize the x-callback-url
url = ''
'''
Default is for any added tasks to be saved
automatically. Set the 'save' variable to '0' to
manually save or cancel each new task as it is
being processed in Fantastical.
'''
save = '1'

# Split the list by commas and iterate over each resulting item
fmt = 'fantastical2://x-callback-url/parse?sentence={}&add={}&x-success={}'
for task in tasks.split(','):
  '''
  Check to see if there is already an item in the
  x-callback-url. If not, create it, allowing for a
  return to calling app, which is argv[2], upon
  success. If there is, then add task_str + &x
  success followed by the URL-encoded url. This
  respects the requirement for nested encoding.
  '''
  task = urllib.parse.quote(task, '')
  if url:
    url = fmt.format(task, save, urllib.parse.quote(url, ''))
  else:
    url = fmt.format(task, save, caller) + '://'

webbrowser.open(url)

# - **ListToFantastical2.py** - This script parses BOTH reminders and events from comma seperated text passed from URL's in LCP, 1Writer, or Drafts and posts them in Fantastical2 and returns you to the caller app. Thanks to Fantastical's natural language parsing, your 'tasks' can be reminders or events.  The reminders must start with a 'Task', 'Todo', 'Reminder', or 'Remind me' pre-text followed by the todo itself.  Events don't need the pre-text. For more on this see [here](http://www.geekswithjuniors.com/note/5-awesome-things-from-fantastical-2-that-can-improve-your-wo.html) and [here](http://plobo.net/recursive-actions-with-launchcenterpro-and-pythonista) for 2 well documented intros to the proper syntax. Inspiration came from [this](https://gist.github.com/pslobo/25af95742e1480210e2e) script.  Thanks goes to @pslobo for his Github contribution. 
