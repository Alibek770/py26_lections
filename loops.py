# while <expression>:
#     <body>

# i = 0 
# while i <= 10:
#     i += 1 #i = i +1
#     print(f'цикл выполнился {i} раз!') 

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'raychel':
#     name1 = input('Vvedite imya: ')
#     name2 = input('Vvedite vtoroe imya: ')
#     i += 1
#     if i >= 5:
#         print('цикл остановлен!')
#         break
# else: 
#     print('Vy vveli pravilnoe imya')

# моржовый оператор
# user = {'username':'John', 'password': 'ilovepython123'}
# i = 3
# while (password := None != user['password']):
#     password = input(f'{user["username"]} vvedite parol\': ')
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany na 5 dney')
#         break
#     else:
#         print(f'{user["username"]} vy uspeshno zashli v sistemu!')

# Код на запрос пароля
# user = {'username':'John', 'password': 'ilovepython123'}
# i = 3
# password = None
# while (password != user['password']):
#     if i == 0:
#         print('Vy zablokirovany na 5 dney')
#         break
#     password = input(f'{user["username"]} vvedite parol\': ')
#     i -= 1
    
# else:
#         print(f'{user["username"]} vy uspeshno zashli v sistemu!')


'--------------------------------------- iter ------------------------------------------'

# for <variable> in <iterable object>:
    # <body> 

# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_[::-1])
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# import random
# ls = []
# for x in range(1,101):
#     ls.append(random.randint(1, 101))
# print(ls)
# ls.sort()
# print(ls)
# for x in ls:
#     for i in ls:
#             if ls.count(x) > 1:
# #                 ls.remove(x)
            
# set1 = set(ls)
# ls = list(set1)
# print(ls, '!!!!!!!')
# ls.sort()
# res = []
# for x in ls:
#     if x % 2 != 0:
#         ls.append(x)
# print(res)


# число 100 
1,
2,4,5, 10

# x = 100
# res = [1,x]
# for i in range(2, int(( x ** 0.5)+1)):
#     if x % i == 0:
#         res.extend({i, x // i})
# res.sort()
# print(res)