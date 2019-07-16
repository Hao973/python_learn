# -*- coding: utf-8 -*- 
# @Time : 2019/7/11 11:40 
# @Author : FengHao 
# @Site :  
# @File : python_4_35_code.py
# @Software: PyCharm Community Edition
class Field(object):
    def __init__(self, name=''):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls

class DatabaseRow(object, metaclass=Meta):
    pass

class Customer(object):
    #  Class attributes
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')

class BetterCustomer(object):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

def test_customer():
    foo = Customer()
    print('Before:', repr(foo.first_name), foo.__dict__)
    foo.first_name = 'Euclid'
    print('After: ', repr(foo.first_name), foo.__dict__)

def test_better_customer():
    foo = BetterCustomer()
    print('Before:', repr(foo.first_name), foo.__dict__)
    foo.first_name = 'Hao'
    print('After: ', repr(foo.first_name), foo.__dict__)

if __name__ == '__main__':
    # test_customer()
    test_better_customer()
