#tuple() -> кортеж, неизменяемый тип данных 

# thistuple = ('apple')
# print(thistuple)
# print(type(thistuple))

# mytuple = 'apple', 'pineapple', 'pan'
# print(mytuple)

# for x in range(1,5):
#     print(x)

# dict1 = {1: 'one', 2: 'two', 3: 'three'}
# print(dict1.items())
# for x,y,z in (1,2,3):
#     print()

# a = [(1,2), (3,4), (5,6)]
# for x, y in a:
#     print(x,y)

# ls = list(range(1, 100_001))
# tp = tuple(range(1, 100_001))

# print('LIST', ls.__sizeof__())
# print('TUPLE', tp.__sizeof__())

# tuple_ = (1,2,3,4,5)
# del tuple_[-1]
# print(tuple_)

# ls = [1,2,3,4,5]
# del ls [-1]
# print(ls)

# print(dir(tuple))

# tuple_ = (1,2,3,4,5,6,7,2,2,2,2,2)
# print(tuple_.index(5))
# print(tuple_.count(2))

# tp = ('apple', 'cherry', 'banana', 'john')
# for x in tp:
#     print(x)
#     print(x * 3)

# i = 0
# while i < 50:
#     print(i)
#     i += 1 #инкримент i = i + 1
#     i -= 1 #дикримент i -= 1

# tp = ('apple', 'cherry', 'banana', 'john')
# x = 0
# while x < len(tp):
#     print(tp[x])
#     x += 1

# + * 
# a = (1,2,3) 
# b = (4,5,6)
# print(a+b)
# print()

# # 1) input:
# tp = (1,8,3,4,5,8,8,9,2)
# target = 8
# first = tp.index(8)
# print(first)
# print(tp.index(8, first + 1))
# #output: result = (8,3,4,5,8)

# if tp.count(8) >1:
#     first = tp.index(8)
#     second = tp.index(8, first +1)
#     result = tp[first :second +1]
# else: 
#     first = tp.index(8)
#     result = tp[first:]
# print(tp, target)
# print(result)

#output: result = (8,5,1,2)

'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'

# #1)
# nums = [2,7,11,15]
# target = 9
# result = [0,1]

# for x  in nums:
#     if target - x == [0]:
#     print(nums.index[x])

#2) nums = [4,11,2,5,1,6]
# taget = 8
# result = 2 5 

# nums = [2,7,11,15]
# target = 9

# for x in nums:
#     num = target - x
#     if num in nums:
#         if num == x:
#             continue
#         print(nums.index(x), nums.index(num))
#         break


