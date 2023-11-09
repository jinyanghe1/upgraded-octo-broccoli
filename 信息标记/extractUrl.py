import requests
from bs4 import BeautifulSoup
demo = requests.get("https://python123.io/ws/demo.html")
soup = BeautifulSoup(demo.text, 'html.parser')
for link in soup.find_all('a'):
    #这里一定要注意是使用find_all，有一个长得很像的函数
    #findall，不要搞混了。
    print(link.get('href'))
