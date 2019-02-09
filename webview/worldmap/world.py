import ui,os, urllib.parse
class WorldDelegate (object):
    def webview_should_start_load(self,webview, url, nav_type):
        if url.startswith('world://'):
            print('country selected:', urllib.parse.unquote(urllib.parse.urlparse(url).netloc))
            return False 
        else:
            return True  

w=ui.WebView()
w.delegate=WorldDelegate()
p=os.path.abspath('world/index.html')
w.load_url(p)
w.present('panel')

