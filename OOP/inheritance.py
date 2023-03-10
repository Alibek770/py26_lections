"Принципы ООП"

# 1. Наследование
# 2. Инкапсуляция 
# 3. Полиморфизм 

# 4. Абстракция 
# 5. Композиция 
# 6. Агрегация 

'--------------------------------------------------------------------------'

# Наследование 
# Наследование позволяет принимать родительсие методы и атрибуты для дочернего класса


# Родительский класс
# Дочерний класс

'--------------------------------------------------------------------------'

# class Animal:
#     def print_info(self):
#         print('I\'m an animal')

# class Croco(Animal):
#     pass

# croco = Croco()
# croco.print_info()

'--------------------------------------------------------------------------'

# class Animal:
#     name = None
#     golos = None 
#     meal = None 

#     def say(self):
#         print(f'This animal is{self.name}:{self.golos}')


#     def eat(self):
#         print(f'This animal is {self.name} eats {self.meal}')

    
# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meal = 'meat'
#     griva = True

#     def info(self):
#         print(f'This is king of animals {self.name}')

# class Dog(Animal):
#     name = 'dog'
#     golos = 'roar'
#     meal = 'meat'

# class Koala(Animal):
#     name = ' koala'
#     golos = 'roar'
#     meal = 'efkalipt'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()

# simba.say()
# simba.eat()
# simba.info()

# julian.say()
# julian.eat()


'--------------------------------------------------------------------------'

# class Person:
#     def info(self):
#         print('I\'m person from Bishkek')

# class Student(Person):
#     def info(self):
#         super().info()
#         print('Im study at Manas university!')

# obj = Student()
# obj.info()

# obj2 = Person()
# obj2.info()


'--------------------------------------------------------------------------'

# class Laptop:
#     def __init__(self,brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price


#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'price' : self.price}

# class MacBook(Laptop):
#     def __init__(self, brand, model, price, year, display):
#         super().__init__(brand, model, price)
#         self.year = year
#         self.display = display 
#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['display'] = self.display
#         return repr

# class Acer(Laptop):
#     def __init__(self, brand, model, price, videocard, display):
#         super().__init__(brand, model, price)
#         self.videocard = videocard
#         self.display = display
#         return repr


#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] = self.videocard
#         repr['display'] = self.display
#         return repr

# mac = MacBook('Apple', 'Air', 1000, 2022, 13)
# print(mac.get_info())

# acer = Acer('Acer', 'Swift', 600, 'gge force 3040', 'xRGB', '14')
# print(acer.get_info())

'--------------------------------------------------------------------------'

# class Employee:
#     bonus = 1.5

#     def __init__(self, first_name, last_name, salary):
#         self.name = f'{first_name} {last_name}'
#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'
        
#     def give_increase(self):
#         self.salary = self.salary * self.bonus
        
#     def __str__(self) -> str:
#         return self.get_info() 

# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language):
#         super().__init__(first_name, last_name, salary)
#         self.prog_lang = language

#     def get_info(self):
#         info = super().get_info()
#         info += ', Prog Language: {self.prog_lang}'
#         return info 
    
    
# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs = []):
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs 

#     def add_devs(self, developer):
#         self.devs.append(developer)

#     def show_devs(self):
#         return [x.get_info() for x in self.devs]

# dev1 = Developer('John', 'Snow', 1500, 'Python')
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
# dev3 = Developer('Lary', 'Page', 1500, 'JS')
# dev4 = Developer('Tirion', 'Lanister', 1000, 'Python')

# man1 = Manager('Jamie', 'Lanister', 2000)
# man2 = Manager('Dastan', 'Katana', 4000, [dev3, dev2])

# print(f'Manager {man1.get_info()}, has {man1.show_devs()} developers!')
# print(f'Manager {man2.get_info()}, has {man2.show_devs()} developers!')

# man1.add_devs(dev1)
# man1.add_devs(dev4)
# man2.add_devs(dev1)

# print('\nAfter:')
# print(f'Manager {man1.get_info()}, has {man1.show_devs()} developers!')
# print(f'Manager {man2.get_info()}, has {man2.show_devs()} developers!')

# dev1.give_increase()
# man2.give_increase()

# print(dev1)
# print(man2)
 
"Task1"
# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass
# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass
# obj = Class2() 
# obj.first() 
# obj.second()
#  obj.third()
#  obj.fourth()

"Task2"
# class A:
#     def method1(self): 
#         print(f'Основной функционал') 
# class B(A): 
#     def method1(self): 
#         super().method1() 
#         print(f'Дополнительный функционал')
# obj = B() 
# obj.method1()

"Task3"
# class MyString(str): 
#     def __init__(self, stroka1): 
#         self.stroka1 = stroka1 
#     def append(self, stroka2): 
#         self.stroka2 = stroka2 
#         self.stroka1 = self.stroka1 + self.stroka2 
#         return self.stroka1 
#     def pop(self): 
#         last_w = self.stroka1[-1] 
#         self.stroka1 = self.stroka1[:-1] 
#         return last_w 
#     def __str__(self) -> str: 
#         return self.stroka1 
# example = MyString('String') 
# example.append('hello')
# print(example.pop()) 
# print(example)

"Task4"
# class MyDict(dict): 
#     def get(self, key): 
#         result = 'Are you kidding?' 
#         return dict.get(self, key, result) 
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))

"Task5"

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         return f"name:{self.name}, age:{self.age}"
    
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().init(name, age)
#         self.faculty = faculty
    
#     def display_student(self):
#         get_info = super().display()
#         return get_info + f", faculty:{self.faculty}"
    
# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display())
# print(obj_student.display_student())

'task 6'
# class ContactList(list):
#     def init(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         a = []
#         for i in self.list_:
#             if name in i:
#                 a.append(i)
#         return a

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))



'task 7'
# class Person:
#     def init(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         return f"name:{self.name}, age:{self.age}"
    
# class Student(Person):
#     def init(self, name, age, faculty):
#         super().init(name, age)
#         self.faculty = faculty
    
#     def display_student(self):
#         get_info = super().display()
#         return get_info + f", faculty:{self.faculty}"
    
# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display())
# print(obj_student.display_student())

'task 8' 
# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
        
    
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(str_):
#     if str_.islower():
#         raise capitals_error
#     else:
#         return(f'ВСЕ ОТЛИЧНО! {str_}')

# print(check_letters("HELLO"))



