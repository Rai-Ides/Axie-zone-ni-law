from bs4 import BeautifulSoup
import requests
import ssl
import urlopen
ssl._create_default_https_context = ssl._create_unverified_context
# request = requests.get("https://axie.zone:3000/server_status")
import json
# html = BeautifulSoup(request.content, "html.parser")
import re
context = ssl._create_unverified_context()
import urllib.request


# # # from there you can search the string using a regex, etc.
# email = re.findall(r"<a href='//(.*?)'", html)
# print(email)

request = urllib.request.Request('https://axie.zone:3000/server_status')
opener = urllib.request.build_opener()
response = opener.open(request)

html = str(response)
sax = str(response.read())
email = re.findall(r'":(.*?),', sax)
print(email)

maintaience = email[0];
battles = email[1]

print(battles)
if maintaience == "false":
    print('{"status": "Running", "Battles:" ' + battles + '}')
else:
    print('{"status": ' + maintaience + ', "Battles:" ' + battles + '}')