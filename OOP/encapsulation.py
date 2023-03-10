# Инкапсуляция:
# 1. Связь данных с методами которые должны управлять этими аттрибутами

# 2. Механизм языка, который позваоляет ограничить доступ к определенным компонентам класса.

# 3. Инкапсуляция как связь

# class Phone:
#     number = '+996707007007'

# def print_number(self):
#     print(f'Мой номер: {self.number}')

# my_phone = Phone()

# my_phone.print_number()

# Инкапсуляция как управление доступом
# 3 уровня доступа в питоне
    # 1. Публичный(public) - number, print_number
    # 2. Защищенный(_protected, parent/child) - _number
    # 3. Приватный(__private, только в текущем) - _number

# class Car:
#     _country = 'Germany'

#     def __init__(self) -> None:
#         self.marka = 'Mercedes-Benz'
#         self._model = 'w140'
#         self.__motor = 'ABC' #private

# obj = Car()
# print(obj.marka)
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)

# class Phone:
#     username = 'John Snow'
#     _caller = 'jamie Lanister'
#     __count_of_calls = 15

#     def call(self):
#         print(f"{self._caller} звонит!")

#     def __increament_of_calls(self):
#         self.__count_of_calls += 1

#     def turn_on(self):
#         print(f'{self.username} взял трубку!')
#         self.__increament_of_calls()

#     def get_count(self):
#         print(self.__count_of_calls)

# obj = Phone()
# obj.get_count()
# obj.call()
# obj.turn_on()
# obj.get_count()

# getter & setter

# Они используются для получения и установки значений в защищенные атрибуты, чтобы избежать 
# прямого доступа к защищенному аттрибуты и еще с помощью сеттеров и гетторов можно добавлять 
# логику проверки при получении данных

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.age = 0

#     def display_info(self):
#         print(f'My name is {self.name}, I\'m {self.age} years old!')

# john = Person('John')
# john.display_info()
# john.name = None
# john.age = -18
# john.display_info()

# class Person:
#     def __init__(self, name) -> None:
#         self.__name = name
#         self.__age = 0

#     def display_info(self):
#         print(f'My name is {self.__name}, I\'m {self.__age} years old!')

#     #getter
#     def get_name(self): return self.__name


#     #setter
#     def set_name(self,name):
#         if not isinstance(name,str):
#             print('Invalid Value!')
#         else:
#             self.__name = name

#     def get_age(self): return self.__age

#     def set_age(self,age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print('Invalid value for age')
#         else:
#             self.__age = age

# john = Person('John')
# john.display_info()
# john.set_name(None)
# john.set_age(-18)
# john.display_info()
# john.set_name('Jamie')
# john.set_age(24)
# john.display_info()

# class Russia():
#     __name = 'Russian Federation'
#     __population = 0

#     def get_population(self): return self.__population

#     def set_population(self, num):
#         if not isinstance(num,int) or num < 0:
#             print('Invalid vlaue for population')
#         else:
#             self.__population = num
    
#     def get_name(self): return self.__name

#     def display_info(self):
#         print(f'population of {self.get_name()}: {self.get_population()}')


# obj = Russia()
# obj.set_population(143_000_000)
# obj.display_info()
# obj.display_info()

'------------------------------------------------------'

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 0

#     def _age_increament(self):
#         self.__age += 1

#     def birthday(self):
#         print(f'{self.name}s birthday')
#         self._age_increament()

#     def display_info(self):
#         print(self.name, self.__age)
    
# obj = Person('John')

# obj = Person('John')
# obj.display_info()
# obj.birthday()
# obj.display_info()

# class Test:
#     def __init__(self) -> None:
#         self.__card_number = value

#     def get_card_number(self): return self.__card_number 

#     def set_card_number(self, value = None):
#         self.__card_number = value 

# a = Test(5)
# print(a.get_card_number())
# a.set_card_number()
# print(a.get_card_number())