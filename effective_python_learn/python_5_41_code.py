# -*- coding: utf-8 -*- 
# @Time : 2019/7/18 下午8:15 
# @Author : FengHao 
# @Site :  
# @File : python_5_41_code.py
# @Software: PyCharm

from time import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def test_1():
    start = time()
    results = list(map(gcd, numbers))
    print(results)
    end = time()
    print('Took %.3f seconds' % (end - start))


def test_2():
    start = time()
    pool = ThreadPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, numbers))
    print(results)
    end = time()
    print('Took %.3f seconds' % (end - start))


def test_3():
    start = time()
    pool = ProcessPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, numbers))
    print(results)
    end = time()
    print('Took %.3f seconds' % (end - start))


if __name__ == '__main__':
    numbers = [(1963309, 2265973), (2030677, 3814172),
               (1551645, 2229620), (2039045, 2020802)]
    test_1()
    test_2()
    test_3()
