import webbrowser
import clipboard
import urllib.request, urllib.parse, urllib.error
text=clipboard.get()
"Getting latest system clipboard contents"
dest= urllib.parse.quote(text,safe='')
end= 'safari-http://maps.apple.com/?daddr='
start='&saddr='
from GetLocation import * 
"Imported GetLocation module"
L=getLocation() 
"Calling getlocation function"
s=urllib.parse.quote(L,safe='')
webbrowser.open(end+dest+start+s)
"opening Apple maps by x-callback-url to find driving directions"

	




