import urllib2

url = "http://bit.ly/GoogleScholar"

webpage = urllib2.urlopen(url) code = webpage.getcode()
info = webpage.info()

headers  = info.dict

new_url = webpage.geturl()
