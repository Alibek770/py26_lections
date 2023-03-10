#############    ООП: Введение    #############

'''
Объектно-ориентированное программирование основано на парадигме императивного программирования, которая использует операторы для изменения состояния программы. Основное внимание уделяется описанию того, как должна работать программа. Примерами императивных языков программирования являются C, C ++, Java, Go, Ruby и Python. Это противоречит декларативному программированию, в котором основное внимание уделяется тому, что должна выполнять компьютерная программа, без указания как. Примерами являются языки запросов к базе данных, такие как SQL и XQuery, где только компьютер сообщает, какие данные откуда запрашивать, а теперь как это сделать.

ООП использует концепцию объектов и классов. Класс можно рассматривать как «чертеж» для объектов. Они могут иметь свои собственные атрибуты (характеристики, которыми они обладают) и методы (действия, которые они выполняют).

Примером класса является класс Dog. Не думайте об этом как о конкретной собаке или о своей собственной собаке. Мы описываем, что собака вообще может делать. Собаки обычно имеют name и age - это атрибуты экземпляра. Собаки могут также лаять (bark) - это метод.

Когда вы говорите о конкретной собаке, это у вас будет объект в программировании: объект является экземпляром класса. Это основной принцип, на котором основано объектно-ориентированное программирование. Так, например, моя собака Ак-Тош принадлежит к классу Dog. Его атрибутами будут name = 'Ak-Tosh'и age = '2'. У другой собаки будут другие атрибуты.

Как создать класс.
Чтобы определить класс в Python, вы можете использовать ключевое слово class, за которым следует имя класса и двоеточие. Внутри класса метод __init__ должен быть определен с def. Это инициализатор, который вы позже сможете использовать для создания экземпляров класса. Это похоже на конструктор в Java. Ему требуется один обязательный параметр: self, который относится к самому объекту. Внутри метода на данный момент используется ключевое слово pass, потому что Python ожидает, что вы что-то там напечатаете. 
'''

# class Dog:

#     def __init__(self):
#         pass

'''
Таким образом у вас есть класс Dog, но еще нет объекта. Давайте создадим один!

Создание объектов.
Чтобы создать экземпляр от класса, введите имя класса, а затем две скобки. Вы можете присвоить это переменной, чтобы в дальнейшем отслеживать объект.
'''

# ak_tosh = Dog()
# print(ak_tosh)
# # <__main__.Dog object at 0x111f47278>

'''
Добавление атрибутов в класс.
После печати ak_tosh становится ясно, что этот объект - собака. Но вы еще не добавили никаких атрибутов. Давайте дадим Dog классу имя и возраст, переписав его:
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

'''
Вы можете видеть, что функция теперь принимает два аргумента после self: name и age. Затем они назначаются self.name и self.age соответственно. Теперь вы можете создать новый объект ak_tosh с именем и возрастом:
'''

# ak_tosh = Dog("Ak-Tosh", 2)

'''
Чтобы получить доступ к атрибутам объекта в Python, вы можете использовать точечную запись. Это делается путем ввода имени объекта, затем точки и имени атрибута.
'''

# print(ak_tosh.name)
# print(ak_tosh.age)
# # Ak-Tosh
# # 2

'''
Это также может быть объединено в более сложное предложение:
'''

# print(ak_tosh.name + " is " + str(ak_tosh.age) + " year(s) old.")
# # Ak-Tosh is 2 year(s) old.
# # Функция str() используется здесь , чтобы преобразовать age атрибут, который представляет собой целое число, в строку.

'''
Определите методы в классе.
Тепер у вас есть класс Dog, у которого есть имя и возраст, которые вы можете отслеживать, но он ничего не делает. Вот тут-то и появляются методы экземпляра. Перепишите класс, чтобы включить метод bark(). Обратите внимание, как снова используется ключевое слово def, а также аргумент self.
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("gav gav!")

'''
Теперь метод bark можно вызывать с помощью точечной нотации после создания нового объекта ak_tosh. Метод должен печатать "gav gav!" на экран. Обратите внимание на круглые скобки в .bark(). Они всегда используются при вызове метода. В этом случае они пусты, поскольку метод bark() не принимает никаких аргументов.
'''

# ak_tosh = Dog("Ak-Tosh", 2)

# ak_tosh.bark()
# # gav gav!

