import requests
import json
import time
import random
import os
from bs4 import BeautifulSoup


class requester(object):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.38 Safari/537.36',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'Host': 'www.lowes.com'
    }
    client = requests.Session()
    proxyList=[]

    def writeProxy(self, proxy, protocol):
        with open('proxies.txt', 'a') as f:
            f.write('{}:{}:{}\n'.format(protocol, proxy['ip'], proxy['port']))
        f.close

    def getProxy(self):
        response = requests.get('https://api.getproxylist.com/proxy?apiKey=3ca0c07c92c686f1a5ff5d688b4884dece0cf375')
        proxy = json.loads(response.text)
        protocol = proxy['protocol']
        print('Getting Proxy')
        if protocol == 'http':
            proxies = {'http': 'http://{}:{}'.format(proxy['ip'], proxy['port']), 'https': 'https://{}:{}'.format(proxy['ip'], proxy['port'])}
        elif protocol == 'socks4':
            proxies = {'http': 'socks4://{}:{}'.format(proxy['ip'], proxy['port']),'https': 'socks4://{}:{}'.format(proxy['ip'], proxy['port'])}
        else:
            pass
        return proxies
       

    def loadProxy(self):
        print('Converting Proxies')
        with open('proxies.txt') as f:
            file_content = f.read()
        file_rows = file_content.split('\n')
        for i in range(len(file_rows)):
            if ':' in file_rows[i]:
                tmp = file_rows[i]
                tmp = tmp.split(':')
                if tmp[0] == 'socks4':
                    proxies = {'http': 'socks4://{}:{}'.format(tmp[1], tmp[2]), 'https': 'socks4://{}:{}'.format(tmp[1], tmp[2])}
                elif tmp[0] ==  'http':
                    proxies = {'http': 'http://{}:{}'.format(tmp[1], tmp[2]), 'https': 'https://{}:{}'.format(tmp[1], tmp[2])}
                self.proxyList = []
                self.proxyList.append(proxies)
        f.close()

    def noAuthProxy(self):
        print('Converting Proxies')
        with open('proxies.txt') as f:
            file_content = f.read()
        file_rows = file_content.split('\n')
        for i in range(len(file_rows)):
            if ':' in file_rows[i]:
                tmp = file_rows[i]
                tmp = tmp.split(':')
                proxies = {'http': 'http://{}:{}'.format(tmp[0], tmp[1]),
                           'https': 'https://{}:{}'.format(tmp[0], tmp[1])}
                print(proxies)
                self.proxyList.append(proxies)
        f.close()

    def privateProxies(self):
        print('Converting Proxies')
        with open('proxies.txt') as f:
            file_content = f.read()
        file_rows = file_content.split('\n')
        for i in range(len(file_rows)):
            if ':' in file_rows[i]:
                tmp = file_rows[i]
                tmp = tmp.split(':')
                proxies = {'http': 'http://' + tmp[2] + ':' + tmp[3] + '@' + tmp[0] + ':' + tmp[1] + '/',
                           'https': 'http://' + tmp[2] + ':' + tmp[3] + '@' + tmp[0] + ':' + tmp[1] + '/'}
                self.proxyList.append(proxies)
                f.close()


    def requestData(self, link):
        #link = 'https://www.lowes.com/pd/{}/productdetail/{}/Guest'.format(product,store)
        connection = False
        while connection != True:
            print('Getting Proxy')
            cookies = {}
            proxy = random.choice(self.proxyList)
            #r = self.client.get('https://www.lowes.com/', headers=self.headers, proxies = proxy)
            #for ck in self.client.cookies:
            #    cookies[ck.name] = ck.value
            cookies['sn'] = '1006'
            cookies['check'] = 'true'
            cookies['spid'] = 'AADDAB39-6D0A-4657-9B02-51CB9D186361'
            cookies['AMCVS_5E00123F5245B2780A490D45%40AdobeOrg'] = '1'
            cookies['s_ecid'] = 'MCMID%7C74881424587846471432159745693054878512'
            cookies['s_visit'] = '1'
            cookies['_px_uAB'] = 'MTk4OHxmYWxzZQ=='
            cookies['_pxvid'] = '2419372f-e98e-11ea-988e-0242ac120007'
            cookies['_gcl_au'] = '1.1.19442024.1598660729'
            cookies['_px_f394gi7Fvmc43dfg_user_id'] = 'MjU1M2ZhZjAtZTk4ZS0xMWVhLWEyMzEtZWZiMzM3N2IwNzcz'
            cookies['user'] = '%7B%22zipPrompt%22%3Atrue%2C%22guest%22%3Atrue%2C%22backendId%22%3A%223061804609%22%2C%22authToken1%22%3A%22179766766015%3DmHk_r2fAog1ZnKb8QUJJcw%3DJ28MVlCPfhZcaGSJOMZHJ8U6Gu0%3D%22%2C%22authToken2%22%3A%22Guest%22%2C%22WCToken%22%3A%223061804609%252CG3Lzg%252Ftw7C3%252BaPowOUre%252FO66unHOLS6UN86XN%252B%252BKtKTn9xoEQgP3bk5DveFHO%252FZQvGzVxH2eQHatysH4SFo%252FYHm21Y3GF30VXUK3QTBQmdFSiU939Jz5N%252BQdVikSmEBNO%252Fl48ogO5abzlrurUYqQsgJT1ezWCe51%252BB3EejntFK8Snir%252FzdyFO7qf0b%252B%252BNaEN84XVMYIRRFwYzaIAgDh41Q%253D%253D%22%2C%22WCTrustedToken%22%3A%223061804609%252CYB7LIZ8ZbEmGsb8VQ6wSARa%252FgGs%253D%22%2C%22personalizationID%22%3A%221599087885096-6482%22%2C%22activityId%22%3A%22179766766015%22%2C%22isGuest%22%3Atrue%2C%22accessTokenClaims%22%3A%22%22%2C%22SSOToken%22%3A%22Guest%22%2C%22storeNumber%22%3A%221034%22%2C%22segment%22%3Anull%2C%22hasReloadedPage%22%3Afalse%7D'
            try:
                r = self.client.get(link, headers=self.headers, proxies=proxy, cookies=cookies)
                if r.status_code == 200:
                    print('Getting Data from ' + link)
                    productData = json.loads(r.text)
                    product = link.split('/')[4]
                    store = link.split('/')[6]
                    pricing = productData['productDetails'][product]['price']
                    title = productData['productDetails'][product]['product']['title']
                    url = 'https://www.lowes.com' + productData['productDetails'][product]['product']['pdURL']
                    if pricing != None:
                        price = pricing['itemPrice']
                        wasPrice = pricing['wasPrice']
                        availabilityQuantity = productData['inventory']['totalAvailableQty']
                        connection = True
                    elif pricing == None:
                        price = '0'
                        availabilityQuantity = '0'
                        wasPrice = '0'
                        connection = True
                    print('Writing to csv')
                    with open('productData.csv', 'a') as p:
                        p.write('{}||{}|{}|||{}|{}|{}|{} \n'.format(product, wasPrice, price, availabilityQuantity, store, url, title))
                        p.close()
                else:
                    print(str(r.status_code) + ' - Request Error Retrying...')
            except:
                print('Having An Issue With The Proxy, Retrying...')
                sleepTime = random.randint(0, 2)
                print('Sleeping for ', sleepTime)
                time.sleep(sleepTime)
