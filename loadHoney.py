from multiprocessing.dummy import Pool as ThreadPool
from create_new_accounts_on_Honey import HoneyUserCreator

def createUserInvokePurchase(i):
    user = HoneyUserCreator()
    user.fakeUserRequest()


def calculateParallel(data, threads=2):
    pool = ThreadPool(threads)
    results = pool.map(createUserInvokePurchase, data)
    pool.close()
    pool.join()
    return results
"""
if __name__ == "__main__":
    N = 1800
    print "works"
    data = range(0, N)
    responses = calculateParallel(data, 100)
    count =0
    for n in range(0, len(responses)):
       if(responses[n] is None or responses[n].status_code!=200):
            count = count + 1
            print responses[n].status_code
    print count
"""


if __name__ == "__main__":
    N = 3000
    count = 0
    for n in range(0, N):
    	resp1 = None
    	resp2 = None
    	resp3 = None
    	resp4 = None
    	user = HoneyUserCreator()
	resp1, resp2, resp3, resp4 = user.fakeUserRequest()
	if(resp1 is not None and resp2 is not None and resp3 is not None and resp4 is not None):
	    count = count +1
    print count
