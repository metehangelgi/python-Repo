import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
    htmlpage = response.read()
type(htmlpage)

import urllib.request
url = 'http://www.simula.no/research/scientific/cbc'
urllib.request.urlretrieve(url, filename='webpage.html')

infile = urllib.request.urlopen(url)
type(infile)


url = 'https://www.ku.edu.tr/'
sayfa=urllib.request.urlopen(url).read()
wf=open(r'c:\x.html','w')
sayfa_utf=sayfa.decode('utf-8')
type(sayfa_utf)

wf.write(sayfa_utf)
wf.close()

#
"""
import urllib
url = \
'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/oxforddata.txt'
urllib.request.urlretrieve(url, filename='Oxford.txt')
"""

""" THIS IS TO SHOW YOU HOW TO READ FROM A URL PRETENDING AS A DIFFERENT APPLICATION
PLEASE DON'T ABUSE THE UK WEATHER SITE, USE THE TEXT FILE PROVIDED TO YOU FOR THE ASSIGNMENT
"""
import urllib.request

url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/oxforddata.txt'

#urllib.request.urlretrieve(url, filename='Oxford_wdata.txt')
"""
from urllib.request import Request
req=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
type(req)
#<class 'urllib.request.Request'>
req
#<urllib.request.Request object at 0x0000009C4B1CABA8>
webpage = urllib.request.urlopen(req).read()
type(webpage)
#<class 'bytes'>
webpage_utf8 = webpage.decode('utf-8')
type(webpage_utf8)
#<class 'str'>
webpage_utf8.replace('\r','')
webpage_utf8[0:100]

with open('weather_data_Oxford2.txt','w') as outf:
    outf.write(webpage_utf8)
"""
