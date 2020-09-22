import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = "http://py4e-data.dr-chuck.net/comments_926856.xml"
    if len(address) < 1: break

    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    tree = ET.fromstring(data)

    lst = []
    results = tree.findall('comments/comment')
    for num in results:
        lst.append((int(num.find("count").text)))
    print(sum(lst))
    break


