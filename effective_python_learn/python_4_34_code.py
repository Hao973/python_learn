# -*- coding: utf-8 -*-
# @Time : 2019/7/11 10:40 
# @Author : FengHao 
# @Site :  
# @File : python_4_34_code.py
# @Software: PyCharm Community Edition
import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})

class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'class': self.__class__.__name__,
                           'args': self.args})

class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D（%d, %d)' % (self.x, self.y)

class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'BetterPoint2D（%d, %d)' % (self.x, self.y)


registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])

class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'EvenBetterPoint2D（%d, %d)' % (self.x, self.y)

register_class(EvenBetterPoint2D)

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass

class Point3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Point3D（%d, %d, %d)' % (self.x, self.y, self.z)

# register_class(Point3D)

def test_point2d():
    point = Point2D(5, 3)
    print('Object: ', point)
    print('Serialized: ', point.serialize())

def test_better_point2d():
    point = BetterPoint2D(5, 3)
    print('Before: ', point)
    data = point.serialize()
    print('Serialized: ', data)
    after = BetterPoint2D.deserialize(data)
    print('After: ', after)

def test_even_better_point_2d():
    point = EvenBetterPoint2D(5, 3)
    print('Before: ', point)
    data = point.serialize()
    print('Serialized: ', data)
    after = deserialize(data)
    print('After: ', after)

def test_point3d():
    point = Point3D(5, 3, 4)
    print('Before: ', point)
    data = point.serialize()
    print('Serialized: ', data)
    after = deserialize(data)
    print('After: ', after)

if __name__ == '__main__':
    # test_point2d()
    # test_better_point2d()
    # test_even_better_point_2d()
    test_point3d()
