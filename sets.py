# Множеств в пайтоне - "контейнер", который содержит в себе уникальные элементы в не упордочном виде

# # {} !!!! dict
# # set()
# a = {'a':1} #словарь
# a = {1,2,3} #множество 

# set1 = {1,2,3,4,5,6,6,7,8,}
# print(set1)
# print(type(set1))

# ls  = ['Hello', 'Hello', 'John', 'Snow', 'John']
# print(ls)
# res = set(ls)
# print(res)
# res = list(res)
# print(res)
# print(type(res))

# ls=[1,2,4,'a',False,True,'n','b']
# str1 = 'Hello world'
# ls.extend(str1)
# # print(ls)
# res = set(ls)
# print(res)

# set1 = {1,2,3,4,5,6,7,8,9}
# set1.pop()
# print(set1)

# FIFO / LIFO
#first in first out / первый заходит, первый выходит
#last in last out / последний заходит, последний выходит

# remove/discard
# remove - error
# discard - None

# set1 = {1,2,3,4,5}
# set1.remove(5)
# set1.discard(4)
# set1.add(15)
# print(set1)

'--------------------------------------------------------------------------------'

'Frozenset'

#frozenset 
# a = {1,2,3,4,5}
# b = frozenset([1,2,3,4,5,6])
# print(a,type(a))
# # print(b, type (b))

# # Создайте кортеж из 8-ми кортежей учащихся ВУЗов. В кортеже будут присутствовать следующие 
# # поля: имя студента, возраст, оценка за семестр, город проживания. Ваш код будет принимать этот кортеж, вычислять
# #  среднюю оценку по всем учащимся и выводить на печать следующее сообщение: “Ученики {список имен студентов через запятую}
# #  в этом семестре хорошо учатся!”. В список студентов, которые выводятся по результатам работы функции, попадут лишь те, у
# #  которых оценка за семестр равна или выше средней по всем учащимся.

# # кортеж(имя, возраст, оценка, город)
# students = (
#     ('Елена', '13', 9, 'Москва'),
#     ('Ольга', '11', 7.9, 'Иваново'),
#     ('Елизавета', '14', 9.1, 'Тверь'),
#     ('Дмитрий', '12', 5.2, 'Челябинск'),
#     ('Максим', '15', 6.1, 'Самара'),
#     ('Николай', '11', 8.7, 'Владивосток'),
#     ('Артур', '13', 5.8, 'Екатеринбург'),
#     ('John', '13', 10, 'WinterFell')
# )

# marks = []
# new = students[2:]
# for x in students:
#     print(x, '!!!!')
#     marks.append(x[2])

# print(marks)
# avg_mark = sum(marks) / len(marks)
# print(avg_mark)

# good_students = []
# for student in students:
#     if student[2]>avg_mark:
#         good_students.append(student[0])
#         print(good_students)

# print(f"Ученики {', '.join(good_students)}  в этом семестре хорошо учатся!")


# a = {'Jane', 'Eyre', 22}
# str1 = ('Hello world!')
# str2 = ("Bye world!")
# a.update((str1) + str2)
# print(a)

# tilek = {'Dodo','ImperiaPizza','FreshBox'}
# timur = {'OchakKebab','FreshBox'}
# alexander = {'FreshBox', 'KFC'}
# elina = {'FreshBox', 'KFC', 'OchakKebab', 'ImperiaPizza'}

# a = tilek.intersection(timur,alexander,elina)

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}

# ingredients.add('помидоры')
# ingredients.discard('колбаса')
# ingredients.remove('шпинат')
# ingredients.update('шпинат')
# ingredients.add('базилик')
# ingredients.discard('сыр чеддар')
# ingredients.add('сыр моцарелла')
# print(ingredients)

tasks #16


# a = [set(),set(),set()]
# inp1 = input()
# inp2 = int(input())
# for i in range(3):
#     if (i+1)== inp2:
#         a[i].add(inp1)
#     else:
#         a[i].add("default value")
# print(a)


