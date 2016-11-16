from fake_email_gen import FakeEmailGenerator

import requests
from bs4 import BeautifulSoup, Comment
import HTMLParser
import json
import time

class HoneyUserCreator:
        createUserUrl = None
	periodicEventUrl = None
	genericEvent = None
	id = None
	createdTime = None
	cookieJar = None
	creationResponse = None
        def __init__(self, url = None):
                self.createUserUrl = "https://d.joinhoney.com/extusers"
		self.periodicEventUrl = "https://s.joinhoney.com/ev/ext001001"
		self.genericEvent = "https://s.joinhoney.com/evs"
	def getNewEmailId(self):
		emailGen = FakeEmailGenerator()
		email = emailGen.getNewEmail()
		data = {"email" : email , "password": "p1234"}
		#return json.dumps(data, ensure_ascii=False) 
		return "email="+email+"&password=p1234"
        def createUser(self):
		postData = self.getNewEmailId()
		headers = {'content-type' : 'application/x-www-form-urlencoded'}
                infoResponse = requests.post(self.createUserUrl, data=postData, headers=headers)
		userData = json.loads(infoResponse.text)
		self.creationResponse = userData
		self.id = userData["id"]
		self.createdTime = userData["created"]
		self.cookieJar = infoResponse.cookies
		self.setCookie()
		print self.cookieJar
                return infoResponse
	def getPeriodicEventUrl(self):
		return self.periodicEventUrl
	def getSrc(self):
		return "extension"
	def getExvField(self):
		exv = "ch.9.2.0."+ self.id + ".7747308260017092690"
		return exv
	def getHoneySessionId(self):
		cTime = int(round(time.time() * 1000))
		return cTime
	def getStoreSessionId(self):
		cTime = int(round(time.time() * 1000))
                return cTime
	def getCookie(self):
		return self.cookieJar
	def setCookie(self):
		self.cookieJar.set("exv", self.getExvField(), domain=".joinhoney.com", path="/")		
	#def placeOrder(self, honeySessId, storeSessId):

	def sendPeriodicEvent(self, honeySessId, storeSessId):
                payload = {'src': self.getSrc(), 'exv': self.getExvField(), 'event': self.getPeriodicEventPayload(honeySessId, storeSessId)}
                headers = self.getRequestHeaders()
                eventResponse = requests.post(self.getPeriodicEventUrl(), headers=headers, cookies= self.getCookie(), data=json.dumps(payload))
                print eventResponse
		print eventResponse.text
                return eventResponse
 
        def getPeriodicEventPayload(self, honeySessId, storeSessId):
                eventPayload = {"store": {"id": "7364884674316784684", "session_id": storeSessId}, "session_id":honeySessId}
                return eventPayload
 
        def getRequestHeaders(self):
                headers = {'Host': 's.joinhoney.com',
                'Connection': 'keep-alive',
                'Content-Length': '177',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'chrome-extension://bmnlcjabgnpnenekpadlanbbkooimhnj',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                'Content-Type': 'application/json',
                'DNT': '1',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.8',
                'X-Honey': '9.2.0'
                }
                return headers
	
		

if __name__ == "__main__":
	user = HoneyUserCreator()
	print user.createUser().text
	time.sleep(2)
	honeySessId = user.getHoneySessionId()
	time.sleep(2)
	storeSessId = user.getStoreSessionId()
	user.sendPeriodicEvent(honeySessId, storeSessId)
