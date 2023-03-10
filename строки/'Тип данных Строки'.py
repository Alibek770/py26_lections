'Тип данных Строки'

'Строки (str) - это набор последовательных символов, которые мы используем для хранения и представления текстовой информации'

name = 'John Snow Man'

# name = 'John'
# '       0123'

"""
Срезы по индексам -  это когда мы получаем определенную часть строки при помощи индексов"
"""

'срезы[start : end : stop]'
"start - начало среза, начальный индекс, по умолчанию стоит 0 индекс"
'end - конец среза, который не включителен, по умолчанию берет до конца'
'step - шаг среза, который указывает через сколько элементов проходиться, по умолчанию стоит 1'

# name - 'John Snow'
# snow = name [5:9] #Snow
# snow = name [5:]  #Snow man, end не указали поэтому он возьмет до конца 
# print(snow)

# John1 = name[0:4]
# John2 = name[:4]
# print(John1)
# print(John2)

# step_2 = name[0:13:2]
# step_3 = name[0:13:3]
# print[step_2] 
# print[step_3]

# name = "John Snow Man"
# reversed_name = name[::-1] #все тоже самое только наоборот
# print(reversed_name)

# # перевернутая строка
# name = "John Snow Man"
# reversed_name_nam = name[8:4:-1] 
# reversed_name_whoS = name[-8:-4:]
# print(reversed_name_nam)
# print(reversed_name_whoS)
# склеивание строк(конкатенация)
# first_name = " Alibek"
# second_name = " Kokumov"
# middle_name = " Talantbekovich"
# full_name = first_name + second_name + middle_name
# print(full_name)
# print(full_name*2.5)

"======================= Форматирование Строк ====================="
'''
Способы(3 вида):
1.) с помощью %s
2.) с помощью (.format())
3.) интерполяция строк (f'строка')
'''

# 1) %

# name = input("Введите свое имя: ")
# name_2 = input ("Введите свое имя: ")
# print("привет, меня зовут ", name)
# print('Privet \'menya\' zovut ' + name + " Talantbekovich")
# age = 25
# print('Privet, menya zovut %s Talantbekovich' %(age))
# print()

#2) .format

# name = input("Введите свое имя:  ")
# age = 25
# result = "Привет, мое имя {}, мне {} лет" .format(name, age)
# print(result)

#3) f"строки"

# name = input('Введите свое имя: ')

# result = f'Привет, {name}, как твое ничего?'
# print(result)

'============================ Экранирование строк ======================='

""""

\n - перенос строки #enter
\t - горизонтальная табуляция #tab
\v - вертикальная табуляция  #вниз

"""
# r
# print('hello world\n my name is Alibek\n\t\'m Sabina\'s Mom')
# print('hello world\n my name is Alibek\n\v\'m Sabina\'s Mom')
# print('Sup baby\n')
# print('Sup baby\n\v')
# print('Sup baby\n\t')