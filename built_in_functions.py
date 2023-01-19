

# zip(iterables) - она соединяет каждый элемент итерируемых 
# обектов между собой, в тип данных tuple и возвращает его

# ls1 = [1,2,3]
# ls2 = [100,200,300]

# res = list(zip(ls1, ls2))

# print(res)


# ls1 = [1,2,3,4,5]
# ls2 = [100,200,300,400,500]
# ls3 = [10,20,30]

# res = list(zip(ls1,ls2,ls3))
# print(res)

# zip для создания словарей

# a = dict([(1,2), (3,4)])
# print(a)
# {1:2, 3:4}.items()
# dict_items[(1,2), (3,4)]

# d_keys = ['hostname', 'location', 'vendor', 'mode', 'IOS', 'IP']
# d_values = ['apple_r1', 'winterfall', 'jobs', 'watch', '16.0', '10.255.0.1']

# res = dict(zip(d_keys, d_values))
# print(res)

# d_keys = ['hostname', 'location', 'vendor', 'mode', 'IOS', 'IP']

# data = {
#     'r1': ['london_r1', 'New Globe Walk', 'Cisco', '4451', '15.4', '10.22.0.1.10'],
#     'r2': ['london_r2', 'North_London', 'Cisco', '4451', '15.4', '10.22.0.11'],
#     'sw1': ['london_sw1', 'South_West', 'Cisco', '3850', '16', '10.25.10.12'],
# }
# print(data)
# for k in data:
#     data[k] = dict(zip(d_keys, data[k]))
# print(data)

'------------------------------------------------------------------------'

# all(), any()

# all(iterable) - возвращает True, если все элементы внутри эттого обьекта истинна, иначе возвращает False

# all([1,2]) -> True
# all([]) -> False
# all(['False', 'John', 5,6,1]) -> True
# all([1,2,3],5, None]) -> False

# print(all([[1,2], 5, 'stroka', True, 1]))

# ip = '10.10.10.10'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

# any - возвращает True, если хотя бы один элемент истинна

# ls = [0,0,0, '', False, 1]
# print(any(ls))

# ignore = ['rm -rf', 'reset', 'alias']
# command = input('Введите команду: ')

# if any(word in command for word in ignore):
#     raise Exception('Invalid command')
# print('Vse ok!')


# task 2

# list_ = [1, 5, -9, 6, -4] 
# result = all(x >3 for x in list_)
# print(result)

# task 3

# list_ = [5, 8, 4, 6, 7]

# result = any(str < 0 for str in list_)

# print(result)

# task 4

# list_ = [1, 2, 3, 4] 

# result = list(map(lambda x: x ** 2, list_))

# print(result)

# task 5 
# list_ = [1, 2, 3, 4] 

# result = list(filter(lambda word: word % 2 == 0, list_))
# print(result)

# task 6 

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]

# result = list(filter(lambda word: len(word) > 7, list_))

# print(result)

# task 8

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 

# list2 = len(list(filter(lambda x: x % 2 == 0, list_)))

# list3 = len(list(filter(lambda y: y % 2 != 0,list_)))

# result = (f'even: {list2}, odd: {list3}')

# print(result)


# task 9

# list_ = [-1, 2, 3, 5, -3, 7] 

# result = list(map(lambda x:True if x > 0 else False, list_))
# print(result)


# task 10

# from functools import reduce

# list_ = ['Paul', 'George', 'Ringo', 'John'] 

# result = reduce(lambda x,y:x if len(x) > len(y) else y, list_)

# print(result)

# task11

# list_ = range(1,50)

# result = list(map(lambda x:'Fizz' if x % 3 == 0 else 'Buzz', list_))

# print(result)

# task14
# string = 'hello'
# for i in enumerate(string):
#     print(i)
# print(enumerate(string))
# string='12345678' 
# result=tuple(enumerate(string)) 
# print(result)