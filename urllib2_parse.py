import urllib2

url = "https://foursquare.com/tyayayayaa/checkin/5304b652498e734439d8711f?s=ScMqmpSLg1buhGXQicDJS4A_FVY&ref=tw"

parsed = urllib2.urlparse.urlparse(url)
query = parsed.query
query_dict = urllib2.urlparse.parse_qs(query)
