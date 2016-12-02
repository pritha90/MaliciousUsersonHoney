import json
import requests
import os
import re
currDir = os.path.dirname(os.path.realpath(__file__))

class CouponProduct:
	coupons = None
	storeId = None
	def __init__(self, storeId="amazon"):
		self.storeId = storeId
		self.couponUrl = "https://d.joinhoney.com/stores/" + self.storeId + "/?coupons=1"

	def getCoupons(self):
		fCode = open(currDir + "/" + self.storeId + "_codes", 'w')
		fProduct = open(currDir + "/" + self.storeId + "_products", 'w')
		storeResponse = requests.get(self.couponUrl)
		couponsData = json.loads(storeResponse.text.encode("ascii","replace"))
		self.coupons = couponsData["coupons"]
		for key in self.coupons:
			productName = ""
			print key.get("code")
			fCode.write(key.get("code")+ "\n")
			description = key.get("description")
			#s= re.search('.*(GET|OFF|[SAVE\s$]\d+[\sON\s])+', description, re.IGNORECASE)
			s= re.search('.*(GET|OFF|SAVE\s[$]\d+\sON\s)+', description, re.IGNORECASE)
			if s:
				productName = description[s.end():].strip()
			else:
				productName = description.strip()
			fProduct.write(key.get("code") + "\t\t" + productName + "\n" )
		fCode.close()
		fProduct.close()

if __name__ == "__main__":
	couponProduct  = CouponProduct("tipsy-elves")
	couponProduct.getCoupons()
