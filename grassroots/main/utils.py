import urllib2
from json import loads


def process_w3w(w3w1, w3w2, w3w3):
    key = 'LX54POZB'
    w3w = '%s.%s.%s' % (w3w1, w3w2, w3w3)
    base_url = 'https://api.what3words.com/v2/forward'
    address = 'addr=%s&key=%s' % (w3w, key)
    formatting = 'lang=en&format=json&display=full'
    url = '%s?%s&%s' % (base_url, address, formatting)
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    content = loads(resp.read())
    lat = content['geometry']['lat']
    lon = content['geometry']['lng']
    return lat, lon
