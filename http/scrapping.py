import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# http://www.dr-chuck.com/page1.htm
url = input('Enter url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieav all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
