from collections import Counter

str='zzzsadaasaskldas'
c=Counter(str)
print(c.most_common(2))

import base64

bytesString = 'sadsadadasdsaddddddddddddddddddddddddddddddddddddddddddddddddddddddd'.encode(encoding="utf-8")
print(base64.b64encode(bytesString))


from collections import *
z=OrderedDict([('AA',12),('CC',22),('BB',100)])
print(z)

dic = OrderedDict()
dic['k1'] = 'v1'
dic['k4'] = 'v2'
dic['k3'] = 'v3'
print(dic)

zz=defaultdict(int)
zz['zzzz']=100
print(zz['zzzz'])
print(zz['zzzz1'])

Stu=namedtuple('Stu',['name','id','age'])
stutuple=Stu('lz',645,22)
print(stutuple.name)
print(stutuple.id)

from  itertools import *

print(list(islice([10,6,2,8,1,3,9],5)))
print(list(islice(count(1),5)))

a={1,2,3,5}
print(a)

print(a | (set(['w','w','e','r','y'])))

from python03 import testimport
testimport()






def z(n):
    if n==1:
        return 1
    else:
        return n*z(n-1)

print(z(400))