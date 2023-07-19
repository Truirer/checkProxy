# checkProxy

## Description

Filter proxies by checking if they are working or the request takes more time than the set amout.
This project is using whatismyip.com to collect ip adresses and any information about the adress. If you want to use any other website change the request headers and the url.

## Getting Started

### Installing

* Clone the git repo by using:
```
git clone https://github.com/Truirer/checkProxy.git
```

### Executing program

* After cloning the repo,
```
cd /testProxy
```
* Open getMyProxies.py
* Add your proxies to allProxies array
* Edit the startProxyCheck function. Function parameters;
```
startProxyCheck(allProxies,protocols,timeoutForRequest,maxRequests)

allProxies= proxies you want to check in array format
protocols = protocols you want to check in array format . Example= ["http","https"]
timeoutForRequest = Request timeout duration in seconds.
maxRequests = Additional requests to test the same proxy address. Set 0 if you want to check every proxy only once.

``` 


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
