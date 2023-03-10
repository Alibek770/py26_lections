from functools import reduce
list_ = [1, 2, 3, 4] 
result = list(reduce(lambda x,y:x+y), list_)
print(result)