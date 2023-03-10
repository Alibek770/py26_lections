# class Auto:
#   def ride(self):
#     print('Riding on a ground')

# class Boat:
#   def swim(self):
#     print('Floating on a water')

# class Amphibian(Auto,Boat):
#   pass


# obj = Amphibian() 
# obj.ride() 
# obj.swim() 

# class ContactList(list):
#   def search_by_name(self):
#     for x in list:
#       if x == self.name:
#         return f'Метод search_by_name возвращает все строки содержащие подстроку {self.name}: '

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])

# all_contacts.search_by_name()



# class Person:
#   def __init__(self,name,last_name,age,email):
#     self.__name = None
#     self.__last_name = None
#     self.__age = None
#     self.__email = None

#   def get_name(self):
#     return self.__name

#   def set_name(self):
#     self.__name = 'John'
#     return self.__name

#   def get_last_name(self):
#     return self.__last_name

#   def set_last_name(self):
#     self.__last_name = 'Snow'
#     return self.__last_name

#   def get_age(self):
#     return self.__age

#   def set_age(self):
#     self.__age = '30'
#     return self.__age

#   def get_email(self):
#     return self.__get_email

#   def set_email(self):
#     self.__email = 'johnsnow@gmail.com'
#     return self.__email

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com