'task1'

# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
# f = [a,b,c]
# for i in f:
#     print(len(i))

# 'task3'

# class Person:
#     def init(self,name,last_name): 
#         self.name = name 
#         self.last_name = last_name 
    
#     def get_info(self): 
#         return f'Привет, меня зовут {self.name} {self.last_name}.' 

# class Employee(Person): 
#     def init(self,work,status, name, last_name): 
#         super().init(name,last_name) 
#         self.work = work 
#         self.status = status 
        
#     def get_info(self): 
#         return f'Привет, меня зовут {self.name} {self.last_name} я работаю в компании {self.work} на должности {self.status}.' 

# class Student(Person): 
    
#     def init(self,university,cource, name, last_name): 
#         super().init(name,last_name) 
#         self.university = university 
#         self.cource = cource 
    
#     def get_info(self): 
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.cource}.' 
        
# person = Person('Иван', 'Петров') 
# employee = Employee('Рога и Копыта', 'директор','Иван', 'Петров') 
# student = Student('КГТУ', '3 курсе','Иван', 'Петров') 

# def get_human_info(object): 
#     print(object.get_info()) 
# get_human_info(employee)