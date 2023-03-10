# существуют 3 вида методов 
# class methods, instance methods, static methods


# isinstance methods - обычные методы, которые принимают первым аргументом self(ссылка на объект.)
# Нужны они для того чтобы внутри метода мы могли работать с атрибутами объекта.

# class A: 
#     def instance_method(self):
#         print('метод объекта')
#         print('первый аргумент', self)

# obj_a = A()
# obj_a.instance_method() #если вызываем у объекта, то self передается автоматически
# A.instance_method(obj_a,5) #если вызываем у класса, то в self нужно передать объект вручную

# class methods - методы, котороые принимают первым аргументом cls(ссылка на класс). 
# Нужны они для создания объектов или изменения атрибутов класса. Для того чтобы создать 
# класс методс нужно воспользоваться декоратором @classmethod

# class B:
#     @classmethod
#     def class_methods(cls,a):
#         print('класс метод')
#         print('первый аргумент:', cls)

# obj_b = B()
# print(B,'!')
# obj_b.class_method(5)
# B.class_method(5)

# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter

#     @classmethod
#     def _inc_counter(cls):
#         cls += 1

# obj1 = C()
# obj2 = C()
# obj3 = C()
# print(C.counter)


# class Pizza:
#     def __init__(self,radius, ingredients) -> None:
#         self.r = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f'готовится пицца размером {self.r * 2} cm')

#     @classmethod
#     def four_cheese(cls,r):
#         pizza = cls(r, 'сыр моцарела', 'чедер', 'голландский', 'брынза')
#         return pizza

# pizza1 = Pizza(17,'пеперони', 'моцарела', 'ананас')
# # pizza2 = Pizza(15, 'сыр моцарела', 'чедер', 'голландский', 'брынза')
# # pizza3 = Pizza(20, 'сыр моцарела', 'чедер', 'голландский', 'брынза')

# pizza2 = Pizza.four_cheese(15)
# pizza3 = Pizza.four_cheese(20)

# class Person:
#     surname = 'Stark'

#     def __init__(self,name, age) -> None:
#         self.name = name 
#         self.age = age

#     @classmethod
#     def from_birth_date(cls,name, date_birth):
#         from datetime import date 
#         age = date.today().year - date_birth
#         return cls(name, age) 

# obj = Person('John', 24)
# print(obj.name, obj.surname, obj.age)
# obj2 = Person.from_birth_date('Sansa', 1961)
# print(obj2.name, obj2.surname, obj2.age)

# staticmethod - просто функции внутри класса, которые не взаимодейтсвуют не с классом не с объектом.
# Находятся они внутри класса лишь потому что их используют только внутри класса, так как вне они бессполезны

# @staticmethod - декоратор 

# class C:
#     @staticmethod
#     def static_method():
#         print('статический метод!')

# obj = C()
# obj.static_method()
# C.static_method()


# class Cylinder:
#     def __init__(self,diameter, height) -> None:
#         self.di = diameter
#         self.h = height
#         self.area = self.get_area(self.di, self.h)

    
#     @staticmethod
#     def get_area(diameter, h):
#         from math import pi
#         circle = pi * (diameter / 2) ** 2
#         side = pi * h * diameter
#         area = circle * 2 + side
#         return round(area,2) 

# obj = Cylinder(10, 7)
# print(f'Area {obj.area}')
    
# obj1 = Cylinder(4,10)
# print(f'Area {obj1.area}')