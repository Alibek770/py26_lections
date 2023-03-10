# sentence = input('Введите предложение: ')
# if sentence [-1] == '?':
#     print('Вопросительное предложение')
# else:
#     print('Обычное предложение')

'Тринарные операторы'

# print('Вопросительное предложение' if sentence[-1] == '?' else 'Обычное предложение')

'---------------------------------------- Ternary operators -------------------------------------------------------'

#Ternary operators(Тернарный оператор) - это конструкция, которая аналогична по своему действию конструкции 
# if/else, но при том записывается в одну строчку.

# number = 21
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)

# <выражение если в условии True> if <условие> else <выражение если в условии <False>

# num = int(input('Vvedite chislo: '))

# res = num -100 if num < 100 else num * 2
# print(res)

# ls = [55, 65, 75, 89, 100, 15,6]
# print(ls)
# choice =  input('Vvedite max/min: ')
# res = max(ls) if choice.lower().strip() == 'max' else min (ls)
# print(res)

'-----------------------------------------------------------------------------------------------'

# -

# print(digits)
# print(type(digits))

# num = int(input('num: '))
# if num.isdigit():
# #     num = int(num)
# print('Important')
# print(num)
# print(type(num))


# from string import digits
# symbols = digits + '-' + '.'
# flag = True
# while flag:

#     is_correct_number = True

#     num1 = input("Vvedite pervoe chislo: ")

#     for x in num1: #587t
#         if not x in symbols:
#             print("Вы ввели неправильное число")
#             is_correct_number = True
#             break

#     if not is_correct_number:
#         continue

#     num2 = input('Vvedite vtoroe chislo: ')

#     for x in num2: #587t
#         if not x in symbols:
#             print('asdfgh')
#             is_correct_number = False
            

#     if not is_correct_number:
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     operator = input('Vvedite operator (+,-,*,/): ')

#     if operator == '+':
#         print(f'result: {num1 + num2}')
#     elif operator == '-':
#         print(f'result: {num1 - num2}')
#     elif operator == '*':
#         print(f'result: {num1 * num2}')
#     elif operator == '/':
#         print(f'result: {num1 / num2}')
#     else:
#         print('not correct opeartor')

#     choice = input('Hotite prodoljit? yes/no ')
#     if choice.lower().strip() == 'no':
#         flag = False
#         print('Poka Poka')

# numbers = input()
# list_ = list[numbers]
# print(list_)
# list_ = list(map(int, numbers))
# print(list_)