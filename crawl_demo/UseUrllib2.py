from urllib import request
from lxml import etree


response = request.urlopen('http://www.chzu.edu.cn/')
html = response.read()
html = html.decode('UTF-8')

selector = etree.HTML(html)
items = selector.xpath("/html/body/nav/div/div/div/ul/li")
for item in items:
    print(item[0].text)

titleHrefs = selector.xpath("/html/body/div[4]/div/div[1]/div/ul[2]/li[3]/div/ul/li/span[1]/a/@href")
for href in titleHrefs:
    print(href[0].text)


