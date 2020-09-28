
class lowezy(object):
    storeId = []
    productid = []
    urlList = []

    def __init__(self):
        with open('store_id.txt', 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                self.storeId.append(line)
            f.close()
        with open('prodid.txt', 'r') as f:
            for link in f:
                link = link.replace('\n', '')
                link = link.split('/')[5]
                self.productid.append(link)
            f.close()

    def genLink(self, storeList, productList):
        for i in range(len(storeList)):
            for j in range(len(productList)):
                url  = 'https://www.lowes.com/pd/{}/productdetail/{}/Guest'.format(productList[j], storeList[i])
                self.urlList.append(url)
