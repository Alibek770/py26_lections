from models import Product, Category 

# Обновление данных 
# query = Product.update(price=500).where(Product.title=='Zara t-shirt')
# print(query)
# query.execute()


# Увеличиваем всем товарам цену
# query = Product.update(price = (Product.price + Product.price * 0.5))
# query.execute()

# удаление данных
# query = Product.delete().where(Product.id == 15)
# query.execute()

# удаление через объект
# product = Product.get(id=13)
# print(product, product.title)
# product.delete_instance()

# query = Product.delete().where(Product.id >= 9)
# print(query)
# query.execute()


