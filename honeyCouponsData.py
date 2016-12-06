from datetime import datetime
import requests
import json
import os
import string
import time
global currDir
currDir = os.path.dirname(os.path.realpath(__file__))
#def salesData(storeId):
global count
count = 0



#def couponsData(storeId):
def generateTimeStamp(time):
    return time.strftime("%Y-%m-%dT%H-%M-%S")

def makeDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def getIndexDirectory(index):
    indexDir = currDir + "/storeIndex/" + index.upper()
    return indexDir

def getStores(index):
    storeSearchUrl = "https://d.joinhoney.com/stores/search?search="
    indexStoreSearchUrl = storeSearchUrl + index
    indexStoresResponse = requests.get(indexStoreSearchUrl)
    if indexStoresResponse is None:
	print "ERROR in getting stores for index " + index
	return
    try:
	indexStoresResponseJson = indexStoresResponse.json()
    except Exception as e:
	print e
	print "Error in getting json for stores for index " + index
	return
    storeDir = currDir + "/storeIndex/"
    storeIndexDir = storeDir + "/" + index.upper()
    makeDirectory(storeDir)
    makeDirectory(storeIndexDir)
    fileName = storeIndexDir + "/stores" + index.upper()
    f = open(fileName, 'w')
    f.write(json.dumps(indexStoresResponseJson,indent=4, sort_keys=True))
    f.close()
    
def getAllStores():
    alphabetList =  list(string.ascii_lowercase)
    for i in alphabetList:
        getStores(i)

#def getCouponsForStore(storeLabel):
#    couponsUrl = "https://d.joinhoney.com/stores/" + storeLabel + "/?coupons=1"
#    couponsResponse = requests.get(couponsUrl)
    
def getStoreInfo(storeLabel):
    infoUrl = "https://d.joinhoney.com/stores/" + storeLabel.lower() + "/?affiliate=1&stats=1&meta=true&coupons=1&sales=1&gold=1"
    infoResponse = requests.get(infoUrl)
    return infoResponse

def writeStoreInfoToFile(storeInfoResponse, storeLabel, index):
    path = getIndexDirectory(index)
    
    if storeInfoResponse is None:
	print "ERROR none storeInfoResponse for store " + storeLabel
	return
    try:
        storeInfoResponseJson = storeInfoResponse.json()
    except Exception as e:
	print e
	print "ERROR in getting json for store " + storeLabel
	return
    label = storeInfoResponseJson["label"]
    if label != storeLabel:
        print "LABEL MISMATCH for " + label + "/" + storeLabel        
    f = open(path + "/" + label + "-" + generateTimeStamp(datetime.now()), 'w')
    f.write(json.dumps(storeInfoResponse.json(), indent=4, sort_keys=True))
    f.close()

def getStoresForIndex(index):
    storeFilePath = getIndexDirectory(index) + "/stores" + index.upper()
    f = open(storeFilePath, 'r')
    storeData = json.load(f)
    #print storeData
    return storeData

def getAllStoreInfoForIndex(index):
    storeList = getStoresForIndex(index)["stores"]
    for i in storeList:
        storeLabel = i["label"]
        storeResponse = getStoreInfo(storeLabel)
	if storeResponse is None:
	    print "ERROR in getting storeResponse for label " + storeLabel
	    return 
        writeStoreInfoToFile(storeResponse, storeLabel, index)

def getrequest(url):
    response = None
    global count
    try:
        response = requests.get(url)
	count = count +1
	if count % 500 ==0:
	    time.sleep(1)
    except Exception as e:
        print e
    return response


def main():
    getAllStores()
    alphabetList =  list(string.ascii_lowercase)
    for alphabet in alphabetList[18:]:
        getAllStoreInfoForIndex(alphabet.upper()) 

if __name__ == "__main__":
    main()
