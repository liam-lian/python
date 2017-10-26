
import functools
def dec(func):
    @functools.wraps(func)
    def wrapper():
        print("before..")
        func()
        print("end")
    return wrapper
@dec
def fun():
    print("call()")
fun()

if(__name__== '__main__'):
   print('123')
