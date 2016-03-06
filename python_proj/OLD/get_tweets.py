import http.client
import json


c = http.client.HTTPConnection('search.twitter.com')
c.request('GET', '/search.json?q=stranglers')
r = c.getresponse()
data = r.read()
datastr = str(data, 'utf-8')
o = json.loads(datastr)
tweets = o['results']
for tweet in tweets:
    print(tweet['text'])