def mul(z,y):
    return z**y

from functools import partial
four=partial(mul,y=4)

print(four(2))



class Animal(object):
    def __init__(self,name):
        self.name=name
    def  greet(self):
        print( 'Hello, I am %s.' % self.name)


print(type(Animal('12')))

def testimport():
    print('success')