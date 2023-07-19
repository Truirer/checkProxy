import requests
import time

count = 0

def startProxyCheck(allProxies,protocols,timeoutForRequest,maxRequests):
    def checkProxy(proxy,protocolArray,timeoutForRequest,maximumRequests):
        global count
        headers = {
            'authority': 'api.whatismyip.com',
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,tr-TR;q=0.8,tr;q=0.7',
            'cache-control': 'no-cache',
            # 'content-length': '0',
            'origin': 'https://www.whatismyip.com',
            'pragma': 'no-cache',
            'referer': 'https://www.whatismyip.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        }
        
        for protocol in protocolArray:
            #loop for all protocols given
            print("Testing " + str(protocol) + " protocol!")
            proxies = {
                str(protocol) : str(proxy),
            }
            time.sleep(1)
            try:
                #try to get a response from a website.
                #any website can be used but API's which return ip address are preferred
                response = requests.post(str(protocol) + '://api.whatismyip.com/wimi.php', headers=headers, proxies=proxies , timeout=timeoutForRequest)
                if(response.status_code == 200):
                    print("Valid Proxy Found: " + str(response.text))
                    with open(str(protocol)+"_ValidProxies.txt", "a", encoding="utf-8") as f:
                        f.write(str(proxy) + ",")
            except:
                #request again using the same proxy.
                if(count < maximumRequests):
                    print("Trying to request again. Requests left: " + str(maximumRequests - count -1))
                    count = count + 1
                    checkProxy(protocol,[str(protocol)],timeoutForRequest,maximumRequests)
                else:
                    count = 0
                    print("Failed to connect to proxy server")

    for index,proxy in enumerate(allProxies):
        print("Testing Proxy: " +str(proxy))
        print("Proxies left: " + str(len(allProxies) - index))
        checkProxy(proxy,protocols,timeoutForRequest,maxRequests)
