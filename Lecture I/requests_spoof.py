import requests
from bs4 import BeautifulSoup

url = "http://www.whoishostingthis.com/tools/user-agent/"

headers = {"User-agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0"}

request_default = requests.get(url)
request_spoofed = requests.get(url, headers=headers)

soup_default = BeautifulSoup(request_default.text, "lxml")
soup_spoofed = BeautifulSoup(request_spoofed.text, "lxml")

print("Default:", soup_default.find(name="div", attrs={"class":"info-box user-agent"}).text)
print("Spoofed:", soup_spoofed.find(name="div", attrs={"class":"info-box user-agent"}).text)

