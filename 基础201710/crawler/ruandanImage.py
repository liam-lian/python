##爬取图片
from urllib import request
import os
import re
from html.parser import  HTMLParser


class mmyhttpparse(HTMLParser):
    def __ini__(self):
       self.x=0
    def handle_starttag( self,tag, attrs):
        if tag=='img':
            if(attrs[0][0]=='src' and attrs[0][1][0:5]=='http:'):
                request.urlretrieve(attrs[0][1],'D:/ppp/'+attrs[0][1][-10:])

def getHtml(url):
    with request.urlopen(url) as f:
        print(url)
        return f.read()


url=r'https://77nali.com/snis-534.html/'
for i in range(1,30):
  data=getHtml(url+str(i))
  par=mmyhttpparse();
  par.feed(str(data))




