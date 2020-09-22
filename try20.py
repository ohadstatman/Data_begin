from bs4 import BeautifulSoup
import ssl
import urllib.request, urllib.parse, urllib.error

ctx = ssl.create_default_context( )
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter url:")
count = input("Enter number of rounds:")
num = 0
position = input("Enter link position:")
while num<int(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    lst = []
    tags = soup("a")
    for tag in tags:
        lst.append(tag.get("href", None))
    url = lst[int(position)]
    num += 1
print(url)


