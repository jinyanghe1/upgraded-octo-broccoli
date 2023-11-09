import requests
#get()方法
#r = requests.get(url)，\
#r是一个response对象，包含了爬虫访问的全部内容
r = requests.get("http://www.baidu.com")
print(r.status_code)
type(r)
print(r.headers)
r.encoding = 'utf-8'
print(r.text)
#response对象的属性 \
#r.status_code 状态码
#r.text url对应的页面内容
#r.encoding header中猜测内容编码
#r.apparent_encoding 内容中猜测内容编码
#r.content 响应内容的二进制格式
