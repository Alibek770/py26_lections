from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin

class Product(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent = 4)
        return 'Saved!'

smarphones = Product()
print(smarphones.post(title = 'Redmi Note 10', description = 'The best phone for own price', qty = 10, price = 250))
print(smarphones.post(title = 'Iphone11pro', description = 'The flagman of iphoen phones', qty = 5, price = 700))
print(smarphones.post(title = 'Samsung Galazy 7', description = 'Productive and well designed', qty = 9, price = 600))
print(smarphones.post(title = 'Nokia', description = 'Usual phone to make calls', qty =3, price = 50))
print(smarphones.post(title = 'Iphone14promax', description = 'Large and Fast', qty = 13, price = 1300))
print(smarphones.post(title = 'Poco Phone 13', description = 'The poco phone for poco users', qty = 6, price = 244))
print()
print(smarphones.list())
print()
print(smarphones.detail(5))
print(smarphones.detail(15))
print()
print(smarphones.patch(15,title = 'Poco Phone 20', price = 500))
print(smarphones.patch(5,title = 'Poco Phone 20'))
print()
print(smarphones.delete(5))
print()
print(smarphones.list())
print(smarphones.save())
