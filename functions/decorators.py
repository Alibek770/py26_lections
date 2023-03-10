# decorators.py

# функция высшего порядка - это функция которая в 
# качестве аргумента принимает другую функцию


# Декоратор - это функция, которая позволяет без изменения кода обернуть другую 
# функцию для того чтобы расширить функционал обернутой функции 

# def decorator(func):
#     print(f'CalledFunc name: {func.__name__}')
#     return func()


# def hello():
#     print('Vsem privet! ')
#     return 'Hello'

# def john():
#     print('Hello my name is John Snow')
#     return 'John Snow'

# hello()
# john()

# a = decorator(hello)
# b = decorator (john)
# print(a,b)

# from typing import Callable

# # Декораторы 

# def benchmark(func: Callable):
#     def wrapper(): #2
#         import time
#         start = time.time()
#         res = func() #3
#         finish = time.time()
#         print(f'Время выполнения функции {func.__name__}: заняло {finish - start}')
#         return res

#     return wrapper
# @benchmark
# def loop(): #4
#     i = 0
#     range_number = 100_000
#     while i <= range_number:
#         print(i)
#         i += 1
#     return i

# def add():
#     i = 0
#     range_number = 1000_000
#     ls = []
#     while i < range_number:
#         i += 1 
#         ls.append(i)
#     return ls 

# print(loop()) #1

# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper( * args, **kwargs):
#         return '<divs>' + func() + '</div'
#     return wrapper

# @div
# @strong
# @div
# def john():
#     return 'John Snow'

# print(john())

# def trace(func):
#     def wrappper(*args, **kwargs):
#         print(f'Trace: вызвана {func.__name__}(), \n {args}, {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвана {func.__name__}(),\nвернула {args} {kwargs}')
#         return original_result
#     return wrappper

# @trace
# def say(name, line):
#     return f' {name}:{line}'

# print(say('John', line = 'Snow'))

# def func():
#     print()




# def repeat(func):
#   def wrapper(num):
#     i = 1
#     while i < num:
#       i +=1
#       func()

#   return wrapper


# @repeat
# def function(name = 4):
#     print(f'{name}')

# function('hello')
