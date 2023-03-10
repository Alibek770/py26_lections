# def func():
#     var =  15
#     return var * 2

# оОбласть видимости и пространство имен или scopes определяет контекст переменной,
# в рамках которого мы можем ее использовать.

# a = 5
# print(a)
# def func():
#     print(a)
# func()

#built-in(Встроенная) - print, len, max
# global(глобальная)
# enclosed(не локоальная, nonlocal)
# local(локальная)

# x = 200

# def func():
#     print(x, '!')

# func()

# a = 10 # global
# print = # built - in 
# def hello(): #  global
#     a = 'Hello World' # local
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')

#LEGB
# local -> enclosed -> global -> built-in

# x = 'global'
# print(x,1)

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x,3)
#     print(x,2)
#     local()
#     print(x,4)

# enclosed()
# print(x,5)

# a = 10

# def func():
#     print(a)
#     a1 = 'local'
#     print(a1)

# func()

# i = 0

# def increment():
#     i = i + 1

# increment()

# global -> позваоляет изменять значение глобальной переменной находясь в локальной или замкнутой области видимо

# nonlocal -> позволяет изменять значение не локальной перменной находясь в локальной области видимости 

# var = 100

# def increment():
#     global var 
#     var += 1 

# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)

# def counter():
#     num = 0
#     def increment():
#         nonlocal num 
#         num += 1 
#         return num 
#     return increment

# c = counter() 
# print(c)
# print(c()) # 1
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# b = counter()
# print(c())
# print(b())
# print(b())
# print(c())

# def counter():
#     num = 0
#     def increment():
#         nonlocal num 
#         num += 1 
#         return num 
#     return increment

# i = counter()

# for x in range(0,100_000):
#     if x % 3 == 0 and x % 5 == 0:
#         res = i()
#         print(res)

# print(f'Result: {res} ')

# print(len(dir(__builtins__)))

# a = 5
# b = 6
# c = 7
# def func():
#     john = 'John Snow'
#     print(locals())

# print(globals())
# print()
# func()

'-----------------------------------------------------------------------------------------------------------'

# Дан список внутри которого список из трех чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,3,5], [5,5,5,5]] -> 6, 11, 20 -> 20

# ls = [[100,2,3], [300,3,5], [5,5,5,5], [45,45,6]]

# result = max(sum(x)for x in ls)

# print(result)

# task 1
# var = 'переменная в foo'
# def foo():
#     global var
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
  
#     def bar():
#         global var
#         var = 'переменная bar'
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# task 2
# x = 'Я глобальная переменная!'
# def my_func():
#     global x 
#     print(x)
#     x = 'Я могу меняться!'
# my_func()
# print(x)

# task 3
# num = 3 
# def mul():
#     global num 
#     
#     num = num ** 2 
# mul()
# mul()
# mul()
# print(num)

# task 4
# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount
# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print(f'Вы заплатили {amount} сом за {log_name}')
#     return balance
# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')    

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()
     
# task 5
# result = 0
# def pow_first(x,y):
#     global result 
#     result = pow(x,y)

# def pow_second(z):
#     global result 
#     result = result % z
    
# pow_first(2, 3)
# pow_second(3)
# print(result)

# task 6

a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
def age_control(a):
    for k,v in a.items()
        if v < 17
        print('Вы не проходите по age-control')
        else:
            print('Вы можете войти в клуб')
print(age_control)
