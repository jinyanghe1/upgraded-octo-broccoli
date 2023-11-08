import requests
path = "./pic.jpg"
url = "https://pics7.baid\
u.com/feed/342ac65c103853437575433e46c1be73cb808853.j\
peg@f_auto?token=416ffdd0ab6f36457de8ae8cd6fcb738"
r = requests.get(url)
print(r.status_code)
#200
with open(path,'wb') as f:
    f.write(r.content)
    f.close()
#r.content 表示爬取资源的二进制内容