# coding: utf-8

# https://forum.omz-software.com/topic/2582/get-web-source-code

import requests
from bs4 import BeautifulSoup

def make_soup(url):
	#in=url out=beautiful soup object
	return BeautifulSoup(requests.get(url).text)
	
def get_iframe_src_html(soup):
	#give beautiful soup object, return html of iframe source
	#this assumes only one iframe:
	src_url = str(soup.find('iframe')['src'])
	#todo: code for more than one iframe in page use case
	
	if 'http' not in src_url:
		#todo: code to attach url root
		pass
	return requests.get(src_url).text
	
	
#example:
example_page = '<html><body><iframe src="https://lite-api.vpnunlimitedapp.com/api/vpn/servers"></iframe><body>'

soup = BeautifulSoup(example_page)

print(get_iframe_src_html(soup))


#example usage:
#soup = make_soup('http://www.google.com')
#iframe_html = get_iframe_src_html(soup)

# --------------------


