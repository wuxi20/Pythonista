# coding: utf-8

# https://forum.omz-software.com/topic/2644/related-with-non-ascii-error

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = eval(input('Enter location : '))
    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode({'sensor':'false','address':address})
    print(('Retrieving ', url))
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print(('Retrieved ', len(data), 'characters'))
    try: js = json.loads(str(data))
    except: js=None
    if 'status' not in js or js['status'] != 'OK':
        print('====Failure to Retrieve====')
        print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print(('lat', lat, 'lng', lng))
    location = js["results"][0]["formatted_address"]
    print(location)



