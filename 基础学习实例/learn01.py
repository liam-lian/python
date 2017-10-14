
#自然字符串，通过给字符串加上前缀r或R来指定，字符串不转义
print(r'this is \n\n\n\\\r')

print('没有那马上都''asdasd')
print (2)

#运算符

num=12
condition=True
while condition:
    if num>20:
        print('too high')
        num=num-1
    elif num<20:
        num=num+1
        print('too low')
    else:
        condition=not condition
        print('good')
else:
    print('while else')
print('end')


for z in (1,2,3,4,5):
    print(z)
#range 是一个生成序列的函数
for z in range(6,10):
    print(z)

#函数的定义和调用
def sayHello():
    print('hello')
sayHello()

globalsx =100
def testglobal():
    ##加上了global说明这个变量不是在函数里面定义的，而是引用自函数外面定义的全局的变量的值
    global globalsx
    globalsx=200
testglobal();
print(globalsx)

#默认参数，调用的时候不赋值就是用默认值
def myprint(meaasge,times=3):
    i=0
    while i<times:
        print(meaasge)
        i=i+1
myprint('msg')
myprint('msg1',5)

#关键参数：对于使用默认参数的函数，可以跳过中间的一些默认参数，直接对于重要参数赋值，使用参数名字
def abc(a,b=100,c=200):
    print('zz')
    print(a)
    print(b)
    print(c)
abc(1.2,3)
abc(1,c=1000)
abc(b=200,a=100)

print(abc.__doc__)

print(abc())


import sys

for i in sys:
    print(i)

