import decoratorTest
# 杨辉三角
def triangle():
    yield  [1]
    yield [1,1]
    pre=[1,1]
    while(True):
        now=[1]
        i=0
        while(i<len(pre)-1):
            now.append(pre[i]+pre[i+1])
            i=i+1
        now.append(1)
        pre=now
        yield pre

n = 0
for t in triangle():
    print(t)
    n = n + 1
    if n == 10:
      break


class Stu(object):
    pass

stu=Stu();
stu.a=abs
print(stu.a(-10))