import os
import sys
import urllib.request, urllib.error, urllib.parse
import random

URLBASE = 'https://raw.githubusercontent.com/ywangd/stash/master'

FNAMES = ['stash.py', 'bin/selfupdate.sh', 'bin/echo.py', 'bin/wget.py', 'bin/unzip.py', 'bin/rm.py', 'bin/alias.py']

HOME2 = os.path.expanduser('~/Documents')

STASH_ROOT = os.path.join(HOME2, 'stash')

os.chdir(HOME2)
if not os.path.exists(STASH_ROOT):
    os.mkdir(STASH_ROOT)

os.chdir(STASH_ROOT)
if not os.path.exists('lib'):
    os.mkdir('lib')
if not os.path.exists('bin'):
    os.mkdir('bin')

print('Downloading files ...')
try:
    for fname in FNAMES:
        # Random number to force refresh
        url = "%s/%s?q=%d" % (URLBASE, fname, random.randint(1, 999999))
        print(url)
        req = urllib.request.Request(url)
        req.add_header('Cache-Control', 'no-cache')
        contents = urllib.request.urlopen(req).read()
        with open(fname, 'w') as outs:
            outs.write(contents)

except:
    print('Please make sure internet connection is available')
    sys.exit(1)

from stash import StaSh
stash = StaSh()
stash('selfupdate', final_outs=sys.stdout)
stash.load_lib()  # reload libraries
stash('version', final_outs=sys.stdout)
stash('echo Installation completed', final_outs=sys.stdout)

