# -*- coding: utf-8 -*- 
# @Time : 2019/7/18 下午7:16 
# @Author : FengHao 
# @Site :  
# @File : python_5_40_code.py
# @Software: PyCharm


def my_coroutine():
    while True:
        received = yield
        print('Received: ', received)


def test_my_coroutine():
    it = my_coroutine()
    next(it)
    it.send('First')
    it.send('Second')


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


def test_minimize():
    it = minimize()
    next(it)
    print(it.send(10))
    print(it.send(4))
    print(it.send(22))
    print(it.send(5))
    print(it.send(-10))


if __name__ == '__main__':
    test_my_coroutine()
    test_minimize()
