#提示用户搜索字符串，调用google geocoding api，

#和从返回的json中提取信息

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break 
    
    #获取用户条目并将URL构造为正确编码的参数
    #并使用urllib从谷歌地理编码API中检索文本. 
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    
    print('Retrieved', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    
    try: js = json.loads(str(data))
    except: js = None 
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure to Retrieve ====')
        print(data)
        continue 
    print(json.dumps(js, indent=4))
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng) 
    location = js['results'][0]['formatted_address']
    print(location)
