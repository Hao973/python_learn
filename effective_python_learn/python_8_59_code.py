# -*- coding: utf-8 -*- 
# @Time : 2019/7/24 上午10:49 
# @Author : FengHao 
# @Site :  
# @File : python_8_59_code.py
# @Software: PyCharm

from random import randint
from cProfile import Profile
from pstats import Stats


def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result


def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)


def test_1():
    test_data = [3, 0, 2, 9, 5, 6, 7, 1]
    print('before', test_data)
    after_data = insertion_sort(test_data)
    print('after', after_data)


def test_2():
    max_size = 10 ** 4
    data = [randint(0, max_size) for _ in range(max_size)]
    test = lambda: insertion_sort(data)
    profiler = Profile()
    profiler.runcall(test)

    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()


if __name__ == '__main__':
    test_2()
