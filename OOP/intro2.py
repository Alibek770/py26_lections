# class Human:
#     age = 0

#     def __init__(self, name, last_name, weight, nationality) -> None:
#         self.name = name + ' ' +last_name
#         self.weight = weight
#         self.nation = nationality
    
#     def birthday(self):
#         import random
#         print(f'\nHappy Birthday, {self.name}!!!')
#         self.age += 1
#         self.weight += random.randint(3,6)

# human1 = Human('John', 'Snow', 3.300, 'American') 
# human2 = Human('Elon', 'Musk', 4.100, 'Kazakh')

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# print('After one year:')

# human1.birthday()
# human2.birthday()

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)

# human1.birthday()
# human2.birthday()
# human1.birthday()
# human2.birthday()
# human1.birthday()

# print(human1.name, human1.age, human1.weight, human1.nation)
# print(human2.name, human2.age, human2.weight, human2.nation)


'------------------------------------------------------------------------------'

# class Student:
#     univer = 'MIT'

#     def __init__(self, name, last) -> None:
#         self.name = f'{name} + {last}'
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False
    
#     def add_points(self, points):
#         self.knowledge += points
#         if self.knowledge > 500:
#             self.is_ready_to_work = True
#             print(f'{self.name} is ready to work!!')

#     def read_book(self, books):
#         self.books.append(books)
#         self.add_points(50)
    
#     def do_lab_work(self):
#         self.add_points(50)

#     def do_project(self):
#         self.add_points(100)

#     def learn_new_language(self, language, points):
#         if not points in range(70,101):
#             raise Exception('Invalid points')
#         self.languages[language] = points
#         self.add_points(points)

# st1 = Student('John', 'Snow')
# st2 = Student('Jamie', 'Lanister')
# print(st1.name)
# print(st2.name)
# print('Before study {st1.name}', st1.books, st1.languages,st1.knowledge)
# print(f'Ready to work: {st1.is_ready_to_work}!')

# st1.read_book('Game of Thrones')
# st1.read_book('Martin Iden')
# st1.read_book('Alghoritms and Data Structures')
# st1.read_book('Eugene Onegin')

# st1.do_lab_work()
# st1.do_lab_work()
# st1.do_project()
# st1.learn_new_language('Python', 90)
# st1.learn_new_language('C++', 75)
# print(f'After study {st1.name}, {st1.books}, {st1.languages},{st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_to_work}!')
'------------------------------------------------------------------------------'
# class Car:

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model 

# def __str__(self) -> str:
#     return f'{self.brand} -> {self.model}'
    
# obj = Car('BMW', '7 series')
# obj2 = Car('Mercedes-Benz', 'w140')
# obj3 = Car('Kia', 'K8')

# print(obj.brand, "!")
# print(obj2.brand, "!!")
# print(obj3.brand, "!!!")

'------------------------------------------------------------------------------'

# class Soda:
#     def __init__(self, ingredient = None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None
        
    
#     def show_my_drink(self):
#         if self.ingredient:
#             print(f'Gazirovka iz {self.ingredient}!')
#         else:
#             print(f'Normal gazirovka')


# a = Soda('Malina')
# a.show_my_drink()

# b = Soda()
# b.show_my_drink()

# class A:
#     pass

# a = A()
# b = 5
# print(isinstance(a, A))
# print(isinstance(b, A))

'------------------------------------------------------------------------------'

# class TriangleChecker():
#     def __init__(self, sides:list) -> None:
#         self.sides = sides

#     def __str__(self) -> str:
#         if not all(isinstance(x, (int,float)) for x in self.sides):
#             return 'нельзя построить треугольник так как все стороны должны быть числами!'
#         if any(x <= 0 for x in self.sides):
#             return 'Нельзя потсроить треугольник так как все стороны должны быть больше нуля'

#         self.sides.sort()
#         if self.sides[0] + self.sides[1] <= self.sides[-1]:
#             return "Нельзя построить треугольник так как сумма двух сторон должна быть больше самой длинной стороны!"
#         return 'Мы можем построить треугольник'



    

# t1 = TriangleChecker([19,12,8])
# print(t1)


'----------------------------------Tasks---------------------------------'

'Task1'

# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year 
#     def show_title(self):
#         return f'Название этой песни {self.title}'
#     def show_author(self):
#         return f'Автор этой песни {self.author}'
#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'
# song = Song(title = 'Happy', author = 'Pharrell Williams', year = 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

'Task2'

# class Circle:
#     color = 'синий'
#     pi = 3.14

# def __init__(self,radius = int) -> int:
#     self.radius = radius

# def get_area(self):
#     return self.pi*(self.radius ** 2) 

# circle = Circle(radius=13)
# circle.color = 'желтый'
# print(circle.color())
# print(circle.get_area())

'Task3'

# class BankAccount: 
#     def __init__(self): 
#         self.balance = 0 
        
#     def withdraw(self, amount): 
#         self.balance -= amount 
#         print(f'Ваш баланс: {self.balance} сом') 
#     def deposit(self, amount): 
#         self.balance += amount 
#         print(f'Ваш баланс: {self.balance} сом') 
# account = BankAccount() 
# account.deposit(1000) 
# account.withdraw(500)

'Task4'

# class Taxi:
#     def __init__(self,name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self, km):
#         self.cost = self.cost_km * km + self.cost
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом'

# taxi1 = Taxi('Namba', cost=10, cost_km=15)
# taxi2 = Taxi('Yandex', cost=11, cost_km=16)
# taxi3 = Taxi('Jorgo', cost=12, cost_km=17)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14)) 

'task 5'
# class Phone:

#     def __init__(self,name,last_name,phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')
# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()

'task 6'

# class Salary:
#     percent = 8

#     def __init__(self, salary,experience):
#         self.salary = salary
#         self.experience = experience
    

#     def count_percent(self):
#         nalog = (self.salary * self.experience) / 100 * self.percent
#         return nalog

# obj = Salary(10000, 10)
# print(obj.count_percent())       

'task7'

# import datetime 
# class Nobel:
#     def __init__(self,category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#     def get_year(self):
#         date_obj = datetime.date.today()
#         k = date_obj.year[]
#         res = k - self.year
#         return f'выиграл {res} лет назад'
# obj1 = Nobel("Литература", 1971, "Пабло Неруда")
# obj2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(obj1.category, obj1.year, obj1.winner)
# print(obj2.category, obj1.year, obj1.winner)
# print(obj1.get_year())
# print(obj2.get_year())