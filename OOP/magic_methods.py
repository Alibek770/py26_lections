# Магические методы (dunder - double underscrore) - методы, у которых два нижних подчеркивания в начале и в конце.
# Магия в том, что мы их не вызываем напрямую, а они вызываются в определенный момент, 
# либо они вызываются определенными операторами или функциями.

# res = 5 + 5 #__add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

#магические методы которые срабатывают при помощи оператора:

# __eq__(self,other) -> == : 5 == 5
# __ne__(self, other) -> !=
# __lt__(self,other)-> <


# __sub__(self,other) -> - __div__ -> /
# __mul__ -> * __mod__ -> %
# __floordiv__ -> // __add__ ->+
# __pow__ -> ** 

# class MyClass:
#     def __init__(self, string) -> None:
#         self.string = string 

#     def __add__(self,other):
#         print('add сработал')
#         print(self,'!!!!')
#         print(other, '****')
#         res = self.string + other.string
#         return MyClass(res)

    
#     def __str__(self) -> str:
#         return self.string

# obj1 = MyClass('John')
# obj2 = MyClass('Jamie')
# obj3 = MyClass('Lanister')
# res = obj1 + obj2 + obj3
# print(res)
# print(res.string)

# class Word(str):
#     def __new__(cls,word):
#         word = word.replace(' ', '')
#         return super().__new__(cls,word)

#     def __init__(self, word) -> None:
#         self.word = word 

#     def __gt__(self, other: str) -> bool:
#         print('gt сработал')
#         print(self,'!!!')
#         print(other, '***')
#         return len(self) > len(other)

# obj1 = Word('John')
# obj2 = Word('Hello world!')
# print(obj1 > obj2)

'-----------------------------------------------------------------------'

# конструктор -> __new__(cls)
# инициализатор -> __init__(self)
# вызываются, когда создаем объект

# class Converter(float):
#     def __new__(cls, __x):
#         print('new сработал')
#         print('cls', '!!!')
#         print(__x,'xxxx')
#         return super().__new__(cls,__x)

#     def __init__(self, x) -> None:
#         print('init сработал')
#         print(self,'!!!!!')
#         self.number = x

# obj = Converter(51)
# print(obj)
'-----------------------------------------------------------------------'

# __str__ -> для отображения строки. которую будут видеть пользоваьели 

# __repr__ -> строковую информацию о том как создать объект 

# __len__ --> len(obj)

# __repr__ --> repr(obj)

# class Base:
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return f'Объект {self.string}'

#     def __repr__(self):
#         return f'Base("string")'

#     def __len__(self):
#         return 5

# user = Base('Hello John')
# print(user)
# print(repr(user))
# obj1 = eval(repr(user)) # Base('string')
# print(obj1)
'-----------------------------------------------------------------------'

# class Person:
#     def __init__(self, attrs: dict):
#         # self.name = attrs['name']
#         # self.a = 5 == setattr(self, 'a', 5)
#         for key, value in attrs.items():
#             setattr(self, key, value)

# alice = Person({'name': 'Alice Rose', 'income': 180000, 'eyes': 'brown'})
# john = Person({'email': 'JohnSnow@gmail.com', 'last_name': 'John' })
# print(f'{alice.name} -- {alice.income} -- {alice.eyes}')
# print(f'{john.email} -- {john.last_name}')
'-----------------------------------------------------------------------'

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls
#     def __getitem__(self, index):
#         print(self.ls[index -1])

# x = MyList([123, 'Hello', 2,4,5])
# x[1]
# x[3]
# x[2]

# __iter__ - вызывается, когда мы итерируем объект 

# class A:
#     def __init__(self,word) -> None:
#         self.word = word

#     def __iter__(self):
#         for i in range(1,10):
#             # print('iter method')
#             yield i 

# x = A('Human')
# for i in x:
#     print(i)

# a = range(1,10)
# print(a)
# for x in a:
#     print(x)

# def generator(num):
#     for i in range(num):
#         yield i 

# a = generator()
# for x in a:
#     print(x)

'-----------------------------------------------------------------------'

# class User:
#     def __init__(self) -> None:
#         self.name = NameError

#     def __call__(self):
#         print(f'User object: {self.name}')

# user1 = User('John Snow')
# user1()


        