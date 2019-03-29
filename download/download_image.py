# coding: utf-8

# https://gist.github.com/beer2011/b53151703781f705d2f9/

import console
console.set_font('Menlo',18)

import appex
from bs4 import BeautifulSoup
import sys
import urllib.request, urllib.error, urllib.parse
import os.path

# download, save images
def download(url):
	img = urllib.request.urlopen(url)
	localfile = open(os.path.basename(url), 'wb')
	localfile.write(img.read())
	img.close()
	localfile.close()

def main():
	if not appex.is_running_extension():
		print('This script is intended to be run from the sharing extension.')
		return
	par_url = appex.get_url()
	print(par_url)
	if not par_url:
		print('No input URL found.')
		return

	# url access
	res = urllib.request.urlopen(par_url)
	# beautifulsoup, perse
	soup = BeautifulSoup(res.read())

	# img, search
	for link in soup.find_all('img'):
		# get image's URL
		img_url = link.get('src')
        	if img_url.startswith('//'):
            		img_url = 'http:' + img_url
		print(img_url)
		# 
		download(img_url)
	
if __name__ == '__main__':
	main()
	

