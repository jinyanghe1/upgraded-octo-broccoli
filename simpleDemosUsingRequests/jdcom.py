#爬取京东商品的详情页
import requests
r = requests.get("https://item.jd.com/2967929.html")
print(r.encoding)
r.encoding = r.apparent_encoding
print(r.text[:1000])

