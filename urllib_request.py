from urllib import request

url = "http://bit.ly/GoogleScholar"

webpage = request.urlopen(url)
code = webpage.getcode()
info = webpage.info()

headers  = info

new_url = webpage.geturl()

print(url, "redirected to", new_url)