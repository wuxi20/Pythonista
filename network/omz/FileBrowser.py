# https://gist.github.com/omz/4051823

import http.server
import socketserver
import webbrowser
import os
os.chdir('/')
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 0), Handler)
port = httpd.server_address[1]
webbrowser.open('http://localhost:' + str(port), stop_when_done=True)
httpd.serve_forever()
