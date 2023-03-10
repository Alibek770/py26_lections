# try except

# try: 
#     <body try> 
# except <Exception>:
#     <body>
# <else>:
#     <body> только если все окей
# <finally>:
#     <body> в любом случае в конце

# num1 = int(input('Vvedite chislo: '))
# print(num1)
# print('Important!')


# try:
#     num1 = int(input('Vvedite chislo: '))
    
# except ValueError:
#     print('Invalid Value')
# else:
#   print(num1)

# print('Important!')


# try:
#     num1  = int(input('Vvedite 1oe chislo: '))
#     num2  = int(input('Vvedite 1oe chislo: '))
#     print(num1 /num2)
# except (ValueError, ZeroDivisionError) as error:

#     print('By vveli nekorectnye dannye')
#     print(error)

# list_ = [1,2,3,4,5]

# try: 
#     index = int(input('Vvedite index: '))
#     res = list_[index]
#     print(res)
# except ValueError:
#     print('ValueError! ')
# except IndexError:
#     print('Index error! ')

# try: 
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     result = num1/ num2
# except ZeroDivisionError:
#     print('na 0 delit\ nelzya')
# except ValueError:
#     print('Invalid symbols for int()!')
# else: 
#     print(result)
# finally:
#     print('The end! ')

#case 1
# path = 8
# steps = 'UDDDUDUU'
# result = 1 dolina


# case2
# path = 10
# steps = DUDDDUUDUU
# result = 2 dolina

# def countingValleys(steps, path):
    
#     count = 0
#     valleys = 0
#     for i in range(steps):
#         if path[i] == 'U':
#             count += 1
#         else:
#             count -= 1
#         if count == 0 and path[i]=='U':
# #             valleys += 1
            
# #     return valleys

# path = 8
# steps = 'UDDDUDUU'

# sea_level = 0
# valleys = 0 

# for step in steps:
#     if step == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             valleys +=1
#     elif step == 'D':
#         sea_level -=1

# print(f'Result: {valleys} count!')

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k in k,v if k replace.items( 'i',' ')  }

# task number 31
# readers = [x[0] for x in SPL_Patrons if x[1] > 100]
# print(readers)

# task number 33
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# saved_amount = [round(x[1] * 11.95,2) for x in SPL_Patrons]
# print(saved_amount)

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }
# hey_ = sum([y['likes']for x,y in dict_.items()if y['rating'] >= 3])
# print(hey_)

# num1 = int(input('Vvedite vash vozrast: ' ))
# if num1 <= 0:
#     print('Ваш возраст должен быть больше 0')
# else:
#     print(f'Ваш возраст:{num1} ')


# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# for k,v in dict_.items():
#         print(k)

# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(dict_['key1']) 
# except KeyError:
#     print('Нет такого ключа!')

try:
    age = int(input('Введите ваш возраст: '))
    if age < 18:
        print('Доступ запрещён')
except ValueError:
        print('Введён некорректный возраст')
else:
        print('Спасибо')
finally:
    print('До свидания')
    
# try:
#     age = int(input('Введите ваш возраст: '))
#     if age < 18:
#         raise ValueError
# except ValueError:        
#     print('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания')