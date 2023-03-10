# JSON - JavaScript Object Notation

# Единый формат, хранения и передачи между приложениями, 
# сайтами, сервисами и языками программирования через сеть интернет,
# <filename>.json файл в формате 


# { 
#     'id': 1,
#     'author': 'Ed Sheeran'
#     'title': 'Perfect'
#     'year': 2015,
#     'hit' : true,
#     'feat': null

# } Это JSON

# наша задача научиться переводить данные JSON в PYTHON dictionary

# !!!
# JS object == {key:value}
# PY dict == {key:value}
# JSON == {key:value}


# Процессы Сериализации и Десириализации данных 

# Сериализация - (Запись данных в JSON) - это перевод из Python обьектов в JSON формат 

# json.dump -> метод записывает Python данные в файл в формате JSON, параллельно сделав сериализацию 

# json.dumps -> метод записывает данные в строку в формате JSON, параллельно сделав сериализацию

# Десериализация (Чтение данных из JSON) -> это процесс перевода из JSONa в Python dict

# json.load -> метод который считывает файл в формате JSON и переводит его в PY dict

# json.loads -> метод который считывает текст в формате JSON и переводит его в PY object


'------------------------------------------------------------------------------------------------------'

# Процесс сериализации

# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'age': 24,
#     'children': None
# }

# print(dict_)
# print(type(dict_))

# json_text = json.dumps(dict_)
# print('--------------')
# print(json_text)
# print(type(json_text))


'------------------------------------------------------------------------------------------------------'

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'age': 24,
#     'wife': False,
#     'children': None
# }
# print(dict_)

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

# with open('new.json', 'r') as file:
#     data = file.read()
#     print(data)


'--------------------------------------------- Процесс десериализации ---------------------------------------------'

# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data)
# print(type(json_data))

# dict_ = json.loads(json_data)
# print(dict_, type(dict_))

# import json 

# with open('new.json') as file:
#     dict_ = json.load(file)
#     print(dict_)
#     print(type(dict_))

# from urllib.request import urlopen
# import json

# url = 'https://randomuser.me/api'
# json_data = urlopen(url)

# print(json_data)
# # print(dir(json_data))
# print(json_data.read())

# dict_ = json.load(json_data) # .loads(json_data.read())
# print(dict_)
# print(type(dict_))

# task6 JSON
# import json
# json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'
# dict_ = json.loads(json_products)
# for i in dict_:
#     if i['rating'] > 4:
#         print(i['title'])

#7 
# import json
# with open('db.json')as file:
#     list_ = json.load(file)
# for product in list_:
#     product["description"] = "..."
# js_list = json.dumps(list_) 
# with open('new_db.json','w') as f1:
#     f1.write(js_list)
    