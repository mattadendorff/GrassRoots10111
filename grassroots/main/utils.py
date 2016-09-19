import urllib2
from json import loads


def process_w3w(w3w1, w3w2, w3w3):
    key = 'LX54POZB'
    address = '%s.%s.%s' % (w3w1, w3w2, w3w3)
    url = 'https://api.what3words.com/v2/forward?addr=%s&key=%s&lang=en&format=json&display=full' % (address, key)
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    content = loads(resp.read())
    lat = content['geometry']['lat']
    lon = content['geometry']['lng']
    return lat, lon
