import urllib.request,urllib.parse, urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/comments_926857.json"
js = urllib.request.urlopen(url , context=ctx)
data =js.read().decode()
x = json.loads(data)
lst = []

for comment in x["comments"]:
    lst.append(int(comment["count"]))
print(sum((lst)))
