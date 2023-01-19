# 'dictionary.py'

# # obj = ['John','Snow', 24, 500, '+996990099999', 'Winterfell']

# # obj = {'name': 'John', 'last_name': 'Snow', 'age': 24, 'cash': 500, 'phone_number': '+996990099999', 'city': 'Winterfell'}

# # print(obj['name'])

# # print(obj['last_name'])

# # print(obj['cash'])

# # print(obj['phone_number'])

# # print(obj['city'])

# #dict - Словарь -> упорядоченная коллекция элементов(python 3.7 -> ordered), 
# # каждый элемент внутри словаря содержится в паре ключ: значение.

# # Ключи должны быть неизменяемым типом данных(str, int, tuple etc.))
# # тогда как значениями могут выступать любые типы данных.

# # thisdict = {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}
# # print(thisdict)
# # print(type(thisdict))

# # ассоциативный массив, hash table, object(js), structure==dictionary(py)
# # user_info = {
# #     'first_name': 'John',
# #     'last_name': 'Snow',
# #     'age': 23,
# #     'email': 'johnsnow88@mail.ru',
# #     'role': 'moderator',
# #     # [1,2,3]: 'list' #this is error
# # }
# # print(user_info)
# # print(user_info.get('first_name'))
# # print(user_info['first_name'])

# '-------------------------------------------------------------------------------------'

# # user_info = {
# # 'first_name': 'John',
# #     'last_name': 'Snow',
# #     'age': 23,
# #     'email': 'johnsnow88@mail.ru',
# #     'role': 'moderator',
# # }
# # print(dir(dict))

# # a = (1,2)
# # print(a, type(a))
# # num1, num2 = a
# # print(num1)
# # print(num2)

# # print(user_info.values())
# # print(user_info.keys())
# # print(user_info.items())
# # print(user_info)

# # for x in user_info.items():
# #     print(x)

# '-------------------------------------------------------------------------------------'

# # dict_ = {1:15, 2:11, 3:18, 4:5, 5:21}

# # for key, value in dict_.items():
# #     if key % 2 == 0:
# #         print(key, 'четное')
# # else:
# #     print(key, 'нечетное')
# #     dict_[key] = value ** 2

# # print(dict_)

# # изменения словаря
# # dict_ = {'name': 'John', 'age': 24}
# # # print(dict_)
# # # dict_['age'] = 23
# # # dict_['address'] = 'Winterfall'
# # # print(dict_)

# # dict_.update({'age': 18, 'address': 'Winterfall'})
# # print(dict_)

# '-------------------------------------------------------------------------------------'

# "FROMKEYS"

# #fromkeys - быстрое создание словаря из ключей 

# # keys = ['one','two','three']

# # new_dict = dict.fromkeys(keys, 'value')

# # print(new_dict)

# # dict_ = {}
# # ls = list(range(1,101))

# # new_dict = dict_.fromkeys(ls, 'None')
# # print(new_dict)

# '-------------------------------------------------------------------------------------'
# "SETDEFAULT"
# #setdefault - работает так же как и метод get(), но если нет такого ключа то он создаст новый

# # dict_ = {'name': 'John', 'age': 24}

# # print(dict_)
# # print(dict_.setdefault('age', 35))
# # print(dict_.setdefault('name'))
# # print(dict_.setdefault('number', 99699009999))
# # print(dict_)

# '-------------------------------------------------------------------------------------'
# 'POP'

# #удаление из словаря

# # #pop(key) - удаляет элемент по ключу

# # dict_ = {'name': 'John', 'last_name': 'Snow', 'address': 'Wintefall'}

# # dict_.pop('name')
# # print(dict_)
# '-------------------------------------------------------------------------------------'

# "POPITEM"

# #popitem() - удаляет последний элемент

# # dict_ = {'name': 'John', 'last_name': 'Snow', 'address': 'Wintefall'}
# # print(dict_)

# # removed = dict_.popitem()

# # dict_.popitem()
# # print(dict_)

# '-------------------------------------------------------------------------------------'

# # roles = {
# #     0: 'Moderator',
# #     1: 'Admin',
# #     2: 'Customer',
# #     3:  'Vendor'
# # }

