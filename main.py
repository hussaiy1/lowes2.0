from requester import requester
from lowezy import lowezy
import threading
import time

if __name__ == "__main__":
    start = time.time()

    lowes = lowezy()
    http = requester()
    storeID = lowes.storeId
    prodID = lowes.productid

    lowes.genLink(storeID, prodID)
    ListUrl = lowes.urlList



    http.privateProxies()

    threads = []
    numbThreads = 1729
    totalThreads = len(ListUrl)
    totalProducts = len(prodID)
    

    for i in range(totalProducts*7):
        threadRange = ListUrl[i*int(len(storeID)/7):(i+1)*int(len(storeID)/7)]
        threads = []
        if len(threadRange) != 0:
            for j in range(len(threadRange)):
                p1 = threading.Thread(target=http.requestData, args=(threadRange[j],))
                p1.start()
                threads.append(p1)
            for thread in threads:
                thread.join()
            print('Sleeping for 1 seconds')
            time.sleep(1)

print('Process Complete, It took', time.time()-start, 'seconds.')