'''
Вспомните, как вы печатали ak_tosh ранее? Код ниже теперь реализует эту функциональность в классе Dog с помощью метода doginfo(). Затем вы создаете еще несколько экземпляров с разными свойствами и вызываете для них метод.
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("gav gav!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " year(s) old.")

# ak_tosh = Dog("Ak-Tosh", 2)
# rex = Dog("Rex", 12)
# bobik = Dog("Bobik", 8)
# ak_tosh.doginfo()
# rex.doginfo()
# bobik.doginfo()
# # Ak-Tosh is 2 year(s) old.
# # Rex is 12 year(s) old.
# # Bobik is 8 year(s) old.

'''
Как видите, вы можете вызывать метод doginfo() для объектов с помощью точечной нотации. Ответ теперь зависит от того, для какого объекте Dog вы вызываете метод.

Поскольку собаки становятся старше, было бы неплохо, если бы вы могли соответствующим образом скорректировать их возраст. Ак-Тош только что исполнилось 3 года, поэтому давайте изменим его возраст.
'''

# ak_tosh.age = 3
# print(ak_tosh.age)
# # 3

'''
Это так же просто, как присвоить новое значение атрибуту. Вы также можете реализовать это как метод birthday() в классе Dog:
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("gav gav!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " year(s) old.")

#     def birthday(self):
#         self.age +=1

# ak_tosh = Dog("Ak-Tosh", 2)
# print(ak_tosh.age)
# # 2
# ak_tosh.birthday()
# print(ak_tosh.age)
# # 3

'''
Теперь вам не нужно вручную менять возраст собаки. Когда у него день рождения, вы можете просто вызвать метод birthday().

Передача аргументов в методы.
Вы хотели бы, чтобы у наших собак был приятель. Это должно быть необязательным, так как не все собаки общительны. Взгляните на метод setBuddy() ниже. Он принимает self, как обычно, и buddy в качестве аргументов. В этом случае buddy будет еще один объект от класса Dog. Установите для self.buddy атрибута значение buddy, а для buddy.buddy атрибута - self. Это означает, что отношения взаимны; ты приятель своего приятеля. В этом случае Ак-Тошу будет приятелем Рекс, а это означает, что Рекс автоматически становится приятелем Ак-Тошу. Вы также можете установить эти атрибуты вручную, вместо определения метода, но это потребует дополнительной работы (написание 2 строк кода вместо 1) каждый раз, когда вы хотите назначить приятеля. 
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("gav gav!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " year(s) old.")

#     def birthday(self):
#         self.age +=1

#     def setBuddy(self, buddy):
#         self.buddy = buddy
#         buddy.buddy = self

'''
Теперь вы можете вызвать метод с точечной нотацией и передать ему другой объект от класса Dog. В этом случае приятелем Ак-Тоша будет Рекс:
'''

# ak_tosh = Dog("Ak-Tosh", 2)
# rex = Dog("Rex", 8)

# ak_tosh.setBuddy(rex)

'''
Если вы сейчас хотите получить какую-нибудь информацию о приятеле Ак-Тоша, вы можете использовать точечную запись дважды. Во-первых, чтобы сослаться на приятеля Ак-Тоша, и во второй раз, чтобы сослаться на его атрибут.
'''

# print(ak_tosh.buddy.name)
# print(ak_tosh.buddy.age)
# # Rex
# # 8

# # Обратите внимание, как это можно сделать для Рекса.

# print(rex.buddy.name)
# print(rex.buddy.age)
# # Ak-Tosh
# # 2

'''
Методы приятеля также могут быть вызваны.
'''

# ak_tosh.buddy.doginfo()
# # Rex is 8 year(s) old.

'''
Теперь вы знаете, как объявлять классы и методы, создавать экземпляры классов, устанавливать их атрибуты и вызывать методы экземпляров. 

С ООП ваш код будет усложняться по мере увеличения вашей программы. У вас будут разные классы, подклассы, объекты, наследование, методы экземпляра и многое другое. Для того, чтобы ваш код был правильно структурирован и читабелен, рекомендуется следовать шаблонам проектирования.
'''
# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f'This animal is {self.name}: {self.golos}')

#     def eat(self):
#         print(f'This animal is {self.name} eats {self.meal}!')

# class Lion(Animal):
#     name = 'lion'
#     meal = 'meat'
#     golos = 'aarrrr!'

# obj =  Lion()
# print(obj.name)
# obj.eat()