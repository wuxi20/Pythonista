# coding: utf-8 

# https://forum.omz-software.com/topic/3004/auto-fill-form-and-simulate-enter/8

# @omz If you want to use webpagetopdf.com, you don't really have to parse the page, emulate clicks etc. You can bypass all that by doing essentially the same as the JavaScript on that page (which isn't much, it basically just generates a random session/conversion ID, makes one GET request to start the conversion, and a couple more to check its status, and to download the result when the conversion has finished). I've made a little script to automate that process without scraping the page:
	
import requests
import urllib.request, urllib.parse, urllib.error
import random
import time

def random_string():
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(alphabet) for i in range(16))

def convert_to_pdf(page_url, verbose=True):
    sid = random_string()
    cid = random_string()
    conv_url = 'https://apple.sftapi.net/appiOS/initData/isTourist/yes/authName/72F2AEC1-E33A-404C-A11D-02702EA44452' % (sid, cid, urllib.parse.quote(page_url, ''))
    if verbose:
        print('Requesting conversion...')
    r = requests.get(conv_url)
    pid = r.json()['pid']
    if verbose:
        print('pid:', pid)
    filename = 'result.pdf'
    while True:
        print('Checking conversion status...')
        r = requests.get('https://apple.sftapi.net/appiOS/initData/isTourist/yes/authName/72F2AEC1-E33A-404C-A11D-02702EA44452' % (sid, cid, pid))
        status_info = r.json()
        if 'file' in status_info:
            filename = status_info['file']
        if verbose:
            print(status_info)
        if status_info['status'] == 'processing':
            time.sleep(1)
        elif status_info['status'] == 'success':
            break
        else:
            return None
    urllib.request.urlretrieve('https://apple.sftapi.net/appiOS/initData/isTourist/yes/authName/72F2AEC1-E33A-404C-A11D-02702EA44452' % (sid, cid), filename)
    return filename

if __name__ == '__main__':
    print('Running demo...')
    page_url = 'https://apple.sftapi.net/appiOS/initData/isTourist/yes/authName/72F2AEC1-E33A-404C-A11D-02702EA44452'
    filename = convert_to_pdf(page_url)
    if filename:
        import console, os
        console.quicklook(os.path.abspath(filename))
    else:
        print('Conversion failed')

