# lesson: Networking: Web Scraping with Python
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python, https://www.youtube.com/watch?v=8DvywoWv6fI&list=PPSV
'''   
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input("Url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all achcor tags 
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
'''
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Url: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all achcor tags 
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

