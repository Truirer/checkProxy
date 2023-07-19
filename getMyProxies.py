from checkProxy import startProxyCheck
#example proxy
allProxies = [
    "socks5://123.123.123.123:12345",
    "socks5://124.124.124.124:12345",
    "socks5://125.125.125.125:12345",
]

startProxyCheck(allProxies,["http","https"],5,3)