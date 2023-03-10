
# task1 files
# with open('task1.txt') as file:
#     for line in file.readlines(9):
#         print(line)


# task 2

# with open('task2.txt') as file:
#     for line in file.readlines(18):
#         print(line)

# task 3 

# with open('task3.txt', 'a+') as file: 
#     file.write('0*1*2*3*4*5*6*7*8*9*') 
# file.seek(0)
# print(file.read())

#task4

# with open('task4.txt','r') as file: 
#     print(len(file.readlines()))
    
# task5

# with open('task5.txt') as file:
#     list = []
#     for line in file.readlines(max):

#         print(line)

# with open('task5.txt', 'r') as f: 
#     list_ = [] 
#     ful = f.read() 
#     for i in ful.split():
#     list_.append(int(i)) 

# with open('task6.txt', 'x') as fw: 
#     fw.write(f'{min(list_)}-{max(list_)}') 


# JSON TASK1
# import json 
# with open('task1.json','r') as file1:
#     python_obj = json.loads(file1.read())

# with open('task1.json','w') as file2:
#     file2.write(str(python_obj))


# JSON TASK2
# import json
# with open('task2.json', 'r') as file_:
#     json_obj = file_.read()
#     python_obj = json.loads(json_obj)

# JSON TASK3
# import json
# python_obj = None  
# json_obj = json.dumps(python_obj)
# print(json_obj) 

# JSON TASK4

# import json
# json_obj = "null"  
# python_obj = json.load(json_obj)
# print(python_obj) 

# import json
# json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'
# python_object = json.loads(json_products)
# print(json_products)
# print(python_object)
# for k,v in python_object.items():
#     if v > 4:
#         print(k)