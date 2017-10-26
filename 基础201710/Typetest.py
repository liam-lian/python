def z(self,n):
    self.n=n
Hello=type('Hello',(object,),dict(__init__=z))
h=Hello(12)
print(h.n)

import logging
try:
    print('try...')
    r = 10 / int('qq')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
    logging.exception(e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    logging.exception(e)
else:
    print('no error!')
finally:
    print('finally...')
    print('END')


print('---------------')


class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid values: %s' % s)
    return 10 / n

try:
    print(int(foo('1')))
except BaseException as e:
    print(e)

print('##################')
def foo(s):
    assert s != 0, 'n is zero!'
    return 10 / s

foo(0)

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value

import unittest
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
        print(r"tttttttttttt\n\n\n")
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
             value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
