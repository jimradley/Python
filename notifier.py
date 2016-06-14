#http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
import requests, time, tweepy
from bs4 import BeautifulSoup
from pushbullet import Pushbullet
from datetime import datetime

def getUrl():
        if (datetime.now().time().hour < 10):
                return requests.get('http://ojp.nationalrail.co.uk/service/ldbboard/dep/MLY/LDS/To')
        else:
                return requests.get('http://ojp.nationalrail.co.uk/service/ldbboard/dep/LDS/MLY/To')

def initTweepy():
        #enter the corresponding information from your Twitter application:
	CONSUMER_KEY = "" #keep the quotes, replace this with your consumer key
	CONSUMER_SECRET = "" #keep the quotes, replace this with your consumer secret key
	ACCESS_KEY = "" #keep the quotes, replace this with your access token
	ACCESS_SECRET = "" #keep the quotes, replace this with your access token secret
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	return tweepy.API(auth)

def initPushbullet():
        return Pushbullet("")

def getContent(html_doc):
   soup = BeautifulSoup(html_doc.text, 'html.parser')
   rows = []
   for row in soup.select("tr")[1:]:
	   cells = row('td')
	   print(cells[0].get_text(strip=True))
	   rows.append("The " + cells[0].get_text(strip=True) + " to " + cells[1].get_text(strip=True) + " is now " + cells[2].get_text())
		  
   return rows

def tweetMesssage(message, api):
        api.update_status(message)


count = -1
sleepCounter = 1
notifiedRows = []

pb = initPushbullet()
tweepy = initTweepy()
html_doc = getUrl()

while (sleepCounter < 120):
		rowContent = getContent(html_doc)
		print(len(rowContent))
		for j in range(0,len(rowContent)):
			print(rowContent[j])
			if ("On time" not in rowContent[j] and rowContent[j] not in notifiedRows):
				push = pb.push_note("Train Notification", rowContent[j] )
				tweetMesssage(rowContent[j], tweepy)
				notifiedRows.append(rowContent[j])
		print("sleeping...")
		time.sleep(60)
		sleepCounter += 1
