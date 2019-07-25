# -*- coding: utf-8 -*- 
# @Time : 2019/7/19 上午10:16 
# @Author : FengHao 
# @Site :  
# @File : python_6_42_code.py
# @Software: PyCharm

from functools import wraps
from time import time, sleep


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        end = time()
        print('%s Took %.3f seconds' % (func.__name__, end - start))
        return result

    return wrapper


@trace
def fibonacci(n):
    """"Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def test_fibonacci():
    fibonacci(3)
    print(fibonacci)
    help(fibonacci)


@trace
def test_sleep_func(num):
    print('sleep %sS' % num)
    sleep(num)


if __name__ == '__main__':
    test_fibonacci()
    test_sleep_func(2)
