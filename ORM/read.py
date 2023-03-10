import peewee
from models import Product, Category

def get_all_categories():
    return Category.select()

def get_all_products():
    return Product.select()

# categories = get_all_categories()
# # print(categories)
# print('Категории в бд: ')
# for x in categories:
#     print(type(x))
#     print(x.name)
#     print(x.created_at)
#     print()

# products = get_all_products()
# print('все товары в бд: ')
# for x in products:
#     print(x.title, x.price, x.category_id.name)
#     print()

# products = get_all_products()
# category = int(input('Vvedite category (1-платья, 2-джинсы, 3-футболки, 4-свитеры, 5-обувь):'))
# for x in products:
#     if x.category_id.category_id == category:
#         print(x.title, x.price, x.category_id.name)

# category_name = input('Vvedite title categorii: ').lower().strip()
# try:
#     category = Category.get(name = category_name)
# except peewee.DoesNotExist:
#     print('Такой категории нет!')

# # print(category)
# # print(category.category_id, type(category.category_id))
# # print(category.name, type(category.name))
# # print(category.created_at, type(category.created_at))
# else:
#     for product in category.products:
#         print(f'Title: {product.title}, price: {product.price}, category: {product.category_id.name}')
