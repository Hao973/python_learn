# -*- coding: utf-8 -*- 
# @Time : 2019/7/15 10:25 
# @Author : FengHao 
# @Site :  
# @File : python_5_37_code.py
# @Software: PyCharm Community Edition

import time
import select

from threading import Thread


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def test_factorize():
    numbers = [2139079, 1214759, 1516637, 1852285]
    start = time.time()
    for number in numbers:
        list(factorize(number))
    end = time.time()
    print('Took %.3f seconds ' % (end - start))


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


def test_factorize_thread():
    numbers = [2139079, 1214759, 1516637, 1852285]
    start = time.time()
    threads = []
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    end = time.time()
    print('Took %.3f seconds' % (end - start))


def slow_systemcall():
    select.select([], [], [], 0.1)


def test_slow_systemcall():
    start = time.time()
    for _ in range(5):
        slow_systemcall()
    end = time.time()
    print('test_slow_systemcall Took %.3f seconds' % (end - start))


def compute_helicopter_location(index):
    pass


def test_slow_systemcall1():
    start = time.time()
    threads = []
    for _ in range(5):
        thread = Thread(target=slow_systemcall)
        thread.start()
        threads.append(thread)

    for i in range(5):
        compute_helicopter_location(i)

    for thread in threads:
        thread.join()

    end = time.time()
    print('test_slow_systemcall1 Took %.3f seconds' % (end - start))


if __name__ == '__main__':
    # test_factorize()
    # test_factorize_thread()
    test_slow_systemcall()
    test_slow_systemcall1()

