# Множественное наследование - это когда класс наследуется от двух и более классов

# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing')


#     def ride(self):
#         print('We\'re riding on the ground!')

# class Plane:
#     def play_music_at_station(self):
#         print('Listening Ed Sheeran!')

#     def fly(self):
#         print('We\'re flying!')

# class FutureAuto(Auto,Plane):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()

'---------------------------------------------------------------'

# class A:
#     def print_a(self):
#         print('A')

# class B:
#     def print_b(self):
#         print('B')

# class C:
#     def print_c(self):
#         print('C')

# class MyCLass(A,B,C):
#     pass

# obj = MyCLass()
# obj.print_A()
# obj.print_B()
# obj.print_C()
# print(MyCLass.mro())

# class Test:
#     pass

# a = Test()
# print(Test.mro())
# print(dir(a))
'---------------------------------------------------------------'

# 'MRO (Method Resolution Order - механизм для корректного поиска родительских методов'. 
# 'Был создан для рещения проблемы ромба,которая появилась после введения класса object в пайтон.'
# 'Поиск идет таким образом что если у родительских классов один общий предок, то идет посик в ширину'

# Проблема ромба(решена с помощью mro)

# class Zero:
#     def say(self):
#         print('class Zero!')

# class First(Zero):
#     def say(self):
#         print('class first')

# class Second(Zero):
#     def say(self):
#         print('class Second')

# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('My Class')

# obj = MyClass()
# obj.say()
# print(MyClass.mro())

# проблема перекрестного наследования

# class Y:
#     pass

# class X:
#     pass

# class A(X,Y):
#     pass

# class B(X,Y):
#     pass

# class MyMRO(type):
#     def mro(cls) -> list[type]:
#         return [cls, A, B, X, Y, object]

# class MyClass(A,B, metaclass = MyMRO):
#     pass

# obj = MyClass()
# print(MyClass.mro())
'---------------------------------------------------------------'
