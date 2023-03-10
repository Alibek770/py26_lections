# from parsing import parse_news
# import telebot
# from telebot import types
# import json

# token = '6034619025:AAELuxZJeoc6bvhi_atkpv7YooB6ac8aMXk'

# bot = telebot.TeleBot(token)

# keyboard = types.ReplyKeyboardMarkUp()
# button1 = types.KeyboardButton('фото')
# button2 = types.KeyboardButton('описание')
# keyboard.add(button1, button2)


# def read_news():
#     with open('data.json') as file:
#         data = json.load(file)
#     return(data)
        

# read_news()
        
# @bot.message_handler(commands=['start'])
# def start_parse(message):
#     bot.send_message(message.chat.id,'Бот приветссвует вас, мы начали парсинг!\nПодождите пару секунд...')
#     print('started')
#     parse_news()
#     print('parsed')
#     data = read_news()
#     print('data')
#     for x in data:
#         dict_ = data(x)
#         bot.send_message(message.chat.id, f'{x} --> {data[x]["title"]}')

#     message_from_bot = bot.send_message(message.chat.id, "Выберите число новости для подробной информации (1-20): ")
#     bot.register_next_step_handler(message_from_bot, check_number)

# def check_number(message):
#     keys = [str(x)for x in range (1,21)]
#     if message.text not in keys


# bot.polling()



