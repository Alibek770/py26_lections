# import peewee
# from models import Category, Product
# import random

# def add_category(name):
#     try:
#         data=Category(name = name.lower().strip())
#         data.save()
#         print(f'Сохранили категорию {name.strip()}!')
#     except (peewee.IntegrityError, peewee.InternalError):
#         print('Такая категория уже существует!')

# add_category('  платья  ')
# add_category('Джинсы')
# add_category('Футболки')
# add_category('Свитеры')
# add_category('Обувь')

# def add_product(name, price, category_name):
#     try:
#         category_id = Category.get(name=category_name.lower().strip())
#     except peewee.DoesNotExist:
#         category = None
    
#     if category_id:
#         data = Product(title=name, price=price, category_id=category_id)
#         data.save()
#         print(f'Сохранили товар {name}!')
#     else:
#         print('Категории {category_name} не существует!')

# add_product('Zara t-shirt', 300, 'футболки')
# add_product('Armani t-shirt', 600, 'футболки')
# add_product('Lacoste', 700, 'платья')
# add_product('Boss', 800, 'свитеры')
# add_product('Nike Air Jordan ', 4000, 'обувь')
# add_product('Levis', 1100, 'джинсы')

    
#---------------------------------

# добавление новых данных 

# add_category('car')
# add_category('telefony')

# with open('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     # print(ls)
#     for x in ls:
#         name = x.replace('\n', ' ')
#         price = random.randint(5000,20000)
#         add_product(name, price,'cars')

# with open('files/telefon.txt', 'r') as file:
#     ls = file.readlines()
#     for x in ls:
#         name = x.replace('\n', '')
#         price = random.randint(200,1000)
#         add_product(name,price, 'telefony')


 