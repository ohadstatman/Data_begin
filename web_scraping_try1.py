import requests

response = requests.get("http://em.wikipedia.org/robot.txt")
test = response.text
print("robot.txt for http://en.wikipedia.org/")
print("==========================")
print(test)