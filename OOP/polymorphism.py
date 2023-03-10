#функция полиморфизма - len()

# print(len('makers'))
# print(len([1,2,3,4,5]))
# print(len({1:2,3:4}))

# +(__add__) - метод полифморфизмма

# print(5+5)
# print('hello' + 'world')
# print([1,2,4] + [5,6,8])

# Полиморфизм - способность метода обрабатывать данные разных типов(объектов от класса),
# обычно это реализуется путем создания базового класса и наличия двух иои более подклассов,
# которые все реализуют(переопределяют) методы с одинаковой сигнатурой(названием).

 
# Широко распрастраненное определение: 'Один интерфейс - много реализаций'

# class Animal:
#     def info(self):
#         pass


#     def make_sound(self):
#         pass

    

# class Dog(Animal):
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 


#     def info(self):
#         print(f'it\'s a dog. Dog name is {self.name}, age {self.age}')


#     def make_sound(self):
#         print('Gav Gav')

    

# class Cat(Animal):
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 


#     def info(self):
#         print(f'it\'s a cat. Cats name is {self.name}, age {self.age}')


#     def make_sound(self):
#         print('Meow Meow')


# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 9)

# for obj in (cat,dog):
#     obj.info()
#     obj.make_sound()
#     print()


# list.pop
# set.pop
# dict.pop

'----------------------------------------------------------------------------------------------------------'

# Абстракция(Абстрактный класс) - его можно рассматривать как набор методов, которые должны
# быть реализованы во всех дочерних классах, которые будут унаследованы от абстрактого класса


# Абстрактный метод - это метод у которого есть объявление но нет реализации

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def info(self):
#         pass

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Квадрат')
#         self.length = length

#     def area(self):
#         return self.length ** 2 

#     def info(self):
#         print(f'Я {self.name}, у меня етсь углы равные 90 градусам!')

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2  

#     def info(self):
#         print(f'Я {self.name}, и я фигура в двумерной плоскости!')

# a = Square(4)
# b = Circle(4)

# for x in (a,b):
#     x.info()
#     print(x.area())
#     print()

# from abc import ABC, abstractclassmethod

# class ChessPiece(ABC):
#     # общий метод, который будут использовать все наследники класса
#     def take(self):
#         print('Take a chess piece!')

#     #абстрактный метод, который необходимо переопределить для каждого наследника
#     @abstractclassmethod
#     def move(self):
#         pass

# class Queen(ChessPiece):
#     def move(self):
#         print('Quenn moves where she wants diaganolly, vertically and horizontally')

# class Pawn(ChessPiece):
#     def move(self):
#         print('The pawn can move directly to one cell')

# class Horse(ChessPiece):
#     def move(self):
#         print('')
    
# q = Queen()
# p = Pawn()
# q.move()
# q.take()
# print()
# p.move()
# p.take()
'----------------------------------------------------------------------------------------------------------'

# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, 
# краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# class Phone:
#     def __init__(self, os, imei):
#         self.__imei = imei
#         self.__battery_level = 100
#         self.__os = os

#     @property
#     def battery_level(self):
#         if self.__battery_level < 0.5:
#             self.__battery_level = 0
#             raise Exception('Telefon razryazhen!')
#         self.__battery_level -= 0.5
#         print(self.__battery_level)
        
#     @property
#     def get_info(self):
#         if self.__battery_level < 0.5:
#             self.__battery_level = 0
#             raise Exception('Telefon razryazhen!')
#         self.__battery_level -= 0.5
#         print(f'OS: {self.__os}, IMEI: {self.__imei}')

#     def play_music(self):
#         if self.__battery_level <= 5:
#             self.__battery_level = 0
#             raise Exception ('Telefon razryazhen!')
#         self.__battery_level -= 5
#         print('Slushaem Mirbeka Atabekova!')

#     def play_video(self):
#         if self.__battery_level <= 10:
#             raise Exception ('Nedopustimyi uroven zaryada!')
#         self.__battery_level -= 7
#         print('Smotrim Toples!')

#     def charge_battery(self, sec):
#         from time import sleep
#         i = 1
#         while i <= sec:
#             sleep(1)
#             if self.__battery_level <100:
#                 self.__battery_level += 1
#                 if self.__battery_level > 100:
#                     self.__battery_level = 100
#             print(f'Zaryad idet! Vash uroven zaryada: {self.__battery_level}')
#             i += 1

# phone = Phone('IOS 15', '241325-113')
# phone.battery_level
# phone.get_info
# phone.play_music()
# phone.play_video()
# phone.battery_level
# phone.charge_battery(20)
# phone.battery_level