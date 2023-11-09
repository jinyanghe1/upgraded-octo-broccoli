import requests
from bs4 import BeautifulSoup#这就是引入BeautifulSoup的模版代码
r = requests.get("http://python123.io/ws/demo.html")
print(r.text[:1000])
demo = r.text
soup = BeautifulSoup(demo , "html.parser")