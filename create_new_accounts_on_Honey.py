from fake_email_gen import FakeEmailGenerator

import requests
from bs4 import BeautifulSoup, Comment
import HTMLParser
import json

class HoneyUserCreator:
        url = None
        def __init__(self, url = None):
                self.url = "https://d.joinhoney.com/extusers"
	def getNewEmailId(self):
		emailGen = FakeEmailGenerator()
		email = emailGen.getNewEmail()
		data = {"email" : email , "password": "p1234"}
		#return json.dumps(data, ensure_ascii=False) 
		return "email="+email+"&password=p1234"
        def doPost(self):
		postData = self.getNewEmailId()
		print postData
		headers = {'content-type' : 'application/x-www-form-urlencoded'}
                infoResponse = requests.post(self.url, data=postData, headers=headers)
		print infoResponse.text
		print infoResponse.cookies['honey.user']
                return infoResponse


if __name__ == "__main__":
	user = HoneyUserCreator()
	print user.doPost().text
