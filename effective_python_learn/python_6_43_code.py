# -*- coding: utf-8 -*- 
# @Time : 2019/7/19 上午10:48 
# @Author : FengHao 
# @Site :  
# @File : python_6_43_code.py
# @Software: PyCharm

import logging
from contextlib import contextmanager


def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


def test_1():
    my_function()


def test_2():
    with debug_logging(logging.DEBUG):
        print('Inside:')
        my_function()
    print('After')
    my_function()


def test_3():
    with log_level(logging.DEBUG, 'my-log') as logger:
        logging.debug('This will not print')
        logger.debug('This is my message!')
        logger.debug('This is my message1!')
        logger.debug('This is my message2!')

    logger = logging.getLogger('my-log')
    logger.debug('Debug will not print')
    logger.error('Error will print')


if __name__ == '__main__':
    # test_1()
    # test_2()
    test_3()
