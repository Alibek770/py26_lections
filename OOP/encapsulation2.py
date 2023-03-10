# Анотация свойств( @property(getter setter))

# class Person:
#     __name = 'John'
#     __age = 22
#     __code = '+996'
#     __number = '555777666'
#     __full_number = __code + __number

#     @property
#     def name(self):
#         '''The name property(getter)'''
#         print('Getter!')
#         print(self.__name)

#     @name.setter
#     def name(self,value):
#         print('Setter')
#         if not isinstance(value, str):
#             print('Не валидные данные')
#             return
#         self.__name = value

#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self,value):
#         if not isinstance(value,int) or not 0 < value < 170:
#             print('Not valid')
#             return
#         self.__age = value

#     def number(self):
#         name = input('Введите свое имя: ')
#         if self.__name != name:
#             print('Invalid name!!')
#             return
#         print(self.__full_number)

#     @number.setter
#     def number(self,value: dict):
#         '''value must be list, first element code and second number!'''
#         if value['code'] != '+996':
#             print('must be Kyrgyzstan number!')
#         elif len(value['number']) != 9:
#             print('Invalid number')
#         self.__code = value['code']
#         self.__number = value['number']
#         self.__full_number = self.__code + self.__number


# obj = Person()
# obj.name
# obj.name = 'Raychel'
# obj.name 
# obj.age 
# obj.number
# obj.number = {'code': '+55', 'number': '706899004'}
# obj.number
# obj.number = {'code': '+996', 'number': '707180562'}
# obj.number

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius

#     @property
#     def radius(self):
#         return self.__radius

#     @radius.setter
#     def radius(self,value):
#         if not isinstance(value,(int,float)):
#             raise Exception('Invalid value, must be ann int on float object!')
#         self.__radius = value

# circle = Circle(42)
# print(circle.radius)
# circle.radius = 15
# print(circle.radius)
    
'Task1'

# class A:
#     def public(self):
#         return 'Public method'

#     def _protected(self):
#         return 'Protected method'

#     def __private(self):
#         return 'Private method'
    
#     def print_protected(self): 
#         self._protected() 
     
#     def print_private(self):
#         self.__private() 

# obj1 = A()
# print(obj1.public()) 
# print(obj1.print_protected())
# print(obj1.print_private())

'Task 2'

# class A:
#     def method1(self):
#         print('Hello World')

# class B(A):
#     pass

# b1 = B()
# b1.method1()

'Task3'

# class Car:
#     __speed = 0

#     def set_speed(self,new):
#         self.__speed = new

#     def show_speed(self):
#         return self.__speed

# car1 = Car()
# print(car1.show_speed())
# car1.set_speed(20)
# print(car1.show_speed())

'Task4'
# class Car:
#     __speed = 0
#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self,new):
#         self.__speed = new
#         return self.__speed

# car1 = Car()
# print(car1.speed)
# car1.speed = 20
# print(car1.speed)

'Task5'
# class Person:
#     name = 'John'
#     _phone_number = '+996 557 55 17 57'
#     __card_number = '9999 9999 9999 9999'

#     @property
#     def number(self):
#         return self.__card_number

# john = Person()
# print(john.name)
# print(john._phone_number)
# print(john.number)

'Task6'
# class Person:
#     def __init__(self,name,phone_number, card_number):
#         self.name = name 
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     @property
#     def number(self):
#         return self.__card_number

# john = Person('john','+996 557 55 17 57', '9999 9999 9999 9999')
# print(john.name)
# print(john._phone_number)
# print(john.number)

'Task 7'
# class Person: 
#   name = "John" 
#   _phone_number = "+996 557 55 17 57" 
#   __card_number = "9999 9999 9999 9999" 
#   def get_number(self): 
#     return self.__card_number 
#   def set_number(self): 
#     self.__card_number = None 
#     return self.__card_number 
# john = Person() 
# john.name = None 
# john._phone_number = None a
# print(john.name) 
# print(john._phone_number) 
# print(john.set_number())

'Task 8'
# class Person:
#     def __init__(self,name, phone_number, card_number):
#         self.name = self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number
    
#     def __validate_name(self,name):
#         if len(name) < 2:
#             return 'John'
#         return name.title() 
    
#     def get_item(self):
#         return self.__card_number

# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(sam.name)
# print(sam._phone_number)
# print(sam.get_item())


'Task 9'
# class Person: 
#     def __init__(self, name, phone_number, card_number): 
#         self.name = name 
#         self._phone_number = self._validate_phone_number(phone_number) 
#         self.__card_number = self.__validate_card_number(card_number) 

#     def _validate_phone_number(self, phone_number): 
#             if isinstance(phone_number, int) and str(phone_number).startswith('996'): return phone_number 
#             return None 
            
#     def __validate_card_number(self, card_number): 
#             if isinstance(card_number, int) and len(str(card_number)) == 16: 
#                 return card_number 
#             return None 

# tolik = Person('Sam', 996557551757, 9999999999999999) 
# print(tolik.name) 
# print(tolik._phone_number) 
# print(tolik._Person__card_number)

'Task15'
# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None

#     def get_name(self):
#         return self.__name

#     def set_name(self,name):
#         self.__name = name 

#     def get_last_name(self):
#         return self.__last_name
    
#     def set_last_name(self,last_name):
#         self.__last_name = last_name 
    
#     def get_age(self):
#         return self.__age 
    
#     def set_age(self,age):
#         self.__age = age 

#     def get_email(self):
#         return self.__email

#     def set_email(self,email):
#         self.__email = email 

# john = Person()
# print(john.get_name()) 
# print(john.get_last_name()) 
# print(john.get_age())
# print(john.get_email())
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name())
# print(john.get_last_name()) 
# print(john.get_age()) 
# print(john.get_email())