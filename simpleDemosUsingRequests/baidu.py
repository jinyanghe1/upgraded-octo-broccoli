import requests
#百度有一个搜索接口
kv = {'wd': 'python'}
r = requests.get("http://baidu.com/s", params=kv)
print(r.request.url)
#'http://www.baidu.com/s?wd=python'
