# x=int(input("number:"))
# if x==0:
#     print('zero')
# elif x>0:
#     print('positive')
# else:
#     print('negative')


r=range(1,9,3)  #1,4,7
print()


#队列
from collections import deque
q=deque([1,2,3,4,5])
q.append(6)
q.popleft()
print(q)



table = str.maketrans('aeiou', '12345')
z='zeeeihasd'.translate(table)
print(z)

d={'name':'lz','age':12}
for key in list(d.keys()):
    del  d[key]
print(d)


list11=[('name','lz'),('zz',[1,2,3,4,5])]
dddd=dict(list11)
dc=dddd.copy()
print(dc)
dc['name']='lzz'
print(dc)
print(dddd)
dc['zz'][0]=123
print(dc)
print(dddd)

print('----------')
from copy import deepcopy
ddc=deepcopy(dddd)
ddc['zz'][1]=11111
print(ddc)
print(dddd)

def printt(*a,**b):
    print(type(a))
    print(type(b))

printt(1,2,zz=1)


llo=[1,2,3,4,5]
llo1=list(filter(lambda x:x>3,llo))
print(llo1)

def zhuangshi(func):
    def inner():
        return '<a>'+func()+'<a>'
    return inner()

@zhuangshi
def deeplevel():
    return 'aaa'


