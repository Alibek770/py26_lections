#Mixins
# Миксины - классы, которые будут использоваться для наследования, но от этих миксинов не создают объекты
# Для чего:

# 1. Вы хотите предоставить множество доп методов для класса 
# 2. Вы хотите использовать одну конкретную функцию во множестве разных классов

# class Machines:
#     def start_engine(self):
#         print('started engine!')

    
# class RadioMixin:
#     def play_radio(self):
#         print('music is playing')

# class Auto(RadioMixin, Machines):
#     pass

# class Plane(Machines):
#     pass

# class Train(RadioMixin,Machines):
#     pass

# obj = Auto()
# obj2 = Plane()
# obj3 = Train()

# obj.start_engine()
# obj.start_engine()
# obj.start_engine()

# obj.play_radio()
# obj3.play_radio()
'---------------------------------------------------------------'

# class FlyMixin:
#     def fly(self):
#         print('я могу летать')

# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')

# class SwimMixin:
#     def swim(self):
#         print('я могу плыть')

# class Human(WalkMixin, SwimMixin):
#     name = 'человек'

#     def talk(self):
#         print('я могу говорить')

# class Fish(SwimMixin):
#     name = 'рыба'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'летучая рыба'

# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     name = 'утка'


'task 1'

# class RadioMixin:
#     def play_music(self,title):
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(Auto,Boat,RadioMixin):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music('!')
# boat.play_music('!!')
# obj.play_music('!!!')

'task2'

# class Auto:
#     def ride(self):
#         print('Riding on a ground')
    
# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto,Boat):
#     pass

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 

'task3'
# class Clock: 
#     def current_time(self): 
#         print('17:10:41') 
# class Alarm: 
#     def on(self): print('08:00:00') 
#     def off(self): print('09:00:00') 
# class AlarmClock(Clock, Alarm):
#     def alarm_on(self): print('Будильник включён') 
# clock = AlarmClock() 
# clock.current_time() 
# clock.alarm_on()

'task5'

# class Square:
#     def __init__(self, side) -> None:
#              self.side = side

#     def get_area(self):
#         return self.side * self.side

# class Triangle:
#     def __init__(self, height, base) -> None:
#           self.height = height
#           self.base = base
#     def get_area(self):
#         return  int(0.5*self.base*self.height)

# class Pyramid(Triangle, Square):
#     def __init__(self, height, base) -> None:
#          super().__init__(height, base)

#     def get_volume(self):
#         return int(1/3*self.base**2*self.height)

# obj = Square(3)
# print(obj.get_area())

# obj2 = Triangle(3,5)
# print(obj2.get_area())

# obj3 = Pyramid(10,10)
# print(obj3.get_volume())

'task6'
# class CreateMixin:
#     def create(self,todo,key):
#         pass


# class DeleteMixin:
#     ...

# class UpdateMixin:
#     ...

# class ReadMixin:
#     ...




# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

#     def create(self,todo, key):
#         if not (key in list(ToDo.todos.keys)):
#             ToDo.todos[key] = todo
#         else: 
#             print('Задача под таким ключём уже существует"')
     
#     def set_deadline(self,deadline):
#         import datetime
#         time_ = datetime.datetime.today().day
#         list_ = time_.split('/')[0]
#         return int(list_) - time_

# obj_1 = ToDo()
# obj_1.create('помыть машину', 'car')
# print(obj_1.todos)

# 'task7'

# class Game:
#     def __init__(self,type,name,extensions):
#         self.type = type
#         self.name = name
#         self.extensions = extensions

#     def get_description(self):
#         get_str = [] 
#         print('Minecraft это инди-игра в жанре песочницы с элементами выживания и открытым миром. ')


# class ExtensionMixin:
#     def add_extension(self):


# class ExtensionMixin:
#     def add_extension(self, extension): 
#         self.extensions.append(extension) 
#         return f'Добавлено новое расширение {extension} для игры {self.name}' 
#     def remove_extension(self, del_extension): 
#         if del_extension in self.extensions: 
#             self.extensions.remove(del_extension) 
#             return f'{del_extension} был отключен от {self.name}' 
#             return 'Такого расширения нет в списке.' 
# class Game(ExtensionMixin):
#     def __init__(self, type, name): 
#         self.type = type 
#         self.name = name 
#         self.extensions = [] 
#     def get_description(self, description): 
#         return f'{self.name} это {description}' 
#     def get_extensions(self): 
#         res = ' '.join(self.extensions) 
#         return res if res else 'Нет подключенных расширений'

