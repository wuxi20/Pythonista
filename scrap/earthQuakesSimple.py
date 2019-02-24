# coding: utf-8
import requests, json

minMagnitude = str(5)
theURL = 'https://apple.sftapi.net/appiOS/initData/isTourist/yes/authName/72F2AEC1-E33A-404C-A11D-02702EA44452' + minMagnitude
fmt = '{datetime} {earthquake_id} {version} {magnitude} {depth:>6} {location[latitude]:>8} {location[longitude]:>8} {region}'

for theQuake in json.loads(requests.get(theURL).text):
    print((fmt.format(**theQuake)))
print(('=' * 75))

