import requests
import json
import time
count = 0
publicIp = ""
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
def startProxyCheck(allProxies,protocols,timeoutForRequest,maxRequests):
    global publicIp
    global headers
    #Get your public ip
    print("Getting Public Ip")
    response = requests.post('https://api.whatismyip.com/wimi.php', headers=headers)
    data = response.text
    x = json.loads(data)
    publicIp = x["ip"]
    print("Your public ip is: " + str(publicIp))


    def getProxy(proxy,protocolArray,timeoutForRequest,maximumRequests):
        global count
        global publicIp
        global headers
        for protocol in protocolArray:
            print("Testing " + str(protocol) + " protocol!")
            proxies = {
                str(protocol) : str(proxy),
            }
            time.sleep(1)
            try:
                response = requests.post(str(protocol) + '://api.whatismyip.com/wimi.php', headers=headers, proxies=proxies , timeout=timeoutForRequest)
                if(response.status_code == 200):
                    data = response.text
                    x = json.loads(data)
                    if(x["ip"] != str(publicIp)):
                        print("Valid Proxy Found: " + str(response.text))
                        with open(str(protocol)+"_ValidProxies.txt", "a", encoding="utf-8") as f:
                            f.write(str(proxy) + ",")
                    else:
                        print("Proxy is not working.")
                        # getProxy(proxy,timeoutForRequest,maximumRequests)
            except:
                if(count < maximumRequests):
                    print("Trying to request again. Requests left: " + str(maximumRequests - count -1))
                    count = count + 1
                    getProxy(protocol,[str(protocol)],timeoutForRequest,maximumRequests)
                else:
                    count = 0
                    print("Failed to connect to proxy server")

    for index,proxy in enumerate(allProxies):
        print("Testing Proxy: " +str(proxy))
        print("Proxies left: " + str(len(allProxies) - index))
        getProxy(proxy,protocols,timeoutForRequest,maxRequests)
