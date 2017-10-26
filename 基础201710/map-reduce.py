#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
#其他小写的规范名字
def normalize(name):
     str=name[0].upper()
     str=str+name[1:].lower()
     return str

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#请编写一个prod()函数，可以接受一个list 并利用reduce()求积
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
print(prod([1,2,3,4,5]))

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    return str(n)==str(n)[-1::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))


#假设我们用一组tuple 表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=lambda t:t[0])
L3=sorted(L,key=lambda x:x[1],reverse=True)
print(L2,L3)

