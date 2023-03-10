# Задание номер 1 

# import datetime 

# class Smartphone:
    

#     def call(self):
#         print('Call this number +99677777777')
        
    
#     def where_to_wear(self):
#         print('You can keep me anywhere')


# class Watch:
#     def see_time(self):
#         now = datetime.datetime.now()
#         print(now.time())
        
        

#     def where_to_wear():
#         print('You should wear me on your hand')

# class SmartWatch(Watch,Smartphone):
#     def where_to_wear():
#         print('You should wear me on your hand')
        
# obj = SmartWatch()
# obj.see_time()
# obj.call()


# Задание номер 2


# class CheckerMixin:
#     def check(self,username,password):
#             if self.username == username and self.password == password: 
#                 self.post_name +=1  
#             else:
#                 print('Error')

                
            
# class Instagram(CheckerMixin):

#     def __init__(self,title,username,password) -> None:
#         self.title = title
#         self.username = username
#         self.password = password
#         self.post_name = []
    
#     def post_post(self,post_name, username, password):
#         if True:
#             print('Succesfully created')
#         else: 
#             print('Invalid Error')



# class TikTok():

#     def __init__(self,title,username,password,video_name) -> None:
#         self.title = title
#         self.username = username
#         self.password = password
#         self.video_name = video_name

#     def post_video(self,post_video, username, password):
#         if self.username == username and self.password == password:
#             print('Succesfully created')
#         else:
#             print('Invalid Error')

# obj = Instagram()

# obj1 = TikTok()