# lesson: Web Services: API Rate Limiting and Security
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python, https://www.youtube.com/watch?v=8DvywoWv6fI&list=PPSV
'''
import urllib.request, urllib.error, urllib.parse
import twurl
import json

Twitter_url = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct_name = input("Enter acct name: ")

    if len(acct_name) <1 :
        break

    url = twurl.augment(Twitter_url,{'screen_name': acct_name, 'count':'5'})

    print("Retriving ",url)

    connect = urllib.request.urlopen(url)
    data = connect.read().decode()

    headers = dict(connect.getheaders())
    print('Remaining: ', headers['x-rate-limit-remaining'])

    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ',s[:50])
'''

import urllib.request, urllib.error, urllib.parse
from twurl import augment
import ssl

print("Calling Twitter")
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',{
    'screen_name':'drchuck',
    'count':'2'
})

print(url)

ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode = ssl.CERT_NONE

connect = urllib.request.urlopen(url,context=ctx)
data = connect.read()
print(data)

headers = dict(connect.getheaders())
print(headers)
