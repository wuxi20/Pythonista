# coding: utf-8

# https://forum.omz-software.com/topic/3626/play-video-on-ios-quick-look/5

import webbrowser, os, requests, re, bs4
import appex
import console
import dialogs

data_dir = os.path.join(os.path.abspath('.'),'Videos')

if not os.path.isdir (data_dir):
	#print(data_dir)
	os.makedirs(data_dir)
	
os.chdir(data_dir)
#ßprint(os.path.abspath('.'))


def DownloadFile(url, filename):
	res = requests.get(url)
	
	try:
		res.raise_for_status()
	except Exception as exc:
		print('There was a problem: %s' % (exc))
		
	with open(filename, "wb") as code:
		code.write(res.content)
		
# the URL below is copy from the console of the above script, I don't know why it quits without saving the file after download but it works in this script

url = 'https://vsb01.520cc.cc/files/mp4/A/AIEdN.mp4?sk=tdVUWMc11zPLO17HpZ0rsg&se=1552373345'

DownloadFile(url, 'temp.mp4')
console.quicklook('temp.mp4')
os.remove('temp.mp4')
