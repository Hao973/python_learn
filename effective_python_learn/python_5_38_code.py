# -*- coding: utf-8 -*- 
# @Time : 2019/7/16 上午10:52 
# @Author : FengHao 
# @Site :  
# @File : python_5_38_code.py
# @Software: PyCharm

from time import time
from threading import Thread, Lock


class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # Read from the sensor
        # ...
        counter.increment(1)


def run_threads(func, how_many, counter):
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def test_counter():
    start = time()
    how_many = 10 ** 5
    counter = Counter()
    run_threads(worker, how_many, counter)
    print('Counter should be %d, found %d' %
          (5 * how_many, counter.count))
    end = time()
    print('Took %.3f seconds ' % (end - start))


def test_locking_counter():
    start = time()
    how_many = 10 ** 5
    counter = LockingCounter()
    run_threads(worker, how_many, counter)
    print('LockingCounter should be %d, found %d' %
          (5 * how_many, counter.count))
    end = time()
    print('Took %.3f seconds ' % (end - start))


if __name__ == '__main__':
    test_counter()
    test_locking_counter()
