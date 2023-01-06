# lesson: Networking: Web Scraping with Python
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input("Url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all achcor tags 
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
    
