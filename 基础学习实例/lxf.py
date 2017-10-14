#杨辉三角
def triangle(n):
    i,j=0,0
    this,last=[],[]
    while i<n:
       this.append(0)
       while j<=i:
           if(j==i):
               this.append(1)
           else:
               this.append(last[j]+last[j+1])
           j=j+1
       yield this[1:]
       last = this
       this=[]
       i=i+1
       j=0
    return 'success'

for z in triangle(12):
    print(z)

['adam', 'LISA', 'barT']

print(list(map(lambda x:x.capitalize(),['adam', 'LISA', 'barT'])))

from functools import reduce
print(reduce(lambda x,y:x*y,[3, 5, 7, 9]))


# 装饰器


def zsq(func):
    def wapper(*args):
        print('我在传入的函数执行之前做一些操作',args)
        func()  # 执行函数
        print('我在目标函数执行后再做一些事情',args)
    return wapper
@zsq
def login():
    print('我进行了登录功能')

def zsq1(*args):
    def wapper(func):
        print('我在传入的函数执行之前做一些操作',args)
        func()  # 执行函数
        print('我在目标函数执行后再做一些事情',args)
    return wapper

@zsq1
def login1():
    print('我进行了登录功能1')


login1(lambda :print(1))

import functools
print("/n/n/n/n/n")


def zsq2(*args):
    def wapper(func):
        @functools.wraps(func)
        def innerwapper(* args_func):
            print('我在传入的函数执行之前做222一些操作',args_func)
            func()  # 执行函数
            print('我在目标函数执行后再做222一些事情',args_func)
        return innerwapper
    return wapper

@zsq2(3,'11',0)
@zsq
def login2():
    print('我进行了登录功能2')



class zz:
    def __call__(self, *args, **kwargs):
        print('this is zz')

    def __getattr__(self, item):
        if(item=='hah'):
          return 12



zzz=zz()
print(zzz.hah)
zzz()



from enum import *
month=Enum('month',('Jan','Feb','Mar'))
print(month.Jan.value)
