# coding: utf-8

# https://forum.omz-software.com/topic/2960/access-to-shared-documents

import urllib.request, urllib.parse, urllib.error,urllib.parse
import appex,console,time
url=appex.get_url()
p=urllib.parse.urlparse(url)
f=urllib.parse.unquote(urllib.parse.unquote(urllib.parse.urlparse(appex.get_url()).path.split('/')[-1]))
urllib.request.urlretrieve(url,f)
import console
console.hud_alert(f)
appex.finish()

