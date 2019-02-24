# coding: utf-8

# https://forum.omz-software.com/topic/3179/capture-specific-webpage-text-using-regex-searchhtml-and-save-as-new-textile/2

import requests
from bs4 import BeautifulSoup

url = 'https://d.applvn.com/device?device_token=MaznYs97JTiqaqEwnZGZ5nwbhbyhlRUP0n3rDZHQHkMpoup_DYUskqTpO9PnIZFAYwPARVNUEv5zZyV4BLup6OS7OqMhzM6DD-3Qecn8oSFhoE7wPmp80ToXq-05aIi_EFBnEHkqGxAaOuElHOsGD-gNgeuaKcaRyNY3U3-9et4%3D'

soup = BeautifulSoup(requests.get(url).text)

print(soup.find('div', id='abstract')) #find one div with id 'abstract' and print

