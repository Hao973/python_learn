# -*- coding: utf-8 -*- 
# @Time : 2019/7/10 10:49 
# @Author : FengHao 
# @Site :  
# @File : python_4_32_code.py 
# @Software: PyCharm Community Edition

class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value of for %s' % name
        setattr(self, name, value)
        return value

class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)

class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

class SavingDB(object):
    def __setattr__(self, name, value):
        # Save some data to the DB log
        # ...
        print('SavingDB Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)

class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('LoggingSavingDB Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)

def test_lazy_db():
    data = LazyDB()
    print('Before:', data.__dict__)
    print('foo: ', data.foo)
    print('After: ', data.__dict__)

def test_logging_lazy_db():
    log_data = LoggingLazyDB()
    print('exists:', log_data.exists)
    print('foo: ', log_data.foo)
    print('foo: ', log_data.foo)

def test_logging_lazy_db_1():
    log_data = LoggingLazyDB()
    print('Before:', log_data.__dict__)
    print('foo exists: ', hasattr(log_data, 'foo'))
    print('After: ', log_data.__dict__)
    print('foo exists: ', hasattr(log_data, 'foo'))

def test_validating_db():
    data = ValidatingDB()
    print('exists:', data.exists)
    print('foo:   ', data.foo)
    print('foo:   ', data.foo)

def test_validating_db_hasattr():
    data = ValidatingDB()
    print('foo, exists', hasattr(data, 'foo'))
    print('foo, exists', hasattr(data, 'foo'))

def test_logging_saving_db():
    data = LoggingSavingDB()
    print('Before: ', data.__dict__)
    data.foo = 5
    print('After: ', data.__dict__)
    data.foo = 7
    print('Finally', data.__dict__)


if __name__ == '__main__':
    # test_validating_db()
    # test_logging_lazy_db_1()
    # test_validating_db_hasattr()
    test_logging_saving_db()
    exit(0)

