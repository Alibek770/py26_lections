#  операторы сравнения
#  условные операторы 
#  логические операторы 

# операторы сравнения
# <,>,==, <=,>=,!=(не равно)

# num1 = 18
# num2 = 15
# print(num1 >= num2)

# stroka1 = 'hello'
# stroka2 = 'world'
# print(ord('H'))
# print(ord('W'))
# print(chr(1100))

# text = "Hello world! My name is John!"

# if ord(text[0]) == 72:
#     print('Yes!')
    
# else: 
#     print('Noooo!')

# условные операторы -  они созданы, чтобы программа могла выполнять разные участки кода взависимости от условия
# if, elif, else 

# if <condition>: 
#     <body if>
#     <body if> #сработает только если true
#     elif <condition>:
#         <body elif>
# elif <condtion>:
#     <body elif>
# else:
#     <body else> #сработает только если во всех остальных false

# string = input("Enter smth: ")

# if string == 'Hello':
#     print("Hello Stranger!")
# elif string == 'John': 
#     print("Welcome back, John Snow!")
# elif string == 'Mercedes':
#     print("mercedes Benz S-class!")
# else: 
#     print('совпадений не найдено')
#     print('The end!')

# email = input("Enter Email: ")
# passworrd1 = input("Enter password: ")

# if len(passworrd1) < 8:
#     raise Exception("Password too short: (password need at least 8 characters!")

# password2 = input('Enter password confirmation: ')

# if password2 != password2:
#     raise Exception('password did not match')
# else:
    # print('Succesfully signed up')

# age = input("Enter your age: ")

# if age.isdigit():
#     age = int(age)
#     print(f'Your age: {age}!')

# else: 
#     raise Exception("Enter the valid age(only digits ")

# if age > 170:
#     raise Exception("Invalid age")    

# if age < 21:
#     print(f'Your age is too young, come after {18 - age} let/goda!')
# else:
#     print('You are able\' your age is good, Welcome!')

# "Логические операторы"
# and -> логическое и  
# or -> лог или
# not -> лог отрицание

# операторы индентификации
# in -> проверяет наличие элемента внутри массива либо строки
# is -> сравнивает ячейки памяти 
# == сравнивает значения
# is not -> отрицательное сравнение двух ячеек

# my_age = 20
# other_age = 18
# result = my_age == 21 or other_age == 18
# print(result)

# result = not my_age==21
# print(result)

# cash = int(input('Enter your cash: '))

# if cash > 1000 and cash < 10000:
#     print("Middle")
# elif  cash >= 10000 and cash < 100_000:
#     print("A lot")
# elif cash >= 100_000:
#     print("Perfect")
# else: 
#     print('not good at all')

# is_google_user = True
# is_github_user = False
# is_age_less_21 = False
# user_coin = 5000

# if (is_google_user or is_github_user) and (is_age_less_21 or user_coin>=5000):
#     print('You can enter the system')
# else: 
#     print('Sorry, you can not enter')

# str1 = 'Hello World'
# choice = input("Enter the character: ")

# if choice in str1:
#     print(f'symbol {choice} in the stroke: "{str1}"!')

# else:   
#  print(f'symbol {choice} not in the stroke: "{str1}"!')

# a = 5
# b = 10

# print(b =='10')

# makers.kg #18

# string = int(input("Число от 1 до 12 "))
# if string == 1 or 2 or 12:
#     print("зима")
    
# elif string == 3 or 4 or 5:
#     print("весна")

# elif string == 6 or 7 or 8:
#     print("лето")

# elif string == 9 or 10 or 11:
#     print("осень")

# else:
#     print("Такого месяца нет")

# str = int(input("Введите строку"))
# if str.isdigit():
#     print("is digit")
# if str.isalpha():
#     print("is alpha")
# else: 
#     print(" is ASCII")

# makers kg

# number 21


# a = int(input())
# b = int(input())
# c = int(input())
# if (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
#     print("rectangular")
# elif (c**2 < a**2 + b**2) or (a**2 < b**2 + c**2) or (b**2 < a**2 + c**2):
#     print("acute")
# elif (c**2 > a**2 + b**2) or (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2):
#     print("obtuse ")
# else:
#     print("impossible")








