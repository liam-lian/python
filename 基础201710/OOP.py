from types import *

class Stu(object):
    def getname(self):
        return self.__name;
    __slots__ = ('zz','ll','__name')

class child(Stu):
    __slots__ = ('pp')
s=Stu()

s.zz=1
print(s.zz)

c=child()
c.pp=1
print(c.pp)


class mysum(object):
    def __getitem__(self, item):
        if (isinstance(item,int)):
            z=0
            for i in range(item+1):
               z=z+i
            return z
        if(isinstance(item,slice)):
            start=item.start
            if(start==None):
                start=0
            z=0
            for i in range(start,item.stop+1):
                z=z+i
            return z
    def __getattr__(self, item):
        if(item=='zz'):
            return lambda :'method'
        else:
            return 12
    def __call__(self, *args, **kwargs):
        print("call==")
su=mysum();
print(su[10])
print(su[1:3])
print(su.zz())
su()

print(callable(mysum()))
