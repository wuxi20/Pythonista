'''
Copyright 2015 Paul Sidnell

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

'''
Takes an Apple Maps pin exported via a WorkFlow action extension and opens it in
Google Maps.

The Workflow Action Extension app (accepts:URLs) is:
	
URL Encode:
	Mode: Encode
Set Variable:
	URL
Text:
	pythonista://Location2GoogleMaps?action=run&args=(URL)
Open URLs
'''

import sys
import urllib.request, urllib.parse, urllib.error
import urllib.parse
import location
import webbrowser
from string import Template

def locationToUrl(lat, long):
	
	tpl = Template ("https://google.com/maps/place/$lat,$long/@$lat,$long,12z");
	params = {"lat" : lat, "long" : int};
	return tpl.substitute(params);
	
url = sys.argv[1];
#url="http://maps.apple.com/maps?address=31%20Stanton%20Road%20Bristol%20England%20BS10%205SJ%20United%20Kingdom&ll=51.504456,-2.590899&q=51.504456,-2.590899&t=m";
ll = urllib.parse.parse_qsl(url, True)[2][1].split(",");
lat = float(ll[0]);
long = float(ll[1]);
url = locationToUrl (lat, int);
webbrowser.open(url);

