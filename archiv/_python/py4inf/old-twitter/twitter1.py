import urllib.request, urllib.parse, urllib.error

TWITTER_URL = 'http://api.twitter.com/1/statuses/friends/ACCT.xml'

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    url = TWITTER_URL.replace('ACCT', acct)
    print('Retrieving', url)
    document = urllib.request.urlopen (url).read()
    print(document[:250])

