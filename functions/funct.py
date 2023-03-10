# num1 = 4
# num2 =6
# num3 = 7
# num4 = 9
# num5 = 15

# def operations(num):
#     print({'2': num ** 2, '3': num3, '100' : num / 100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)

# Функция - это именованная часть программы, 
# которая содержит в себе определенный набор инструкций,и которая может вызываться в других частях программы столько раз сколько угодно 

# def name_of_function(<a, b>) #параметры ]

    # <body> # код, какая то логпка который возвращает конечный результат 

    #<return> # оператор для вощвращения результата

    #name_of_function(<5,6> #аргументы)

    # Параметры функции -  переменные которые будут принимать данные которые мы передаем в функцию

#Аргументы - данные которые ммы передаем в функцию в моменте когда ее вызываем

# return - оператор который нужен для того чтобы фунция возвращала результат, если return не указать то фунция возвращает None 


# ls = [1,2,23,3,4,5,5,6]

# str1 = 'Hello World'



# def our_len(obj ):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#         print('result:', i)

# our_len(ls)
# our_len(str1)

# res = max([1,2,3,4])
# print(res)
# print(max([1,2,3]))


# def isEven(num):
#     if num % 2 == 0:
#         return True 
#     else: 
#         return False
# print(isEven(7))
# print(isEven(9))
# print(isEven(10))

# def isEven(obj:int) -> bool:
#     '''Our function returns True or False while checking number for even number'''
#     if obj % 2 == 0:
#         return True
#     return False

# print(isEven ())

# from typing import List

# def get_polindrom(words: List[str]) -> List[str]:
#     '''Function return a polindrom list of strings!'''
#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             r
#             result.append(x)
#     return result

# ls = ['John', 'Ono', 'kazak', 'peter', 'dovod', 'radar', 'apa', 'piko']
# print(f'result: {get_polindrom(ls)}')
# print(get_polindrom(['john', 'snow', 'from']))

'''Напишите функцию которая будет возвращать ваш депозит через определнное время с процентом 10%, 
возращать финальное количество денег. Мин периодa вложения 3 года. Мин ставка денек 30 000 сомов'''

# from typing import Optional

# def get_percentage(money: float, period: int) -> float:
#     '''returns final amount of money'''
#     if money> 30000:
#         raise ValueError('Invalid value for money')
#     elif period < 3:
#         raise ValueError ('Invalid value for period parametr!')

#     i = 0
#     while i < period:
#         money += money * 0.1 
#         # money = money * 1.1
#         #money = money + (money / 100 * 10)
#         i +=1 
#     return money

# try:
#     money = float(input("Сколько денег вы вложили? "))
#     time = int(input("На какой срок вы вложили денеждные средства? "))
# except ValueError:
#     print('Invalid values!')
# else:
#     print(get_percentage(money, time))

 
'----------------------------------------------------------------------------'

# Default parametres

# def func():
#     print('Hello World!')

# def print_welcome(name='user'):
#     print(f'welcome,{name} ')

# print_welcome('John Snow')

# def introduce(name: str, lastname: str, work: str = None):
#     print(f'This persons name is {name}')
#     print(f'This persons last name is {lastname}!')
#     if work:
#         print(f'This persons work is {work}! ')

# introduce('John', 'Snow')
# introduce('Sultan' 'Katana')

'----------------------------------------------------------------------------'



# def get_reverse_text(text:str) -> str:
#     '''reversing the text'''
#     ls = text.split(' ')
#     # print(ls[::-1])
#     return ' '.join(ls[::-1])

# str = 'Hello World! My name is John, lastname is Snow. Nice to meet you!'

# get_reverse_text(str)

# task 1
# def add (a,b):
#      return a+b 
# print(add(2,3))
# task 2
# def get_string_length(str):
#     return len(str)
# print(get_string_length('hello'))

# task 4
# def divide(int1, int2):
#     return int1/int2
# print(divide(5,10))

# def is_palindrome(Mom):
#     for x in Mom:
#         if x == x:
#             return True
#         else: 
#             return 'False'

# task 11


# def func11(a,b,c):
#     if c != 0:
#         return (a + b)/c
#     else:
#         return a + b
# print(func11(5,6,0))

# task 10
# def sum_digits(num):
#      return(sum([int(x) for x in str(num)])) 
# print(sum_digits(105))

# # task 12
# def func12(str):
#     x for x func12:
#     return x.lower
# print((["hEllo", "wORld"]))

# def get_info(lastname, name = 'пользователь'):
#   return f' привет {name}, по фамилии {lastname}'
# welcome(last_name = Пушкин, name = Александр)
# print

# task13

# def func13(str): 
#     return {x:str.count(x) for x in str} 
# print(func13("Hello"))

# def welcome(name,last_name):
#     return f'welcome {name}, {last_name}'
# name = input('Введите ваше имя:' )
# last_name = input('Введите вашу фамилию: ')
# print(welcome (name, last_name))