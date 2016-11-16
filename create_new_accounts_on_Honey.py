from fake_email_gen import FakeEmailGenerator

import requests
from bs4 import BeautifulSoup, Comment
import HTMLParser
import json
import time

class HoneyUserCreator:
        url = None
	id = None
	createdTime = None
	cookieJar = None
	creationResponse = None
        def __init__(self, url = None):
                self.url = "https://d.joinhoney.com/extusers"
	def getNewEmailId(self):
		emailGen = FakeEmailGenerator()
		email = emailGen.getNewEmail()
		data = {"email" : email , "password": "p1234"}
		#return json.dumps(data, ensure_ascii=False) 
		return "email="+email+"&password=p1234"
        def createUser(self):
		postData = self.getNewEmailId()
		print postData
		headers = {'content-type' : 'application/x-www-form-urlencoded'}
                infoResponse = requests.post(self.url, data=postData, headers=headers)
		userdata = json.loads(infoResponse.text)
		self.creationResponse = userdata
		self.id = userData["id"]
		self.createdTime = userData["created"]
		self.cookieJar = infoResponse.cookies
		for cookie in infoResponse.cookies:
			print cookie.expires
			print cookie
                return infoResponse
	def getSrc(self)
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
	def placeOrder(self, honeySessId, storeSessId):
		

if __name__ == "__main__":
	user = HoneyUserCreator()
	print user.createUser().text
	time.sleep(2)
	honeySessId = user.getHoneySessionId()
	time.sleep(2)
	storeSessId = user.getStoreSessionId()
	
