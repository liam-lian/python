##从百度图片中爬取，全部搜索结果的图片，保存在文件中
from urllib import request
import os
import re

def getHtml(url):
    with request.urlopen(url) as f:
        return f.read()

strkeyword=input('keyword:')
keyword=str(strkeyword.encode('utf-8'))[2:-1].replace(r'\x','%').upper()

urlbase=r'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1508500426040_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='
url=urlbase+keyword



data=getHtml(url)

f=open('D:/12.txt','w')
f.write(str(data))

pattern=re.compile(r'"middleURL":"(.*?.jpg)"')
x=0
path=os.path.join(os.path.join('D:/','zz'),strkeyword)
os.mkdir(path)
for l in pattern.findall(str(data)):
    request.urlretrieve(l,os.path.join(path,str(x))+'.jpg')
    x+=1
print('end.the dir is %s' % path)