# # users = {
# #     '1': {'username': 'JohnSnow', 'role': roles[1]},

# #     '2': {'username': 'JamieLanister', 'role': roles[2]},

# #     '3':{'username': 'Mufasa', 'role': roles[3]}

# # }

# # product = {
# #     'id': 1,
# #     'title': 'iphone 14 Pro Max',
# #     'description': 'Lorem Ipsum',
# #     'price': 200
# # }

# # i = "1"
# # while i == '1'or i == '2':
   
   
# #     i = (input('Введите что хотите сделать?\nЕсли хотите просмотреть товар,'
# #     'то нажмите 1\n Если хотите изменить товар то нажмите 2\nЕсли хотите выйти то нажмите 3 или что то другое \nВаш выбор: '))

# #     if i == '1':
# #         print(product)
# #     elif i == '2':
# #         id_user = (input("\nВведите ваш ID: "))
# #         if not users.get(id_user):
# #             print('Нет такого юзера ')
# #         elif users.get(id_user)['role'] == roles[1]:
# #             choice = input('Введите что изменить (title, description, price): ')
# #             new = input(f'Введите нвоое значение {choice}: ')
# #             product.update({choice: new})
# #             print('Updated')
# #         else:
# #             print("У тебя нет на это разрешения")
        
# # d = {

# #     1:'one',
# #     2:'two',
# #     3:'three'

# # }


# # print(len(d))
# # print(1 in d, 5 in d)

# # a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# # if a.get {None} del.a:
# #     print(a)

# # a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# # ot1 = a.copy()
# # for v in ot1():
# #     del None[v]
# # print(ot1)

# # a = {'a': 3, 'b': 2}
# # b = sum(a.values())
# # print(b)

# # dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# # b = l[::2]
# # print(b)

# 'Калькулятор'
# # num1 = int(input("Введите первое число: "))
# # num2 = int(input("Введите второе число: "))
# # o1 = num1 + num2 
# # o2 = num1 - num2
# # o3 = num1 * num2
# # o4 = num1 / num2
# # o5 = num1 % num2
# # o6 = num1 ** num2
# # o7 = num1 // num2
# # operation = input("Выберите операцию из следующих: + - * / % * * : ")
# # if operation == ('+'):
# #     print(o1)
# # elif operation == ('-'):
# #     print(o2)
# # elif operation == ('*'):
# #     print(o3)
# # elif operation == ('/'):
# #     print(o4)
# # elif operation == ('%'):
# #     print(o5)
# # elif operation == ('**'):
# #     print(o6)
# # elif operation == ('//'):
# #     print(o7)
# # print()


# num1 = int(input("Введите первое число: "))
# operation = input("Выберите операцию из следующих: + - * / % * * : ")
# num2 = int(input("Введите второе число: "))
# o1 = num1 + num2 
# o2 = num1 - num2
# o3 = num1 * num2
# o4 = num1 / num2
# o5 = num1 % num2
# o6 = num1 ** num2
# o7 = num1 // num2
# if operation == ('+'):
#     print(o1)
# elif operation == ('-'):
#     print(o2)
# elif operation == ('*'):
#     print(o3)
# elif operation == ('/'):
#     print(o4)
# elif operation == ('%'):
#     print(o5)
# elif operation == ('**'):
#     print(o6)
# elif operation == ('//'):
#     print(o7)
# print()

#22
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k,v in dict_.items():
#     if v != None:
#         dict_.pop(k)
# print(dict_)

# #25
# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# for k,v in dict_.items():
#     if num in dict_:
    
#     elif num == num:
#         print()

#27
# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# dict2 = {}
# for k,v in dict_.items():
#     for x,y in v.items():
#         dict2.setdefault(k,y)
# print(dict2)

#28
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k,v in dict1.items():
#     for x,y in v.items():
#         for l,c in x,y():
#            p = l * c
# dict2.setdefault(k,p)

#30
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# for k,v in dict_.items():
#     sorted_dict(dict_, items=dict_.get)
# print(sorted_dict)

# #32
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()
# for k,v in dict_.items():
#     if k in dict_:
#         print("Key is present in the dictionary")
#     else:
#         print("Key is not present in the dictionary")