import urllib.request, urllib.error, urllib.parse
import re

#urls = ['http://youtube.com', 'http://google.com', 'http://yahoo.com', 'http://www.inquirer.net']
urls = ['https://us5.beijingxi.net/shared.php?api=2&appstore=0&build=71&carrierName=%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1&identifierForVendor=F3333819-1EF7-4180-932A-F4EBD2E00B91&isoCountryCode=cn&lang=zh-Hans-CN&mobileCountryCode=460&mobileNetworkCode=11&network=ethernetOrWiFi&version=1.3.7']
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

i = 0
while i < len(urls):
    html_file = urllib.request.urlopen(urls[i])
    html_text = html_file.read()
    titles = re.findall(pattern, html_text)
    print(titles)
    i += 1
