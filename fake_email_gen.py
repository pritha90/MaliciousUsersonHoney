import requests
from bs4 import BeautifulSoup, Comment
import HTMLParser

class FakeEmailGenerator:
	url = None
	def __init__(self, url = None):
		self.url = "http://www.fakemailgenerator.com/" 
	def doGet(self):
		infoResponse = requests.get(self.url)
		return infoResponse
	def getNewEmail(self):
		response = self.doGet()
		soup = BeautifulSoup(response.text, "html.parser")
		domain = soup.find(id="domain").text
		email = soup.find(id="home-email")["value"]
		return email.strip() + domain.strip()

if __name__ == "__main__":
	emailGen = FakeEmailGenerator()
	print emailGen.getNewEmail()
