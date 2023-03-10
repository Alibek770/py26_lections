"ООП - Обьектно ориентированное программирование"

# Класс -> это описание того, как должен выглядеть обьект, т.е в классе мы 
# описывем какими свойствами(данными) и поведением должен обладать обьект 

# Обьект -> это сущность которую мы создаем от класса, у обьекта есть состояние свойств(данных)

# Целью создания было связать данные(атрибуты) с функциями(методы) которые использовали их

# Свойствами(атрибуты) - называют обычные переменные внутри класса, # в которых хранятся данные определнного обьекта

# Методы - это обычные функции которые описывает поведение обьекта, функции внутри класса называют методами


'---------------------------------------------------------------------------------------------------------------------'

# john = ['John', 'Snow', 'King of North', 30]

# def show_info(human):
#     print(f'Name: {human[0]} {human[1]}, Age: {human[-1]}, Job: {human[2]}, Salary:{human[3]}')


# show_info(john)

# class Human:
#     def __init__(self, name, last_name,age, job, salary) -> None:
#         self.name = name + " " + last_name
#         self.last = last_name 
#         self.age = age
#         self.job = job
#         self.salary = salary


#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job:{self.job}, Salary: {self.salary}'

# john = Human('John', 'Snow', 30, 'King of North', 5000)

# sultan = Human('Sultan', 'Katana', 19, 'Mentor', 100)

# # print(dir(john))
# print(john.show_info())
# print(john.name)
# print(john.age)
# print('----')
# print(sultan.show_info())
# print(sultan.name)


'---------------------------------------------------------------------------------------------------------------------'


# class Dog:
#     #аттрибуты класса 
#     age = 0
#     ushi = True

#     def __init__(self,name,color) -> None:
#         """Инициализатор, именно здесь создаются аттрибуты обьекта"""
#         #  В self прилетает ссылка на обьект от класса
#         self.name = name # атррибуты обьекта
#         self.color = color 

#     def bark(self):
#         print(f'{self.name}лает!')

# bobik = Dog('Bobik', 'brown')
# yumi = Dog(name='Yumi', color='white')
# aktosh = Dog('Aktosh', 'gray')

# print(f'{bobik.name}, {bobik.name}, age:{bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')

# print(f'{yumi.name}, {yumi.name}, age:{yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')

# print(f'{aktosh.name}, {aktosh.name}, age:{aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')

# bobik.age = 2
# bobik.age = 1
# aktosh.age = 3
# aktosh.ushi = False

# print('After')

# print(f'{bobik.name}, {bobik.name}, age:{bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')

# print(f'{yumi.name}, {yumi.name}, age:{yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')

# print(f'{aktosh.name}, {aktosh.name}, age:{aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')

# class Human:
#     age = 0

#     def __init__(self) -> None:
#         print('init worked')
#         self.raychel = 'raychel'

#     def method1(self):
#         self.john = 'john'
#         print('method1 worked')

# obj = Human()
# print(obj.raychel)
# obj.method1()
# print(obj.john)     

# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def show_title(self):
#         return f'Название этой песни {self.title}'
#     def show_author(self):
#         return f'Автор этой песни {self.author}'
#     def show_year(self):
#         return f'Эта песня вышла в {self.year}'
# song = Song(title = 'Happy', author = 'Pharrell Williams', year = 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())


