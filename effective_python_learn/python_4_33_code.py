# -*- coding: utf-8 -*- 
# @Time : 2019/7/11 10:17 
# @Author : FengHao 
# @Site :  
# @File : python_4_33_code.py
# @Software: PyCharm Community Edition

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

class ValidataPolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Don't validate the abstract Polygon class
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass=ValidataPolygon):
    sides = None  # Specified by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Triangle(Polygon):
    sides = 3

print("Before class")
class Line(Polygon):
    print('Before sides')
    sides = 1
    print('After sides')
print('After class')

if __name__ == '__main__':
    pass
