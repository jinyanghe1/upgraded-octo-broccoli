import requests
url = "http://www.ipshudi.com/"
kv = {'user-agents': 'Mozilla/5.0'}
r = requests.get(url + '202.204.80.112'+'.htm',headers= kv)
print(r.status_code)#200
print(r.text)
'''
发现了一个神奇的事情，用到的网站ping不通，但是
浏览器访问正常。见https://blog.csdn.net/weixin_41699562/article/details/100190268
'''
