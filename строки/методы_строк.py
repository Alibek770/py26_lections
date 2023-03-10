"=================== Метода Строк ==================="

# print(dir(str)) "список методов"

# str.replace
# "replace"
# str.replace(старое значение, новое значение)

# "strip" 
# # str.strip() - метод строк, который убирает пробелы в начале и конце строки 

# text = ' hello world'
# result = text.strip()
# print(text) 
# print(result)

# print(len(text))
# print(len(result))

# # str.rstrip - убирает пробелы справа(в конце)
# text = '       hello world      '
# result = text.rstrip()
# print(result)

# print(len(result()))
# # str.lstrip - убирает пробелы слева(сначала)

# text = '       hello world      '
# result = text.lstrip() #убирает слева все пробелы
# print(result) # 'hello world '

# print(len(result())) #17

'ISDIGIT, ISNUMERIC, ISDECIMAL'
#str.isdigit() - 
#str.isnumeric() - это методы строк, которые проверяют состоит ли наша строка из чисел
#str.isdecimal()

# text = '22'
# print(text.isdigit()) #true
# print(text.isdecimal()) #true
# print(text.isnumeric()) #true

# age = input("Введите свой возраст:  ")
# print(age.isdigit())

# 'ISALPHA'
# #str.isalpha() - это метод строк который проверяет состоит ли наша строка только из латиницы или кирилицы

# text = "hello world"
# print(text.isalpha()) #False, так как пробел это не кириллица или латиница

# text_2 = "helloworld"
# print(text_2.isalpha()) #True, так как вся строка состоит из латиницы


'ISALNUM'

# #str.isalnum() - это метод, который проверяет на то что состоит ли наша строка из чисел и символов латинского или киррильского алфавита


# text = 'abds48'
# print(text.isalnum()) #True, так как строка состоит из латиницы и чисел

'ISLOWER, ISUPPER' 

#str.islower - метод строк, который проверяет на нижний регистр(с маленькой буквы)
#str.isupper - метод строк, который проверяет на вверхний регистр(с большой буквы)

# text = "makers"
# print(text.islower()) #true
# print(text.isupper()) #false

# text_2 = "MAKERS32"
# print(text_2.islower()) #False
# print(text_2.isupper()) #False

"ISTITLE"

#str.istitle - проверяет начинается ли предлложения с вверхнего регистра (с большой буквы)

# name = 'alibek kokumov'
# name2 = 'Alibek Kokumov'
# print(name.istitle()) #False
# print(name2.istitle()) #True

"INDEX"
#str.index(values, start, end) - это метод строк, который возвращает индекс заданого значения (values)

# text = 'makers bootcamp'
# print(text.index('z', 7)) #12, ищет в слове bootcamp

"COUNT"
#str.count(values, start) - метод строк который считает сколько у нас значений(values) есть в строке
# text = 'codingiseas4324234y'
# print(text.count('i')) #2 от начала до конца

# text = 'codingiseasy'
# print(text.count('i',5)) #1 от начала до конца

# text = 'codingiseasy'
# print(text.count('i', 5, 9)) #1 c 5-го индекса до 9-го включительно

"FIND"
#str.find(values, start, end) - это метод строк, такой же как и метод строк str.index(смотреть выше), но он не выведетт ошибку, если значения(values)
# нету в строке, он просто вернет индекс -1


# text = 'makers bootcamp'
# print(text.find('a',)) # распечатает -1

# text = 'makers bootcamp'
# print(text.index('a',)) # распечатает ValueError (not found)

"SWAPCASE"

#str.swapcase() - метод строк который меняет на противоположный регистр (а -> A), (A -> a) (makers -> MAKERS) or (mAkErS -> MaKeRs)

# text = 'CoDiNgIsEaSy'
# print(text.swapcase())

# text2 = input("Введите свой текст: ")
# print(text2.swapcase())

"CAPITALIZE"
#str.capitalize() - это метод строк, который меняет первую букву строки на вверхний регистр(маленькую на заглавную) остальное на нижний
# text = input("Введите свой текст: ")
# print(text.capitalize())


"TITLE"

#str.title() - это метод строк, который переводит начало каждого слова в строке в верхний регистр

# text = input("Write your text: ")
# print(text.title())

"SPLIT"
#str.split(разделитель) - это метод строк, который строку переводит в лист при помощи разделителя

# text = input('Введите числа через запятую: ')
# print(text.split())

"JOIN"
#'соединитель'.join(list) - это метод строк, который соединяет элементы листа

# list_ = ['12', '23', '54', '24']

# print('*'.join(list_))

# string = "FKJDSAKDKJHDSAJDASDKJSAHKJHDASJKH"
# print(string(len(string())))