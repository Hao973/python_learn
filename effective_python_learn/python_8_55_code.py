# -*- coding: utf-8 -*- 
# @Time : 2019/7/23 下午8:03 
# @Author : FengHao 
# @Site :  
# @File : python_8_55_code.py
# @Software: PyCharm

class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_opaque_class():
    obj = OpaqueClass(1, 2)
    print(obj)
    print(obj.__dict__)


class BetterClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)


def test_better_class():
    obj = BetterClass(1, 2)
    print(obj)


def test_print():
    print('foo bar')
    print('%s ' % 'foo bar')
    print(5)
    print('5')
    a = '\x07'
    print(a)
    print(repr(a))
    b = eval(repr(a))
    assert a == b
    print(repr(5))
    print(repr('5'))
    print('%r' % 5)
    print('%r' % '5')


if __name__ == '__main__':
    test_opaque_class()
    test_better_class()
