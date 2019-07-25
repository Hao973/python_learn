# -*- coding: utf-8 -*- 
# @Time : 2019/7/23 下午8:28 
# @Author : FengHao 
# @Site :  
# @File : python_8_56_code.py
# @Software: PyCharm

from unittest import TestCase


def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError('Must supply str or bytes, found: %r' % data)


class UtilsTestCase(TestCase):
    def test_to_str(self):
        self.assertEqual('hello', to_str(b'hello'))

    def test_to_str_str(self):
        self.assertEqual('hello', to_str('hello'))

    def test_to_str_bad(self):
        self.assertRaises(TypeError, to_str, object())


if __name__ == '__main__':
    UtilsTestCase()
